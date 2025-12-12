#!/usr/bin/env bash
# Reconstruct a linear branch from detached/tag-only history.
# For each tag whose name is X.Y.Z or 'X.Y.Z', create a new commit on the
# branch preserving tree, author, committer, dates, and message.
# Creates normalized tags vX.Y.Z.
# Idempotent and resumable.
#
# Usage:
#   clean_repo.sh [options]
# Options:
#   -n, --limit <num>     Limit number of version tags processed this run (0 = unlimited)
#   -p, --tag-prefix <p>  Prefix for new normalized tags (default: v)
#       --dry-run         Show intended actions without writing refs
#       (Supports prerelease tags like 1.2.3-beta or 4.0.2-test)
#   -h, --help            Show help and exit
# Examples:
#   ./scripts/clean_repo.sh --dry-run -n 5
#   ./scripts/clean_repo.sh --limit 40
#   ./scripts/clean_repo.sh --tag-prefix rel-

set -euo pipefail
IFS=$'\n\t'

# Replace previous simple arg handling with structured parsing
BRANCH_NAME="reconstructed-history"  # hard-coded branch name
DRY_RUN="0"  # set by flag only
LIMIT="0"    # number of version tags to process (creating or re-tagging)
DEBUG_MODE="0"
SHOW_TAGS="0"
TAG_PREFIX="v"

#--------------------------------------
# Logging helpers
#--------------------------------------
# log: print normal log line
log() { printf "[clean-repo] %s\n" "$*"; }
# warn: print warning line to stderr
warn() { printf "[clean-repo][warn] %s\n" "$*" >&2; }
# err: print error and exit
err() { printf "[clean-repo][error] %s\n" "$*" >&2; exit 1; }

#--------------------------------------
# ensure_repo: verify we are inside a git repository
#--------------------------------------
ensure_repo() {
  if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    err "Not inside a git repository. Initialize or cd into the repo first."
  fi
}

#--------------------------------------
# ensure_tags_present: attempt fetch if no local tags present
#--------------------------------------
ensure_tags_present() {
  local count remote
  count=$(git tag --list | wc -l | tr -d ' ')
  if [ "$count" -gt 0 ]; then
    [ "$DEBUG_MODE" = "1" ] && log "[debug] Found $count existing local tags"
    return 0
  fi
  remote=$(git remote | head -n1 || true)
  if [ -z "$remote" ]; then
    warn "No tags and no remote found; cannot fetch tags"
    return 0
  fi
  log "No local tags detected. Fetching tags from '$remote'..."
  git fetch --tags "$remote" >/dev/null 2>&1 || warn "Failed to fetch tags from $remote"
}

#--------------------------------------
# list_all_tags: robust tag enumeration. Falls back to packed-refs if git tag --list empty.
#--------------------------------------
list_all_tags() {
  local tags
  tags=$(git tag --list 2>/dev/null || true)
  if [ -n "$tags" ]; then
    printf '%s\n' "$tags"
    return 0
  fi
  # Fallback to packed-refs (lightweight tags may be packed)
  if [ -f .git/packed-refs ]; then
    awk '/^#/ {next} /^\^/ {next} /refs\/tags\// { sub(/.*refs\/tags\//, ""); print }' .git/packed-refs
  fi
}

