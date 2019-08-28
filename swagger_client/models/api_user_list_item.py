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


class ApiUserListItem(object):
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
        'id': 'str',
        'is_active': 'bool',
        'is_admin': 'bool',
        'session_ttl': 'int',
        'updated_at': 'datetime',
        'username': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'id': 'id',
        'is_active': 'isActive',
        'is_admin': 'isAdmin',
        'session_ttl': 'sessionTTL',
        'updated_at': 'updatedAt',
        'username': 'username'
    }

    def __init__(self, created_at=None, id=None, is_active=None, is_admin=None, session_ttl=None, updated_at=None, username=None):  # noqa: E501
        """ApiUserListItem - a model defined in Swagger"""  # noqa: E501

        self._created_at = None
        self._id = None
        self._is_active = None
        self._is_admin = None
        self._session_ttl = None
        self._updated_at = None
        self._username = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if id is not None:
            self.id = id
        if is_active is not None:
            self.is_active = is_active
        if is_admin is not None:
            self.is_admin = is_admin
        if session_ttl is not None:
            self.session_ttl = session_ttl
        if updated_at is not None:
            self.updated_at = updated_at
        if username is not None:
            self.username = username

    @property
    def created_at(self):
        """Gets the created_at of this ApiUserListItem.  # noqa: E501

        Created at timestamp.  # noqa: E501

        :return: The created_at of this ApiUserListItem.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ApiUserListItem.

        Created at timestamp.  # noqa: E501

        :param created_at: The created_at of this ApiUserListItem.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this ApiUserListItem.  # noqa: E501

        User ID. Will be set automatically on create.  # noqa: E501

        :return: The id of this ApiUserListItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiUserListItem.

        User ID. Will be set automatically on create.  # noqa: E501

        :param id: The id of this ApiUserListItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_active(self):
        """Gets the is_active of this ApiUserListItem.  # noqa: E501

        Set to false to disable the user.  # noqa: E501

        :return: The is_active of this ApiUserListItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this ApiUserListItem.

        Set to false to disable the user.  # noqa: E501

        :param is_active: The is_active of this ApiUserListItem.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def is_admin(self):
        """Gets the is_admin of this ApiUserListItem.  # noqa: E501

        Set to true to make the user a global administrator.  # noqa: E501

        :return: The is_admin of this ApiUserListItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """Sets the is_admin of this ApiUserListItem.

        Set to true to make the user a global administrator.  # noqa: E501

        :param is_admin: The is_admin of this ApiUserListItem.  # noqa: E501
        :type: bool
        """

        self._is_admin = is_admin

    @property
    def session_ttl(self):
        """Gets the session_ttl of this ApiUserListItem.  # noqa: E501

        The session timeout, in minutes.  # noqa: E501

        :return: The session_ttl of this ApiUserListItem.  # noqa: E501
        :rtype: int
        """
        return self._session_ttl

    @session_ttl.setter
    def session_ttl(self, session_ttl):
        """Sets the session_ttl of this ApiUserListItem.

        The session timeout, in minutes.  # noqa: E501

        :param session_ttl: The session_ttl of this ApiUserListItem.  # noqa: E501
        :type: int
        """

        self._session_ttl = session_ttl

    @property
    def updated_at(self):
        """Gets the updated_at of this ApiUserListItem.  # noqa: E501

        Last update timestamp.  # noqa: E501

        :return: The updated_at of this ApiUserListItem.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ApiUserListItem.

        Last update timestamp.  # noqa: E501

        :param updated_at: The updated_at of this ApiUserListItem.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def username(self):
        """Gets the username of this ApiUserListItem.  # noqa: E501

        Username of the user.  # noqa: E501

        :return: The username of this ApiUserListItem.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ApiUserListItem.

        Username of the user.  # noqa: E501

        :param username: The username of this ApiUserListItem.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(ApiUserListItem, dict):
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
        if not isinstance(other, ApiUserListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other