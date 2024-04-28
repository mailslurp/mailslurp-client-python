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


class Email(object):
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
        'id': 'str',
        'user_id': 'str',
        'inbox_id': 'str',
        'domain_id': 'str',
        'to': 'list[str]',
        '_from': 'str',
        'sender': 'Sender',
        'recipients': 'EmailRecipients',
        'reply_to': 'str',
        'cc': 'list[str]',
        'bcc': 'list[str]',
        'headers': 'dict(str, str)',
        'headers_map': 'dict(str, list[str])',
        'attachments': 'list[str]',
        'subject': 'str',
        'body': 'str',
        'body_excerpt': 'str',
        'text_excerpt': 'str',
        'body_md5_hash': 'str',
        'is_html': 'bool',
        'charset': 'str',
        'analysis': 'EmailAnalysis',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'read': 'bool',
        'team_access': 'bool',
        'is_x_amp_html': 'bool',
        'body_part_content_types': 'list[str]',
        'html': 'bool',
        'xamp_html': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'userId',
        'inbox_id': 'inboxId',
        'domain_id': 'domainId',
        'to': 'to',
        '_from': 'from',
        'sender': 'sender',
        'recipients': 'recipients',
        'reply_to': 'replyTo',
        'cc': 'cc',
        'bcc': 'bcc',
        'headers': 'headers',
        'headers_map': 'headersMap',
        'attachments': 'attachments',
        'subject': 'subject',
        'body': 'body',
        'body_excerpt': 'bodyExcerpt',
        'text_excerpt': 'textExcerpt',
        'body_md5_hash': 'bodyMD5Hash',
        'is_html': 'isHTML',
        'charset': 'charset',
        'analysis': 'analysis',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'read': 'read',
        'team_access': 'teamAccess',
        'is_x_amp_html': 'isXAmpHtml',
        'body_part_content_types': 'bodyPartContentTypes',
        'html': 'html',
        'xamp_html': 'xampHtml'
    }

    def __init__(self, id=None, user_id=None, inbox_id=None, domain_id=None, to=None, _from=None, sender=None, recipients=None, reply_to=None, cc=None, bcc=None, headers=None, headers_map=None, attachments=None, subject=None, body=None, body_excerpt=None, text_excerpt=None, body_md5_hash=None, is_html=None, charset=None, analysis=None, created_at=None, updated_at=None, read=None, team_access=None, is_x_amp_html=None, body_part_content_types=None, html=None, xamp_html=None, local_vars_configuration=None):  # noqa: E501
        """Email - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._user_id = None
        self._inbox_id = None
        self._domain_id = None
        self._to = None
        self.__from = None
        self._sender = None
        self._recipients = None
        self._reply_to = None
        self._cc = None
        self._bcc = None
        self._headers = None
        self._headers_map = None
        self._attachments = None
        self._subject = None
        self._body = None
        self._body_excerpt = None
        self._text_excerpt = None
        self._body_md5_hash = None
        self._is_html = None
        self._charset = None
        self._analysis = None
        self._created_at = None
        self._updated_at = None
        self._read = None
        self._team_access = None
        self._is_x_amp_html = None
        self._body_part_content_types = None
        self._html = None
        self._xamp_html = None
        self.discriminator = None

        self.id = id
        self.user_id = user_id
        self.inbox_id = inbox_id
        self.domain_id = domain_id
        self.to = to
        self._from = _from
        self.sender = sender
        self.recipients = recipients
        self.reply_to = reply_to
        self.cc = cc
        self.bcc = bcc
        self.headers = headers
        self.headers_map = headers_map
        self.attachments = attachments
        self.subject = subject
        self.body = body
        self.body_excerpt = body_excerpt
        self.text_excerpt = text_excerpt
        self.body_md5_hash = body_md5_hash
        self.is_html = is_html
        self.charset = charset
        self.analysis = analysis
        self.created_at = created_at
        self.updated_at = updated_at
        self.read = read
        self.team_access = team_access
        self.is_x_amp_html = is_x_amp_html
        self.body_part_content_types = body_part_content_types
        if html is not None:
            self.html = html
        if xamp_html is not None:
            self.xamp_html = xamp_html

    @property
    def id(self):
        """Gets the id of this Email.  # noqa: E501

        ID of the email entity  # noqa: E501

        :return: The id of this Email.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Email.

        ID of the email entity  # noqa: E501

        :param id: The id of this Email.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this Email.  # noqa: E501

        ID of user that email belongs to  # noqa: E501

        :return: The user_id of this Email.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Email.

        ID of user that email belongs to  # noqa: E501

        :param user_id: The user_id of this Email.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def inbox_id(self):
        """Gets the inbox_id of this Email.  # noqa: E501

        ID of the inbox that received the email  # noqa: E501

        :return: The inbox_id of this Email.  # noqa: E501
        :rtype: str
        """
        return self._inbox_id

    @inbox_id.setter
    def inbox_id(self, inbox_id):
        """Sets the inbox_id of this Email.

        ID of the inbox that received the email  # noqa: E501

        :param inbox_id: The inbox_id of this Email.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and inbox_id is None:  # noqa: E501
            raise ValueError("Invalid value for `inbox_id`, must not be `None`")  # noqa: E501

        self._inbox_id = inbox_id

    @property
    def domain_id(self):
        """Gets the domain_id of this Email.  # noqa: E501

        ID of the domain that received the email  # noqa: E501

        :return: The domain_id of this Email.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this Email.

        ID of the domain that received the email  # noqa: E501

        :param domain_id: The domain_id of this Email.  # noqa: E501
        :type: str
        """

        self._domain_id = domain_id

    @property
    def to(self):
        """Gets the to of this Email.  # noqa: E501

        List of `To` recipient email addresses that the email was addressed to. See recipients object for names.  # noqa: E501

        :return: The to of this Email.  # noqa: E501
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this Email.

        List of `To` recipient email addresses that the email was addressed to. See recipients object for names.  # noqa: E501

        :param to: The to of this Email.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and to is None:  # noqa: E501
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def _from(self):
        """Gets the _from of this Email.  # noqa: E501

        Who the email was sent from. An email address - see fromName for the sender name.  # noqa: E501

        :return: The _from of this Email.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this Email.

        Who the email was sent from. An email address - see fromName for the sender name.  # noqa: E501

        :param _from: The _from of this Email.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def sender(self):
        """Gets the sender of this Email.  # noqa: E501


        :return: The sender of this Email.  # noqa: E501
        :rtype: Sender
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this Email.


        :param sender: The sender of this Email.  # noqa: E501
        :type: Sender
        """

        self._sender = sender

    @property
    def recipients(self):
        """Gets the recipients of this Email.  # noqa: E501


        :return: The recipients of this Email.  # noqa: E501
        :rtype: EmailRecipients
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this Email.


        :param recipients: The recipients of this Email.  # noqa: E501
        :type: EmailRecipients
        """

        self._recipients = recipients

    @property
    def reply_to(self):
        """Gets the reply_to of this Email.  # noqa: E501

        The `replyTo` field on the received email message  # noqa: E501

        :return: The reply_to of this Email.  # noqa: E501
        :rtype: str
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """Sets the reply_to of this Email.

        The `replyTo` field on the received email message  # noqa: E501

        :param reply_to: The reply_to of this Email.  # noqa: E501
        :type: str
        """

        self._reply_to = reply_to

    @property
    def cc(self):
        """Gets the cc of this Email.  # noqa: E501

        List of `CC` recipients email addresses that the email was addressed to. See recipients object for names.  # noqa: E501

        :return: The cc of this Email.  # noqa: E501
        :rtype: list[str]
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this Email.

        List of `CC` recipients email addresses that the email was addressed to. See recipients object for names.  # noqa: E501

        :param cc: The cc of this Email.  # noqa: E501
        :type: list[str]
        """

        self._cc = cc

    @property
    def bcc(self):
        """Gets the bcc of this Email.  # noqa: E501

        List of `BCC` recipients email addresses that the email was addressed to. See recipients object for names.  # noqa: E501

        :return: The bcc of this Email.  # noqa: E501
        :rtype: list[str]
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc):
        """Sets the bcc of this Email.

        List of `BCC` recipients email addresses that the email was addressed to. See recipients object for names.  # noqa: E501

        :param bcc: The bcc of this Email.  # noqa: E501
        :type: list[str]
        """

        self._bcc = bcc

    @property
    def headers(self):
        """Gets the headers of this Email.  # noqa: E501

        Collection of SMTP headers attached to email  # noqa: E501

        :return: The headers of this Email.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this Email.

        Collection of SMTP headers attached to email  # noqa: E501

        :param headers: The headers of this Email.  # noqa: E501
        :type: dict(str, str)
        """

        self._headers = headers

    @property
    def headers_map(self):
        """Gets the headers_map of this Email.  # noqa: E501

        Multi-value map of SMTP headers attached to email  # noqa: E501

        :return: The headers_map of this Email.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._headers_map

    @headers_map.setter
    def headers_map(self, headers_map):
        """Sets the headers_map of this Email.

        Multi-value map of SMTP headers attached to email  # noqa: E501

        :param headers_map: The headers_map of this Email.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._headers_map = headers_map

    @property
    def attachments(self):
        """Gets the attachments of this Email.  # noqa: E501

        List of IDs of attachments found in the email. Use these IDs with the Inbox and Email Controllers to download attachments and attachment meta data such as filesize, name, extension.  # noqa: E501

        :return: The attachments of this Email.  # noqa: E501
        :rtype: list[str]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this Email.

        List of IDs of attachments found in the email. Use these IDs with the Inbox and Email Controllers to download attachments and attachment meta data such as filesize, name, extension.  # noqa: E501

        :param attachments: The attachments of this Email.  # noqa: E501
        :type: list[str]
        """

        self._attachments = attachments

    @property
    def subject(self):
        """Gets the subject of this Email.  # noqa: E501

        The subject line of the email message as specified by SMTP subject header  # noqa: E501

        :return: The subject of this Email.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this Email.

        The subject line of the email message as specified by SMTP subject header  # noqa: E501

        :param subject: The subject of this Email.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def body(self):
        """Gets the body of this Email.  # noqa: E501

        The body of the email message as text parsed from the SMTP message body (does not include attachments). Fetch the raw content to access the SMTP message and use the attachments property to access attachments. The body is stored separately to the email entity so the body is not returned in paginated results only in full single email or wait requests.  # noqa: E501

        :return: The body of this Email.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this Email.

        The body of the email message as text parsed from the SMTP message body (does not include attachments). Fetch the raw content to access the SMTP message and use the attachments property to access attachments. The body is stored separately to the email entity so the body is not returned in paginated results only in full single email or wait requests.  # noqa: E501

        :param body: The body of this Email.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def body_excerpt(self):
        """Gets the body_excerpt of this Email.  # noqa: E501

        An excerpt of the body of the email message for quick preview. Takes HTML content part if exists falls back to TEXT content part if not  # noqa: E501

        :return: The body_excerpt of this Email.  # noqa: E501
        :rtype: str
        """
        return self._body_excerpt

    @body_excerpt.setter
    def body_excerpt(self, body_excerpt):
        """Sets the body_excerpt of this Email.

        An excerpt of the body of the email message for quick preview. Takes HTML content part if exists falls back to TEXT content part if not  # noqa: E501

        :param body_excerpt: The body_excerpt of this Email.  # noqa: E501
        :type: str
        """

        self._body_excerpt = body_excerpt

    @property
    def text_excerpt(self):
        """Gets the text_excerpt of this Email.  # noqa: E501

        An excerpt of the body of the email message for quick preview. Takes TEXT content part if exists  # noqa: E501

        :return: The text_excerpt of this Email.  # noqa: E501
        :rtype: str
        """
        return self._text_excerpt

    @text_excerpt.setter
    def text_excerpt(self, text_excerpt):
        """Sets the text_excerpt of this Email.

        An excerpt of the body of the email message for quick preview. Takes TEXT content part if exists  # noqa: E501

        :param text_excerpt: The text_excerpt of this Email.  # noqa: E501
        :type: str
        """

        self._text_excerpt = text_excerpt

    @property
    def body_md5_hash(self):
        """Gets the body_md5_hash of this Email.  # noqa: E501

        A hash signature of the email message using MD5. Useful for comparing emails without fetching full body.  # noqa: E501

        :return: The body_md5_hash of this Email.  # noqa: E501
        :rtype: str
        """
        return self._body_md5_hash

    @body_md5_hash.setter
    def body_md5_hash(self, body_md5_hash):
        """Sets the body_md5_hash of this Email.

        A hash signature of the email message using MD5. Useful for comparing emails without fetching full body.  # noqa: E501

        :param body_md5_hash: The body_md5_hash of this Email.  # noqa: E501
        :type: str
        """

        self._body_md5_hash = body_md5_hash

    @property
    def is_html(self):
        """Gets the is_html of this Email.  # noqa: E501

        Is the email body content type HTML?  # noqa: E501

        :return: The is_html of this Email.  # noqa: E501
        :rtype: bool
        """
        return self._is_html

    @is_html.setter
    def is_html(self, is_html):
        """Sets the is_html of this Email.

        Is the email body content type HTML?  # noqa: E501

        :param is_html: The is_html of this Email.  # noqa: E501
        :type: bool
        """

        self._is_html = is_html

    @property
    def charset(self):
        """Gets the charset of this Email.  # noqa: E501

        Detected character set of the email body such as UTF-8  # noqa: E501

        :return: The charset of this Email.  # noqa: E501
        :rtype: str
        """
        return self._charset

    @charset.setter
    def charset(self, charset):
        """Sets the charset of this Email.

        Detected character set of the email body such as UTF-8  # noqa: E501

        :param charset: The charset of this Email.  # noqa: E501
        :type: str
        """

        self._charset = charset

    @property
    def analysis(self):
        """Gets the analysis of this Email.  # noqa: E501


        :return: The analysis of this Email.  # noqa: E501
        :rtype: EmailAnalysis
        """
        return self._analysis

    @analysis.setter
    def analysis(self, analysis):
        """Sets the analysis of this Email.


        :param analysis: The analysis of this Email.  # noqa: E501
        :type: EmailAnalysis
        """

        self._analysis = analysis

    @property
    def created_at(self):
        """Gets the created_at of this Email.  # noqa: E501

        When was the email received by MailSlurp  # noqa: E501

        :return: The created_at of this Email.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Email.

        When was the email received by MailSlurp  # noqa: E501

        :param created_at: The created_at of this Email.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Email.  # noqa: E501

        When was the email last updated  # noqa: E501

        :return: The updated_at of this Email.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Email.

        When was the email last updated  # noqa: E501

        :param updated_at: The updated_at of this Email.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def read(self):
        """Gets the read of this Email.  # noqa: E501

        Read flag. Has the email ever been viewed in the dashboard or fetched via the API with a hydrated body? If so the email is marked as read. Paginated results do not affect read status. Read status is different to email opened event as it depends on your own account accessing the email. Email opened is determined by tracking pixels sent to other uses if enable during sending. You can listened for both email read and email opened events using webhooks.  # noqa: E501

        :return: The read of this Email.  # noqa: E501
        :rtype: bool
        """
        return self._read

    @read.setter
    def read(self, read):
        """Sets the read of this Email.

        Read flag. Has the email ever been viewed in the dashboard or fetched via the API with a hydrated body? If so the email is marked as read. Paginated results do not affect read status. Read status is different to email opened event as it depends on your own account accessing the email. Email opened is determined by tracking pixels sent to other uses if enable during sending. You can listened for both email read and email opened events using webhooks.  # noqa: E501

        :param read: The read of this Email.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and read is None:  # noqa: E501
            raise ValueError("Invalid value for `read`, must not be `None`")  # noqa: E501

        self._read = read

    @property
    def team_access(self):
        """Gets the team_access of this Email.  # noqa: E501

        Can the email be accessed by organization team members  # noqa: E501

        :return: The team_access of this Email.  # noqa: E501
        :rtype: bool
        """
        return self._team_access

    @team_access.setter
    def team_access(self, team_access):
        """Sets the team_access of this Email.

        Can the email be accessed by organization team members  # noqa: E501

        :param team_access: The team_access of this Email.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and team_access is None:  # noqa: E501
            raise ValueError("Invalid value for `team_access`, must not be `None`")  # noqa: E501

        self._team_access = team_access

    @property
    def is_x_amp_html(self):
        """Gets the is_x_amp_html of this Email.  # noqa: E501

        Is the email body content type x-amp-html Amp4Email?  # noqa: E501

        :return: The is_x_amp_html of this Email.  # noqa: E501
        :rtype: bool
        """
        return self._is_x_amp_html

    @is_x_amp_html.setter
    def is_x_amp_html(self, is_x_amp_html):
        """Sets the is_x_amp_html of this Email.

        Is the email body content type x-amp-html Amp4Email?  # noqa: E501

        :param is_x_amp_html: The is_x_amp_html of this Email.  # noqa: E501
        :type: bool
        """

        self._is_x_amp_html = is_x_amp_html

    @property
    def body_part_content_types(self):
        """Gets the body_part_content_types of this Email.  # noqa: E501

        A list of detected multipart mime message body part content types such as text/plain and text/html. Can be used with email bodyPart endpoints to fetch individual body parts.  # noqa: E501

        :return: The body_part_content_types of this Email.  # noqa: E501
        :rtype: list[str]
        """
        return self._body_part_content_types

    @body_part_content_types.setter
    def body_part_content_types(self, body_part_content_types):
        """Sets the body_part_content_types of this Email.

        A list of detected multipart mime message body part content types such as text/plain and text/html. Can be used with email bodyPart endpoints to fetch individual body parts.  # noqa: E501

        :param body_part_content_types: The body_part_content_types of this Email.  # noqa: E501
        :type: list[str]
        """

        self._body_part_content_types = body_part_content_types

    @property
    def html(self):
        """Gets the html of this Email.  # noqa: E501


        :return: The html of this Email.  # noqa: E501
        :rtype: bool
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this Email.


        :param html: The html of this Email.  # noqa: E501
        :type: bool
        """

        self._html = html

    @property
    def xamp_html(self):
        """Gets the xamp_html of this Email.  # noqa: E501


        :return: The xamp_html of this Email.  # noqa: E501
        :rtype: bool
        """
        return self._xamp_html

    @xamp_html.setter
    def xamp_html(self, xamp_html):
        """Sets the xamp_html of this Email.


        :param xamp_html: The xamp_html of this Email.  # noqa: E501
        :type: bool
        """

        self._xamp_html = xamp_html

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
        if not isinstance(other, Email):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Email):
            return True

        return self.to_dict() != other.to_dict()
