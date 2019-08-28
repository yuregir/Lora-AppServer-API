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
from swagger_client.api.gateway_service_api import GatewayServiceApi  # noqa: E501
from swagger_client.rest import ApiException


class TestGatewayServiceApi(unittest.TestCase):
    """GatewayServiceApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.gateway_service_api.GatewayServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create(self):
        """Test case for create

        Create creates the given gateway.  # noqa: E501
        """
        pass

    def test_delete(self):
        """Test case for delete

        Delete deletes the gateway matching the given mac address.  # noqa: E501
        """
        pass

    def test_get(self):
        """Test case for get

        Get returns the gateway for the requested mac address.  # noqa: E501
        """
        pass

    def test_get_last_ping(self):
        """Test case for get_last_ping

        GetLastPing returns the last emitted ping and gateways receiving this ping.  # noqa: E501
        """
        pass

    def test_get_stats(self):
        """Test case for get_stats

        GetStats lists the gateway stats given the query parameters.  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List lists the gateways.  # noqa: E501
        """
        pass

    def test_stream_frame_logs(self):
        """Test case for stream_frame_logs

        StreamFrameLogs streams the uplink and downlink frame-logs for the given gateway ID. Notes:   * These are the raw LoRaWAN frames and this endpoint is intended for debugging only.   * This endpoint does not work from a web-browser.  # noqa: E501
        """
        pass

    def test_update(self):
        """Test case for update

        Update updates the gateway matching the given mac address.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()