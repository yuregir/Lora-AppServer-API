# swagger_client.NetworkServerServiceApi

All URIs are relative to *http://api.teke.li:9090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](NetworkServerServiceApi.md#create) | **POST** /api/network-servers | Create creates the given network-server.
[**delete**](NetworkServerServiceApi.md#delete) | **DELETE** /api/network-servers/{id} | Delete deletes the network-server matching the given id.
[**get**](NetworkServerServiceApi.md#get) | **GET** /api/network-servers/{id} | Get returns the network-server matching the given id.
[**list**](NetworkServerServiceApi.md#list) | **GET** /api/network-servers | List lists the available network-servers.
[**update**](NetworkServerServiceApi.md#update) | **PUT** /api/network-servers/{network_server.id} | Update updates the given network-server.


# **create**
> ApiCreateNetworkServerResponse create(body)

Create creates the given network-server.

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
api_instance = swagger_client.NetworkServerServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.ApiCreateNetworkServerRequest() # ApiCreateNetworkServerRequest | 

try:
    # Create creates the given network-server.
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkServerServiceApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiCreateNetworkServerRequest**](ApiCreateNetworkServerRequest.md)|  | 

### Return type

[**ApiCreateNetworkServerResponse**](ApiCreateNetworkServerResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> object delete(id)

Delete deletes the network-server matching the given id.

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
api_instance = swagger_client.NetworkServerServiceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Network-server ID.

try:
    # Delete deletes the network-server matching the given id.
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkServerServiceApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Network-server ID. | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ApiGetNetworkServerResponse get(id)

Get returns the network-server matching the given id.

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
api_instance = swagger_client.NetworkServerServiceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Network-server ID.

try:
    # Get returns the network-server matching the given id.
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkServerServiceApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Network-server ID. | 

### Return type

[**ApiGetNetworkServerResponse**](ApiGetNetworkServerResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ApiListNetworkServerResponse list(limit=limit, offset=offset, organization_id=organization_id)

List lists the available network-servers.

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
api_instance = swagger_client.NetworkServerServiceApi(swagger_client.ApiClient(configuration))
limit = 'limit_example' # str | Max number of items to return. (optional)
offset = 'offset_example' # str | Offset in the result-set (for pagination). (optional)
organization_id = 'organization_id_example' # str | Organization id to filter on. (optional)

try:
    # List lists the available network-servers.
    api_response = api_instance.list(limit=limit, offset=offset, organization_id=organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkServerServiceApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| Max number of items to return. | [optional] 
 **offset** | **str**| Offset in the result-set (for pagination). | [optional] 
 **organization_id** | **str**| Organization id to filter on. | [optional] 

### Return type

[**ApiListNetworkServerResponse**](ApiListNetworkServerResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> object update(network_server_id, body)

Update updates the given network-server.

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
api_instance = swagger_client.NetworkServerServiceApi(swagger_client.ApiClient(configuration))
network_server_id = 'network_server_id_example' # str | Network-server ID.
body = swagger_client.ApiUpdateNetworkServerRequest() # ApiUpdateNetworkServerRequest | 

try:
    # Update updates the given network-server.
    api_response = api_instance.update(network_server_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkServerServiceApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_server_id** | **str**| Network-server ID. | 
 **body** | [**ApiUpdateNetworkServerRequest**](ApiUpdateNetworkServerRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