#--------------------------------------
# load_sorted_version_tags: build list of sortable lines "<epoch> <tag>"
# Filters out normalized prefix+semver tags and non-semver tags. Shows interactive progress if TTY.
#--------------------------------------
load_sorted_version_tags() {
  echo "Building list of version tags..." >&2
  ensure_tags_present
  local all_tags commit_hash commit_epoch sort_input="" normalized scanned=0 last_update=0 throttle=15 total start_ts progress_enabled=0 first_dump_limit=10 first_dump_count=0
  all_tags=$(list_all_tags || true)
  if [ -z "$all_tags" ]; then
    warn "No tags found after fetch and packed-refs fallback. Nothing to do."; return 1
  fi
  if [ "$SHOW_TAGS" = "1" ]; then
    echo "First 40 raw tags:" >&2
    printf '%s\n' "$all_tags" | head -n 40 >&2
  fi
  total=$(printf '%s\n' "$all_tags" | wc -l | tr -d ' ')
  [ -t 1 ] && progress_enabled=1
  start_ts=$(date +%s)
  if [ "$DEBUG_MODE" = "1" ]; then
    log "[debug] Raw tag count: $total"
  fi
  if [ "$progress_enabled" -eq 1 ]; then
    printf "[clean-repo] Scanning %d tags (unfiltered)...\r" "$total" >&2
  fi
  for tag in $all_tags; do
    scanned=$((scanned+1))
    normalized=$(normalize_tag_name "$tag")
    if [ "$DEBUG_MODE" = "1" ] && [ $first_dump_count -lt $first_dump_limit ]; then
      log "[debug] tag_raw='$tag' tag_norm='$normalized'"
      first_dump_count=$((first_dump_count+1))
    fi
    # Skip already normalized prefix+semver tags (created by this script previously)
    if [[ "$normalized" == "$TAG_PREFIX"* ]]; then
      local rem="${normalized#"$TAG_PREFIX"}"
      if is_semver "$rem"; then
        continue
      fi
    fi
    commit_hash=$(git rev-list -1 "$tag" 2>/dev/null || true)
    if [ -z "$commit_hash" ]; then
      [ "$DEBUG_MODE" = "1" ] && warn "Unresolvable tag (no commit): $tag"
      continue
    fi
    commit_epoch=$(git show -s --format='%ct' "$commit_hash")
    sort_input+="$commit_epoch $tag\n"
    if [ "$progress_enabled" -eq 1 ] && [ $((scanned - last_update)) -ge $throttle ]; then
      last_update=$scanned
      printf "\r[clean-repo] Scanning tags (%d/%d)... collected %d candidates" "$scanned" "$total" "$(printf '%s' "$sort_input" | grep -c '^')" >&2
    fi
  done
  if [ -z "$sort_input" ]; then
    warn "All tags filtered (only normalized or unresolved)."; return 1
  fi
  if [ "$progress_enabled" -eq 1 ]; then
    local duration end_ts collected
    end_ts=$(date +%s); duration=$((end_ts-start_ts))
    collected=$(printf '%s' "$sort_input" | grep -c '^')
    printf "\r[clean-repo] Tag collection complete (%d/%d). Collected %d candidates in %.2fs\n" "$scanned" "$total" "$collected" "$duration" >&2
  fi
  printf '%b' "$sort_input" | sort -k1,1n
}

#--------------------------------------
# ensure_branch_ref: sets PREV_NEW_COMMIT if branch exists, logs state
#--------------------------------------
ensure_branch_ref() {
  if ! git show-ref --verify --quiet "refs/heads/${BRANCH_NAME}"; then
    log "Branch '${BRANCH_NAME}' does not exist yet. It will be created with first replayed commit."
  else
    log "Branch '${BRANCH_NAME}' already exists. Will append new commits to its tip if needed."
    PREV_NEW_COMMIT=$(git rev-parse "refs/heads/${BRANCH_NAME}")
  fi
}

