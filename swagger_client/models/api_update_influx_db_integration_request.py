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

from swagger_client.models.api_influx_db_integration import ApiInfluxDBIntegration  # noqa: F401,E501


class ApiUpdateInfluxDBIntegrationRequest(object):
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
        'integration': 'ApiInfluxDBIntegration'
    }

    attribute_map = {
        'integration': 'integration'
    }

    def __init__(self, integration=None):  # noqa: E501
        """ApiUpdateInfluxDBIntegrationRequest - a model defined in Swagger"""  # noqa: E501

        self._integration = None
        self.discriminator = None

        if integration is not None:
            self.integration = integration

    @property
    def integration(self):
        """Gets the integration of this ApiUpdateInfluxDBIntegrationRequest.  # noqa: E501

        Integration object.  # noqa: E501

        :return: The integration of this ApiUpdateInfluxDBIntegrationRequest.  # noqa: E501
        :rtype: ApiInfluxDBIntegration
        """
        return self._integration

    @integration.setter
    def integration(self, integration):
        """Sets the integration of this ApiUpdateInfluxDBIntegrationRequest.

        Integration object.  # noqa: E501

        :param integration: The integration of this ApiUpdateInfluxDBIntegrationRequest.  # noqa: E501
        :type: ApiInfluxDBIntegration
        """

        self._integration = integration

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
        if issubclass(ApiUpdateInfluxDBIntegrationRequest, dict):
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
        if not isinstance(other, ApiUpdateInfluxDBIntegrationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
