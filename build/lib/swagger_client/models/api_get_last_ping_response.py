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

from swagger_client.models.api_ping_rx import ApiPingRX  # noqa: F401,E501


class ApiGetLastPingResponse(object):
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
        'dr': 'int',
        'frequency': 'int',
        'ping_rx': 'list[ApiPingRX]'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'dr': 'dr',
        'frequency': 'frequency',
        'ping_rx': 'pingRX'
    }

    def __init__(self, created_at=None, dr=None, frequency=None, ping_rx=None):  # noqa: E501
        """ApiGetLastPingResponse - a model defined in Swagger"""  # noqa: E501

        self._created_at = None
        self._dr = None
        self._frequency = None
        self._ping_rx = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if dr is not None:
            self.dr = dr
        if frequency is not None:
            self.frequency = frequency
        if ping_rx is not None:
            self.ping_rx = ping_rx

    @property
    def created_at(self):
        """Gets the created_at of this ApiGetLastPingResponse.  # noqa: E501

        Created at timestamp.  # noqa: E501

        :return: The created_at of this ApiGetLastPingResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ApiGetLastPingResponse.

        Created at timestamp.  # noqa: E501

        :param created_at: The created_at of this ApiGetLastPingResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def dr(self):
        """Gets the dr of this ApiGetLastPingResponse.  # noqa: E501

        Data-rate.  # noqa: E501

        :return: The dr of this ApiGetLastPingResponse.  # noqa: E501
        :rtype: int
        """
        return self._dr

    @dr.setter
    def dr(self, dr):
        """Sets the dr of this ApiGetLastPingResponse.

        Data-rate.  # noqa: E501

        :param dr: The dr of this ApiGetLastPingResponse.  # noqa: E501
        :type: int
        """

        self._dr = dr

    @property
    def frequency(self):
        """Gets the frequency of this ApiGetLastPingResponse.  # noqa: E501

        Frequency (Hz).  # noqa: E501

        :return: The frequency of this ApiGetLastPingResponse.  # noqa: E501
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this ApiGetLastPingResponse.

        Frequency (Hz).  # noqa: E501

        :param frequency: The frequency of this ApiGetLastPingResponse.  # noqa: E501
        :type: int
        """

        self._frequency = frequency

    @property
    def ping_rx(self):
        """Gets the ping_rx of this ApiGetLastPingResponse.  # noqa: E501

        Gateways and meta-data of reception.  # noqa: E501

        :return: The ping_rx of this ApiGetLastPingResponse.  # noqa: E501
        :rtype: list[ApiPingRX]
        """
        return self._ping_rx

    @ping_rx.setter
    def ping_rx(self, ping_rx):
        """Sets the ping_rx of this ApiGetLastPingResponse.

        Gateways and meta-data of reception.  # noqa: E501

        :param ping_rx: The ping_rx of this ApiGetLastPingResponse.  # noqa: E501
        :type: list[ApiPingRX]
        """

        self._ping_rx = ping_rx

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
        if issubclass(ApiGetLastPingResponse, dict):
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
        if not isinstance(other, ApiGetLastPingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
