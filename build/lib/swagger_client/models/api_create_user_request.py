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

from swagger_client.models.api_user import ApiUser  # noqa: F401,E501
from swagger_client.models.api_user_organization import ApiUserOrganization  # noqa: F401,E501


class ApiCreateUserRequest(object):
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
        'organizations': 'list[ApiUserOrganization]',
        'password': 'str',
        'user': 'ApiUser'
    }

    attribute_map = {
        'organizations': 'organizations',
        'password': 'password',
        'user': 'user'
    }

    def __init__(self, organizations=None, password=None, user=None):  # noqa: E501
        """ApiCreateUserRequest - a model defined in Swagger"""  # noqa: E501

        self._organizations = None
        self._password = None
        self._user = None
        self.discriminator = None

        if organizations is not None:
            self.organizations = organizations
        if password is not None:
            self.password = password
        if user is not None:
            self.user = user

    @property
    def organizations(self):
        """Gets the organizations of this ApiCreateUserRequest.  # noqa: E501

        Add the user to the following organizations.  # noqa: E501

        :return: The organizations of this ApiCreateUserRequest.  # noqa: E501
        :rtype: list[ApiUserOrganization]
        """
        return self._organizations

    @organizations.setter
    def organizations(self, organizations):
        """Sets the organizations of this ApiCreateUserRequest.

        Add the user to the following organizations.  # noqa: E501

        :param organizations: The organizations of this ApiCreateUserRequest.  # noqa: E501
        :type: list[ApiUserOrganization]
        """

        self._organizations = organizations

    @property
    def password(self):
        """Gets the password of this ApiCreateUserRequest.  # noqa: E501

        Password of the user.  # noqa: E501

        :return: The password of this ApiCreateUserRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ApiCreateUserRequest.

        Password of the user.  # noqa: E501

        :param password: The password of this ApiCreateUserRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def user(self):
        """Gets the user of this ApiCreateUserRequest.  # noqa: E501

        User object to create.  # noqa: E501

        :return: The user of this ApiCreateUserRequest.  # noqa: E501
        :rtype: ApiUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ApiCreateUserRequest.

        User object to create.  # noqa: E501

        :param user: The user of this ApiCreateUserRequest.  # noqa: E501
        :type: ApiUser
        """

        self._user = user

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
        if issubclass(ApiCreateUserRequest, dict):
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
        if not isinstance(other, ApiCreateUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
