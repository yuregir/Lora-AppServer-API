# swagger_client.InternalServiceApi

All URIs are relative to *http://api.teke.li:9090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**branding**](InternalServiceApi.md#branding) | **GET** /api/internal/branding | Get the branding for the UI
[**global_search**](InternalServiceApi.md#global_search) | **GET** /api/internal/search | Perform a global search.
[**login**](InternalServiceApi.md#login) | **POST** /api/internal/login | Log in a user
[**profile**](InternalServiceApi.md#profile) | **GET** /api/internal/profile | Get the current user&#39;s profile


# **branding**
> ApiBrandingResponse branding()

Get the branding for the UI

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
api_instance = swagger_client.InternalServiceApi(swagger_client.ApiClient(configuration))

try:
    # Get the branding for the UI
    api_response = api_instance.branding()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalServiceApi->branding: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiBrandingResponse**](ApiBrandingResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **global_search**
> ApiGlobalSearchResponse global_search(search=search, limit=limit, offset=offset)

Perform a global search.

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
api_instance = swagger_client.InternalServiceApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | Search query. (optional)
limit = 'limit_example' # str | Max number of results to return. (optional)
offset = 'offset_example' # str | Offset offset of the result-set (for pagination). (optional)

try:
    # Perform a global search.
    api_response = api_instance.global_search(search=search, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalServiceApi->global_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search query. | [optional] 
 **limit** | **str**| Max number of results to return. | [optional] 
 **offset** | **str**| Offset offset of the result-set (for pagination). | [optional] 

### Return type

[**ApiGlobalSearchResponse**](ApiGlobalSearchResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> ApiLoginResponse login(body)

Log in a user

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
api_instance = swagger_client.InternalServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.ApiLoginRequest() # ApiLoginRequest | 

try:
    # Log in a user
    api_response = api_instance.login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalServiceApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiLoginRequest**](ApiLoginRequest.md)|  | 

### Return type

[**ApiLoginResponse**](ApiLoginResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile**
> ApiProfileResponse profile()

Get the current user's profile

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
api_instance = swagger_client.InternalServiceApi(swagger_client.ApiClient(configuration))

try:
    # Get the current user's profile
    api_response = api_instance.profile()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternalServiceApi->profile: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiProfileResponse**](ApiProfileResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