#--------------------------------------
# normalize_tag_name: simpler robust stripping
# Args: raw tag name
# Prints normalized name
#--------------------------------------
# Enhanced normalization: strip surrounding matching single OR double quotes and whitespace
normalize_tag_name() {
  local t="$1"
  # Trim leading/trailing whitespace
  t=$(printf '%s' "$t" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
  # Remove one pair of matching surrounding quotes if present
  if [ ${#t} -ge 2 ]; then
    local first="${t:0:1}" last="${t: -1}"
    if { [ "$first" = '"' ] && [ "$last" = '"' ]; } || { [ "$first" = "'" ] && [ "$last" = "'" ]; }; then
      t="${t:1:${#t}-2}"
    fi
  fi
  printf '%s' "$t"
}

#--------------------------------------
# is_semver: accept X.Y.Z with optional -/_/. prerelease and +build segments (normalized quotes removed)
# Returns 0 if matches, 1 otherwise
#--------------------------------------
# Simplified semver: require three numeric components separated by dots; allow optional prerelease (one or more groups) and optional build.
# Examples matched: 1.2.3 1.2.3-test 1.2.3-test.alpha 1.2.3_test 1.2.3-test+build.5 10.20.30
is_semver() {
  [[ "$1" =~ ^[0-9]+(\.[0-9]+){2}([._-][0-9A-Za-z.-]+)*(\+[0-9A-Za-z.-]+)?$ ]]
}

#--------------------------------------
# gather_commit_metadata: export metadata of original commit into variables
# Globals set: author_name, author_email, author_date, committer_name, committer_email, committer_date, commit_message, tree_hash
#--------------------------------------
# shellcheck disable=SC2034
# (Variables intentionally used globally after function call)

author_name=""; author_email=""; author_date=""; committer_name=""; committer_email=""; committer_date=""; commit_message=""; tree_hash=""
gather_commit_metadata() {
  local commit_hash="$1"
  author_name=$(git show -s --format='%an' "$commit_hash")
  author_email=$(git show -s --format='%ae' "$commit_hash")
  author_date=$(git show -s --format='%ai' "$commit_hash")
  committer_name=$(git show -s --format='%cn' "$commit_hash")
  committer_email=$(git show -s --format='%ce' "$commit_hash")
  committer_date=$(git show -s --format='%ci' "$commit_hash")
  commit_message=$(git show -s --format='%B' "$commit_hash")
  tree_hash=$(git show -s --format='%T' "$commit_hash")
}

#--------------------------------------
# find_existing_replay_commit: search branch for a commit identical to orig commit metadata
# Args: original commit hash
# Prints matching commit hash if found
#--------------------------------------
find_existing_replay_commit() {
  local orig_commit="$1"
  local tree commit_msg a_name a_email a_date c_name c_email c_date
  tree=$(git show -s --format='%T' "$orig_commit")
  commit_msg=$(git show -s --format='%B' "$orig_commit" | sed 's/[[:space:]]*$//')
  a_name=$(git show -s --format='%an' "$orig_commit")
  a_email=$(git show -s --format='%ae' "$orig_commit")
  a_date=$(git show -s --format='%ai' "$orig_commit")
  c_name=$(git show -s --format='%cn' "$orig_commit")
  c_email=$(git show -s --format='%ce' "$orig_commit")
  c_date=$(git show -s --format='%ci' "$orig_commit")
  if ! git show-ref --verify --quiet "refs/heads/${BRANCH_NAME}"; then
    return 1
  fi
  while IFS= read -r commit_hash; do
    local bt ba_name ba_email ba_date bc_name bc_email bc_date bmsg
    bt=$(git show -s --format='%T' "$commit_hash")
    [ "$bt" != "$tree" ] && continue
    ba_name=$(git show -s --format='%an' "$commit_hash")
    ba_email=$(git show -s --format='%ae' "$commit_hash")
    ba_date=$(git show -s --format='%ai' "$commit_hash")
    bc_name=$(git show -s --format='%cn' "$commit_hash")
    bc_email=$(git show -s --format='%ce' "$commit_hash")
    bc_date=$(git show -s --format='%ci' "$commit_hash")
    bmsg=$(git show -s --format='%B' "$commit_hash" | sed 's/[[:space:]]*$//')
    if [ "$ba_name" = "$a_name" ] && [ "$ba_email" = "$a_email" ] && [ "$ba_date" = "$a_date" ] && \
       [ "$bc_name" = "$c_name" ] && [ "$bc_email" = "$c_email" ] && [ "$bc_date" = "$c_date" ] && \
       [ "$bmsg" = "$commit_msg" ]; then
      printf '%s' "$commit_hash"
      return 0
    fi
  done < <(git rev-list "${BRANCH_NAME}" || true)
  return 1
}

#--------------------------------------
# create_replay_commit: create new commit preserving metadata and ancestry
# Uses global metadata variables populated by gather_commit_metadata.
# Prints new commit hash.
#--------------------------------------
create_replay_commit() {
  if [ -z "$PREV_NEW_COMMIT" ]; then
    printf '%s' "$commit_message" | \
      GIT_AUTHOR_NAME="$author_name" \
      GIT_AUTHOR_EMAIL="$author_email" \
      GIT_AUTHOR_DATE="$author_date" \
      GIT_COMMITTER_NAME="$committer_name" \
      GIT_COMMITTER_EMAIL="$committer_email" \
      GIT_COMMITTER_DATE="$committer_date" \
      git commit-tree "$tree_hash"
  else
    printf '%s' "$commit_message" | \
      GIT_AUTHOR_NAME="$author_name" \
      GIT_AUTHOR_EMAIL="$author_email" \
      GIT_AUTHOR_DATE="$author_date" \
      GIT_COMMITTER_NAME="$committer_name" \
      GIT_COMMITTER_EMAIL="$committer_email" \
      GIT_COMMITTER_DATE="$committer_date" \
      git commit-tree "$tree_hash" -p "$PREV_NEW_COMMIT"
  fi
}

#--------------------------------------
# tag_exists: check if normalized tag already exists
# Args: tag name
#--------------------------------------
tag_exists() { git rev-parse -q --verify "refs/tags/$1" >/dev/null 2>&1; }

#--------------------------------------
# create_normalized_tag: create tag unless DRY_RUN
# Args: tag name, commit hash
#--------------------------------------
create_normalized_tag() {
  local tag="$1" commit="$2"
  if [ "$DRY_RUN" = "1" ]; then
    log "[DRY_RUN] Would create tag $tag -> $commit"
  else
    git tag "$tag" "$commit"
  fi
}

#--------------------------------------
# update_branch_ref: move branch ref to new commit unless DRY_RUN
# Args: commit hash
#--------------------------------------
update_branch_ref() {
  local commit="$1"
  if [ "$DRY_RUN" = "1" ]; then
    log "[DRY_RUN] Would update branch ${BRANCH_NAME} -> $commit"
  else
    git update-ref "refs/heads/${BRANCH_NAME}" "$commit"
  fi
  PREV_NEW_COMMIT="$commit"
}

#--------------------------------------
# process_tags: main loop over sorted tag lines
#--------------------------------------
process_tags() {
  local sorted_lines="$1" line epoch raw_tag clean_tag semver new_tag orig_commit existing_replay new_commit
  while read -r line; do
    [ -z "$line" ] && continue
    epoch=$(printf '%s' "$line" | awk '{print $1}')
    raw_tag=$(printf '%s' "$line" | cut -d' ' -f2-)
    clean_tag=$(normalize_tag_name "$raw_tag")
    if ! is_semver "$clean_tag"; then
      skipped_non_version=$((skipped_non_version+1))
      continue
    fi
    semver="$clean_tag"
    new_tag="${TAG_PREFIX}${semver}"  # include prerelease/build if present
    if tag_exists "$new_tag"; then
      skipped_existing=$((skipped_existing+1))
      continue
    fi
    orig_commit=$(git rev-list -1 "$raw_tag" 2>/dev/null || true)
    if [ -z "$orig_commit" ]; then
      warn "Failed to resolve commit for tag $raw_tag (epoch $epoch)."; skipped_unresolved=$((skipped_unresolved+1)); continue
    fi
    existing_replay=$(find_existing_replay_commit "$orig_commit" || true)
    if [ -n "$existing_replay" ]; then
      reused_commits=$((reused_commits+1))
      processed_any=true
      create_normalized_tag "$new_tag" "$existing_replay"
      log "Reused existing replay commit $existing_replay for original tag '$raw_tag' -> added tag ${new_tag}"
      processed_count=$((processed_count+1))
      if [ "$LIMIT" -gt 0 ] && [ "$processed_count" -ge "$LIMIT" ]; then
        log "Reached processing limit ($LIMIT). Stopping early."; break
      fi
      continue
    fi
    gather_commit_metadata "$orig_commit"
    if [ "$DRY_RUN" = "1" ]; then
      log "[DRY_RUN] Would create commit for tag $raw_tag -> $new_tag with tree $tree_hash"
      processed_any=true
      processed_count=$((processed_count+1))
      if [ "$LIMIT" -gt 0 ] && [ "$processed_count" -ge "$LIMIT" ]; then
        log "Reached processing limit ($LIMIT) in dry run. Stopping early."; break
      fi
      continue
    fi
    new_commit=$(create_replay_commit)
    update_branch_ref "$new_commit"
    created_commits=$((created_commits+1))
    processed_any=true
    create_normalized_tag "$new_tag" "$new_commit"
    log "Created commit $new_commit and tag ${new_tag} (from original tag '${raw_tag}' -> commit ${orig_commit})"
    processed_count=$((processed_count+1))
    if [ "$LIMIT" -gt 0 ] && [ "$processed_count" -ge "$LIMIT" ]; then
      log "Reached processing limit ($LIMIT). Stopping early."; break
    fi
  done <<< "$sorted_lines"
}

#--------------------------------------
# summarize: print final summary
#--------------------------------------
summarize() {
  local limit_note=""
  if [ "$LIMIT" -gt 0 ]; then
    limit_note=" (limit $LIMIT, processed $processed_count)"
  else
    limit_note=" (unlimited, processed $processed_count)"
  fi
  if [ "$DRY_RUN" = "1" ]; then
    log "Dry run complete${limit_note}. Created (virtually) $created_commits commits. Reused: $reused_commits. Skipped existing: $skipped_existing; Non-version: $skipped_non_version; Unresolved: $skipped_unresolved"
    return
  fi
  if ! $processed_any; then
    log "No new commits or tags to create${limit_note}. Repository already normalized or no candidate tags. (Skipped existing: $skipped_existing; Non-version: $skipped_non_version; Unresolved: $skipped_unresolved; Reused: $reused_commits)"
  else
    log "Done${limit_note}. Created $created_commits new commits. Reused $reused_commits existing commits. Skipped existing: $skipped_existing; Non-version: $skipped_non_version; Unresolved: $skipped_unresolved. Branch: ${BRANCH_NAME}" 
    log "Tip of '${BRANCH_NAME}' is $(git rev-parse "refs/heads/${BRANCH_NAME}" 2>/dev/null || echo 'N/A')"
  fi
  log "To inspect: git log --oneline ${BRANCH_NAME}"
  log "To push:    git push origin ${BRANCH_NAME} --tags"
}

#--------------------------------------
# show_help: print help message
#--------------------------------------
show_help() {
  sed -n '1,40p' "$0" | grep '^#' | sed 's/^# \{0,1\}//'
}

#--------------------------------------
# parse_args: parse command-line arguments
#--------------------------------------
parse_args() {
  local arg
  while [ $# -gt 0 ]; do
    arg="$1"
    case "$arg" in
      -n|--limit)
        shift || err "Missing value for $arg"
        LIMIT="${1:-}"; [[ -z "$LIMIT" || ! "$LIMIT" =~ ^[0-9]+$ ]] && err "Invalid numeric limit: $LIMIT"
        ;;
      -p|--tag-prefix)
        shift || err "Missing value for $arg"
        TAG_PREFIX="${1:-}"; [ -z "$TAG_PREFIX" ] && err "Tag prefix cannot be empty"
        ;;
      --dry-run)
        DRY_RUN="1"
        ;;
      --debug)
        DEBUG_MODE="1"
        ;;
      --show-tags)
        SHOW_TAGS="1"
        ;;
      -h|--help)
        show_help; exit 0
        ;;
      --)
        shift; break
        ;;
      -*)
        err "Unknown option: $arg"
        ;;
      *)
        warn "Ignoring extra positional argument: $arg"
        ;;
    esac
    shift || true
  done
}

