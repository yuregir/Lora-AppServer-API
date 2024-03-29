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

from swagger_client.models.api_service_profile import ApiServiceProfile  # noqa: F401,E501


class ApiGetServiceProfileResponse(object):
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
        'created_at': 'datetime',
        'service_profile': 'ApiServiceProfile',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'service_profile': 'serviceProfile',
        'updated_at': 'updatedAt'
    }

    def __init__(self, created_at=None, service_profile=None, updated_at=None):  # noqa: E501
        """ApiGetServiceProfileResponse - a model defined in Swagger"""  # noqa: E501

        self._created_at = None
        self._service_profile = None
        self._updated_at = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if service_profile is not None:
            self.service_profile = service_profile
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this ApiGetServiceProfileResponse.  # noqa: E501

        Created at timestamp.  # noqa: E501

        :return: The created_at of this ApiGetServiceProfileResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ApiGetServiceProfileResponse.

        Created at timestamp.  # noqa: E501

        :param created_at: The created_at of this ApiGetServiceProfileResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def service_profile(self):
        """Gets the service_profile of this ApiGetServiceProfileResponse.  # noqa: E501

        Service-profile object.  # noqa: E501

        :return: The service_profile of this ApiGetServiceProfileResponse.  # noqa: E501
        :rtype: ApiServiceProfile
        """
        return self._service_profile

    @service_profile.setter
    def service_profile(self, service_profile):
        """Sets the service_profile of this ApiGetServiceProfileResponse.

        Service-profile object.  # noqa: E501

        :param service_profile: The service_profile of this ApiGetServiceProfileResponse.  # noqa: E501
        :type: ApiServiceProfile
        """

        self._service_profile = service_profile

    @property
    def updated_at(self):
        """Gets the updated_at of this ApiGetServiceProfileResponse.  # noqa: E501

        Last update timestamp.  # noqa: E501

        :return: The updated_at of this ApiGetServiceProfileResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ApiGetServiceProfileResponse.

        Last update timestamp.  # noqa: E501

        :param updated_at: The updated_at of this ApiGetServiceProfileResponse.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if issubclass(ApiGetServiceProfileResponse, dict):
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
        if not isinstance(other, ApiGetServiceProfileResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
