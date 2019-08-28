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

from swagger_client.models.api_uplink_rx_info import ApiUplinkRXInfo  # noqa: F401,E501
from swagger_client.models.gw_uplink_tx_info import GwUplinkTXInfo  # noqa: F401,E501


class ApiUplinkFrameLog(object):
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
        'phy_payload_json': 'str',
        'rx_info': 'list[ApiUplinkRXInfo]',
        'tx_info': 'GwUplinkTXInfo'
    }

    attribute_map = {
        'phy_payload_json': 'phyPayloadJSON',
        'rx_info': 'rxInfo',
        'tx_info': 'txInfo'
    }

    def __init__(self, phy_payload_json=None, rx_info=None, tx_info=None):  # noqa: E501
        """ApiUplinkFrameLog - a model defined in Swagger"""  # noqa: E501

        self._phy_payload_json = None
        self._rx_info = None
        self._tx_info = None
        self.discriminator = None

        if phy_payload_json is not None:
            self.phy_payload_json = phy_payload_json
        if rx_info is not None:
            self.rx_info = rx_info
        if tx_info is not None:
            self.tx_info = tx_info

    @property
    def phy_payload_json(self):
        """Gets the phy_payload_json of this ApiUplinkFrameLog.  # noqa: E501

        LoRaWAN PHYPayload.  # noqa: E501

        :return: The phy_payload_json of this ApiUplinkFrameLog.  # noqa: E501
        :rtype: str
        """
        return self._phy_payload_json

    @phy_payload_json.setter
    def phy_payload_json(self, phy_payload_json):
        """Sets the phy_payload_json of this ApiUplinkFrameLog.

        LoRaWAN PHYPayload.  # noqa: E501

        :param phy_payload_json: The phy_payload_json of this ApiUplinkFrameLog.  # noqa: E501
        :type: str
        """

        self._phy_payload_json = phy_payload_json

    @property
    def rx_info(self):
        """Gets the rx_info of this ApiUplinkFrameLog.  # noqa: E501

        RX information of the uplink.  # noqa: E501

        :return: The rx_info of this ApiUplinkFrameLog.  # noqa: E501
        :rtype: list[ApiUplinkRXInfo]
        """
        return self._rx_info

    @rx_info.setter
    def rx_info(self, rx_info):
        """Sets the rx_info of this ApiUplinkFrameLog.

        RX information of the uplink.  # noqa: E501

        :param rx_info: The rx_info of this ApiUplinkFrameLog.  # noqa: E501
        :type: list[ApiUplinkRXInfo]
        """

        self._rx_info = rx_info

    @property
    def tx_info(self):
        """Gets the tx_info of this ApiUplinkFrameLog.  # noqa: E501

        TX information of the uplink.  # noqa: E501

        :return: The tx_info of this ApiUplinkFrameLog.  # noqa: E501
        :rtype: GwUplinkTXInfo
        """
        return self._tx_info

    @tx_info.setter
    def tx_info(self, tx_info):
        """Sets the tx_info of this ApiUplinkFrameLog.

        TX information of the uplink.  # noqa: E501

        :param tx_info: The tx_info of this ApiUplinkFrameLog.  # noqa: E501
        :type: GwUplinkTXInfo
        """

        self._tx_info = tx_info

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
        if issubclass(ApiUplinkFrameLog, dict):
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
        if not isinstance(other, ApiUplinkFrameLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
