# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails and SMS from dynamically allocated email addresses and phone numbers. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.  ## Resources  - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://docs.mailslurp.com/) - [Examples](https://github.com/mailslurp/examples) repository  # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Contact: contact@mailslurp.dev
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class CreateInboxDto(object):
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
        'email_address': 'str',
        'domain_name': 'str',
        'domain_id': 'str',
        'name': 'str',
        'description': 'str',
        'use_domain_pool': 'bool',
        'tags': 'list[str]',
        'expires_at': 'datetime',
        'favourite': 'bool',
        'expires_in': 'int',
        'allow_team_access': 'bool',
        'inbox_type': 'str',
        'virtual_inbox': 'bool',
        'use_short_address': 'bool',
        'prefix': 'str'
    }

    attribute_map = {
        'email_address': 'emailAddress',
        'domain_name': 'domainName',
        'domain_id': 'domainId',
        'name': 'name',
        'description': 'description',
        'use_domain_pool': 'useDomainPool',
        'tags': 'tags',
        'expires_at': 'expiresAt',
        'favourite': 'favourite',
        'expires_in': 'expiresIn',
        'allow_team_access': 'allowTeamAccess',
        'inbox_type': 'inboxType',
        'virtual_inbox': 'virtualInbox',
        'use_short_address': 'useShortAddress',
        'prefix': 'prefix'
    }

    def __init__(self, email_address=None, domain_name=None, domain_id=None, name=None, description=None, use_domain_pool=None, tags=None, expires_at=None, favourite=None, expires_in=None, allow_team_access=None, inbox_type=None, virtual_inbox=None, use_short_address=None, prefix=None, local_vars_configuration=None):  # noqa: E501
        """CreateInboxDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email_address = None
        self._domain_name = None
        self._domain_id = None
        self._name = None
        self._description = None
        self._use_domain_pool = None
        self._tags = None
        self._expires_at = None
        self._favourite = None
        self._expires_in = None
        self._allow_team_access = None
        self._inbox_type = None
        self._virtual_inbox = None
        self._use_short_address = None
        self._prefix = None
        self.discriminator = None

        self.email_address = email_address
        self.domain_name = domain_name
        self.domain_id = domain_id
        self.name = name
        self.description = description
        self.use_domain_pool = use_domain_pool
        self.tags = tags
        self.expires_at = expires_at
        self.favourite = favourite
        self.expires_in = expires_in
        self.allow_team_access = allow_team_access
        self.inbox_type = inbox_type
        self.virtual_inbox = virtual_inbox
        self.use_short_address = use_short_address
        self.prefix = prefix

    @property
    def email_address(self):
        """Gets the email_address of this CreateInboxDto.  # noqa: E501

        A custom email address to use with the inbox. Defaults to null. When null MailSlurp will assign a random email address to the inbox such as `123@mailslurp.com`. If you use the `useDomainPool` option when the email address is null it will generate an email address with a more varied domain ending such as `123@mailslurp.info` or `123@mailslurp.biz`. When a custom email address is provided the address is split into a domain and the domain is queried against your user. If you have created the domain in the MailSlurp dashboard and verified it you can use any email address that ends with the domain. Note domain types must match the inbox type - so `SMTP` inboxes will only work with `SMTP` type domains. Avoid `SMTP` inboxes if you need to send emails as they can only receive. Send an email to this address and the inbox will receive and store it for you. To retrieve the email use the Inbox and Email Controller endpoints with the inbox ID.  # noqa: E501

        :return: The email_address of this CreateInboxDto.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this CreateInboxDto.

        A custom email address to use with the inbox. Defaults to null. When null MailSlurp will assign a random email address to the inbox such as `123@mailslurp.com`. If you use the `useDomainPool` option when the email address is null it will generate an email address with a more varied domain ending such as `123@mailslurp.info` or `123@mailslurp.biz`. When a custom email address is provided the address is split into a domain and the domain is queried against your user. If you have created the domain in the MailSlurp dashboard and verified it you can use any email address that ends with the domain. Note domain types must match the inbox type - so `SMTP` inboxes will only work with `SMTP` type domains. Avoid `SMTP` inboxes if you need to send emails as they can only receive. Send an email to this address and the inbox will receive and store it for you. To retrieve the email use the Inbox and Email Controller endpoints with the inbox ID.  # noqa: E501

        :param email_address: The email_address of this CreateInboxDto.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def domain_name(self):
        """Gets the domain_name of this CreateInboxDto.  # noqa: E501

        FQDN domain name for the domain you have verified. Will be appended with a randomly assigned recipient name. Use the `emailAddress` option instead to specify the full custom inbox.  # noqa: E501

        :return: The domain_name of this CreateInboxDto.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this CreateInboxDto.

        FQDN domain name for the domain you have verified. Will be appended with a randomly assigned recipient name. Use the `emailAddress` option instead to specify the full custom inbox.  # noqa: E501

        :param domain_name: The domain_name of this CreateInboxDto.  # noqa: E501
        :type: str
        """

        self._domain_name = domain_name

    @property
    def domain_id(self):
        """Gets the domain_id of this CreateInboxDto.  # noqa: E501

        ID of custom domain to use for email address.  # noqa: E501

        :return: The domain_id of this CreateInboxDto.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this CreateInboxDto.

        ID of custom domain to use for email address.  # noqa: E501

        :param domain_id: The domain_id of this CreateInboxDto.  # noqa: E501
        :type: str
        """

        self._domain_id = domain_id

    @property
    def name(self):
        """Gets the name of this CreateInboxDto.  # noqa: E501

        Optional name of the inbox. Displayed in the dashboard for easier search and used as the sender name when sending emails.  # noqa: E501

        :return: The name of this CreateInboxDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateInboxDto.

        Optional name of the inbox. Displayed in the dashboard for easier search and used as the sender name when sending emails.  # noqa: E501

        :param name: The name of this CreateInboxDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateInboxDto.  # noqa: E501

        Optional description of the inbox for labelling purposes. Is shown in the dashboard and can be used with  # noqa: E501

        :return: The description of this CreateInboxDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateInboxDto.

        Optional description of the inbox for labelling purposes. Is shown in the dashboard and can be used with  # noqa: E501

        :param description: The description of this CreateInboxDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def use_domain_pool(self):
        """Gets the use_domain_pool of this CreateInboxDto.  # noqa: E501

        Use the MailSlurp domain name pool with this inbox when creating the email address. Defaults to null. If enabled the inbox will be an email address with a domain randomly chosen from a list of the MailSlurp domains. This is useful when the default `@mailslurp.com` email addresses used with inboxes are blocked or considered spam by a provider or receiving service. When domain pool is enabled an email address will be generated ending in `@mailslurp.{world,info,xyz,...}` . This means a TLD is randomly selecting from a list of `.biz`, `.info`, `.xyz` etc to add variance to the generated email addresses. When null or false MailSlurp uses the default behavior of `@mailslurp.com` or custom email address provided by the emailAddress field. Note this feature is only available for `HTTP` inbox types.  # noqa: E501

        :return: The use_domain_pool of this CreateInboxDto.  # noqa: E501
        :rtype: bool
        """
        return self._use_domain_pool

    @use_domain_pool.setter
    def use_domain_pool(self, use_domain_pool):
        """Sets the use_domain_pool of this CreateInboxDto.

        Use the MailSlurp domain name pool with this inbox when creating the email address. Defaults to null. If enabled the inbox will be an email address with a domain randomly chosen from a list of the MailSlurp domains. This is useful when the default `@mailslurp.com` email addresses used with inboxes are blocked or considered spam by a provider or receiving service. When domain pool is enabled an email address will be generated ending in `@mailslurp.{world,info,xyz,...}` . This means a TLD is randomly selecting from a list of `.biz`, `.info`, `.xyz` etc to add variance to the generated email addresses. When null or false MailSlurp uses the default behavior of `@mailslurp.com` or custom email address provided by the emailAddress field. Note this feature is only available for `HTTP` inbox types.  # noqa: E501

        :param use_domain_pool: The use_domain_pool of this CreateInboxDto.  # noqa: E501
        :type: bool
        """

        self._use_domain_pool = use_domain_pool

    @property
    def tags(self):
        """Gets the tags of this CreateInboxDto.  # noqa: E501

        Tags that inbox has been tagged with. Tags can be added to inboxes to group different inboxes within an account. You can also search for inboxes by tag in the dashboard UI.  # noqa: E501

        :return: The tags of this CreateInboxDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateInboxDto.

        Tags that inbox has been tagged with. Tags can be added to inboxes to group different inboxes within an account. You can also search for inboxes by tag in the dashboard UI.  # noqa: E501

        :param tags: The tags of this CreateInboxDto.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def expires_at(self):
        """Gets the expires_at of this CreateInboxDto.  # noqa: E501

        Optional inbox expiration date. If null then this inbox is permanent and the emails in it won't be deleted. If an expiration date is provided or is required by your plan the inbox will be closed when the expiration time is reached. Expired inboxes still contain their emails but can no longer send or receive emails. An ExpiredInboxRecord is created when an inbox and the email address and inbox ID are recorded. The expiresAt property is a timestamp string in ISO DateTime Format yyyy-MM-dd'T'HH:mm:ss.SSSXXX.  # noqa: E501

        :return: The expires_at of this CreateInboxDto.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this CreateInboxDto.

        Optional inbox expiration date. If null then this inbox is permanent and the emails in it won't be deleted. If an expiration date is provided or is required by your plan the inbox will be closed when the expiration time is reached. Expired inboxes still contain their emails but can no longer send or receive emails. An ExpiredInboxRecord is created when an inbox and the email address and inbox ID are recorded. The expiresAt property is a timestamp string in ISO DateTime Format yyyy-MM-dd'T'HH:mm:ss.SSSXXX.  # noqa: E501

        :param expires_at: The expires_at of this CreateInboxDto.  # noqa: E501
        :type: datetime
        """

        self._expires_at = expires_at

    @property
    def favourite(self):
        """Gets the favourite of this CreateInboxDto.  # noqa: E501

        Is the inbox a favorite. Marking an inbox as a favorite is typically done in the dashboard for quick access or filtering  # noqa: E501

        :return: The favourite of this CreateInboxDto.  # noqa: E501
        :rtype: bool
        """
        return self._favourite

    @favourite.setter
    def favourite(self, favourite):
        """Sets the favourite of this CreateInboxDto.

        Is the inbox a favorite. Marking an inbox as a favorite is typically done in the dashboard for quick access or filtering  # noqa: E501

        :param favourite: The favourite of this CreateInboxDto.  # noqa: E501
        :type: bool
        """

        self._favourite = favourite

    @property
    def expires_in(self):
        """Gets the expires_in of this CreateInboxDto.  # noqa: E501

        Number of milliseconds that inbox should exist for  # noqa: E501

        :return: The expires_in of this CreateInboxDto.  # noqa: E501
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this CreateInboxDto.

        Number of milliseconds that inbox should exist for  # noqa: E501

        :param expires_in: The expires_in of this CreateInboxDto.  # noqa: E501
        :type: int
        """

        self._expires_in = expires_in

    @property
    def allow_team_access(self):
        """Gets the allow_team_access of this CreateInboxDto.  # noqa: E501

        DEPRECATED (team access is always true). Grant team access to this inbox and the emails that belong to it for team members of your organization.  # noqa: E501

        :return: The allow_team_access of this CreateInboxDto.  # noqa: E501
        :rtype: bool
        """
        return self._allow_team_access

    @allow_team_access.setter
    def allow_team_access(self, allow_team_access):
        """Sets the allow_team_access of this CreateInboxDto.

        DEPRECATED (team access is always true). Grant team access to this inbox and the emails that belong to it for team members of your organization.  # noqa: E501

        :param allow_team_access: The allow_team_access of this CreateInboxDto.  # noqa: E501
        :type: bool
        """

        self._allow_team_access = allow_team_access

    @property
    def inbox_type(self):
        """Gets the inbox_type of this CreateInboxDto.  # noqa: E501

        Type of inbox. HTTP inboxes are faster and better for most cases. SMTP inboxes are more suited for public facing inbound messages (but cannot send).  # noqa: E501

        :return: The inbox_type of this CreateInboxDto.  # noqa: E501
        :rtype: str
        """
        return self._inbox_type

    @inbox_type.setter
    def inbox_type(self, inbox_type):
        """Sets the inbox_type of this CreateInboxDto.

        Type of inbox. HTTP inboxes are faster and better for most cases. SMTP inboxes are more suited for public facing inbound messages (but cannot send).  # noqa: E501

        :param inbox_type: The inbox_type of this CreateInboxDto.  # noqa: E501
        :type: str
        """
        allowed_values = [None,"HTTP_INBOX", "SMTP_INBOX"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and inbox_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `inbox_type` ({0}), must be one of {1}"  # noqa: E501
                .format(inbox_type, allowed_values)
            )

        self._inbox_type = inbox_type

    @property
    def virtual_inbox(self):
        """Gets the virtual_inbox of this CreateInboxDto.  # noqa: E501

        Virtual inbox prevents any outbound emails from being sent. It creates sent email records but will never send real emails to recipients. Great for testing and faking email sending.  # noqa: E501

        :return: The virtual_inbox of this CreateInboxDto.  # noqa: E501
        :rtype: bool
        """
        return self._virtual_inbox

    @virtual_inbox.setter
    def virtual_inbox(self, virtual_inbox):
        """Sets the virtual_inbox of this CreateInboxDto.

        Virtual inbox prevents any outbound emails from being sent. It creates sent email records but will never send real emails to recipients. Great for testing and faking email sending.  # noqa: E501

        :param virtual_inbox: The virtual_inbox of this CreateInboxDto.  # noqa: E501
        :type: bool
        """

        self._virtual_inbox = virtual_inbox

    @property
    def use_short_address(self):
        """Gets the use_short_address of this CreateInboxDto.  # noqa: E501

        Use a shorter email address under 31 characters  # noqa: E501

        :return: The use_short_address of this CreateInboxDto.  # noqa: E501
        :rtype: bool
        """
        return self._use_short_address

    @use_short_address.setter
    def use_short_address(self, use_short_address):
        """Sets the use_short_address of this CreateInboxDto.

        Use a shorter email address under 31 characters  # noqa: E501

        :param use_short_address: The use_short_address of this CreateInboxDto.  # noqa: E501
        :type: bool
        """

        self._use_short_address = use_short_address

    @property
    def prefix(self):
        """Gets the prefix of this CreateInboxDto.  # noqa: E501

        Prefix to add before the email address for easier labelling or identification.  # noqa: E501

        :return: The prefix of this CreateInboxDto.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this CreateInboxDto.

        Prefix to add before the email address for easier labelling or identification.  # noqa: E501

        :param prefix: The prefix of this CreateInboxDto.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

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
        if not isinstance(other, CreateInboxDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateInboxDto):
            return True

        return self.to_dict() != other.to_dict()
