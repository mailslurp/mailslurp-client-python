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


class PageConnectorSyncEvents(object):
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
        'content': 'list[ConnectorSyncEventProjection]',
        'pageable': 'PageableObject',
        'total_pages': 'int',
        'total_elements': 'int',
        'last': 'bool',
        'number_of_elements': 'int',
        'first': 'bool',
        'size': 'int',
        'number': 'int',
        'sort': 'SortObject',
        'empty': 'bool'
    }

    attribute_map = {
        'content': 'content',
        'pageable': 'pageable',
        'total_pages': 'totalPages',
        'total_elements': 'totalElements',
        'last': 'last',
        'number_of_elements': 'numberOfElements',
        'first': 'first',
        'size': 'size',
        'number': 'number',
        'sort': 'sort',
        'empty': 'empty'
    }

    def __init__(self, content=None, pageable=None, total_pages=None, total_elements=None, last=None, number_of_elements=None, first=None, size=None, number=None, sort=None, empty=None, local_vars_configuration=None):  # noqa: E501
        """PageConnectorSyncEvents - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._content = None
        self._pageable = None
        self._total_pages = None
        self._total_elements = None
        self._last = None
        self._number_of_elements = None
        self._first = None
        self._size = None
        self._number = None
        self._sort = None
        self._empty = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if pageable is not None:
            self.pageable = pageable
        self.total_pages = total_pages
        self.total_elements = total_elements
        if last is not None:
            self.last = last
        if number_of_elements is not None:
            self.number_of_elements = number_of_elements
        if first is not None:
            self.first = first
        if size is not None:
            self.size = size
        if number is not None:
            self.number = number
        if sort is not None:
            self.sort = sort
        if empty is not None:
            self.empty = empty

    @property
    def content(self):
        """Gets the content of this PageConnectorSyncEvents.  # noqa: E501


        :return: The content of this PageConnectorSyncEvents.  # noqa: E501
        :rtype: list[ConnectorSyncEventProjection]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this PageConnectorSyncEvents.


        :param content: The content of this PageConnectorSyncEvents.  # noqa: E501
        :type: list[ConnectorSyncEventProjection]
        """

        self._content = content

    @property
    def pageable(self):
        """Gets the pageable of this PageConnectorSyncEvents.  # noqa: E501


        :return: The pageable of this PageConnectorSyncEvents.  # noqa: E501
        :rtype: PageableObject
        """
        return self._pageable

    @pageable.setter
    def pageable(self, pageable):
        """Sets the pageable of this PageConnectorSyncEvents.


        :param pageable: The pageable of this PageConnectorSyncEvents.  # noqa: E501
        :type: PageableObject
        """

        self._pageable = pageable

    @property
    def total_pages(self):
        """Gets the total_pages of this PageConnectorSyncEvents.  # noqa: E501


        :return: The total_pages of this PageConnectorSyncEvents.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this PageConnectorSyncEvents.


        :param total_pages: The total_pages of this PageConnectorSyncEvents.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_pages is None:  # noqa: E501
            raise ValueError("Invalid value for `total_pages`, must not be `None`")  # noqa: E501

        self._total_pages = total_pages

    @property
    def total_elements(self):
        """Gets the total_elements of this PageConnectorSyncEvents.  # noqa: E501


        :return: The total_elements of this PageConnectorSyncEvents.  # noqa: E501
        :rtype: int
        """
        return self._total_elements

    @total_elements.setter
    def total_elements(self, total_elements):
        """Sets the total_elements of this PageConnectorSyncEvents.


        :param total_elements: The total_elements of this PageConnectorSyncEvents.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_elements is None:  # noqa: E501
            raise ValueError("Invalid value for `total_elements`, must not be `None`")  # noqa: E501

        self._total_elements = total_elements

    @property
    def last(self):
        """Gets the last of this PageConnectorSyncEvents.  # noqa: E501


        :return: The last of this PageConnectorSyncEvents.  # noqa: E501
        :rtype: bool
        """
        return self._last

    @last.setter
    def last(self, last):
        """Sets the last of this PageConnectorSyncEvents.


        :param last: The last of this PageConnectorSyncEvents.  # noqa: E501
        :type: bool
        """

        self._last = last

    @property
    def number_of_elements(self):
        """Gets the number_of_elements of this PageConnectorSyncEvents.  # noqa: E501


        :return: The number_of_elements of this PageConnectorSyncEvents.  # noqa: E501
        :rtype: int
        """
        return self._number_of_elements

    @number_of_elements.setter
    def number_of_elements(self, number_of_elements):
        """Sets the number_of_elements of this PageConnectorSyncEvents.


        :param number_of_elements: The number_of_elements of this PageConnectorSyncEvents.  # noqa: E501
        :type: int
        """

        self._number_of_elements = number_of_elements

    @property
    def first(self):
        """Gets the first of this PageConnectorSyncEvents.  # noqa: E501


        :return: The first of this PageConnectorSyncEvents.  # noqa: E501
        :rtype: bool
        """
        return self._first

    @first.setter
    def first(self, first):
        """Sets the first of this PageConnectorSyncEvents.


        :param first: The first of this PageConnectorSyncEvents.  # noqa: E501
        :type: bool
        """

        self._first = first

    @property
    def size(self):
        """Gets the size of this PageConnectorSyncEvents.  # noqa: E501


        :return: The size of this PageConnectorSyncEvents.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this PageConnectorSyncEvents.


        :param size: The size of this PageConnectorSyncEvents.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def number(self):
        """Gets the number of this PageConnectorSyncEvents.  # noqa: E501


        :return: The number of this PageConnectorSyncEvents.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this PageConnectorSyncEvents.


        :param number: The number of this PageConnectorSyncEvents.  # noqa: E501
        :type: int
        """

        self._number = number

    @property
    def sort(self):
        """Gets the sort of this PageConnectorSyncEvents.  # noqa: E501


        :return: The sort of this PageConnectorSyncEvents.  # noqa: E501
        :rtype: SortObject
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this PageConnectorSyncEvents.


        :param sort: The sort of this PageConnectorSyncEvents.  # noqa: E501
        :type: SortObject
        """

        self._sort = sort

    @property
    def empty(self):
        """Gets the empty of this PageConnectorSyncEvents.  # noqa: E501


        :return: The empty of this PageConnectorSyncEvents.  # noqa: E501
        :rtype: bool
        """
        return self._empty

    @empty.setter
    def empty(self, empty):
        """Sets the empty of this PageConnectorSyncEvents.


        :param empty: The empty of this PageConnectorSyncEvents.  # noqa: E501
        :type: bool
        """

        self._empty = empty

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
        if not isinstance(other, PageConnectorSyncEvents):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PageConnectorSyncEvents):
            return True

        return self.to_dict() != other.to_dict()
