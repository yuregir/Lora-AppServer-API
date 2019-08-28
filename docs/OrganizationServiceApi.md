# swagger_client.OrganizationServiceApi

All URIs are relative to *http://api.teke.li:9090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user**](OrganizationServiceApi.md#add_user) | **POST** /api/organizations/{organization_user.organization_id}/users | Add a new user to an organization.
[**create**](OrganizationServiceApi.md#create) | **POST** /api/organizations | Create a new organization.
[**delete**](OrganizationServiceApi.md#delete) | **DELETE** /api/organizations/{id} | Delete an organization.
[**delete_user**](OrganizationServiceApi.md#delete_user) | **DELETE** /api/organizations/{organization_id}/users/{user_id} | Delete a user from an organization.
[**get**](OrganizationServiceApi.md#get) | **GET** /api/organizations/{id} | Get data for a particular organization.
[**get_user**](OrganizationServiceApi.md#get_user) | **GET** /api/organizations/{organization_id}/users/{user_id} | Get data for a particular organization user.
[**list**](OrganizationServiceApi.md#list) | **GET** /api/organizations | Get organization list.
[**list_users**](OrganizationServiceApi.md#list_users) | **GET** /api/organizations/{organization_id}/users | Get organization&#39;s user list.
[**update**](OrganizationServiceApi.md#update) | **PUT** /api/organizations/{organization.id} | Update an existing organization.
[**update_user**](OrganizationServiceApi.md#update_user) | **PUT** /api/organizations/{organization_user.organization_id}/users/{organization_user.user_id} | Update a user in an organization.


# **add_user**
> object add_user(organization_user_organization_id, body)

Add a new user to an organization.

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
api_instance = swagger_client.OrganizationServiceApi(swagger_client.ApiClient(configuration))
organization_user_organization_id = 'organization_user_organization_id_example' # str | Organization ID.
body = swagger_client.ApiAddOrganizationUserRequest() # ApiAddOrganizationUserRequest | 

try:
    # Add a new user to an organization.
    api_response = api_instance.add_user(organization_user_organization_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationServiceApi->add_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_user_organization_id** | **str**| Organization ID. | 
 **body** | [**ApiAddOrganizationUserRequest**](ApiAddOrganizationUserRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> ApiCreateOrganizationResponse create(body)

Create a new organization.

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
api_instance = swagger_client.OrganizationServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.ApiCreateOrganizationRequest() # ApiCreateOrganizationRequest | 

try:
    # Create a new organization.
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationServiceApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiCreateOrganizationRequest**](ApiCreateOrganizationRequest.md)|  | 

### Return type

[**ApiCreateOrganizationResponse**](ApiCreateOrganizationResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> object delete(id)

Delete an organization.

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
api_instance = swagger_client.OrganizationServiceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Organization ID.

try:
    # Delete an organization.
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationServiceApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organization ID. | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> object delete_user(organization_id, user_id)

Delete a user from an organization.

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
api_instance = swagger_client.OrganizationServiceApi(swagger_client.ApiClient(configuration))
organization_id = 'organization_id_example' # str | Organization ID.
user_id = 'user_id_example' # str | User ID.

try:
    # Delete a user from an organization.
    api_response = api_instance.delete_user(organization_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationServiceApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID. | 
 **user_id** | **str**| User ID. | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ApiGetOrganizationResponse get(id)

Get data for a particular organization.

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
api_instance = swagger_client.OrganizationServiceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Organization ID.

try:
    # Get data for a particular organization.
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationServiceApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Organization ID. | 

### Return type

[**ApiGetOrganizationResponse**](ApiGetOrganizationResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> ApiGetOrganizationUserResponse get_user(organization_id, user_id)

Get data for a particular organization user.

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
api_instance = swagger_client.OrganizationServiceApi(swagger_client.ApiClient(configuration))
organization_id = 'organization_id_example' # str | Organization ID.
user_id = 'user_id_example' # str | User ID.

try:
    # Get data for a particular organization user.
    api_response = api_instance.get_user(organization_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationServiceApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID. | 
 **user_id** | **str**| User ID. | 

### Return type

[**ApiGetOrganizationUserResponse**](ApiGetOrganizationUserResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ApiListOrganizationResponse list(limit=limit, offset=offset, search=search)

Get organization list.

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
api_instance = swagger_client.OrganizationServiceApi(swagger_client.ApiClient(configuration))
limit = 'limit_example' # str | Max number of organizations to return in the result-set. (optional)
offset = 'offset_example' # str | Offset in the result-set (for pagination). (optional)
search = 'search_example' # str | When provided, the given string will be used to search on displayName. (optional)

try:
    # Get organization list.
    api_response = api_instance.list(limit=limit, offset=offset, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationServiceApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| Max number of organizations to return in the result-set. | [optional] 
 **offset** | **str**| Offset in the result-set (for pagination). | [optional] 
 **search** | **str**| When provided, the given string will be used to search on displayName. | [optional] 

### Return type

[**ApiListOrganizationResponse**](ApiListOrganizationResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> ApiListOrganizationUsersResponse list_users(organization_id, limit=limit, offset=offset)

Get organization's user list.

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
api_instance = swagger_client.OrganizationServiceApi(swagger_client.ApiClient(configuration))
organization_id = 'organization_id_example' # str | Organization ID.
limit = 56 # int | Max number of users to return in the result-set. (optional)
offset = 56 # int | Offset in the result-set (for pagination). (optional)

try:
    # Get organization's user list.
    api_response = api_instance.list_users(organization_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationServiceApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID. | 
 **limit** | **int**| Max number of users to return in the result-set. | [optional] 
 **offset** | **int**| Offset in the result-set (for pagination). | [optional] 

### Return type

[**ApiListOrganizationUsersResponse**](ApiListOrganizationUsersResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> object update(organization_id, body)

Update an existing organization.

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
api_instance = swagger_client.OrganizationServiceApi(swagger_client.ApiClient(configuration))
organization_id = 'organization_id_example' # str | Organization ID.
body = swagger_client.ApiUpdateOrganizationRequest() # ApiUpdateOrganizationRequest | 

try:
    # Update an existing organization.
    api_response = api_instance.update(organization_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationServiceApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID. | 
 **body** | [**ApiUpdateOrganizationRequest**](ApiUpdateOrganizationRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> object update_user(organization_user_organization_id, organization_user_user_id, body)

Update a user in an organization.

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
api_instance = swagger_client.OrganizationServiceApi(swagger_client.ApiClient(configuration))
organization_user_organization_id = 'organization_user_organization_id_example' # str | Organization ID.
organization_user_user_id = 'organization_user_user_id_example' # str | User ID.
body = swagger_client.ApiUpdateOrganizationUserRequest() # ApiUpdateOrganizationUserRequest | 

try:
    # Update a user in an organization.
    api_response = api_instance.update_user(organization_user_organization_id, organization_user_user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationServiceApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_user_organization_id** | **str**| Organization ID. | 
 **organization_user_user_id** | **str**| User ID. | 
 **body** | [**ApiUpdateOrganizationUserRequest**](ApiUpdateOrganizationUserRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

