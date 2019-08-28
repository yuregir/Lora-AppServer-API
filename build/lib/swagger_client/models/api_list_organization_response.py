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

from swagger_client.models.api_organization_list_item import ApiOrganizationListItem  # noqa: F401,E501


class ApiListOrganizationResponse(object):
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
        'result': 'list[ApiOrganizationListItem]',
        'total_count': 'str'
    }

    attribute_map = {
        'result': 'result',
        'total_count': 'totalCount'
    }

    def __init__(self, result=None, total_count=None):  # noqa: E501
        """ApiListOrganizationResponse - a model defined in Swagger"""  # noqa: E501

        self._result = None
        self._total_count = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if total_count is not None:
            self.total_count = total_count

    @property
    def result(self):
        """Gets the result of this ApiListOrganizationResponse.  # noqa: E501


        :return: The result of this ApiListOrganizationResponse.  # noqa: E501
        :rtype: list[ApiOrganizationListItem]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ApiListOrganizationResponse.


        :param result: The result of this ApiListOrganizationResponse.  # noqa: E501
        :type: list[ApiOrganizationListItem]
        """

        self._result = result

    @property
    def total_count(self):
        """Gets the total_count of this ApiListOrganizationResponse.  # noqa: E501

        Total number of organizations.  # noqa: E501

        :return: The total_count of this ApiListOrganizationResponse.  # noqa: E501
        :rtype: str
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ApiListOrganizationResponse.

        Total number of organizations.  # noqa: E501

        :param total_count: The total_count of this ApiListOrganizationResponse.  # noqa: E501
        :type: str
        """

        self._total_count = total_count

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
        if issubclass(ApiListOrganizationResponse, dict):
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
        if not isinstance(other, ApiListOrganizationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
