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


class ApiGatewayStats(object):
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
        'rx_packets_received': 'int',
        'rx_packets_received_ok': 'int',
        'timestamp': 'datetime',
        'tx_packets_emitted': 'int',
        'tx_packets_received': 'int'
    }

    attribute_map = {
        'rx_packets_received': 'rxPacketsReceived',
        'rx_packets_received_ok': 'rxPacketsReceivedOK',
        'timestamp': 'timestamp',
        'tx_packets_emitted': 'txPacketsEmitted',
        'tx_packets_received': 'txPacketsReceived'
    }

    def __init__(self, rx_packets_received=None, rx_packets_received_ok=None, timestamp=None, tx_packets_emitted=None, tx_packets_received=None):  # noqa: E501
        """ApiGatewayStats - a model defined in Swagger"""  # noqa: E501

        self._rx_packets_received = None
        self._rx_packets_received_ok = None
        self._timestamp = None
        self._tx_packets_emitted = None
        self._tx_packets_received = None
        self.discriminator = None

        if rx_packets_received is not None:
            self.rx_packets_received = rx_packets_received
        if rx_packets_received_ok is not None:
            self.rx_packets_received_ok = rx_packets_received_ok
        if timestamp is not None:
            self.timestamp = timestamp
        if tx_packets_emitted is not None:
            self.tx_packets_emitted = tx_packets_emitted
        if tx_packets_received is not None:
            self.tx_packets_received = tx_packets_received

    @property
    def rx_packets_received(self):
        """Gets the rx_packets_received of this ApiGatewayStats.  # noqa: E501

        Packets received by the gateway.  # noqa: E501

        :return: The rx_packets_received of this ApiGatewayStats.  # noqa: E501
        :rtype: int
        """
        return self._rx_packets_received

    @rx_packets_received.setter
    def rx_packets_received(self, rx_packets_received):
        """Sets the rx_packets_received of this ApiGatewayStats.

        Packets received by the gateway.  # noqa: E501

        :param rx_packets_received: The rx_packets_received of this ApiGatewayStats.  # noqa: E501
        :type: int
        """

        self._rx_packets_received = rx_packets_received

    @property
    def rx_packets_received_ok(self):
        """Gets the rx_packets_received_ok of this ApiGatewayStats.  # noqa: E501

        Packets received by the gateway that passed the CRC check.  # noqa: E501

        :return: The rx_packets_received_ok of this ApiGatewayStats.  # noqa: E501
        :rtype: int
        """
        return self._rx_packets_received_ok

    @rx_packets_received_ok.setter
    def rx_packets_received_ok(self, rx_packets_received_ok):
        """Sets the rx_packets_received_ok of this ApiGatewayStats.

        Packets received by the gateway that passed the CRC check.  # noqa: E501

        :param rx_packets_received_ok: The rx_packets_received_ok of this ApiGatewayStats.  # noqa: E501
        :type: int
        """

        self._rx_packets_received_ok = rx_packets_received_ok

    @property
    def timestamp(self):
        """Gets the timestamp of this ApiGatewayStats.  # noqa: E501

        Timestamp of the (aggregated) measurement.  # noqa: E501

        :return: The timestamp of this ApiGatewayStats.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ApiGatewayStats.

        Timestamp of the (aggregated) measurement.  # noqa: E501

        :param timestamp: The timestamp of this ApiGatewayStats.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def tx_packets_emitted(self):
        """Gets the tx_packets_emitted of this ApiGatewayStats.  # noqa: E501

        Packets transmitted by the gateway.  # noqa: E501

        :return: The tx_packets_emitted of this ApiGatewayStats.  # noqa: E501
        :rtype: int
        """
        return self._tx_packets_emitted

    @tx_packets_emitted.setter
    def tx_packets_emitted(self, tx_packets_emitted):
        """Sets the tx_packets_emitted of this ApiGatewayStats.

        Packets transmitted by the gateway.  # noqa: E501

        :param tx_packets_emitted: The tx_packets_emitted of this ApiGatewayStats.  # noqa: E501
        :type: int
        """

        self._tx_packets_emitted = tx_packets_emitted

    @property
    def tx_packets_received(self):
        """Gets the tx_packets_received of this ApiGatewayStats.  # noqa: E501

        Packets received by the gateway for transmission.  # noqa: E501

        :return: The tx_packets_received of this ApiGatewayStats.  # noqa: E501
        :rtype: int
        """
        return self._tx_packets_received

    @tx_packets_received.setter
    def tx_packets_received(self, tx_packets_received):
        """Sets the tx_packets_received of this ApiGatewayStats.

        Packets received by the gateway for transmission.  # noqa: E501

        :param tx_packets_received: The tx_packets_received of this ApiGatewayStats.  # noqa: E501
        :type: int
        """

        self._tx_packets_received = tx_packets_received

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
        if issubclass(ApiGatewayStats, dict):
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
        if not isinstance(other, ApiGatewayStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
