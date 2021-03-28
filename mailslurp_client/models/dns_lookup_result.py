# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.   ## Resources - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository   # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class DNSLookupResult(object):
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
        'name': 'str',
        'record_entries': 'list[str]',
        'record_type': 'str',
        'ttl': 'int'
    }

    attribute_map = {
        'name': 'name',
        'record_entries': 'recordEntries',
        'record_type': 'recordType',
        'ttl': 'ttl'
    }

    def __init__(self, name=None, record_entries=None, record_type=None, ttl=None, local_vars_configuration=None):  # noqa: E501
        """DNSLookupResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._record_entries = None
        self._record_type = None
        self._ttl = None
        self.discriminator = None

        self.name = name
        self.record_entries = record_entries
        self.record_type = record_type
        self.ttl = ttl

    @property
    def name(self):
        """Gets the name of this DNSLookupResult.  # noqa: E501


        :return: The name of this DNSLookupResult.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DNSLookupResult.


        :param name: The name of this DNSLookupResult.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def record_entries(self):
        """Gets the record_entries of this DNSLookupResult.  # noqa: E501


        :return: The record_entries of this DNSLookupResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._record_entries

    @record_entries.setter
    def record_entries(self, record_entries):
        """Sets the record_entries of this DNSLookupResult.


        :param record_entries: The record_entries of this DNSLookupResult.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and record_entries is None:  # noqa: E501
            raise ValueError("Invalid value for `record_entries`, must not be `None`")  # noqa: E501

        self._record_entries = record_entries

    @property
    def record_type(self):
        """Gets the record_type of this DNSLookupResult.  # noqa: E501


        :return: The record_type of this DNSLookupResult.  # noqa: E501
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        """Sets the record_type of this DNSLookupResult.


        :param record_type: The record_type of this DNSLookupResult.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and record_type is None:  # noqa: E501
            raise ValueError("Invalid value for `record_type`, must not be `None`")  # noqa: E501
        allowed_values = ["A", "NS", "MD", "MF", "CNAME", "SOA", "MB", "MG", "MR", "NULL", "WKS", "PTR", "HINFO", "MINFO", "MX", "TXT", "RP", "AFSDB", "X25", "ISDN", "RT", "NSAP", "NSAP_PTR", "SIG", "KEY", "PX", "GPOS", "AAAA", "LOC", "NXT", "EID", "NIMLOC", "SRV", "ATMA", "NAPTR", "KX", "CERT", "A6", "DNAME", "SINK", "OPT", "APL", "DS", "SSHFP", "IPSECKEY", "RRSIG", "NSEC", "DNSKEY", "DHCID", "NSEC3", "NSEC3PARAM", "TLSA", "SMIMEA", "HIP", "NINFO", "RKEY", "TALINK", "CDS", "CDNSKEY", "OPENPGPKEY", "CSYNC", "ZONEMD", "SVCB", "HTTPS", "SPF", "UINFO", "UID", "GID", "UNSPEC", "NID", "L32", "L64", "LP", "EUI48", "EUI64", "TKEY", "TSIG", "IXFR", "AXFR", "MAILB", "MAILA", "ANY", "URI", "CAA", "AVC", "DOA", "AMTRELAY", "TA", "DLV"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and record_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `record_type` ({0}), must be one of {1}"  # noqa: E501
                .format(record_type, allowed_values)
            )

        self._record_type = record_type

    @property
    def ttl(self):
        """Gets the ttl of this DNSLookupResult.  # noqa: E501


        :return: The ttl of this DNSLookupResult.  # noqa: E501
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this DNSLookupResult.


        :param ttl: The ttl of this DNSLookupResult.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and ttl is None:  # noqa: E501
            raise ValueError("Invalid value for `ttl`, must not be `None`")  # noqa: E501

        self._ttl = ttl

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
        if not isinstance(other, DNSLookupResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DNSLookupResult):
            return True

        return self.to_dict() != other.to_dict()