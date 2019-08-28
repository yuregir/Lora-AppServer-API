# swagger_client.GatewayProfileServiceApi

All URIs are relative to *http://api.teke.li:9090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](GatewayProfileServiceApi.md#create) | **POST** /api/gateway-profiles | Create creates the given gateway-profile.
[**delete**](GatewayProfileServiceApi.md#delete) | **DELETE** /api/gateway-profiles/{id} | Delete deletes the gateway-profile matching the given id.
[**get**](GatewayProfileServiceApi.md#get) | **GET** /api/gateway-profiles/{id} | Get returns the gateway-profile matching the given id.
[**list**](GatewayProfileServiceApi.md#list) | **GET** /api/gateway-profiles | List returns the existing gateway-profiles.
[**update**](GatewayProfileServiceApi.md#update) | **PUT** /api/gateway-profiles/{gateway_profile.id} | Update updates the given gateway-profile.


# **create**
> ApiCreateGatewayProfileResponse create(body)

Create creates the given gateway-profile.

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
api_instance = swagger_client.GatewayProfileServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.ApiCreateGatewayProfileRequest() # ApiCreateGatewayProfileRequest | 

try:
    # Create creates the given gateway-profile.
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayProfileServiceApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiCreateGatewayProfileRequest**](ApiCreateGatewayProfileRequest.md)|  | 

### Return type

[**ApiCreateGatewayProfileResponse**](ApiCreateGatewayProfileResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> object delete(id)

Delete deletes the gateway-profile matching the given id.

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
api_instance = swagger_client.GatewayProfileServiceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Gateway-profile id (UUID string).

try:
    # Delete deletes the gateway-profile matching the given id.
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayProfileServiceApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Gateway-profile id (UUID string). | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ApiGetGatewayProfileResponse get(id)

Get returns the gateway-profile matching the given id.

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
api_instance = swagger_client.GatewayProfileServiceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Gateway-profile ID (UUID string).

try:
    # Get returns the gateway-profile matching the given id.
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayProfileServiceApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Gateway-profile ID (UUID string). | 

### Return type

[**ApiGetGatewayProfileResponse**](ApiGetGatewayProfileResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ApiListGatewayProfilesResponse list(limit=limit, offset=offset, network_server_id=network_server_id)

List returns the existing gateway-profiles.

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
api_instance = swagger_client.GatewayProfileServiceApi(swagger_client.ApiClient(configuration))
limit = 'limit_example' # str | Max number of items to return. (optional)
offset = 'offset_example' # str | Offset in the result-set (for pagination). (optional)
network_server_id = 'network_server_id_example' # str | Network-server ID to filter on (optional). (optional)

try:
    # List returns the existing gateway-profiles.
    api_response = api_instance.list(limit=limit, offset=offset, network_server_id=network_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayProfileServiceApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| Max number of items to return. | [optional] 
 **offset** | **str**| Offset in the result-set (for pagination). | [optional] 
 **network_server_id** | **str**| Network-server ID to filter on (optional). | [optional] 

### Return type

[**ApiListGatewayProfilesResponse**](ApiListGatewayProfilesResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> object update(gateway_profile_id, body)

Update updates the given gateway-profile.

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
api_instance = swagger_client.GatewayProfileServiceApi(swagger_client.ApiClient(configuration))
gateway_profile_id = 'gateway_profile_id_example' # str | Gateway-profile ID (UUID string).
body = swagger_client.ApiUpdateGatewayProfileRequest() # ApiUpdateGatewayProfileRequest | 

try:
    # Update updates the given gateway-profile.
    api_response = api_instance.update(gateway_profile_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GatewayProfileServiceApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_profile_id** | **str**| Gateway-profile ID (UUID string). | 
 **body** | [**ApiUpdateGatewayProfileRequest**](ApiUpdateGatewayProfileRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

