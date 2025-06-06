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


class CreateEmergencyAddressOptions(object):
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
        'customer_name': 'str',
        'address1': 'str',
        'city': 'str',
        'region': 'str',
        'postal_code': 'str',
        'iso_country_code': 'str',
        'display_name': 'str'
    }

    attribute_map = {
        'customer_name': 'customerName',
        'address1': 'address1',
        'city': 'city',
        'region': 'region',
        'postal_code': 'postalCode',
        'iso_country_code': 'isoCountryCode',
        'display_name': 'displayName'
    }

    def __init__(self, customer_name=None, address1=None, city=None, region=None, postal_code=None, iso_country_code=None, display_name=None, local_vars_configuration=None):  # noqa: E501
        """CreateEmergencyAddressOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._customer_name = None
        self._address1 = None
        self._city = None
        self._region = None
        self._postal_code = None
        self._iso_country_code = None
        self._display_name = None
        self.discriminator = None

        self.customer_name = customer_name
        self.address1 = address1
        self.city = city
        self.region = region
        self.postal_code = postal_code
        self.iso_country_code = iso_country_code
        if display_name is not None:
            self.display_name = display_name

    @property
    def customer_name(self):
        """Gets the customer_name of this CreateEmergencyAddressOptions.  # noqa: E501


        :return: The customer_name of this CreateEmergencyAddressOptions.  # noqa: E501
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """Sets the customer_name of this CreateEmergencyAddressOptions.


        :param customer_name: The customer_name of this CreateEmergencyAddressOptions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and customer_name is None:  # noqa: E501
            raise ValueError("Invalid value for `customer_name`, must not be `None`")  # noqa: E501

        self._customer_name = customer_name

    @property
    def address1(self):
        """Gets the address1 of this CreateEmergencyAddressOptions.  # noqa: E501


        :return: The address1 of this CreateEmergencyAddressOptions.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this CreateEmergencyAddressOptions.


        :param address1: The address1 of this CreateEmergencyAddressOptions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and address1 is None:  # noqa: E501
            raise ValueError("Invalid value for `address1`, must not be `None`")  # noqa: E501

        self._address1 = address1

    @property
    def city(self):
        """Gets the city of this CreateEmergencyAddressOptions.  # noqa: E501


        :return: The city of this CreateEmergencyAddressOptions.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this CreateEmergencyAddressOptions.


        :param city: The city of this CreateEmergencyAddressOptions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and city is None:  # noqa: E501
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def region(self):
        """Gets the region of this CreateEmergencyAddressOptions.  # noqa: E501


        :return: The region of this CreateEmergencyAddressOptions.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CreateEmergencyAddressOptions.


        :param region: The region of this CreateEmergencyAddressOptions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and region is None:  # noqa: E501
            raise ValueError("Invalid value for `region`, must not be `None`")  # noqa: E501

        self._region = region

    @property
    def postal_code(self):
        """Gets the postal_code of this CreateEmergencyAddressOptions.  # noqa: E501


        :return: The postal_code of this CreateEmergencyAddressOptions.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this CreateEmergencyAddressOptions.


        :param postal_code: The postal_code of this CreateEmergencyAddressOptions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and postal_code is None:  # noqa: E501
            raise ValueError("Invalid value for `postal_code`, must not be `None`")  # noqa: E501

        self._postal_code = postal_code

    @property
    def iso_country_code(self):
        """Gets the iso_country_code of this CreateEmergencyAddressOptions.  # noqa: E501


        :return: The iso_country_code of this CreateEmergencyAddressOptions.  # noqa: E501
        :rtype: str
        """
        return self._iso_country_code

    @iso_country_code.setter
    def iso_country_code(self, iso_country_code):
        """Sets the iso_country_code of this CreateEmergencyAddressOptions.


        :param iso_country_code: The iso_country_code of this CreateEmergencyAddressOptions.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and iso_country_code is None:  # noqa: E501
            raise ValueError("Invalid value for `iso_country_code`, must not be `None`")  # noqa: E501
        allowed_values = ["US", "GB", "AU", "CA", "EE", "HK", "PL", "CH", "PT", "NL", "IL", "SE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and iso_country_code not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `iso_country_code` ({0}), must be one of {1}"  # noqa: E501
                .format(iso_country_code, allowed_values)
            )

        self._iso_country_code = iso_country_code

    @property
    def display_name(self):
        """Gets the display_name of this CreateEmergencyAddressOptions.  # noqa: E501


        :return: The display_name of this CreateEmergencyAddressOptions.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CreateEmergencyAddressOptions.


        :param display_name: The display_name of this CreateEmergencyAddressOptions.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

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
        if not isinstance(other, CreateEmergencyAddressOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateEmergencyAddressOptions):
            return True

        return self.to_dict() != other.to_dict()
