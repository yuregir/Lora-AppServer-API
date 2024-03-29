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

from swagger_client.models.api_device_profile import ApiDeviceProfile  # noqa: F401,E501


class ApiUpdateDeviceProfileRequest(object):
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
        'device_profile': 'ApiDeviceProfile'
    }

    attribute_map = {
        'device_profile': 'deviceProfile'
    }

    def __init__(self, device_profile=None):  # noqa: E501
        """ApiUpdateDeviceProfileRequest - a model defined in Swagger"""  # noqa: E501

        self._device_profile = None
        self.discriminator = None

        if device_profile is not None:
            self.device_profile = device_profile

    @property
    def device_profile(self):
        """Gets the device_profile of this ApiUpdateDeviceProfileRequest.  # noqa: E501

        Device-profile object to update.  # noqa: E501

        :return: The device_profile of this ApiUpdateDeviceProfileRequest.  # noqa: E501
        :rtype: ApiDeviceProfile
        """
        return self._device_profile

    @device_profile.setter
    def device_profile(self, device_profile):
        """Sets the device_profile of this ApiUpdateDeviceProfileRequest.

        Device-profile object to update.  # noqa: E501

        :param device_profile: The device_profile of this ApiUpdateDeviceProfileRequest.  # noqa: E501
        :type: ApiDeviceProfile
        """

        self._device_profile = device_profile

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
        if issubclass(ApiUpdateDeviceProfileRequest, dict):
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
        if not isinstance(other, ApiUpdateDeviceProfileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
