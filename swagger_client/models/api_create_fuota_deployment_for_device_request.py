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

from swagger_client.models.api_fuota_deployment import ApiFUOTADeployment  # noqa: F401,E501


class ApiCreateFUOTADeploymentForDeviceRequest(object):
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
        'dev_eui': 'str',
        'fuota_deployment': 'ApiFUOTADeployment'
    }

    attribute_map = {
        'dev_eui': 'devEUI',
        'fuota_deployment': 'fuotaDeployment'
    }

    def __init__(self, dev_eui=None, fuota_deployment=None):  # noqa: E501
        """ApiCreateFUOTADeploymentForDeviceRequest - a model defined in Swagger"""  # noqa: E501

        self._dev_eui = None
        self._fuota_deployment = None
        self.discriminator = None

        if dev_eui is not None:
            self.dev_eui = dev_eui
        if fuota_deployment is not None:
            self.fuota_deployment = fuota_deployment

    @property
    def dev_eui(self):
        """Gets the dev_eui of this ApiCreateFUOTADeploymentForDeviceRequest.  # noqa: E501

        Device EUI (HEX encoded).  # noqa: E501

        :return: The dev_eui of this ApiCreateFUOTADeploymentForDeviceRequest.  # noqa: E501
        :rtype: str
        """
        return self._dev_eui

    @dev_eui.setter
    def dev_eui(self, dev_eui):
        """Sets the dev_eui of this ApiCreateFUOTADeploymentForDeviceRequest.

        Device EUI (HEX encoded).  # noqa: E501

        :param dev_eui: The dev_eui of this ApiCreateFUOTADeploymentForDeviceRequest.  # noqa: E501
        :type: str
        """

        self._dev_eui = dev_eui

    @property
    def fuota_deployment(self):
        """Gets the fuota_deployment of this ApiCreateFUOTADeploymentForDeviceRequest.  # noqa: E501

        FUOTA deployment.  # noqa: E501

        :return: The fuota_deployment of this ApiCreateFUOTADeploymentForDeviceRequest.  # noqa: E501
        :rtype: ApiFUOTADeployment
        """
        return self._fuota_deployment

    @fuota_deployment.setter
    def fuota_deployment(self, fuota_deployment):
        """Sets the fuota_deployment of this ApiCreateFUOTADeploymentForDeviceRequest.

        FUOTA deployment.  # noqa: E501

        :param fuota_deployment: The fuota_deployment of this ApiCreateFUOTADeploymentForDeviceRequest.  # noqa: E501
        :type: ApiFUOTADeployment
        """

        self._fuota_deployment = fuota_deployment

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
        if issubclass(ApiCreateFUOTADeploymentForDeviceRequest, dict):
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
        if not isinstance(other, ApiCreateFUOTADeploymentForDeviceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
