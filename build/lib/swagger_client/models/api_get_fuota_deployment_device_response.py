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

from swagger_client.models.api_fuota_deployment_device_list_item import ApiFUOTADeploymentDeviceListItem  # noqa: F401,E501


class ApiGetFUOTADeploymentDeviceResponse(object):
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
        'deployment_device': 'ApiFUOTADeploymentDeviceListItem'
    }

    attribute_map = {
        'deployment_device': 'deploymentDevice'
    }

    def __init__(self, deployment_device=None):  # noqa: E501
        """ApiGetFUOTADeploymentDeviceResponse - a model defined in Swagger"""  # noqa: E501

        self._deployment_device = None
        self.discriminator = None

        if deployment_device is not None:
            self.deployment_device = deployment_device

    @property
    def deployment_device(self):
        """Gets the deployment_device of this ApiGetFUOTADeploymentDeviceResponse.  # noqa: E501


        :return: The deployment_device of this ApiGetFUOTADeploymentDeviceResponse.  # noqa: E501
        :rtype: ApiFUOTADeploymentDeviceListItem
        """
        return self._deployment_device

    @deployment_device.setter
    def deployment_device(self, deployment_device):
        """Sets the deployment_device of this ApiGetFUOTADeploymentDeviceResponse.


        :param deployment_device: The deployment_device of this ApiGetFUOTADeploymentDeviceResponse.  # noqa: E501
        :type: ApiFUOTADeploymentDeviceListItem
        """

        self._deployment_device = deployment_device

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
        if issubclass(ApiGetFUOTADeploymentDeviceResponse, dict):
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
        if not isinstance(other, ApiGetFUOTADeploymentDeviceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
