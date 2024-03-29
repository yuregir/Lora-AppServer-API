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


class ApiDeviceActivation(object):
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
        'a_f_cnt_down': 'int',
        'app_s_key': 'str',
        'dev_addr': 'str',
        'dev_eui': 'str',
        'f_cnt_up': 'int',
        'f_nwk_s_int_key': 'str',
        'n_f_cnt_down': 'int',
        'nwk_s_enc_key': 'str',
        's_nwk_s_int_key': 'str'
    }

    attribute_map = {
        'a_f_cnt_down': 'aFCntDown',
        'app_s_key': 'appSKey',
        'dev_addr': 'devAddr',
        'dev_eui': 'devEUI',
        'f_cnt_up': 'fCntUp',
        'f_nwk_s_int_key': 'fNwkSIntKey',
        'n_f_cnt_down': 'nFCntDown',
        'nwk_s_enc_key': 'nwkSEncKey',
        's_nwk_s_int_key': 'sNwkSIntKey'
    }

    def __init__(self, a_f_cnt_down=None, app_s_key=None, dev_addr=None, dev_eui=None, f_cnt_up=None, f_nwk_s_int_key=None, n_f_cnt_down=None, nwk_s_enc_key=None, s_nwk_s_int_key=None):  # noqa: E501
        """ApiDeviceActivation - a model defined in Swagger"""  # noqa: E501

        self._a_f_cnt_down = None
        self._app_s_key = None
        self._dev_addr = None
        self._dev_eui = None
        self._f_cnt_up = None
        self._f_nwk_s_int_key = None
        self._n_f_cnt_down = None
        self._nwk_s_enc_key = None
        self._s_nwk_s_int_key = None
        self.discriminator = None

        if a_f_cnt_down is not None:
            self.a_f_cnt_down = a_f_cnt_down
        if app_s_key is not None:
            self.app_s_key = app_s_key
        if dev_addr is not None:
            self.dev_addr = dev_addr
        if dev_eui is not None:
            self.dev_eui = dev_eui
        if f_cnt_up is not None:
            self.f_cnt_up = f_cnt_up
        if f_nwk_s_int_key is not None:
            self.f_nwk_s_int_key = f_nwk_s_int_key
        if n_f_cnt_down is not None:
            self.n_f_cnt_down = n_f_cnt_down
        if nwk_s_enc_key is not None:
            self.nwk_s_enc_key = nwk_s_enc_key
        if s_nwk_s_int_key is not None:
            self.s_nwk_s_int_key = s_nwk_s_int_key

    @property
    def a_f_cnt_down(self):
        """Gets the a_f_cnt_down of this ApiDeviceActivation.  # noqa: E501

        Downlink application frame-counter.  # noqa: E501

        :return: The a_f_cnt_down of this ApiDeviceActivation.  # noqa: E501
        :rtype: int
        """
        return self._a_f_cnt_down

    @a_f_cnt_down.setter
    def a_f_cnt_down(self, a_f_cnt_down):
        """Sets the a_f_cnt_down of this ApiDeviceActivation.

        Downlink application frame-counter.  # noqa: E501

        :param a_f_cnt_down: The a_f_cnt_down of this ApiDeviceActivation.  # noqa: E501
        :type: int
        """

        self._a_f_cnt_down = a_f_cnt_down

    @property
    def app_s_key(self):
        """Gets the app_s_key of this ApiDeviceActivation.  # noqa: E501

        Application session key (HEX encoded).  # noqa: E501

        :return: The app_s_key of this ApiDeviceActivation.  # noqa: E501
        :rtype: str
        """
        return self._app_s_key

    @app_s_key.setter
    def app_s_key(self, app_s_key):
        """Sets the app_s_key of this ApiDeviceActivation.

        Application session key (HEX encoded).  # noqa: E501

        :param app_s_key: The app_s_key of this ApiDeviceActivation.  # noqa: E501
        :type: str
        """

        self._app_s_key = app_s_key

    @property
    def dev_addr(self):
        """Gets the dev_addr of this ApiDeviceActivation.  # noqa: E501

        Device address (HEX encoded).  # noqa: E501

        :return: The dev_addr of this ApiDeviceActivation.  # noqa: E501
        :rtype: str
        """
        return self._dev_addr

    @dev_addr.setter
    def dev_addr(self, dev_addr):
        """Sets the dev_addr of this ApiDeviceActivation.

        Device address (HEX encoded).  # noqa: E501

        :param dev_addr: The dev_addr of this ApiDeviceActivation.  # noqa: E501
        :type: str
        """

        self._dev_addr = dev_addr

    @property
    def dev_eui(self):
        """Gets the dev_eui of this ApiDeviceActivation.  # noqa: E501

        Device EUI (HEX encoded).  # noqa: E501

        :return: The dev_eui of this ApiDeviceActivation.  # noqa: E501
        :rtype: str
        """
        return self._dev_eui

    @dev_eui.setter
    def dev_eui(self, dev_eui):
        """Sets the dev_eui of this ApiDeviceActivation.

        Device EUI (HEX encoded).  # noqa: E501

        :param dev_eui: The dev_eui of this ApiDeviceActivation.  # noqa: E501
        :type: str
        """

        self._dev_eui = dev_eui

    @property
    def f_cnt_up(self):
        """Gets the f_cnt_up of this ApiDeviceActivation.  # noqa: E501

        Uplink frame-counter.  # noqa: E501

        :return: The f_cnt_up of this ApiDeviceActivation.  # noqa: E501
        :rtype: int
        """
        return self._f_cnt_up

    @f_cnt_up.setter
    def f_cnt_up(self, f_cnt_up):
        """Sets the f_cnt_up of this ApiDeviceActivation.

        Uplink frame-counter.  # noqa: E501

        :param f_cnt_up: The f_cnt_up of this ApiDeviceActivation.  # noqa: E501
        :type: int
        """

        self._f_cnt_up = f_cnt_up

    @property
    def f_nwk_s_int_key(self):
        """Gets the f_nwk_s_int_key of this ApiDeviceActivation.  # noqa: E501

        Forwarding network session integrity key (HEX encoded).  # noqa: E501

        :return: The f_nwk_s_int_key of this ApiDeviceActivation.  # noqa: E501
        :rtype: str
        """
        return self._f_nwk_s_int_key

    @f_nwk_s_int_key.setter
    def f_nwk_s_int_key(self, f_nwk_s_int_key):
        """Sets the f_nwk_s_int_key of this ApiDeviceActivation.

        Forwarding network session integrity key (HEX encoded).  # noqa: E501

        :param f_nwk_s_int_key: The f_nwk_s_int_key of this ApiDeviceActivation.  # noqa: E501
        :type: str
        """

        self._f_nwk_s_int_key = f_nwk_s_int_key

    @property
    def n_f_cnt_down(self):
        """Gets the n_f_cnt_down of this ApiDeviceActivation.  # noqa: E501

        Downlink network frame-counter.  # noqa: E501

        :return: The n_f_cnt_down of this ApiDeviceActivation.  # noqa: E501
        :rtype: int
        """
        return self._n_f_cnt_down

    @n_f_cnt_down.setter
    def n_f_cnt_down(self, n_f_cnt_down):
        """Sets the n_f_cnt_down of this ApiDeviceActivation.

        Downlink network frame-counter.  # noqa: E501

        :param n_f_cnt_down: The n_f_cnt_down of this ApiDeviceActivation.  # noqa: E501
        :type: int
        """

        self._n_f_cnt_down = n_f_cnt_down

    @property
    def nwk_s_enc_key(self):
        """Gets the nwk_s_enc_key of this ApiDeviceActivation.  # noqa: E501

        Network session encryption key (HEX encoded).  # noqa: E501

        :return: The nwk_s_enc_key of this ApiDeviceActivation.  # noqa: E501
        :rtype: str
        """
        return self._nwk_s_enc_key

    @nwk_s_enc_key.setter
    def nwk_s_enc_key(self, nwk_s_enc_key):
        """Sets the nwk_s_enc_key of this ApiDeviceActivation.

        Network session encryption key (HEX encoded).  # noqa: E501

        :param nwk_s_enc_key: The nwk_s_enc_key of this ApiDeviceActivation.  # noqa: E501
        :type: str
        """

        self._nwk_s_enc_key = nwk_s_enc_key

    @property
    def s_nwk_s_int_key(self):
        """Gets the s_nwk_s_int_key of this ApiDeviceActivation.  # noqa: E501

        Serving network session integrity key (HEX encoded).  # noqa: E501

        :return: The s_nwk_s_int_key of this ApiDeviceActivation.  # noqa: E501
        :rtype: str
        """
        return self._s_nwk_s_int_key

    @s_nwk_s_int_key.setter
    def s_nwk_s_int_key(self, s_nwk_s_int_key):
        """Sets the s_nwk_s_int_key of this ApiDeviceActivation.

        Serving network session integrity key (HEX encoded).  # noqa: E501

        :param s_nwk_s_int_key: The s_nwk_s_int_key of this ApiDeviceActivation.  # noqa: E501
        :type: str
        """

        self._s_nwk_s_int_key = s_nwk_s_int_key

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
        if issubclass(ApiDeviceActivation, dict):
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
        if not isinstance(other, ApiDeviceActivation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
