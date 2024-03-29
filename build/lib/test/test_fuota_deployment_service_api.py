# coding: utf-8

"""
    LoRa App Server REST API

     For more information about the usage of the LoRa App Server (REST) API, see [https://docs.loraserver.io/lora-app-server/api/](https://docs.loraserver.io/lora-app-server/api/).   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.fuota_deployment_service_api import FUOTADeploymentServiceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestFUOTADeploymentServiceApi(unittest.TestCase):
    """FUOTADeploymentServiceApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.fuota_deployment_service_api.FUOTADeploymentServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_for_device(self):
        """Test case for create_for_device

        CreateForDevice creates a deployment for the given DevEUI.  # noqa: E501
        """
        pass

    def test_get(self):
        """Test case for get

        Get returns the fuota deployment for the given id.  # noqa: E501
        """
        pass

    def test_get_deployment_device(self):
        """Test case for get_deployment_device

        GetDeploymentDevice returns the deployment device.  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List lists the fuota deployments.  # noqa: E501
        """
        pass

    def test_list_deployment_devices(self):
        """Test case for list_deployment_devices

        ListDeploymentDevices lists the devices (and status) for the given fuota deployment ID.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