# Parse CLI before any operations
parse_args "$@"

# Startup context log (added)
startup_log() {
  local limit_text
  if [ "$LIMIT" -gt 0 ]; then
    limit_text="$LIMIT"
  else
    limit_text="unlimited"
  fi
  log "Starting with branch='$BRANCH_NAME' limit=$limit_text dry_run=$DRY_RUN debug=$DEBUG_MODE"
}

# Global counters
processed_any=false
skipped_existing=0
created_commits=0
skipped_non_version=0
skipped_unresolved=0
reused_commits=0
PREV_NEW_COMMIT=""
processed_count=0
TOTAL_VERSION_TAGS=0
COMPLETED_VERSION_TAGS=0

#--------------------------------------
# compute_progress_stats: count total semantic version tags and those already normalized
# Args: sorted tag lines
# Sets globals: TOTAL_VERSION_TAGS, COMPLETED_VERSION_TAGS
#--------------------------------------
compute_progress_stats() {
  local sorted_lines="$1" line raw_tag clean_tag semver new_tag scanned=0 last_update=0 throttle=15 start_ts candidate_count
  TOTAL_VERSION_TAGS=0
  COMPLETED_VERSION_TAGS=0
  local progress_enabled=0
  local classification_debug_limit=30 classification_debug_count=0
  if [ -t 1 ] && [ "$DEBUG_MODE" = "0" ]; then
    progress_enabled=1
  fi
  candidate_count=$(printf '%s' "$sorted_lines" | grep -c '^[0-9]')
  start_ts=$(date +%s)
  if [ "$progress_enabled" -eq 1 ]; then
    printf '[clean-repo] Classifying %d candidate tags...\r' "$candidate_count"
  fi
  local nonmatch_samples="" nonmatch_limit=25
  while read -r line; do
    [ -z "$line" ] && continue
    scanned=$((scanned+1))
    raw_tag=$(printf '%s' "$line" | cut -d' ' -f2-)
    clean_tag=$(normalize_tag_name "$raw_tag")
    if is_semver "$clean_tag"; then
      TOTAL_VERSION_TAGS=$((TOTAL_VERSION_TAGS+1))
      semver="$clean_tag"
      new_tag="${TAG_PREFIX}${semver}"
      tag_exists "$new_tag" && COMPLETED_VERSION_TAGS=$((COMPLETED_VERSION_TAGS+1))
      if [ "$DEBUG_MODE" = "1" ] && [ $classification_debug_count -lt $classification_debug_limit ]; then
        log "[debug] MATCH semver='$clean_tag' normalized='$new_tag' present=$(if tag_exists "$new_tag"; then echo yes; else echo no; fi)"
        classification_debug_count=$((classification_debug_count+1))
      fi
    else
      if [ "$DEBUG_MODE" = "1" ] && [ $nonmatch_samples -lt $nonmatch_limit ]; then
        log "[debug] NO_MATCH raw='$raw_tag' clean='$clean_tag'"
        nonmatch_samples=$((nonmatch_samples+1))
      fi
    fi
    if [ "$progress_enabled" -eq 1 ] && [ $((scanned - last_update)) -ge $throttle ]; then
      last_update=$scanned
      printf "\r[clean-repo] Classifying (%d/%d)... version-like %d, normalized %d" "$scanned" "$candidate_count" "$TOTAL_VERSION_TAGS" "$COMPLETED_VERSION_TAGS"
    fi
  done <<< "$sorted_lines"
  if [ "$progress_enabled" -eq 1 ]; then
    local duration end_ts
    end_ts=$(date +%s); duration=$((end_ts-start_ts))
    printf "\r[clean-repo] Classification complete (%d/%d). Version-like %d | normalized %d | %.2fs\n" "$scanned" "$candidate_count" "$TOTAL_VERSION_TAGS" "$COMPLETED_VERSION_TAGS" "$duration"
  fi
  if [ "$DEBUG_MODE" = "1" ] && [ "$TOTAL_VERSION_TAGS" -eq 0 ]; then
    warn "No semver matches detected among $candidate_count candidates. Regex: ^[0-9]+(\\.[0-9]+){2}([._-][0-9A-Za-z.-]+)*(\\+[0-9A-Za-z.-]+)?$"
  fi
}

