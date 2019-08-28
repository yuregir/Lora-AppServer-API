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


class ApiDeviceQueueItem(object):
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
        'confirmed': 'bool',
        'data': 'str',
        'dev_eui': 'str',
        'f_cnt': 'int',
        'f_port': 'int',
        'json_object': 'str'
    }

    attribute_map = {
        'confirmed': 'confirmed',
        'data': 'data',
        'dev_eui': 'devEUI',
        'f_cnt': 'fCnt',
        'f_port': 'fPort',
        'json_object': 'jsonObject'
    }

    def __init__(self, confirmed=None, data=None, dev_eui=None, f_cnt=None, f_port=None, json_object=None):  # noqa: E501
        """ApiDeviceQueueItem - a model defined in Swagger"""  # noqa: E501

        self._confirmed = None
        self._data = None
        self._dev_eui = None
        self._f_cnt = None
        self._f_port = None
        self._json_object = None
        self.discriminator = None

        if confirmed is not None:
            self.confirmed = confirmed
        if data is not None:
            self.data = data
        if dev_eui is not None:
            self.dev_eui = dev_eui
        if f_cnt is not None:
            self.f_cnt = f_cnt
        if f_port is not None:
            self.f_port = f_port
        if json_object is not None:
            self.json_object = json_object

    @property
    def confirmed(self):
        """Gets the confirmed of this ApiDeviceQueueItem.  # noqa: E501

        Set this to true when an acknowledgement from the device is required. Please note that this must not be used to guarantee a delivery.  # noqa: E501

        :return: The confirmed of this ApiDeviceQueueItem.  # noqa: E501
        :rtype: bool
        """
        return self._confirmed

    @confirmed.setter
    def confirmed(self, confirmed):
        """Sets the confirmed of this ApiDeviceQueueItem.

        Set this to true when an acknowledgement from the device is required. Please note that this must not be used to guarantee a delivery.  # noqa: E501

        :param confirmed: The confirmed of this ApiDeviceQueueItem.  # noqa: E501
        :type: bool
        """

        self._confirmed = confirmed

    @property
    def data(self):
        """Gets the data of this ApiDeviceQueueItem.  # noqa: E501

        Base64 encoded data. Or use the json_object field when an application codec has been configured.  # noqa: E501

        :return: The data of this ApiDeviceQueueItem.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ApiDeviceQueueItem.

        Base64 encoded data. Or use the json_object field when an application codec has been configured.  # noqa: E501

        :param data: The data of this ApiDeviceQueueItem.  # noqa: E501
        :type: str
        """
        if data is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', data):  # noqa: E501
            raise ValueError(r"Invalid value for `data`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._data = data

    @property
    def dev_eui(self):
        """Gets the dev_eui of this ApiDeviceQueueItem.  # noqa: E501

        Device EUI (HEX encoded).  # noqa: E501

        :return: The dev_eui of this ApiDeviceQueueItem.  # noqa: E501
        :rtype: str
        """
        return self._dev_eui

    @dev_eui.setter
    def dev_eui(self, dev_eui):
        """Sets the dev_eui of this ApiDeviceQueueItem.

        Device EUI (HEX encoded).  # noqa: E501

        :param dev_eui: The dev_eui of this ApiDeviceQueueItem.  # noqa: E501
        :type: str
        """

        self._dev_eui = dev_eui

    @property
    def f_cnt(self):
        """Gets the f_cnt of this ApiDeviceQueueItem.  # noqa: E501

        Downlink frame-counter. This will be automatically set on enquue.  # noqa: E501

        :return: The f_cnt of this ApiDeviceQueueItem.  # noqa: E501
        :rtype: int
        """
        return self._f_cnt

    @f_cnt.setter
    def f_cnt(self, f_cnt):
        """Sets the f_cnt of this ApiDeviceQueueItem.

        Downlink frame-counter. This will be automatically set on enquue.  # noqa: E501

        :param f_cnt: The f_cnt of this ApiDeviceQueueItem.  # noqa: E501
        :type: int
        """

        self._f_cnt = f_cnt

    @property
    def f_port(self):
        """Gets the f_port of this ApiDeviceQueueItem.  # noqa: E501

        FPort used (must be > 0)  # noqa: E501

        :return: The f_port of this ApiDeviceQueueItem.  # noqa: E501
        :rtype: int
        """
        return self._f_port

    @f_port.setter
    def f_port(self, f_port):
        """Sets the f_port of this ApiDeviceQueueItem.

        FPort used (must be > 0)  # noqa: E501

        :param f_port: The f_port of this ApiDeviceQueueItem.  # noqa: E501
        :type: int
        """

        self._f_port = f_port

    @property
    def json_object(self):
        """Gets the json_object of this ApiDeviceQueueItem.  # noqa: E501

        JSON object (string). Only use this when an application codec has been configured that can convert this object into binary form.  # noqa: E501

        :return: The json_object of this ApiDeviceQueueItem.  # noqa: E501
        :rtype: str
        """
        return self._json_object

    @json_object.setter
    def json_object(self, json_object):
        """Sets the json_object of this ApiDeviceQueueItem.

        JSON object (string). Only use this when an application codec has been configured that can convert this object into binary form.  # noqa: E501

        :param json_object: The json_object of this ApiDeviceQueueItem.  # noqa: E501
        :type: str
        """

        self._json_object = json_object

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
        if issubclass(ApiDeviceQueueItem, dict):
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
        if not isinstance(other, ApiDeviceQueueItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other