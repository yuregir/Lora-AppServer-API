# coding: utf-8

"""
    LoRa App Server REST API

     For more information about the usage of the LoRa App Server (REST) API, see [https://docs.loraserver.io/lora-app-server/api/](https://docs.loraserver.io/lora-app-server/api/).   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ApiOrganization(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'can_have_gateways': 'bool',
        'display_name': 'str',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'can_have_gateways': 'canHaveGateways',
        'display_name': 'displayName',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, can_have_gateways=None, display_name=None, id=None, name=None):  # noqa: E501
        """ApiOrganization - a model defined in Swagger"""  # noqa: E501

        self._can_have_gateways = None
        self._display_name = None
        self._id = None
        self._name = None
        self.discriminator = None

        if can_have_gateways is not None:
            self.can_have_gateways = can_have_gateways
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def can_have_gateways(self):
        """Gets the can_have_gateways of this ApiOrganization.  # noqa: E501

        Can the organization create and \"own\" Gateways?  # noqa: E501

        :return: The can_have_gateways of this ApiOrganization.  # noqa: E501
        :rtype: bool
        """
        return self._can_have_gateways

    @can_have_gateways.setter
    def can_have_gateways(self, can_have_gateways):
        """Sets the can_have_gateways of this ApiOrganization.

        Can the organization create and \"own\" Gateways?  # noqa: E501

        :param can_have_gateways: The can_have_gateways of this ApiOrganization.  # noqa: E501
        :type: bool
        """

        self._can_have_gateways = can_have_gateways

    @property
    def display_name(self):
        """Gets the display_name of this ApiOrganization.  # noqa: E501

        Organization display name.  # noqa: E501

        :return: The display_name of this ApiOrganization.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ApiOrganization.

        Organization display name.  # noqa: E501

        :param display_name: The display_name of this ApiOrganization.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this ApiOrganization.  # noqa: E501

        Organization ID.  # noqa: E501

        :return: The id of this ApiOrganization.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiOrganization.

        Organization ID.  # noqa: E501

        :param id: The id of this ApiOrganization.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ApiOrganization.  # noqa: E501

        Organization name.  # noqa: E501

        :return: The name of this ApiOrganization.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiOrganization.

        Organization name.  # noqa: E501

        :param name: The name of this ApiOrganization.  # noqa: E501
        :type: str
        """

        self._name = name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ApiOrganization, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApiOrganization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
