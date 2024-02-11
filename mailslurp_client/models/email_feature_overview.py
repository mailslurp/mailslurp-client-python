# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://docs.mailslurp.com/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Contact: contact@mailslurp.dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class EmailFeatureOverview(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'feature': 'str',
        'title': 'str',
        'description': 'str',
        'category': 'str',
        'notes': 'str',
        'notes_numbers': 'dict(str, str)',
        'feature_statistics': 'list[EmailFeatureFamilyStatistics]',
        'statuses': 'list[str]'
    }

    attribute_map = {
        'feature': 'feature',
        'title': 'title',
        'description': 'description',
        'category': 'category',
        'notes': 'notes',
        'notes_numbers': 'notesNumbers',
        'feature_statistics': 'featureStatistics',
        'statuses': 'statuses'
    }

    def __init__(self, feature=None, title=None, description=None, category=None, notes=None, notes_numbers=None, feature_statistics=None, statuses=None, local_vars_configuration=None):  # noqa: E501
        """EmailFeatureOverview - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._feature = None
        self._title = None
        self._description = None
        self._category = None
        self._notes = None
        self._notes_numbers = None
        self._feature_statistics = None
        self._statuses = None
        self.discriminator = None

        self.feature = feature
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if category is not None:
            self.category = category
        if notes is not None:
            self.notes = notes
        if notes_numbers is not None:
            self.notes_numbers = notes_numbers
        if feature_statistics is not None:
            self.feature_statistics = feature_statistics
        self.statuses = statuses

    @property
    def feature(self):
        """Gets the feature of this EmailFeatureOverview.  # noqa: E501


        :return: The feature of this EmailFeatureOverview.  # noqa: E501
        :rtype: str
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this EmailFeatureOverview.


        :param feature: The feature of this EmailFeatureOverview.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and feature is None:  # noqa: E501
            raise ValueError("Invalid value for `feature`, must not be `None`")  # noqa: E501
        allowed_values = ["amp", "css-accent-color", "css-align-items", "css-animation", "css-aspect-ratio", "css-at-font-face", "css-at-import", "css-at-keyframes", "css-at-media", "css-at-supports", "css-background-blend-mode", "css-background-clip", "css-background-color", "css-background-image", "css-background-origin", "css-background-position", "css-background-repeat", "css-background-size", "css-background", "css-block-inline-size", "css-border-image", "css-border-inline-block-individual", "css-border-inline-block-longhand", "css-border-inline-block", "css-border-radius-logical", "css-border-radius", "css-border", "css-box-shadow", "css-box-sizing", "css-caption-side", "css-clip-path", "css-column-count", "css-column-layout-properties", "css-direction", "css-display-flex", "css-display-grid", "css-display-none", "css-display", "css-filter", "css-flex-direction", "css-flex-wrap", "css-float", "css-font-kerning", "css-font-weight", "css-font", "css-gap", "css-grid-template", "css-height", "css-hyphens", "css-inline-size", "css-justify-content", "css-left-right-top-bottom", "css-letter-spacing", "css-line-height", "css-list-style-image", "css-list-style-position", "css-list-style-type", "css-list-style", "css-margin-block-start-end", "css-margin-inline-block", "css-margin-inline-start-end", "css-margin-inline", "css-margin", "css-max-block-size", "css-max-height", "css-max-width", "css-min-height", "css-min-inline-size", "css-min-width", "css-mix-blend-mode", "css-object-fit", "css-object-position", "css-opacity", "css-outline-offset", "css-outline", "css-overflow-wrap", "css-overflow", "css-padding-block-start-end", "css-padding-inline-block", "css-padding-inline-start-end", "css-padding", "css-position", "css-tab-size", "css-table-layout", "css-text-align-last", "css-text-align", "css-text-decoration-color", "css-text-decoration-thickness", "css-text-decoration", "css-text-emphasis-position", "css-text-emphasis", "css-text-indent", "css-text-overflow", "css-text-shadow", "css-text-transform", "css-text-underline-offset", "css-transform", "css-vertical-align", "css-visibility", "css-white-space", "css-width", "css-word-break", "css-writing-mode", "css-z-index", "html-abbr", "html-address", "html-align", "html-anchor-links", "html-aria-describedby", "html-aria-hidden", "html-aria-label", "html-aria-labelledby", "html-aria-live", "html-audio", "html-background", "html-base", "html-blockquote", "html-body", "html-button-reset", "html-button-submit", "html-code", "html-del", "html-dfn", "html-dialog", "html-dir", "html-div", "html-doctype", "html-form", "html-h1-h6", "html-height", "html-image-maps", "html-input-checkbox", "html-input-hidden", "html-input-radio", "html-input-reset", "html-input-submit", "html-input-text", "html-lang", "html-link", "html-lists", "html-loading-attribute", "html-mailto-links", "html-marquee", "html-meter", "html-object", "html-p", "html-picture", "html-pre", "html-progress", "html-required", "html-role", "html-rp", "html-rt", "html-ruby", "html-select", "html-semantics", "html-small", "html-span", "html-srcset", "html-strike", "html-strong", "html-style", "html-svg", "html-table", "html-target", "html-textarea", "html-valign", "html-video", "html-wbr", "html-width", "image-avif", "image-base64", "image-bmp", "image-gif", "image-ico", "image-jpg", "image-png", "image-svg", "image-webp", "unsupported"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and feature not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `feature` ({0}), must be one of {1}"  # noqa: E501
                .format(feature, allowed_values)
            )

        self._feature = feature

    @property
    def title(self):
        """Gets the title of this EmailFeatureOverview.  # noqa: E501


        :return: The title of this EmailFeatureOverview.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this EmailFeatureOverview.


        :param title: The title of this EmailFeatureOverview.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this EmailFeatureOverview.  # noqa: E501


        :return: The description of this EmailFeatureOverview.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EmailFeatureOverview.


        :param description: The description of this EmailFeatureOverview.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def category(self):
        """Gets the category of this EmailFeatureOverview.  # noqa: E501


        :return: The category of this EmailFeatureOverview.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this EmailFeatureOverview.


        :param category: The category of this EmailFeatureOverview.  # noqa: E501
        :type: str
        """
        allowed_values = ["css", "html", "image", "others"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and category not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"  # noqa: E501
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def notes(self):
        """Gets the notes of this EmailFeatureOverview.  # noqa: E501


        :return: The notes of this EmailFeatureOverview.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this EmailFeatureOverview.


        :param notes: The notes of this EmailFeatureOverview.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def notes_numbers(self):
        """Gets the notes_numbers of this EmailFeatureOverview.  # noqa: E501


        :return: The notes_numbers of this EmailFeatureOverview.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._notes_numbers

    @notes_numbers.setter
    def notes_numbers(self, notes_numbers):
        """Sets the notes_numbers of this EmailFeatureOverview.


        :param notes_numbers: The notes_numbers of this EmailFeatureOverview.  # noqa: E501
        :type: dict(str, str)
        """

        self._notes_numbers = notes_numbers

    @property
    def feature_statistics(self):
        """Gets the feature_statistics of this EmailFeatureOverview.  # noqa: E501


        :return: The feature_statistics of this EmailFeatureOverview.  # noqa: E501
        :rtype: list[EmailFeatureFamilyStatistics]
        """
        return self._feature_statistics

    @feature_statistics.setter
    def feature_statistics(self, feature_statistics):
        """Sets the feature_statistics of this EmailFeatureOverview.


        :param feature_statistics: The feature_statistics of this EmailFeatureOverview.  # noqa: E501
        :type: list[EmailFeatureFamilyStatistics]
        """

        self._feature_statistics = feature_statistics

    @property
    def statuses(self):
        """Gets the statuses of this EmailFeatureOverview.  # noqa: E501


        :return: The statuses of this EmailFeatureOverview.  # noqa: E501
        :rtype: list[str]
        """
        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        """Sets the statuses of this EmailFeatureOverview.


        :param statuses: The statuses of this EmailFeatureOverview.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and statuses is None:  # noqa: E501
            raise ValueError("Invalid value for `statuses`, must not be `None`")  # noqa: E501
        allowed_values = ["SUPPORTED", "PARTIAL", "NOT_SUPPORTED", "UNKNOWN"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(statuses).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `statuses` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(statuses) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._statuses = statuses

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EmailFeatureOverview):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailFeatureOverview):
            return True

        return self.to_dict() != other.to_dict()