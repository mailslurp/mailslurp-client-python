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


class CreateConnectorImapFetchOptions(object):
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
        'select_folder': 'str',
        'search_terms': 'str'
    }

    attribute_map = {
        'select_folder': 'selectFolder',
        'search_terms': 'searchTerms'
    }

    def __init__(self, select_folder=None, search_terms=None, local_vars_configuration=None):  # noqa: E501
        """CreateConnectorImapFetchOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._select_folder = None
        self._search_terms = None
        self.discriminator = None

        if select_folder is not None:
            self.select_folder = select_folder
        if search_terms is not None:
            self.search_terms = search_terms

    @property
    def select_folder(self):
        """Gets the select_folder of this CreateConnectorImapFetchOptions.  # noqa: E501


        :return: The select_folder of this CreateConnectorImapFetchOptions.  # noqa: E501
        :rtype: str
        """
        return self._select_folder

    @select_folder.setter
    def select_folder(self, select_folder):
        """Sets the select_folder of this CreateConnectorImapFetchOptions.


        :param select_folder: The select_folder of this CreateConnectorImapFetchOptions.  # noqa: E501
        :type: str
        """

        self._select_folder = select_folder

    @property
    def search_terms(self):
        """Gets the search_terms of this CreateConnectorImapFetchOptions.  # noqa: E501


        :return: The search_terms of this CreateConnectorImapFetchOptions.  # noqa: E501
        :rtype: str
        """
        return self._search_terms

    @search_terms.setter
    def search_terms(self, search_terms):
        """Sets the search_terms of this CreateConnectorImapFetchOptions.


        :param search_terms: The search_terms of this CreateConnectorImapFetchOptions.  # noqa: E501
        :type: str
        """

        self._search_terms = search_terms

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
        if not isinstance(other, CreateConnectorImapFetchOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateConnectorImapFetchOptions):
            return True

        return self.to_dict() != other.to_dict()
