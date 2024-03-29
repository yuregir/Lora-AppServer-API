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


class ApiGatewayProfileListItem(object):
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
        'name': 'str',
        'network_server_id': 'str',
        'network_server_name': 'str',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'id': 'id',
        'name': 'name',
        'network_server_id': 'networkServerID',
        'network_server_name': 'networkServerName',
        'updated_at': 'updatedAt'
    }

    def __init__(self, created_at=None, id=None, name=None, network_server_id=None, network_server_name=None, updated_at=None):  # noqa: E501
        """ApiGatewayProfileListItem - a model defined in Swagger"""  # noqa: E501

        self._created_at = None
        self._id = None
        self._name = None
        self._network_server_id = None
        self._network_server_name = None
        self._updated_at = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if network_server_id is not None:
            self.network_server_id = network_server_id
        if network_server_name is not None:
            self.network_server_name = network_server_name
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this ApiGatewayProfileListItem.  # noqa: E501

        Created at timestamp.  # noqa: E501

        :return: The created_at of this ApiGatewayProfileListItem.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ApiGatewayProfileListItem.

        Created at timestamp.  # noqa: E501

        :param created_at: The created_at of this ApiGatewayProfileListItem.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this ApiGatewayProfileListItem.  # noqa: E501

        Gateway-profile ID (UUID string).  # noqa: E501

        :return: The id of this ApiGatewayProfileListItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiGatewayProfileListItem.

        Gateway-profile ID (UUID string).  # noqa: E501

        :param id: The id of this ApiGatewayProfileListItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ApiGatewayProfileListItem.  # noqa: E501

        Gateway-profile name,  # noqa: E501

        :return: The name of this ApiGatewayProfileListItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiGatewayProfileListItem.

        Gateway-profile name,  # noqa: E501

        :param name: The name of this ApiGatewayProfileListItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def network_server_id(self):
        """Gets the network_server_id of this ApiGatewayProfileListItem.  # noqa: E501

        Network-server ID on which the gateway-profile is provisioned.  # noqa: E501

        :return: The network_server_id of this ApiGatewayProfileListItem.  # noqa: E501
        :rtype: str
        """
        return self._network_server_id

    @network_server_id.setter
    def network_server_id(self, network_server_id):
        """Sets the network_server_id of this ApiGatewayProfileListItem.

        Network-server ID on which the gateway-profile is provisioned.  # noqa: E501

        :param network_server_id: The network_server_id of this ApiGatewayProfileListItem.  # noqa: E501
        :type: str
        """

        self._network_server_id = network_server_id

    @property
    def network_server_name(self):
        """Gets the network_server_name of this ApiGatewayProfileListItem.  # noqa: E501

        Network-server name.  # noqa: E501

        :return: The network_server_name of this ApiGatewayProfileListItem.  # noqa: E501
        :rtype: str
        """
        return self._network_server_name

    @network_server_name.setter
    def network_server_name(self, network_server_name):
        """Sets the network_server_name of this ApiGatewayProfileListItem.

        Network-server name.  # noqa: E501

        :param network_server_name: The network_server_name of this ApiGatewayProfileListItem.  # noqa: E501
        :type: str
        """

        self._network_server_name = network_server_name

    @property
    def updated_at(self):
        """Gets the updated_at of this ApiGatewayProfileListItem.  # noqa: E501

        Last update timestamp.  # noqa: E501

        :return: The updated_at of this ApiGatewayProfileListItem.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ApiGatewayProfileListItem.

        Last update timestamp.  # noqa: E501

        :param updated_at: The updated_at of this ApiGatewayProfileListItem.  # noqa: E501
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
        if issubclass(ApiGatewayProfileListItem, dict):
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
        if not isinstance(other, ApiGatewayProfileListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
