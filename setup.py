from setuptools import setup, find_packages 

setup(
    name="mailslurp-client",
    version="11.7.7",
    description="Official MailSlurp Python SDK Email API",
    author="MailSlurp",
    author_email="support@mailslurp.zendesk.com",
    url="https://www.mailslurp.com/docs/python",
    keywords=["MailSlurp", "Email", "SMTP", "Mailer", "MailSlurp API", "Test"],
    install_requires=["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"],
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""
# MailSlurp Python Client

> Create real email addresses on demand. Send and receive emails and attachments from code and tests using Python.

MailSlurp is an email API service that lets you create real email addresses in code. You can then send and receive emails and attachments in Python applications and tests.

## Quick links

- [Method Documentation](./docs)
- [PyPI Package](https://pypi.org/project/mailslurp-client/)
- [Github Source](https://github.com/mailslurp/mailslurp-client-python)

## Get started

This section describes how to get up and running with the Python client.

See the [examples page](https://www.mailslurp.com/examples/) for more examples and use with common frameworks such as Django, Flask and Pytest.

See the method documentation for a [list of all functions](./docs)

### Create API Key

First you'll need an API Key. [Create a free account](https://app.mailslurp.com) and copy the key from your dashboard.

### Install package

MailSlurp has an official PyPI package called `mailslurp-client`. It supports Python version 2 and 3.

```bash
pip install mailslurp-client
```

On some systems you may need to install `distutils`.

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

### List inboxes

```python
def test_can_list_inboxes(self):
    # use the with keyword to create an api client
    with mailslurp_client.ApiClient(configuration) as api_client:
        # create an inbox using the inbox controller
        inbox_controller = mailslurp_client.InboxControllerApi(api_client)
        inboxes = inbox_controller.get_all_inboxes(page=0)

        # pagination properties
        assert inboxes.total_pages > 0
        assert inboxes.total_elements > 0

        # view contents
        assert len(inboxes.content[0].id) > 0
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

### Use attachments
To send attachments first use the `AttachmentControllerApi` to upload a file or byte stream. Then use the attachment ID returned with subsequent send calls.

```python
@staticmethod
def upload_attachment():
    with mailslurp_client.ApiClient(configuration) as api_client:
        import base64

        file_bytes = "Your file's bytes".encode("utf-8")
        encoded_contents = base64.b64encode(file_bytes)
        attachment_controller = mailslurp_client.AttachmentControllerApi(api_client)

        upload_options = mailslurp_client.UploadAttachmentOptions(
            content_type="text/plain",
            filename="test.txt",
            base64_contents=str(encoded_contents, 'utf-8')
        )
        print("upload_options = {}".format(upload_options))
        return attachment_controller.upload_attachment(upload_options)
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
        send_email_options.attachments = self.upload_attachment() # see previous section

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

### Download attachments
```python

def receive_email_and_extract_content_example():
    with mailslurp_client.ApiClient(configuration) as api_client:
        # wait for email to be received by inbox 2
        email = wait_controller.wait_for_latest_email(inbox_id=inbox_2.id, timeout=30000, unread_only=True)

        # assert that the message was received
        assert email.inbox_id == inbox_2.id
        assert email.subject == "Hello"
        
        # attachment ids pressent
        assert len(email.attachments) == 1

        # download attachment content
        email_controller = mailslurp_client.EmailControllerApi(api_client)
        downloaded_bytes = email_controller.download_attachment(email.attachments[0], email.id)
        assert len(downloaded_bytes) > 0

        # alternatively download as base64 string with more meta data
        email_controller = mailslurp_client.EmailControllerApi(api_client)
        downloaded_attachment = email_controller.download_attachment_base64(email.attachments[0], email.id)
        assert downloaded_attachment.content_type == "text/plain"
        base64_contents = downloaded_attachment.base64_file_contents
        import base64
        attachment_bytes = base64.b64decode(base64_contents)
        assert len(attachment_bytes) > 0
```

### Verify email address
You can verify email addresses with MailSlurp. This will perform SMTP queries for the email address on your behalf.

```python
def test_validate_email(self):
    with mailslurp_client.ApiClient(configuration) as api_client:
        mailserver_controller = mailslurp_client.MailServerControllerApi(api_client)
        verify_options = mailslurp_client.VerifyEmailAddressOptions(email_address="test@gmail.com")
        result = mailserver_controller.verify_email_address(verify_options=verify_options)
        assert result.error is None
        assert result.is_valid is True
```

## SDK Documentation

See the [guides page](https://www.mailslurp.com/guides/) or [the examples](https://www.github.com/mailslurp/examples) or the [Method Documentation](./docs) for full usage.    
    """,
    long_description_content_type="text/markdown"
)
