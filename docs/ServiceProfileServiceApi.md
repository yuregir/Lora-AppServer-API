# swagger_client.ServiceProfileServiceApi

All URIs are relative to *http://api.teke.li:9090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ServiceProfileServiceApi.md#create) | **POST** /api/service-profiles | Create creates the given service-profile.
[**delete**](ServiceProfileServiceApi.md#delete) | **DELETE** /api/service-profiles/{id} | Delete deletes the service-profile matching the given id.
[**get**](ServiceProfileServiceApi.md#get) | **GET** /api/service-profiles/{id} | Get returns the service-profile matching the given id.
[**list**](ServiceProfileServiceApi.md#list) | **GET** /api/service-profiles | List lists the available service-profiles.
[**update**](ServiceProfileServiceApi.md#update) | **PUT** /api/service-profiles/{service_profile.id} | Update updates the given serviceprofile.


# **create**
> ApiCreateServiceProfileResponse create(body)

Create creates the given service-profile.

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
api_instance = swagger_client.ServiceProfileServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.ApiCreateServiceProfileRequest() # ApiCreateServiceProfileRequest | 

try:
    # Create creates the given service-profile.
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceProfileServiceApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiCreateServiceProfileRequest**](ApiCreateServiceProfileRequest.md)|  | 

### Return type

[**ApiCreateServiceProfileResponse**](ApiCreateServiceProfileResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> object delete(id)

Delete deletes the service-profile matching the given id.

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
api_instance = swagger_client.ServiceProfileServiceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Service-profile ID (UUID string).

try:
    # Delete deletes the service-profile matching the given id.
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceProfileServiceApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Service-profile ID (UUID string). | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ApiGetServiceProfileResponse get(id)

Get returns the service-profile matching the given id.

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
api_instance = swagger_client.ServiceProfileServiceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Service-profile ID (UUID string).

try:
    # Get returns the service-profile matching the given id.
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceProfileServiceApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Service-profile ID (UUID string). | 

### Return type

[**ApiGetServiceProfileResponse**](ApiGetServiceProfileResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ApiListServiceProfileResponse list(limit=limit, offset=offset, organization_id=organization_id)

List lists the available service-profiles.

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
api_instance = swagger_client.ServiceProfileServiceApi(swagger_client.ApiClient(configuration))
limit = 'limit_example' # str | Max number of items to return. (optional)
offset = 'offset_example' # str | Offset in the result-set (for pagination). (optional)
organization_id = 'organization_id_example' # str | Organization id to filter on. (optional)

try:
    # List lists the available service-profiles.
    api_response = api_instance.list(limit=limit, offset=offset, organization_id=organization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceProfileServiceApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| Max number of items to return. | [optional] 
 **offset** | **str**| Offset in the result-set (for pagination). | [optional] 
 **organization_id** | **str**| Organization id to filter on. | [optional] 

### Return type

[**ApiListServiceProfileResponse**](ApiListServiceProfileResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> object update(service_profile_id, body)

Update updates the given serviceprofile.

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
api_instance = swagger_client.ServiceProfileServiceApi(swagger_client.ApiClient(configuration))
service_profile_id = 'service_profile_id_example' # str | Service-profile ID (UUID string). This will be automatically set on create.
body = swagger_client.ApiUpdateServiceProfileRequest() # ApiUpdateServiceProfileRequest | 

try:
    # Update updates the given serviceprofile.
    api_response = api_instance.update(service_profile_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceProfileServiceApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_profile_id** | **str**| Service-profile ID (UUID string). This will be automatically set on create. | 
 **body** | [**ApiUpdateServiceProfileRequest**](ApiUpdateServiceProfileRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

