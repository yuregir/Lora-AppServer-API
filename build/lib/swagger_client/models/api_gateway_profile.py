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

from swagger_client.models.api_gateway_profile_extra_channel import ApiGatewayProfileExtraChannel  # noqa: F401,E501


class ApiGatewayProfile(object):
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
        'channels': 'list[int]',
        'extra_channels': 'list[ApiGatewayProfileExtraChannel]',
        'id': 'str',
        'name': 'str',
        'network_server_id': 'str'
    }

    attribute_map = {
        'channels': 'channels',
        'extra_channels': 'extraChannels',
        'id': 'id',
        'name': 'name',
        'network_server_id': 'networkServerID'
    }

    def __init__(self, channels=None, extra_channels=None, id=None, name=None, network_server_id=None):  # noqa: E501
        """ApiGatewayProfile - a model defined in Swagger"""  # noqa: E501

        self._channels = None
        self._extra_channels = None
        self._id = None
        self._name = None
        self._network_server_id = None
        self.discriminator = None

        if channels is not None:
            self.channels = channels
        if extra_channels is not None:
            self.extra_channels = extra_channels
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if network_server_id is not None:
            self.network_server_id = network_server_id

    @property
    def channels(self):
        """Gets the channels of this ApiGatewayProfile.  # noqa: E501

        Default channels (channels specified by the LoRaWAN Regional Parameters specification) enabled for this configuration.  # noqa: E501

        :return: The channels of this ApiGatewayProfile.  # noqa: E501
        :rtype: list[int]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this ApiGatewayProfile.

        Default channels (channels specified by the LoRaWAN Regional Parameters specification) enabled for this configuration.  # noqa: E501

        :param channels: The channels of this ApiGatewayProfile.  # noqa: E501
        :type: list[int]
        """

        self._channels = channels

    @property
    def extra_channels(self):
        """Gets the extra_channels of this ApiGatewayProfile.  # noqa: E501

        Extra channels added to the channel-configuration (in case the LoRaWAN region supports adding custom channels).  # noqa: E501

        :return: The extra_channels of this ApiGatewayProfile.  # noqa: E501
        :rtype: list[ApiGatewayProfileExtraChannel]
        """
        return self._extra_channels

    @extra_channels.setter
    def extra_channels(self, extra_channels):
        """Sets the extra_channels of this ApiGatewayProfile.

        Extra channels added to the channel-configuration (in case the LoRaWAN region supports adding custom channels).  # noqa: E501

        :param extra_channels: The extra_channels of this ApiGatewayProfile.  # noqa: E501
        :type: list[ApiGatewayProfileExtraChannel]
        """

        self._extra_channels = extra_channels

    @property
    def id(self):
        """Gets the id of this ApiGatewayProfile.  # noqa: E501

        Gateway-profile ID (UUID string).  # noqa: E501

        :return: The id of this ApiGatewayProfile.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiGatewayProfile.

        Gateway-profile ID (UUID string).  # noqa: E501

        :param id: The id of this ApiGatewayProfile.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ApiGatewayProfile.  # noqa: E501

        Name of the gateway-profile.  # noqa: E501

        :return: The name of this ApiGatewayProfile.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiGatewayProfile.

        Name of the gateway-profile.  # noqa: E501

        :param name: The name of this ApiGatewayProfile.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def network_server_id(self):
        """Gets the network_server_id of this ApiGatewayProfile.  # noqa: E501

        Network-server ID of the gateway-profile.  # noqa: E501

        :return: The network_server_id of this ApiGatewayProfile.  # noqa: E501
        :rtype: str
        """
        return self._network_server_id

    @network_server_id.setter
    def network_server_id(self, network_server_id):
        """Sets the network_server_id of this ApiGatewayProfile.

        Network-server ID of the gateway-profile.  # noqa: E501

        :param network_server_id: The network_server_id of this ApiGatewayProfile.  # noqa: E501
        :type: str
        """

        self._network_server_id = network_server_id

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
        if issubclass(ApiGatewayProfile, dict):
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
        if not isinstance(other, ApiGatewayProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other