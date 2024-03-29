# coding: utf-8

"""
    LoRa App Server REST API

     For more information about the usage of the LoRa App Server (REST) API, see [https://docs.loraserver.io/lora-app-server/api/](https://docs.loraserver.io/lora-app-server/api/).   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class GatewayServiceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create(self, body, **kwargs):  # noqa: E501
        """Create creates the given gateway.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApiCreateGatewayRequest body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create creates the given gateway.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ApiCreateGatewayRequest body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeaderAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/gateways', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete(self, id, **kwargs):  # noqa: E501
        """Delete deletes the gateway matching the given mac address.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Gateway ID (HEX encoded). (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete deletes the gateway matching the given mac address.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Gateway ID (HEX encoded). (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeaderAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/gateways/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get(self, id, **kwargs):  # noqa: E501
        """Get returns the gateway for the requested mac address.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Gateway ID (HEX encoded). (required)
        :return: ApiGetGatewayResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get returns the gateway for the requested mac address.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Gateway ID (HEX encoded). (required)
        :return: ApiGetGatewayResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeaderAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/gateways/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiGetGatewayResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_last_ping(self, gateway_id, **kwargs):  # noqa: E501
        """GetLastPing returns the last emitted ping and gateways receiving this ping.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_last_ping(gateway_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gateway_id: Gateway ID (HEX encoded). (required)
        :return: ApiGetLastPingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_last_ping_with_http_info(gateway_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_last_ping_with_http_info(gateway_id, **kwargs)  # noqa: E501
            return data

    def get_last_ping_with_http_info(self, gateway_id, **kwargs):  # noqa: E501
        """GetLastPing returns the last emitted ping and gateways receiving this ping.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_last_ping_with_http_info(gateway_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gateway_id: Gateway ID (HEX encoded). (required)
        :return: ApiGetLastPingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gateway_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_last_ping" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gateway_id' is set
        if ('gateway_id' not in params or
                params['gateway_id'] is None):
            raise ValueError("Missing the required parameter `gateway_id` when calling `get_last_ping`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in params:
            path_params['gateway_id'] = params['gateway_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeaderAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/gateways/{gateway_id}/pings/last', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiGetLastPingResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_stats(self, gateway_id, **kwargs):  # noqa: E501
        """GetStats lists the gateway stats given the query parameters.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stats(gateway_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gateway_id: Gateway ID (HEX encoded). (required)
        :param str interval: Aggregation interval.  One of \"second\", \"minute\", \"hour\", \"day\", \"week\", \"month\", \"quarter\", \"year\".  Case insensitive.
        :param datetime start_timestamp: Timestamp to start from.
        :param datetime end_timestamp: Timestamp until to get from.
        :return: ApiGetGatewayStatsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_stats_with_http_info(gateway_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_stats_with_http_info(gateway_id, **kwargs)  # noqa: E501
            return data

    def get_stats_with_http_info(self, gateway_id, **kwargs):  # noqa: E501
        """GetStats lists the gateway stats given the query parameters.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_stats_with_http_info(gateway_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gateway_id: Gateway ID (HEX encoded). (required)
        :param str interval: Aggregation interval.  One of \"second\", \"minute\", \"hour\", \"day\", \"week\", \"month\", \"quarter\", \"year\".  Case insensitive.
        :param datetime start_timestamp: Timestamp to start from.
        :param datetime end_timestamp: Timestamp until to get from.
        :return: ApiGetGatewayStatsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gateway_id', 'interval', 'start_timestamp', 'end_timestamp']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gateway_id' is set
        if ('gateway_id' not in params or
                params['gateway_id'] is None):
            raise ValueError("Missing the required parameter `gateway_id` when calling `get_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in params:
            path_params['gateway_id'] = params['gateway_id']  # noqa: E501

        query_params = []
        if 'interval' in params:
            query_params.append(('interval', params['interval']))  # noqa: E501
        if 'start_timestamp' in params:
            query_params.append(('startTimestamp', params['start_timestamp']))  # noqa: E501
        if 'end_timestamp' in params:
            query_params.append(('endTimestamp', params['end_timestamp']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeaderAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/gateways/{gateway_id}/stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiGetGatewayStatsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list(self, **kwargs):  # noqa: E501
        """List lists the gateways.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Max number of nodes to return in the result-set.
        :param int offset: Offset of the result-set (for pagination).
        :param str organization_id: ID of the organization for which to filter on, when left blank the response will return all gateways to which the user has access to.
        :param str search: Search on name or gateway MAC (optional).
        :return: ApiListGatewayResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_with_http_info(self, **kwargs):  # noqa: E501
        """List lists the gateways.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: Max number of nodes to return in the result-set.
        :param int offset: Offset of the result-set (for pagination).
        :param str organization_id: ID of the organization for which to filter on, when left blank the response will return all gateways to which the user has access to.
        :param str search: Search on name or gateway MAC (optional).
        :return: ApiListGatewayResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'organization_id', 'search']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'organization_id' in params:
            query_params.append(('organizationID', params['organization_id']))  # noqa: E501
        if 'search' in params:
            query_params.append(('search', params['search']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeaderAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/gateways', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiListGatewayResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stream_frame_logs(self, gateway_id, **kwargs):  # noqa: E501
        """StreamFrameLogs streams the uplink and downlink frame-logs for the given gateway ID. Notes:   * These are the raw LoRaWAN frames and this endpoint is intended for debugging only.   * This endpoint does not work from a web-browser.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stream_frame_logs(gateway_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gateway_id: Gateway ID (HEX encoded). (required)
        :return: XStreamDefinitionsapiStreamGatewayFrameLogsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stream_frame_logs_with_http_info(gateway_id, **kwargs)  # noqa: E501
        else:
            (data) = self.stream_frame_logs_with_http_info(gateway_id, **kwargs)  # noqa: E501
            return data

    def stream_frame_logs_with_http_info(self, gateway_id, **kwargs):  # noqa: E501
        """StreamFrameLogs streams the uplink and downlink frame-logs for the given gateway ID. Notes:   * These are the raw LoRaWAN frames and this endpoint is intended for debugging only.   * This endpoint does not work from a web-browser.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stream_frame_logs_with_http_info(gateway_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gateway_id: Gateway ID (HEX encoded). (required)
        :return: XStreamDefinitionsapiStreamGatewayFrameLogsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gateway_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stream_frame_logs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gateway_id' is set
        if ('gateway_id' not in params or
                params['gateway_id'] is None):
            raise ValueError("Missing the required parameter `gateway_id` when calling `stream_frame_logs`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in params:
            path_params['gateway_id'] = params['gateway_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeaderAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/gateways/{gateway_id}/frames', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='XStreamDefinitionsapiStreamGatewayFrameLogsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update(self, gateway_id, body, **kwargs):  # noqa: E501
        """Update updates the gateway matching the given mac address.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update(gateway_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gateway_id: Gateway ID (HEX encoded). (required)
        :param ApiUpdateGatewayRequest body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_with_http_info(gateway_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_with_http_info(gateway_id, body, **kwargs)  # noqa: E501
            return data

    def update_with_http_info(self, gateway_id, body, **kwargs):  # noqa: E501
        """Update updates the gateway matching the given mac address.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_with_http_info(gateway_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str gateway_id: Gateway ID (HEX encoded). (required)
        :param ApiUpdateGatewayRequest body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['gateway_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'gateway_id' is set
        if ('gateway_id' not in params or
                params['gateway_id'] is None):
            raise ValueError("Missing the required parameter `gateway_id` when calling `update`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'gateway_id' in params:
            path_params['gateway.id'] = params['gateway_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyHeaderAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/gateways/{gateway.id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
