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


class InboxDto(object):
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
        'created_at': 'datetime',
        'name': 'str',
        'description': 'str',
        'email_address': 'str',
        'expires_at': 'str',
        'favourite': 'bool',
        'tags': 'list[str]',
        'inbox_type': 'str',
        'read_only': 'bool',
        'virtual_inbox': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'userId',
        'created_at': 'createdAt',
        'name': 'name',
        'description': 'description',
        'email_address': 'emailAddress',
        'expires_at': 'expiresAt',
        'favourite': 'favourite',
        'tags': 'tags',
        'inbox_type': 'inboxType',
        'read_only': 'readOnly',
        'virtual_inbox': 'virtualInbox'
    }

    def __init__(self, id=None, user_id=None, created_at=None, name=None, description=None, email_address=None, expires_at=None, favourite=None, tags=None, inbox_type=None, read_only=None, virtual_inbox=None, local_vars_configuration=None):  # noqa: E501
        """InboxDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._user_id = None
        self._created_at = None
        self._name = None
        self._description = None
        self._email_address = None
        self._expires_at = None
        self._favourite = None
        self._tags = None
        self._inbox_type = None
        self._read_only = None
        self._virtual_inbox = None
        self.discriminator = None

        self.id = id
        if user_id is not None:
            self.user_id = user_id
        self.created_at = created_at
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        self.email_address = email_address
        if expires_at is not None:
            self.expires_at = expires_at
        self.favourite = favourite
        if tags is not None:
            self.tags = tags
        if inbox_type is not None:
            self.inbox_type = inbox_type
        self.read_only = read_only
        self.virtual_inbox = virtual_inbox

    @property
    def id(self):
        """Gets the id of this InboxDto.  # noqa: E501

        ID of the inbox. The ID is a UUID-V4 format string. Use the inboxId for calls to Inbox and Email Controller endpoints. See the emailAddress property for the email address or the inbox. To get emails in an inbox use the WaitFor and Inbox Controller methods `waitForLatestEmail` and `getEmails` methods respectively. Inboxes can be used with aliases to forward emails automatically.  # noqa: E501

        :return: The id of this InboxDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InboxDto.

        ID of the inbox. The ID is a UUID-V4 format string. Use the inboxId for calls to Inbox and Email Controller endpoints. See the emailAddress property for the email address or the inbox. To get emails in an inbox use the WaitFor and Inbox Controller methods `waitForLatestEmail` and `getEmails` methods respectively. Inboxes can be used with aliases to forward emails automatically.  # noqa: E501

        :param id: The id of this InboxDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this InboxDto.  # noqa: E501

        ID of user that inbox belongs to  # noqa: E501

        :return: The user_id of this InboxDto.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this InboxDto.

        ID of user that inbox belongs to  # noqa: E501

        :param user_id: The user_id of this InboxDto.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def created_at(self):
        """Gets the created_at of this InboxDto.  # noqa: E501

        When the inbox was created. Time stamps are in ISO DateTime Format `yyyy-MM-dd'T'HH:mm:ss.SSSXXX` e.g. `2000-10-31T01:30:00.000-05:00`.  # noqa: E501

        :return: The created_at of this InboxDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InboxDto.

        When the inbox was created. Time stamps are in ISO DateTime Format `yyyy-MM-dd'T'HH:mm:ss.SSSXXX` e.g. `2000-10-31T01:30:00.000-05:00`.  # noqa: E501

        :param created_at: The created_at of this InboxDto.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def name(self):
        """Gets the name of this InboxDto.  # noqa: E501

        Name of the inbox and used as the sender name when sending emails .Displayed in the dashboard for easier search  # noqa: E501

        :return: The name of this InboxDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InboxDto.

        Name of the inbox and used as the sender name when sending emails .Displayed in the dashboard for easier search  # noqa: E501

        :param name: The name of this InboxDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this InboxDto.  # noqa: E501

        Description of an inbox for labelling and searching purposes  # noqa: E501

        :return: The description of this InboxDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InboxDto.

        Description of an inbox for labelling and searching purposes  # noqa: E501

        :param description: The description of this InboxDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def email_address(self):
        """Gets the email_address of this InboxDto.  # noqa: E501

        The inbox's email address. Inbox projections and previews may not include the email address. To view the email address fetch the inbox entity directly. Send an email to this address and the inbox will receive and store it for you. Note the email address in MailSlurp match characters exactly and are case sensitive so `+123` additions are considered different addresses. To retrieve the email use the Inbox and Email Controller endpoints with the inbox ID.  # noqa: E501

        :return: The email_address of this InboxDto.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this InboxDto.

        The inbox's email address. Inbox projections and previews may not include the email address. To view the email address fetch the inbox entity directly. Send an email to this address and the inbox will receive and store it for you. Note the email address in MailSlurp match characters exactly and are case sensitive so `+123` additions are considered different addresses. To retrieve the email use the Inbox and Email Controller endpoints with the inbox ID.  # noqa: E501

        :param email_address: The email_address of this InboxDto.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and email_address is None:  # noqa: E501
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def expires_at(self):
        """Gets the expires_at of this InboxDto.  # noqa: E501

        Inbox expiration time. When, if ever, the inbox should expire and be deleted. If null then this inbox is permanent and the emails in it won't be deleted. This is the default behavior unless expiration date is set. If an expiration date is set and the time is reached MailSlurp will expire the inbox and move it to an expired inbox entity. You can still access the emails belonging to it but it can no longer send or receive email.  # noqa: E501

        :return: The expires_at of this InboxDto.  # noqa: E501
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this InboxDto.

        Inbox expiration time. When, if ever, the inbox should expire and be deleted. If null then this inbox is permanent and the emails in it won't be deleted. This is the default behavior unless expiration date is set. If an expiration date is set and the time is reached MailSlurp will expire the inbox and move it to an expired inbox entity. You can still access the emails belonging to it but it can no longer send or receive email.  # noqa: E501

        :param expires_at: The expires_at of this InboxDto.  # noqa: E501
        :type: str
        """

        self._expires_at = expires_at

    @property
    def favourite(self):
        """Gets the favourite of this InboxDto.  # noqa: E501

        Is the inbox a favorite inbox. Make an inbox a favorite is typically done in the dashboard for quick access or filtering  # noqa: E501

        :return: The favourite of this InboxDto.  # noqa: E501
        :rtype: bool
        """
        return self._favourite

    @favourite.setter
    def favourite(self, favourite):
        """Sets the favourite of this InboxDto.

        Is the inbox a favorite inbox. Make an inbox a favorite is typically done in the dashboard for quick access or filtering  # noqa: E501

        :param favourite: The favourite of this InboxDto.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and favourite is None:  # noqa: E501
            raise ValueError("Invalid value for `favourite`, must not be `None`")  # noqa: E501

        self._favourite = favourite

    @property
    def tags(self):
        """Gets the tags of this InboxDto.  # noqa: E501

        Tags that inbox has been tagged with. Tags can be added to inboxes to group different inboxes within an account. You can also search for inboxes by tag in the dashboard UI.  # noqa: E501

        :return: The tags of this InboxDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this InboxDto.

        Tags that inbox has been tagged with. Tags can be added to inboxes to group different inboxes within an account. You can also search for inboxes by tag in the dashboard UI.  # noqa: E501

        :param tags: The tags of this InboxDto.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def inbox_type(self):
        """Gets the inbox_type of this InboxDto.  # noqa: E501

        Type of inbox. HTTP inboxes are faster and better for most cases. SMTP inboxes are more suited for public facing inbound messages (but cannot send).  # noqa: E501

        :return: The inbox_type of this InboxDto.  # noqa: E501
        :rtype: str
        """
        return self._inbox_type

    @inbox_type.setter
    def inbox_type(self, inbox_type):
        """Sets the inbox_type of this InboxDto.

        Type of inbox. HTTP inboxes are faster and better for most cases. SMTP inboxes are more suited for public facing inbound messages (but cannot send).  # noqa: E501

        :param inbox_type: The inbox_type of this InboxDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["HTTP_INBOX", "SMTP_INBOX"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and inbox_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `inbox_type` ({0}), must be one of {1}"  # noqa: E501
                .format(inbox_type, allowed_values)
            )

        self._inbox_type = inbox_type

    @property
    def read_only(self):
        """Gets the read_only of this InboxDto.  # noqa: E501

        Is the inbox readOnly for the caller. Read only means can not be deleted or modified. This flag is present when using team accounts and shared inboxes.  # noqa: E501

        :return: The read_only of this InboxDto.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this InboxDto.

        Is the inbox readOnly for the caller. Read only means can not be deleted or modified. This flag is present when using team accounts and shared inboxes.  # noqa: E501

        :param read_only: The read_only of this InboxDto.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and read_only is None:  # noqa: E501
            raise ValueError("Invalid value for `read_only`, must not be `None`")  # noqa: E501

        self._read_only = read_only

    @property
    def virtual_inbox(self):
        """Gets the virtual_inbox of this InboxDto.  # noqa: E501

        Virtual inbox can receive email but will not send emails to real recipients. Will save sent email record but never send an actual email. Perfect for testing mail server actions.  # noqa: E501

        :return: The virtual_inbox of this InboxDto.  # noqa: E501
        :rtype: bool
        """
        return self._virtual_inbox

    @virtual_inbox.setter
    def virtual_inbox(self, virtual_inbox):
        """Sets the virtual_inbox of this InboxDto.

        Virtual inbox can receive email but will not send emails to real recipients. Will save sent email record but never send an actual email. Perfect for testing mail server actions.  # noqa: E501

        :param virtual_inbox: The virtual_inbox of this InboxDto.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and virtual_inbox is None:  # noqa: E501
            raise ValueError("Invalid value for `virtual_inbox`, must not be `None`")  # noqa: E501

        self._virtual_inbox = virtual_inbox

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
        if not isinstance(other, InboxDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InboxDto):
            return True

        return self.to_dict() != other.to_dict()
