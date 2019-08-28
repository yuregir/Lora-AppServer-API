# swagger_client.DeviceProfileServiceApi

All URIs are relative to *http://api.teke.li:9090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](DeviceProfileServiceApi.md#create) | **POST** /api/device-profiles | Create creates the given device-profile.
[**delete**](DeviceProfileServiceApi.md#delete) | **DELETE** /api/device-profiles/{id} | Delete deletes the device-profile matching the given id.
[**get**](DeviceProfileServiceApi.md#get) | **GET** /api/device-profiles/{id} | Get returns the device-profile matching the given id.
[**list**](DeviceProfileServiceApi.md#list) | **GET** /api/device-profiles | List lists the available device-profiles.
[**update**](DeviceProfileServiceApi.md#update) | **PUT** /api/device-profiles/{device_profile.id} | Update updates the given device-profile.


# **create**
> ApiCreateDeviceProfileResponse create(body)

Create creates the given device-profile.

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
api_instance = swagger_client.DeviceProfileServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.ApiCreateDeviceProfileRequest() # ApiCreateDeviceProfileRequest | 

try:
    # Create creates the given device-profile.
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceProfileServiceApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiCreateDeviceProfileRequest**](ApiCreateDeviceProfileRequest.md)|  | 

### Return type

[**ApiCreateDeviceProfileResponse**](ApiCreateDeviceProfileResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> object delete(id)

Delete deletes the device-profile matching the given id.

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
api_instance = swagger_client.DeviceProfileServiceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Device-profile ID (UUID string).

try:
    # Delete deletes the device-profile matching the given id.
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceProfileServiceApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device-profile ID (UUID string). | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ApiGetDeviceProfileResponse get(id)

Get returns the device-profile matching the given id.

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
api_instance = swagger_client.DeviceProfileServiceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Device-profile ID (UUID string).

try:
    # Get returns the device-profile matching the given id.
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceProfileServiceApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Device-profile ID (UUID string). | 

### Return type

[**ApiGetDeviceProfileResponse**](ApiGetDeviceProfileResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ApiListDeviceProfileResponse list(limit=limit, offset=offset, organization_id=organization_id, application_id=application_id)

List lists the available device-profiles.

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
api_instance = swagger_client.DeviceProfileServiceApi(swagger_client.ApiClient(configuration))
limit = 'limit_example' # str | Max number of items to return. (optional)
offset = 'offset_example' # str | Offset in the result-set (for pagination). (optional)
organization_id = 'organization_id_example' # str | Organization id to filter on. (optional)
application_id = 'application_id_example' # str | Application id to filter on. (optional)

try:
    # List lists the available device-profiles.
    api_response = api_instance.list(limit=limit, offset=offset, organization_id=organization_id, application_id=application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceProfileServiceApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| Max number of items to return. | [optional] 
 **offset** | **str**| Offset in the result-set (for pagination). | [optional] 
 **organization_id** | **str**| Organization id to filter on. | [optional] 
 **application_id** | **str**| Application id to filter on. | [optional] 

### Return type

[**ApiListDeviceProfileResponse**](ApiListDeviceProfileResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> object update(device_profile_id, body)

Update updates the given device-profile.

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
api_instance = swagger_client.DeviceProfileServiceApi(swagger_client.ApiClient(configuration))
device_profile_id = 'device_profile_id_example' # str | Device-profile ID (UUID string).
body = swagger_client.ApiUpdateDeviceProfileRequest() # ApiUpdateDeviceProfileRequest | 

try:
    # Update updates the given device-profile.
    api_response = api_instance.update(device_profile_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceProfileServiceApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_profile_id** | **str**| Device-profile ID (UUID string). | 
 **body** | [**ApiUpdateDeviceProfileRequest**](ApiUpdateDeviceProfileRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

