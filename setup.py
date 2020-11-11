from setuptools import setup, find_packages 

setup(
    name="mailslurp-client",
    version="8.0.9",
    description="Official MailSlurp Python SDK Email API",
    author="MailSlurp",
    author_email="support@mailslurp.zendesk.com",
    url="https://www.mailslurp.com/docs/python",
    keywords=["MailSlurp", "Email", "SMTP", "Mailer", "MailSlurp API", "Test"],
    install_requires=["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"],
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""
---
label: Python
title: Python Email API
icon: devicon-python-plain
featured: true
meta:
  - name: description
    content: Send and receive emails in Python, Django, Flask and more.
---

# MailSlurp Python Client

> Create real email addresses on demand. Send and receive emails and attachments from code and tests using Python.

MailSlurp is an email API service that lets you create real email addresses in code. You can then send and receive emails and attachments in Python applications and tests.

## Quick links

- [Method Documentation](./docs)
- [PyPI Package](https://pypi.org/project/mailslurp-client/)
- [Github Source](https://github.com/mailslurp/mailslurp-client-python)

## Get started

:::tip
This section describes how to get up and running with the Python client.

See the [examples page](https://www.mailslurp.com/examples/) for more examples and use with common frameworks such as Django, Flask and Pytest.

See the method documentation for a [list of all functions](https://github.com/mailslurp/mailslurp-client-python)
:::

### Create API Key

First you'll need an API Key. [Create a free account](https://app.mailslurp.com) and copy the key from your dashboard.

### Install package

MailSlurp has an official PyPI package called `mailslurp-client`. It supports Python version 2 and 3.

```bash
pip install mailslurp-client
```

### Configure

Once installed you can import `mailslurp_client` and create a configuration with your [API Key](https://app.mailslurp.com).

```python
import mailslurp_client

configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = "your-api-key-here"
```

## Common usage

MailSlurp can be used to create email addresses than can send and receive real emails and attachments in Python.

### Create an email address

Use `with` statements to create controllers for each endpoint of the MailSlurp API.

```python
def create_inbox_example():
    with mailslurp_client.ApiClient(configuration) as api_client:

        # create an inbox using the inbox controller
        api_instance = mailslurp_client.InboxControllerApi(api_client)
        inbox = api_instance.create_inbox()

        # check the id and email_address of the inbox
        assert len(inbox.id) > 0
        assert "mailslurp.com" in inbox.email_address
```

### Send emails

```python
def send_email_example():
    with mailslurp_client.ApiClient(configuration) as api_client:
        # first create an inbox
        api_instance = mailslurp_client.InboxControllerApi(api_client)
        inbox = api_instance.create_inbox()

        # send email from the inbox
        send_email_options = mailslurp_client.SendEmailOptions()
        send_email_options.to = [inbox.email_address]
        send_email_options.subject = "Hello"
        send_email_options.body = "Your message"
        send_email_options.is_html = True
        api_instance.send_email(inbox.id, send_email_options=send_email_options)
```

### Receive emails and extract content

```python
def receive_email_and_extract_content_example():
    with mailslurp_client.ApiClient(configuration) as api_client:
        # create two inboxes for testing
        inbox_controller = mailslurp_client.InboxControllerApi(api_client)
        inbox_1 = inbox_controller.create_inbox()
        inbox_2 = inbox_controller.create_inbox()

        # send email from inbox 1 to inbox 2
        send_email_options = mailslurp_client.SendEmailOptions()
        send_email_options.to = [inbox_2.email_address]
        send_email_options.subject = "Hello inbox 2"
        send_email_options.body = "Your code is: 123"
        inbox_controller.send_email(inbox_1.id, send_email_options=send_email_options)

        # receive email for inbox 2
        waitfor_controller = mailslurp_client.WaitForControllerApi(api_client)
        email = waitfor_controller.wait_for_latest_email(inbox_id=inbox_2.id, timeout=30000, unread_only=True)

        assert email.subject == "Hello inbox 2"

        # extract content from body
        import re
        pattern = re.compile('Your code is: ([0-9]{3})')
        matches = pattern.match(email.body)
        code = matches.group(1)

        assert code == "123"
```

## SDK Documentation

See the [guides page](/guides/) for examples or the [Method Documentation](./docs) for full usage.    
    """,
    long_description_content_type="text/markdown"
)