#--------------------------------------
# print_progress_overview: output startup progress metrics
#--------------------------------------
print_progress_overview() {
  local remaining percent
  remaining=$((TOTAL_VERSION_TAGS-COMPLETED_VERSION_TAGS))
  if [ "$TOTAL_VERSION_TAGS" -eq 0 ]; then
    percent="100.00"
  else
    percent=$(awk -v c=$COMPLETED_VERSION_TAGS -v t=$TOTAL_VERSION_TAGS 'BEGIN{printf "%.2f", (c/t)*100}')
  fi
  log "Found $TOTAL_VERSION_TAGS version-tagged commits. Already processed $COMPLETED_VERSION_TAGS. Remaining $remaining ($percent%)."
  if [ "$DEBUG_MODE" = "1" ]; then
    log "[debug] Limit=$LIMIT DryRun=$DRY_RUN Branch=$BRANCH_NAME Candidates=$(printf '%s' "$1" | grep -c '^[0-9]')"
  fi
}

#--------------------------------------
# main: entrypoint
#--------------------------------------
main() {
  ensure_repo
  startup_log
  ensure_branch_ref
  local sorted
  if ! sorted=$(load_sorted_version_tags); then
    # If branch requested and does not exist, optionally create it at current HEAD when no tags (resumable baseline)
    if ! git show-ref --verify --quiet "refs/heads/${BRANCH_NAME}"; then
      if [ "$DRY_RUN" = "1" ]; then
        log "Dry run: would create empty branch '${BRANCH_NAME}' at HEAD ($(git rev-parse HEAD)) because no tags found."
      else
        git branch "$BRANCH_NAME" >/dev/null 2>&1 || git update-ref "refs/heads/${BRANCH_NAME}" "$(git rev-parse HEAD)"
        log "Created empty branch '${BRANCH_NAME}' at HEAD ($(git rev-parse HEAD)) due to absence of version tags."
      fi
    fi
    log "No candidate tags discovered. Ensure tags are fetched (git fetch --tags) or repository cloned with full history."; summarize; exit 0
  fi
  compute_progress_stats "$sorted"
  print_progress_overview "$sorted"
  process_tags "$sorted"
  summarize
}

main "$@"