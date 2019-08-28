# swagger_client.MulticastGroupServiceApi

All URIs are relative to *http://api.teke.li:9090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_device**](MulticastGroupServiceApi.md#add_device) | **POST** /api/multicast-groups/{multicast_group_id}/devices | AddDevice adds the given device to the multicast-group.
[**create**](MulticastGroupServiceApi.md#create) | **POST** /api/multicast-groups | Create creates the given multicast-group.
[**delete**](MulticastGroupServiceApi.md#delete) | **DELETE** /api/multicast-groups/{id} | Delete deletes a multicast-group given an ID.
[**enqueue**](MulticastGroupServiceApi.md#enqueue) | **POST** /api/multicast-groups/{multicast_queue_item.multicast_group_id}/queue | Enqueue adds the given item to the multicast-queue.
[**flush_queue**](MulticastGroupServiceApi.md#flush_queue) | **DELETE** /api/multicast-groups/{multicast_group_id}/queue | FlushQueue flushes the multicast-group queue.
[**get**](MulticastGroupServiceApi.md#get) | **GET** /api/multicast-groups/{id} | Get returns a multicast-group given an ID.
[**list**](MulticastGroupServiceApi.md#list) | **GET** /api/multicast-groups | List lists the available multicast-groups.
[**list_queue**](MulticastGroupServiceApi.md#list_queue) | **GET** /api/multicast-groups/{multicast_group_id}/queue | ListQueue lists the items in the multicast-group queue.
[**remove_device**](MulticastGroupServiceApi.md#remove_device) | **DELETE** /api/multicast-groups/{multicast_group_id}/devices/{dev_eui} | RemoveDevice removes the given device from the multicast-group.
[**update**](MulticastGroupServiceApi.md#update) | **PUT** /api/multicast-groups/{multicast_group.id} | Update updates the given multicast-group.


# **add_device**
> object add_device(multicast_group_id, body)

AddDevice adds the given device to the multicast-group.

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
api_instance = swagger_client.MulticastGroupServiceApi(swagger_client.ApiClient(configuration))
multicast_group_id = 'multicast_group_id_example' # str | Multicast-group ID (string formatted UUID).
body = swagger_client.ApiAddDeviceToMulticastGroupRequest() # ApiAddDeviceToMulticastGroupRequest | 

try:
    # AddDevice adds the given device to the multicast-group.
    api_response = api_instance.add_device(multicast_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MulticastGroupServiceApi->add_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multicast_group_id** | **str**| Multicast-group ID (string formatted UUID). | 
 **body** | [**ApiAddDeviceToMulticastGroupRequest**](ApiAddDeviceToMulticastGroupRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> ApiCreateMulticastGroupResponse create(body)

Create creates the given multicast-group.

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
api_instance = swagger_client.MulticastGroupServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.ApiCreateMulticastGroupRequest() # ApiCreateMulticastGroupRequest | 

try:
    # Create creates the given multicast-group.
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MulticastGroupServiceApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiCreateMulticastGroupRequest**](ApiCreateMulticastGroupRequest.md)|  | 

### Return type

[**ApiCreateMulticastGroupResponse**](ApiCreateMulticastGroupResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> object delete(id)

Delete deletes a multicast-group given an ID.

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
api_instance = swagger_client.MulticastGroupServiceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID (string formatted UUID).

try:
    # Delete deletes a multicast-group given an ID.
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MulticastGroupServiceApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID (string formatted UUID). | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enqueue**
> ApiEnqueueMulticastQueueItemResponse enqueue(multicast_queue_item_multicast_group_id, body)

Enqueue adds the given item to the multicast-queue.

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
api_instance = swagger_client.MulticastGroupServiceApi(swagger_client.ApiClient(configuration))
multicast_queue_item_multicast_group_id = 'multicast_queue_item_multicast_group_id_example' # str | Multicast-group ID (string formatted UUID).
body = swagger_client.ApiEnqueueMulticastQueueItemRequest() # ApiEnqueueMulticastQueueItemRequest | 

try:
    # Enqueue adds the given item to the multicast-queue.
    api_response = api_instance.enqueue(multicast_queue_item_multicast_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MulticastGroupServiceApi->enqueue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multicast_queue_item_multicast_group_id** | **str**| Multicast-group ID (string formatted UUID). | 
 **body** | [**ApiEnqueueMulticastQueueItemRequest**](ApiEnqueueMulticastQueueItemRequest.md)|  | 

### Return type

[**ApiEnqueueMulticastQueueItemResponse**](ApiEnqueueMulticastQueueItemResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flush_queue**
> object flush_queue(multicast_group_id)

FlushQueue flushes the multicast-group queue.

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
api_instance = swagger_client.MulticastGroupServiceApi(swagger_client.ApiClient(configuration))
multicast_group_id = 'multicast_group_id_example' # str | Multicast-group ID (string formatted UUID).

try:
    # FlushQueue flushes the multicast-group queue.
    api_response = api_instance.flush_queue(multicast_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MulticastGroupServiceApi->flush_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multicast_group_id** | **str**| Multicast-group ID (string formatted UUID). | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ApiGetMulticastGroupResponse get(id)

Get returns a multicast-group given an ID.

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
api_instance = swagger_client.MulticastGroupServiceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID (string formatted UUID).

try:
    # Get returns a multicast-group given an ID.
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MulticastGroupServiceApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID (string formatted UUID). | 

### Return type

[**ApiGetMulticastGroupResponse**](ApiGetMulticastGroupResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ApiListMulticastGroupResponse list(limit=limit, offset=offset, organization_id=organization_id, dev_eui=dev_eui, service_profile_id=service_profile_id, search=search)

List lists the available multicast-groups.

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
api_instance = swagger_client.MulticastGroupServiceApi(swagger_client.ApiClient(configuration))
limit = 'limit_example' # str | Max number of items to return. (optional)
offset = 'offset_example' # str | Offset in the result-set (for pagination). (optional)
organization_id = 'organization_id_example' # str | Organization id to filter on. (optional)
dev_eui = 'dev_eui_example' # str | Device EUI (HEX encoded string) to filter on. (optional)
service_profile_id = 'service_profile_id_example' # str | Service-profile ID to filter on. (optional)
search = 'search_example' # str | Search can be used to search on the multicast-group name. (optional)

try:
    # List lists the available multicast-groups.
    api_response = api_instance.list(limit=limit, offset=offset, organization_id=organization_id, dev_eui=dev_eui, service_profile_id=service_profile_id, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MulticastGroupServiceApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| Max number of items to return. | [optional] 
 **offset** | **str**| Offset in the result-set (for pagination). | [optional] 
 **organization_id** | **str**| Organization id to filter on. | [optional] 
 **dev_eui** | **str**| Device EUI (HEX encoded string) to filter on. | [optional] 
 **service_profile_id** | **str**| Service-profile ID to filter on. | [optional] 
 **search** | **str**| Search can be used to search on the multicast-group name. | [optional] 

### Return type

[**ApiListMulticastGroupResponse**](ApiListMulticastGroupResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_queue**
> ApiListMulticastGroupQueueItemsResponse list_queue(multicast_group_id)

ListQueue lists the items in the multicast-group queue.

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
api_instance = swagger_client.MulticastGroupServiceApi(swagger_client.ApiClient(configuration))
multicast_group_id = 'multicast_group_id_example' # str | Multicast-group ID (string formatted UUID).

try:
    # ListQueue lists the items in the multicast-group queue.
    api_response = api_instance.list_queue(multicast_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MulticastGroupServiceApi->list_queue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multicast_group_id** | **str**| Multicast-group ID (string formatted UUID). | 

### Return type

[**ApiListMulticastGroupQueueItemsResponse**](ApiListMulticastGroupQueueItemsResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_device**
> object remove_device(multicast_group_id, dev_eui)

RemoveDevice removes the given device from the multicast-group.

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
api_instance = swagger_client.MulticastGroupServiceApi(swagger_client.ApiClient(configuration))
multicast_group_id = 'multicast_group_id_example' # str | Multicast-group ID (string formatted UUID).
dev_eui = 'dev_eui_example' # str | Device EUI (HEX encoded string).

try:
    # RemoveDevice removes the given device from the multicast-group.
    api_response = api_instance.remove_device(multicast_group_id, dev_eui)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MulticastGroupServiceApi->remove_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multicast_group_id** | **str**| Multicast-group ID (string formatted UUID). | 
 **dev_eui** | **str**| Device EUI (HEX encoded string). | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> object update(multicast_group_id, body)

Update updates the given multicast-group.

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
api_instance = swagger_client.MulticastGroupServiceApi(swagger_client.ApiClient(configuration))
multicast_group_id = 'multicast_group_id_example' # str | ID (string formatted UUID). This will be generated automatically on create.
body = swagger_client.ApiUpdateMulticastGroupRequest() # ApiUpdateMulticastGroupRequest | 

try:
    # Update updates the given multicast-group.
    api_response = api_instance.update(multicast_group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MulticastGroupServiceApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **multicast_group_id** | **str**| ID (string formatted UUID). This will be generated automatically on create. | 
 **body** | [**ApiUpdateMulticastGroupRequest**](ApiUpdateMulticastGroupRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

