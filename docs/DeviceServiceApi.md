# swagger_client.DeviceServiceApi

All URIs are relative to *http://api.teke.li:9090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate**](DeviceServiceApi.md#activate) | **POST** /api/devices/{device_activation.dev_eui}/activate | Activate (re)activates the device (only when ABP is set to true).
[**create**](DeviceServiceApi.md#create) | **POST** /api/devices | Create creates the given device.
[**create_keys**](DeviceServiceApi.md#create_keys) | **POST** /api/devices/{device_keys.dev_eui}/keys | CreateKeys creates the given device-keys.
[**deactivate**](DeviceServiceApi.md#deactivate) | **DELETE** /api/devices/{dev_eui}/activation | Deactivate de-activates the device.
[**delete**](DeviceServiceApi.md#delete) | **DELETE** /api/devices/{dev_eui} | Delete deletes the device matching the given DevEUI.
[**delete_keys**](DeviceServiceApi.md#delete_keys) | **DELETE** /api/devices/{dev_eui}/keys | DeleteKeys deletes the device-keys for the given DevEUI.
[**get**](DeviceServiceApi.md#get) | **GET** /api/devices/{dev_eui} | Get returns the device matching the given DevEUI.
[**get_activation**](DeviceServiceApi.md#get_activation) | **GET** /api/devices/{dev_eui}/activation | GetActivation returns the current activation details of the device (OTAA and ABP).
[**get_keys**](DeviceServiceApi.md#get_keys) | **GET** /api/devices/{dev_eui}/keys | GetKeys returns the device-keys for the given DevEUI.
[**get_random_dev_addr**](DeviceServiceApi.md#get_random_dev_addr) | **POST** /api/devices/{dev_eui}/getRandomDevAddr | GetRandomDevAddr returns a random DevAddr taking the NwkID prefix into account.
[**list**](DeviceServiceApi.md#list) | **GET** /api/devices | List returns the available devices.
[**stream_event_logs**](DeviceServiceApi.md#stream_event_logs) | **GET** /api/devices/{dev_eui}/events | StreamEventLogs stream the device events (uplink payloads, ACKs, joins, errors).   * This endpoint is intended for debugging only.   * This endpoint does not work from a web-browser.
[**stream_frame_logs**](DeviceServiceApi.md#stream_frame_logs) | **GET** /api/devices/{dev_eui}/frames | StreamFrameLogs streams the uplink and downlink frame-logs for the given DevEUI.   * These are the raw LoRaWAN frames and this endpoint is intended for debugging only.   * This endpoint does not work from a web-browser.
[**update**](DeviceServiceApi.md#update) | **PUT** /api/devices/{device.dev_eui} | Update updates the device matching the given DevEUI.
[**update_keys**](DeviceServiceApi.md#update_keys) | **PUT** /api/devices/{device_keys.dev_eui}/keys | UpdateKeys updates the device-keys.


# **activate**
> object activate(device_activation_dev_eui, body)

Activate (re)activates the device (only when ABP is set to true).

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
api_instance = swagger_client.DeviceServiceApi(swagger_client.ApiClient(configuration))
device_activation_dev_eui = 'device_activation_dev_eui_example' # str | Device EUI (HEX encoded).
body = swagger_client.ApiActivateDeviceRequest() # ApiActivateDeviceRequest | 

try:
    # Activate (re)activates the device (only when ABP is set to true).
    api_response = api_instance.activate(device_activation_dev_eui, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->activate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_activation_dev_eui** | **str**| Device EUI (HEX encoded). | 
 **body** | [**ApiActivateDeviceRequest**](ApiActivateDeviceRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> object create(body)

Create creates the given device.

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
api_instance = swagger_client.DeviceServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.ApiCreateDeviceRequest() # ApiCreateDeviceRequest | 

try:
    # Create creates the given device.
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiCreateDeviceRequest**](ApiCreateDeviceRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_keys**
> object create_keys(device_keys_dev_eui, body)

CreateKeys creates the given device-keys.

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
api_instance = swagger_client.DeviceServiceApi(swagger_client.ApiClient(configuration))
device_keys_dev_eui = 'device_keys_dev_eui_example' # str | Device EUI (HEX encoded).
body = swagger_client.ApiCreateDeviceKeysRequest() # ApiCreateDeviceKeysRequest | 

try:
    # CreateKeys creates the given device-keys.
    api_response = api_instance.create_keys(device_keys_dev_eui, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->create_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_keys_dev_eui** | **str**| Device EUI (HEX encoded). | 
 **body** | [**ApiCreateDeviceKeysRequest**](ApiCreateDeviceKeysRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate**
> object deactivate(dev_eui)

Deactivate de-activates the device.

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
api_instance = swagger_client.DeviceServiceApi(swagger_client.ApiClient(configuration))
dev_eui = 'dev_eui_example' # str | Device EUI (HEX encoded).

try:
    # Deactivate de-activates the device.
    api_response = api_instance.deactivate(dev_eui)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->deactivate: %s\n" % e)
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

# **delete**
> object delete(dev_eui)

Delete deletes the device matching the given DevEUI.

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
api_instance = swagger_client.DeviceServiceApi(swagger_client.ApiClient(configuration))
dev_eui = 'dev_eui_example' # str | Device EUI (HEX encoded).

try:
    # Delete deletes the device matching the given DevEUI.
    api_response = api_instance.delete(dev_eui)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->delete: %s\n" % e)
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

# **delete_keys**
> object delete_keys(dev_eui)

DeleteKeys deletes the device-keys for the given DevEUI.

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
api_instance = swagger_client.DeviceServiceApi(swagger_client.ApiClient(configuration))
dev_eui = 'dev_eui_example' # str | Device EUI (HEX encoded).

try:
    # DeleteKeys deletes the device-keys for the given DevEUI.
    api_response = api_instance.delete_keys(dev_eui)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->delete_keys: %s\n" % e)
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

# **get**
> ApiGetDeviceResponse get(dev_eui)

Get returns the device matching the given DevEUI.

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
api_instance = swagger_client.DeviceServiceApi(swagger_client.ApiClient(configuration))
dev_eui = 'dev_eui_example' # str | Device EUI (HEX encoded).

try:
    # Get returns the device matching the given DevEUI.
    api_response = api_instance.get(dev_eui)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dev_eui** | **str**| Device EUI (HEX encoded). | 

### Return type

[**ApiGetDeviceResponse**](ApiGetDeviceResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activation**
> ApiGetDeviceActivationResponse get_activation(dev_eui)

GetActivation returns the current activation details of the device (OTAA and ABP).

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
api_instance = swagger_client.DeviceServiceApi(swagger_client.ApiClient(configuration))
dev_eui = 'dev_eui_example' # str | Device EUI (HEX encoded).

try:
    # GetActivation returns the current activation details of the device (OTAA and ABP).
    api_response = api_instance.get_activation(dev_eui)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->get_activation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dev_eui** | **str**| Device EUI (HEX encoded). | 

### Return type

[**ApiGetDeviceActivationResponse**](ApiGetDeviceActivationResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_keys**
> ApiGetDeviceKeysResponse get_keys(dev_eui)

GetKeys returns the device-keys for the given DevEUI.

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
api_instance = swagger_client.DeviceServiceApi(swagger_client.ApiClient(configuration))
dev_eui = 'dev_eui_example' # str | Device EUI (HEX encoded).

try:
    # GetKeys returns the device-keys for the given DevEUI.
    api_response = api_instance.get_keys(dev_eui)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->get_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dev_eui** | **str**| Device EUI (HEX encoded). | 

### Return type

[**ApiGetDeviceKeysResponse**](ApiGetDeviceKeysResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_random_dev_addr**
> ApiGetRandomDevAddrResponse get_random_dev_addr(dev_eui)

GetRandomDevAddr returns a random DevAddr taking the NwkID prefix into account.

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
api_instance = swagger_client.DeviceServiceApi(swagger_client.ApiClient(configuration))
dev_eui = 'dev_eui_example' # str | Device EUI (HEX encoded).

try:
    # GetRandomDevAddr returns a random DevAddr taking the NwkID prefix into account.
    api_response = api_instance.get_random_dev_addr(dev_eui)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->get_random_dev_addr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dev_eui** | **str**| Device EUI (HEX encoded). | 

### Return type

[**ApiGetRandomDevAddrResponse**](ApiGetRandomDevAddrResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ApiListDeviceResponse list(limit=limit, offset=offset, application_id=application_id, search=search, multicast_group_id=multicast_group_id, service_profile_id=service_profile_id)

List returns the available devices.

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
api_instance = swagger_client.DeviceServiceApi(swagger_client.ApiClient(configuration))
limit = 'limit_example' # str | Max number of devices to return in the result-set. (optional)
offset = 'offset_example' # str | Offset in the result-set (for pagination). (optional)
application_id = 'application_id_example' # str | Application ID to filter on. (optional)
search = 'search_example' # str | Search on name or DevEUI. (optional)
multicast_group_id = 'multicast_group_id_example' # str | Multicast-group ID to filter on (string formatted UUID). (optional)
service_profile_id = 'service_profile_id_example' # str | Service-profile ID to filter on (string formatted UUID). (optional)

try:
    # List returns the available devices.
    api_response = api_instance.list(limit=limit, offset=offset, application_id=application_id, search=search, multicast_group_id=multicast_group_id, service_profile_id=service_profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| Max number of devices to return in the result-set. | [optional] 
 **offset** | **str**| Offset in the result-set (for pagination). | [optional] 
 **application_id** | **str**| Application ID to filter on. | [optional] 
 **search** | **str**| Search on name or DevEUI. | [optional] 
 **multicast_group_id** | **str**| Multicast-group ID to filter on (string formatted UUID). | [optional] 
 **service_profile_id** | **str**| Service-profile ID to filter on (string formatted UUID). | [optional] 

### Return type

[**ApiListDeviceResponse**](ApiListDeviceResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_event_logs**
> XStreamDefinitionsapiStreamDeviceEventLogsResponse stream_event_logs(dev_eui)

StreamEventLogs stream the device events (uplink payloads, ACKs, joins, errors).   * This endpoint is intended for debugging only.   * This endpoint does not work from a web-browser.

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
api_instance = swagger_client.DeviceServiceApi(swagger_client.ApiClient(configuration))
dev_eui = 'dev_eui_example' # str | Device EUI (HEX encoded).

try:
    # StreamEventLogs stream the device events (uplink payloads, ACKs, joins, errors).   * This endpoint is intended for debugging only.   * This endpoint does not work from a web-browser.
    api_response = api_instance.stream_event_logs(dev_eui)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->stream_event_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dev_eui** | **str**| Device EUI (HEX encoded). | 

### Return type

[**XStreamDefinitionsapiStreamDeviceEventLogsResponse**](XStreamDefinitionsapiStreamDeviceEventLogsResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_frame_logs**
> XStreamDefinitionsapiStreamDeviceFrameLogsResponse stream_frame_logs(dev_eui)

StreamFrameLogs streams the uplink and downlink frame-logs for the given DevEUI.   * These are the raw LoRaWAN frames and this endpoint is intended for debugging only.   * This endpoint does not work from a web-browser.

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
api_instance = swagger_client.DeviceServiceApi(swagger_client.ApiClient(configuration))
dev_eui = 'dev_eui_example' # str | Device EUI (HEX encoded).

try:
    # StreamFrameLogs streams the uplink and downlink frame-logs for the given DevEUI.   * These are the raw LoRaWAN frames and this endpoint is intended for debugging only.   * This endpoint does not work from a web-browser.
    api_response = api_instance.stream_frame_logs(dev_eui)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->stream_frame_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dev_eui** | **str**| Device EUI (HEX encoded). | 

### Return type

[**XStreamDefinitionsapiStreamDeviceFrameLogsResponse**](XStreamDefinitionsapiStreamDeviceFrameLogsResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> object update(device_dev_eui, body)

Update updates the device matching the given DevEUI.

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
api_instance = swagger_client.DeviceServiceApi(swagger_client.ApiClient(configuration))
device_dev_eui = 'device_dev_eui_example' # str | Device EUI (HEX encoded).
body = swagger_client.ApiUpdateDeviceRequest() # ApiUpdateDeviceRequest | 

try:
    # Update updates the device matching the given DevEUI.
    api_response = api_instance.update(device_dev_eui, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_dev_eui** | **str**| Device EUI (HEX encoded). | 
 **body** | [**ApiUpdateDeviceRequest**](ApiUpdateDeviceRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_keys**
> object update_keys(device_keys_dev_eui, body)

UpdateKeys updates the device-keys.

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
api_instance = swagger_client.DeviceServiceApi(swagger_client.ApiClient(configuration))
device_keys_dev_eui = 'device_keys_dev_eui_example' # str | Device EUI (HEX encoded).
body = swagger_client.ApiUpdateDeviceKeysRequest() # ApiUpdateDeviceKeysRequest | 

try:
    # UpdateKeys updates the device-keys.
    api_response = api_instance.update_keys(device_keys_dev_eui, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceServiceApi->update_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_keys_dev_eui** | **str**| Device EUI (HEX encoded). | 
 **body** | [**ApiUpdateDeviceKeysRequest**](ApiUpdateDeviceKeysRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

