# swagger_client.UserServiceApi

All URIs are relative to *http://api.teke.li:9090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](UserServiceApi.md#create) | **POST** /api/users | Create a new user.
[**delete**](UserServiceApi.md#delete) | **DELETE** /api/users/{id} | Delete a user.
[**get**](UserServiceApi.md#get) | **GET** /api/users/{id} | Get data for a particular user.
[**list**](UserServiceApi.md#list) | **GET** /api/users | Get user list.
[**update**](UserServiceApi.md#update) | **PUT** /api/users/{user.id} | Update an existing user.
[**update_password**](UserServiceApi.md#update_password) | **PUT** /api/users/{user_id}/password | UpdatePassword updates a password.


# **create**
> ApiCreateUserResponse create(body)

Create a new user.

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
api_instance = swagger_client.UserServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.ApiCreateUserRequest() # ApiCreateUserRequest | 

try:
    # Create a new user.
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserServiceApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiCreateUserRequest**](ApiCreateUserRequest.md)|  | 

### Return type

[**ApiCreateUserResponse**](ApiCreateUserResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> object delete(id)

Delete a user.

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
api_instance = swagger_client.UserServiceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | User ID.

try:
    # Delete a user.
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserServiceApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User ID. | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ApiGetUserResponse get(id)

Get data for a particular user.

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
api_instance = swagger_client.UserServiceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | User ID.

try:
    # Get data for a particular user.
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserServiceApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User ID. | 

### Return type

[**ApiGetUserResponse**](ApiGetUserResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ApiListUserResponse list(limit=limit, offset=offset, search=search)

Get user list.

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
api_instance = swagger_client.UserServiceApi(swagger_client.ApiClient(configuration))
limit = 'limit_example' # str | Max number of user to return in the result-set. (optional)
offset = 'offset_example' # str | Offset in the result-set (for pagination). (optional)
search = 'search_example' # str | When provided, the given string will be used to search on username. (optional)

try:
    # Get user list.
    api_response = api_instance.list(limit=limit, offset=offset, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserServiceApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| Max number of user to return in the result-set. | [optional] 
 **offset** | **str**| Offset in the result-set (for pagination). | [optional] 
 **search** | **str**| When provided, the given string will be used to search on username. | [optional] 

### Return type

[**ApiListUserResponse**](ApiListUserResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> object update(user_id, body)

Update an existing user.

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
api_instance = swagger_client.UserServiceApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | User ID. Will be set automatically on create.
body = swagger_client.ApiUpdateUserRequest() # ApiUpdateUserRequest | 

try:
    # Update an existing user.
    api_response = api_instance.update(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserServiceApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID. Will be set automatically on create. | 
 **body** | [**ApiUpdateUserRequest**](ApiUpdateUserRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password**
> object update_password(user_id, body)

UpdatePassword updates a password.

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
api_instance = swagger_client.UserServiceApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | User ID.
body = swagger_client.ApiUpdateUserPasswordRequest() # ApiUpdateUserPasswordRequest | 

try:
    # UpdatePassword updates a password.
    api_response = api_instance.update_password(user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserServiceApi->update_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID. | 
 **body** | [**ApiUpdateUserPasswordRequest**](ApiUpdateUserPasswordRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

