# MailSlurp Python Client

> Create real email addresses on demand. Send and receive emails and attachments from code and tests using Python.

MailSlurp is an email API service that lets you create real email addresses in code. You can then send and receive emails and attachments in Python applications and tests.

## Quick links

- [Method Documentation](https://mailslurp.github.io/mailslurp-client-python/)
- [PyPI Package](https://pypi.org/project/mailslurp-client/)
- [Github Source](https://github.com/mailslurp/mailslurp-client-python)
- [Send email using SMTP in Python](https://www.mailslurp.com/smtp/python-send-email-smtp/)
- [SMTP access details](https://www.mailslurp.com/guides/smtp-imap/)

## Get started

This section describes how to get up and running with the Python client.

See the [examples page](https://www.mailslurp.com/examples/) for more examples and use with common frameworks such as Django, Flask and Pytest.

See the method documentation for a [list of all functions](https://mailslurp.github.io/mailslurp-client-python/) or jump to common controllers below:

- [InboxController](https://mailslurp.github.io/mailslurp-client-python/api/inbox_controller_api.html)
- [EmailController](https://mailslurp.github.io/mailslurp-client-python/api/email_controller_api.html)
- [SMSController](https://mailslurp.github.io/mailslurp-client-python/api/sms_controller_api.html)
- [WaitForController](https://mailslurp.github.io/mailslurp-client-python/api/wait_for_controller_api.html)

### Create API Key

First you'll need an API Key. [Create a free account](https://app.mailslurp.com) and copy the key from your dashboard.

### Install package

MailSlurp has an official PyPI package called `mailslurp-client`. It supports Python version 2 and 3.

```bash
pip install mailslurp-client
```

On some systems you may need to install `distutils`.

### Configure

Once installed you can import `mailslurp_client` and create a [configuration](https://mailslurp.github.io/mailslurp-client-python/configuration.html) with your [API Key](https://app.mailslurp.com).

```python
import mailslurp_client

configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = "your-api-key-here"
```

Then you can create API controller instances using the configuration:

```python
with mailslurp_client.ApiClient(configuration) as api_client:

    # create an inbox using the inbox controller
    api_instance = mailslurp_client.InboxControllerApi(api_client)
```

See the [controllers overview](https://mailslurp.github.io/mailslurp-client-python/api/index.html) for all API methods.

## Common usage

MailSlurp can be used to create email addresses than can send and receive real emails, SMS, and attachments in Python. 

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

See the [inbox controller](https://mailslurp.github.io/mailslurp-client-python/api/inbox_controller_api.html) for more methods.

#### Inbox types

Inboxes can be either `SMTP` or `HTTP` type. Set the inbox type using the `inboxType` property. SMTP inboxes are handled by a custom mailserver and support a wide range of clients while HTTP inboxes use Amazon SES and don't support some older clients like Outlook. SMTP inboxes are recommended for public facing email addresses while HTTP inboxes are best for application testing. Please see the guide on [types of inboxes](https://www.mailslurp.com/guides/smtp-vs-http-email-inboxes/) for more information.

### List inboxes

List inboxes using the [inbox controller](https://mailslurp.github.io/mailslurp-client-python/api/inbox_controller_api.html):

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
Send emails with the [inbox controller](https://mailslurp.github.io/mailslurp-client-python/api/inbox_controller_api.html):

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

### Send email using SMTP
To use SMTP clients first create an SMTP type inbox and use the inbox controller `get_imap_smtp_access` method on the [inbox controller](https://mailslurp.github.io/mailslurp-client-python/api/inbox_controller_api.html) to obtain the username, password, port and host.

```python
import os
import mailslurp_client
from smtplib import SMTP
from mailslurp_client import CreateInboxDto

api_key = os.environ.get('API_KEY')
assert api_key is not None

# create a mailslurp configuration
configuration = mailslurp_client.Configuration()
configuration.api_key['x-api-key'] = api_key


class Test_MailSlurp_SDK:
    # Can send email with SMTP
    def test_can_send_with_smtp(self):
        with mailslurp_client.ApiClient(configuration) as api_client:
            # create an SMTP inbox
            inbox_controller = mailslurp_client.InboxControllerApi(api_client)
            inbox1 = inbox_controller.create_inbox_with_options(CreateInboxDto(inbox_type="SMTP_INBOX"))
            inbox2 = inbox_controller.create_inbox()
            assert "@mailslurp.mx" in inbox1.email_address

            # get smtp imap access
            smtp_access = inbox_controller.get_imap_smtp_access(inbox_id=inbox1.id)
            msg = "Subject: Test subject\r\n\r\nThis is the body"

            # configure smtp client using access details
            with SMTP(host=smtp_access.smtp_server_host, port=smtp_access.smtp_server_port) as smtp:
                smtp.login(user=smtp_access.smtp_username, password=smtp_access.smtp_password)
                smtp.sendmail(from_addr=inbox1.email_address, to_addrs=[inbox2.email_address], msg=msg)
                smtp.quit()

            # test that email is sent
            wait_for_controller = mailslurp_client.WaitForControllerApi(api_client)
            email = wait_for_controller.wait_for_latest_email(inbox_id=inbox2.id)
            assert "Test subject" in email.subject
```

### Use attachments

To send attachments first use the [attachment controller](https://mailslurp.github.io/mailslurp-client-python/api/attachment_controller_api.html) to upload a file or byte stream. Then use the attachment ID returned with subsequent send calls.

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
Use the [wait for controller](https://mailslurp.github.io/mailslurp-client-python/api/wait_for_controller_api.html) to wait for an expected email count to be satisfied and then return those emails.

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

See the [guides page](https://www.mailslurp.com/guides/) or [the examples](https://www.github.com/mailslurp/examples) or the [Method Documentation](https://mailslurp.github.io/mailslurp-client-python/) for full usage.
