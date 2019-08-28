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

from swagger_client.models.api_downlink_frame_log import ApiDownlinkFrameLog  # noqa: F401,E501
from swagger_client.models.api_uplink_frame_log import ApiUplinkFrameLog  # noqa: F401,E501


class ApiStreamGatewayFrameLogsResponse(object):
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
        'downlink_frame': 'ApiDownlinkFrameLog',
        'uplink_frame': 'ApiUplinkFrameLog'
    }

    attribute_map = {
        'downlink_frame': 'downlinkFrame',
        'uplink_frame': 'uplinkFrame'
    }

    def __init__(self, downlink_frame=None, uplink_frame=None):  # noqa: E501
        """ApiStreamGatewayFrameLogsResponse - a model defined in Swagger"""  # noqa: E501

        self._downlink_frame = None
        self._uplink_frame = None
        self.discriminator = None

        if downlink_frame is not None:
            self.downlink_frame = downlink_frame
        if uplink_frame is not None:
            self.uplink_frame = uplink_frame

    @property
    def downlink_frame(self):
        """Gets the downlink_frame of this ApiStreamGatewayFrameLogsResponse.  # noqa: E501

        Contains a downlink frame.  # noqa: E501

        :return: The downlink_frame of this ApiStreamGatewayFrameLogsResponse.  # noqa: E501
        :rtype: ApiDownlinkFrameLog
        """
        return self._downlink_frame

    @downlink_frame.setter
    def downlink_frame(self, downlink_frame):
        """Sets the downlink_frame of this ApiStreamGatewayFrameLogsResponse.

        Contains a downlink frame.  # noqa: E501

        :param downlink_frame: The downlink_frame of this ApiStreamGatewayFrameLogsResponse.  # noqa: E501
        :type: ApiDownlinkFrameLog
        """

        self._downlink_frame = downlink_frame

    @property
    def uplink_frame(self):
        """Gets the uplink_frame of this ApiStreamGatewayFrameLogsResponse.  # noqa: E501

        Contains an uplink frame.  # noqa: E501

        :return: The uplink_frame of this ApiStreamGatewayFrameLogsResponse.  # noqa: E501
        :rtype: ApiUplinkFrameLog
        """
        return self._uplink_frame

    @uplink_frame.setter
    def uplink_frame(self, uplink_frame):
        """Sets the uplink_frame of this ApiStreamGatewayFrameLogsResponse.

        Contains an uplink frame.  # noqa: E501

        :param uplink_frame: The uplink_frame of this ApiStreamGatewayFrameLogsResponse.  # noqa: E501
        :type: ApiUplinkFrameLog
        """

        self._uplink_frame = uplink_frame

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
        if issubclass(ApiStreamGatewayFrameLogsResponse, dict):
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
        if not isinstance(other, ApiStreamGatewayFrameLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
