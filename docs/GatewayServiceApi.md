# swagger_client.GatewayServiceApi

All URIs are relative to *http://api.teke.li:9090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](GatewayServiceApi.md#create) | **POST** /api/gateways | Create creates the given gateway.
[**delete**](GatewayServiceApi.md#delete) | **DELETE** /api/gateways/{id} | Delete deletes the gateway matching the given mac address.
[**get**](GatewayServiceApi.md#get) | **GET** /api/gateways/{id} | Get returns the gateway for the requested mac address.
[**get_last_ping**](GatewayServiceApi.md#get_last_ping) | **GET** /api/gateways/{gateway_id}/pings/last | GetLastPing returns the last emitted ping and gateways receiving this ping.
[**get_stats**](GatewayServiceApi.md#get_stats) | **GET** /api/gateways/{gateway_id}/stats | GetStats lists the gateway stats given the query parameters.
[**list**](GatewayServiceApi.md#list) | **GET** /api/gateways | List lists the gateways.
[**stream_frame_logs**](GatewayServiceApi.md#stream_frame_logs) | **GET** /api/gateways/{gateway_id}/frames | StreamFrameLogs streams the uplink and downlink frame-logs for the given gateway ID. Notes:   * These are the raw LoRaWAN frames and this endpoint is intended for debugging only.   * This endpoint does not work from a web-browser.
[**update**](GatewayServiceApi.md#update) | **PUT** /api/gateways/{gateway.id} | Update updates the gateway matching the given mac address.


# **create**
> object create(body)

Create creates the given gateway.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeaderAuth
configuration = swagger_client.Configuration()
configuration.api_key['Grpc-Metadata-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Grpc-Metadata-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.GatewayServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.ApiCreateGatewayRequest() # ApiCreateGatewayRequest | 

try:
    # Create creates the given gateway.
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayServiceApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiCreateGatewayRequest**](ApiCreateGatewayRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> object delete(id)

Delete deletes the gateway matching the given mac address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeaderAuth
configuration = swagger_client.Configuration()
configuration.api_key['Grpc-Metadata-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Grpc-Metadata-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.GatewayServiceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Gateway ID (HEX encoded).

try:
    # Delete deletes the gateway matching the given mac address.
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayServiceApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Gateway ID (HEX encoded). | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ApiGetGatewayResponse get(id)

Get returns the gateway for the requested mac address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeaderAuth
configuration = swagger_client.Configuration()
configuration.api_key['Grpc-Metadata-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Grpc-Metadata-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.GatewayServiceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Gateway ID (HEX encoded).

try:
    # Get returns the gateway for the requested mac address.
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayServiceApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Gateway ID (HEX encoded). | 

### Return type

[**ApiGetGatewayResponse**](ApiGetGatewayResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_ping**
> ApiGetLastPingResponse get_last_ping(gateway_id)

GetLastPing returns the last emitted ping and gateways receiving this ping.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeaderAuth
configuration = swagger_client.Configuration()
configuration.api_key['Grpc-Metadata-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Grpc-Metadata-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.GatewayServiceApi(swagger_client.ApiClient(configuration))
gateway_id = 'gateway_id_example' # str | Gateway ID (HEX encoded).

try:
    # GetLastPing returns the last emitted ping and gateways receiving this ping.
    api_response = api_instance.get_last_ping(gateway_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayServiceApi->get_last_ping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **str**| Gateway ID (HEX encoded). | 

### Return type

[**ApiGetLastPingResponse**](ApiGetLastPingResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats**
> ApiGetGatewayStatsResponse get_stats(gateway_id, interval=interval, start_timestamp=start_timestamp, end_timestamp=end_timestamp)

GetStats lists the gateway stats given the query parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeaderAuth
configuration = swagger_client.Configuration()
configuration.api_key['Grpc-Metadata-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Grpc-Metadata-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.GatewayServiceApi(swagger_client.ApiClient(configuration))
gateway_id = 'gateway_id_example' # str | Gateway ID (HEX encoded).
interval = 'interval_example' # str | Aggregation interval.  One of \"second\", \"minute\", \"hour\", \"day\", \"week\", \"month\", \"quarter\", \"year\".  Case insensitive. (optional)
start_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Timestamp to start from. (optional)
end_timestamp = '2013-10-20T19:20:30+01:00' # datetime | Timestamp until to get from. (optional)

try:
    # GetStats lists the gateway stats given the query parameters.
    api_response = api_instance.get_stats(gateway_id, interval=interval, start_timestamp=start_timestamp, end_timestamp=end_timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayServiceApi->get_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **str**| Gateway ID (HEX encoded). | 
 **interval** | **str**| Aggregation interval.  One of \&quot;second\&quot;, \&quot;minute\&quot;, \&quot;hour\&quot;, \&quot;day\&quot;, \&quot;week\&quot;, \&quot;month\&quot;, \&quot;quarter\&quot;, \&quot;year\&quot;.  Case insensitive. | [optional] 
 **start_timestamp** | **datetime**| Timestamp to start from. | [optional] 
 **end_timestamp** | **datetime**| Timestamp until to get from. | [optional] 

### Return type

[**ApiGetGatewayStatsResponse**](ApiGetGatewayStatsResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ApiListGatewayResponse list(limit=limit, offset=offset, organization_id=organization_id, search=search)

List lists the gateways.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeaderAuth
configuration = swagger_client.Configuration()
configuration.api_key['Grpc-Metadata-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Grpc-Metadata-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.GatewayServiceApi(swagger_client.ApiClient(configuration))
limit = 56 # int | Max number of nodes to return in the result-set. (optional)
offset = 56 # int | Offset of the result-set (for pagination). (optional)
organization_id = 'organization_id_example' # str | ID of the organization for which to filter on, when left blank the response will return all gateways to which the user has access to. (optional)
search = 'search_example' # str | Search on name or gateway MAC (optional). (optional)

try:
    # List lists the gateways.
    api_response = api_instance.list(limit=limit, offset=offset, organization_id=organization_id, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayServiceApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Max number of nodes to return in the result-set. | [optional] 
 **offset** | **int**| Offset of the result-set (for pagination). | [optional] 
 **organization_id** | **str**| ID of the organization for which to filter on, when left blank the response will return all gateways to which the user has access to. | [optional] 
 **search** | **str**| Search on name or gateway MAC (optional). | [optional] 

### Return type

[**ApiListGatewayResponse**](ApiListGatewayResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_frame_logs**
> XStreamDefinitionsapiStreamGatewayFrameLogsResponse stream_frame_logs(gateway_id)

StreamFrameLogs streams the uplink and downlink frame-logs for the given gateway ID. Notes:   * These are the raw LoRaWAN frames and this endpoint is intended for debugging only.   * This endpoint does not work from a web-browser.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeaderAuth
configuration = swagger_client.Configuration()
configuration.api_key['Grpc-Metadata-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Grpc-Metadata-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.GatewayServiceApi(swagger_client.ApiClient(configuration))
gateway_id = 'gateway_id_example' # str | Gateway ID (HEX encoded).

try:
    # StreamFrameLogs streams the uplink and downlink frame-logs for the given gateway ID. Notes:   * These are the raw LoRaWAN frames and this endpoint is intended for debugging only.   * This endpoint does not work from a web-browser.
    api_response = api_instance.stream_frame_logs(gateway_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayServiceApi->stream_frame_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **str**| Gateway ID (HEX encoded). | 

### Return type

[**XStreamDefinitionsapiStreamGatewayFrameLogsResponse**](XStreamDefinitionsapiStreamGatewayFrameLogsResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> object update(gateway_id, body)

Update updates the gateway matching the given mac address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyHeaderAuth
configuration = swagger_client.Configuration()
configuration.api_key['Grpc-Metadata-Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Grpc-Metadata-Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.GatewayServiceApi(swagger_client.ApiClient(configuration))
gateway_id = 'gateway_id_example' # str | Gateway ID (HEX encoded).
body = swagger_client.ApiUpdateGatewayRequest() # ApiUpdateGatewayRequest | 

try:
    # Update updates the gateway matching the given mac address.
    api_response = api_instance.update(gateway_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayServiceApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **str**| Gateway ID (HEX encoded). | 
 **body** | [**ApiUpdateGatewayRequest**](ApiUpdateGatewayRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

