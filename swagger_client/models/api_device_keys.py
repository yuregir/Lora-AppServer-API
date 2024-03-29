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


class ApiDeviceKeys(object):
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
        'app_key': 'str',
        'dev_eui': 'str',
        'gen_app_key': 'str',
        'nwk_key': 'str'
    }

    attribute_map = {
        'app_key': 'appKey',
        'dev_eui': 'devEUI',
        'gen_app_key': 'genAppKey',
        'nwk_key': 'nwkKey'
    }

    def __init__(self, app_key=None, dev_eui=None, gen_app_key=None, nwk_key=None):  # noqa: E501
        """ApiDeviceKeys - a model defined in Swagger"""  # noqa: E501

        self._app_key = None
        self._dev_eui = None
        self._gen_app_key = None
        self._nwk_key = None
        self.discriminator = None

        if app_key is not None:
            self.app_key = app_key
        if dev_eui is not None:
            self.dev_eui = dev_eui
        if gen_app_key is not None:
            self.gen_app_key = gen_app_key
        if nwk_key is not None:
            self.nwk_key = nwk_key

    @property
    def app_key(self):
        """Gets the app_key of this ApiDeviceKeys.  # noqa: E501

        Application root key (HEX encoded). Note: This field only needs to be set for LoRaWAN 1.1.x devices!  # noqa: E501

        :return: The app_key of this ApiDeviceKeys.  # noqa: E501
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        """Sets the app_key of this ApiDeviceKeys.

        Application root key (HEX encoded). Note: This field only needs to be set for LoRaWAN 1.1.x devices!  # noqa: E501

        :param app_key: The app_key of this ApiDeviceKeys.  # noqa: E501
        :type: str
        """

        self._app_key = app_key

    @property
    def dev_eui(self):
        """Gets the dev_eui of this ApiDeviceKeys.  # noqa: E501

        Device EUI (HEX encoded).  # noqa: E501

        :return: The dev_eui of this ApiDeviceKeys.  # noqa: E501
        :rtype: str
        """
        return self._dev_eui

    @dev_eui.setter
    def dev_eui(self, dev_eui):
        """Sets the dev_eui of this ApiDeviceKeys.

        Device EUI (HEX encoded).  # noqa: E501

        :param dev_eui: The dev_eui of this ApiDeviceKeys.  # noqa: E501
        :type: str
        """

        self._dev_eui = dev_eui

    @property
    def gen_app_key(self):
        """Gets the gen_app_key of this ApiDeviceKeys.  # noqa: E501

        Gen application key (HEX encoded). This is an optional key that only must be set for LORaWAN 1.0.x devices that implement the remote multicast setup specification.  # noqa: E501

        :return: The gen_app_key of this ApiDeviceKeys.  # noqa: E501
        :rtype: str
        """
        return self._gen_app_key

    @gen_app_key.setter
    def gen_app_key(self, gen_app_key):
        """Sets the gen_app_key of this ApiDeviceKeys.

        Gen application key (HEX encoded). This is an optional key that only must be set for LORaWAN 1.0.x devices that implement the remote multicast setup specification.  # noqa: E501

        :param gen_app_key: The gen_app_key of this ApiDeviceKeys.  # noqa: E501
        :type: str
        """

        self._gen_app_key = gen_app_key

    @property
    def nwk_key(self):
        """Gets the nwk_key of this ApiDeviceKeys.  # noqa: E501

        Network root key (HEX encoded). Note: For LoRaWAN 1.0.x, use this field for the LoRaWAN 1.0.x 'AppKey`!  # noqa: E501

        :return: The nwk_key of this ApiDeviceKeys.  # noqa: E501
        :rtype: str
        """
        return self._nwk_key

    @nwk_key.setter
    def nwk_key(self, nwk_key):
        """Sets the nwk_key of this ApiDeviceKeys.

        Network root key (HEX encoded). Note: For LoRaWAN 1.0.x, use this field for the LoRaWAN 1.0.x 'AppKey`!  # noqa: E501

        :param nwk_key: The nwk_key of this ApiDeviceKeys.  # noqa: E501
        :type: str
        """

        self._nwk_key = nwk_key

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
        if issubclass(ApiDeviceKeys, dict):
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
        if not isinstance(other, ApiDeviceKeys):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
