# swagger_client.DeviceQueueServiceApi

All URIs are relative to *http://api.teke.li:9090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enqueue**](DeviceQueueServiceApi.md#enqueue) | **POST** /api/devices/{device_queue_item.dev_eui}/queue | Enqueue adds the given item to the device-queue.
[**flush**](DeviceQueueServiceApi.md#flush) | **DELETE** /api/devices/{dev_eui}/queue | Flush flushes the downlink device-queue.
[**list**](DeviceQueueServiceApi.md#list) | **GET** /api/devices/{dev_eui}/queue | List lists the items in the device-queue.


# **enqueue**
> ApiEnqueueDeviceQueueItemResponse enqueue(device_queue_item_dev_eui, body)

Enqueue adds the given item to the device-queue.

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
api_instance = swagger_client.DeviceQueueServiceApi(swagger_client.ApiClient(configuration))
device_queue_item_dev_eui = 'device_queue_item_dev_eui_example' # str | Device EUI (HEX encoded).
body = swagger_client.ApiEnqueueDeviceQueueItemRequest() # ApiEnqueueDeviceQueueItemRequest | 

try:
    # Enqueue adds the given item to the device-queue.
    api_response = api_instance.enqueue(device_queue_item_dev_eui, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceQueueServiceApi->enqueue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_queue_item_dev_eui** | **str**| Device EUI (HEX encoded). | 
 **body** | [**ApiEnqueueDeviceQueueItemRequest**](ApiEnqueueDeviceQueueItemRequest.md)|  | 

### Return type

[**ApiEnqueueDeviceQueueItemResponse**](ApiEnqueueDeviceQueueItemResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **flush**
> object flush(dev_eui)

Flush flushes the downlink device-queue.

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
api_instance = swagger_client.DeviceQueueServiceApi(swagger_client.ApiClient(configuration))
dev_eui = 'dev_eui_example' # str | Device EUI (HEX encoded).

try:
    # Flush flushes the downlink device-queue.
    api_response = api_instance.flush(dev_eui)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceQueueServiceApi->flush: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dev_eui** | **str**| Device EUI (HEX encoded). | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ApiListDeviceQueueItemsResponse list(dev_eui)

List lists the items in the device-queue.

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
api_instance = swagger_client.DeviceQueueServiceApi(swagger_client.ApiClient(configuration))
dev_eui = 'dev_eui_example' # str | Device EUI (HEX encoded).

try:
    # List lists the items in the device-queue.
    api_response = api_instance.list(dev_eui)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceQueueServiceApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dev_eui** | **str**| Device EUI (HEX encoded). | 

### Return type

[**ApiListDeviceQueueItemsResponse**](ApiListDeviceQueueItemsResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

