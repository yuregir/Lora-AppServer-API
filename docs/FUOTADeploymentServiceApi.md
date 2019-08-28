# swagger_client.FUOTADeploymentServiceApi

All URIs are relative to *http://api.teke.li:9090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_for_device**](FUOTADeploymentServiceApi.md#create_for_device) | **POST** /api/devices/{dev_eui}/fuota-deployments | CreateForDevice creates a deployment for the given DevEUI.
[**get**](FUOTADeploymentServiceApi.md#get) | **GET** /api/fuota-deployments/{id} | Get returns the fuota deployment for the given id.
[**get_deployment_device**](FUOTADeploymentServiceApi.md#get_deployment_device) | **GET** /api/fuota-deployments/{fuota_deployment_id}/devices/{dev_eui} | GetDeploymentDevice returns the deployment device.
[**list**](FUOTADeploymentServiceApi.md#list) | **GET** /api/fuota-deployments | List lists the fuota deployments.
[**list_deployment_devices**](FUOTADeploymentServiceApi.md#list_deployment_devices) | **GET** /api/fuota-deployments/{fuota_deployment_id}/devices | ListDeploymentDevices lists the devices (and status) for the given fuota deployment ID.


# **create_for_device**
> ApiCreateFUOTADeploymentForDeviceResponse create_for_device(dev_eui, body)

CreateForDevice creates a deployment for the given DevEUI.

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
api_instance = swagger_client.FUOTADeploymentServiceApi(swagger_client.ApiClient(configuration))
dev_eui = 'dev_eui_example' # str | Device EUI (HEX encoded).
body = swagger_client.ApiCreateFUOTADeploymentForDeviceRequest() # ApiCreateFUOTADeploymentForDeviceRequest | 

try:
    # CreateForDevice creates a deployment for the given DevEUI.
    api_response = api_instance.create_for_device(dev_eui, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FUOTADeploymentServiceApi->create_for_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dev_eui** | **str**| Device EUI (HEX encoded). | 
 **body** | [**ApiCreateFUOTADeploymentForDeviceRequest**](ApiCreateFUOTADeploymentForDeviceRequest.md)|  | 

### Return type

[**ApiCreateFUOTADeploymentForDeviceResponse**](ApiCreateFUOTADeploymentForDeviceResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ApiGetFUOTADeploymentResponse get(id)

Get returns the fuota deployment for the given id.

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
api_instance = swagger_client.FUOTADeploymentServiceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the deployment (string formatted UUID). This value will be automatically assigned on create.

try:
    # Get returns the fuota deployment for the given id.
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FUOTADeploymentServiceApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the deployment (string formatted UUID). This value will be automatically assigned on create. | 

### Return type

[**ApiGetFUOTADeploymentResponse**](ApiGetFUOTADeploymentResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_device**
> ApiGetFUOTADeploymentDeviceResponse get_deployment_device(fuota_deployment_id, dev_eui)

GetDeploymentDevice returns the deployment device.

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
api_instance = swagger_client.FUOTADeploymentServiceApi(swagger_client.ApiClient(configuration))
fuota_deployment_id = 'fuota_deployment_id_example' # str | ID of the deployment (string formatted UUID). This value will be automatically assigned on create.
dev_eui = 'dev_eui_example' # str | Device EUI (HEX encoded).

try:
    # GetDeploymentDevice returns the deployment device.
    api_response = api_instance.get_deployment_device(fuota_deployment_id, dev_eui)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FUOTADeploymentServiceApi->get_deployment_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fuota_deployment_id** | **str**| ID of the deployment (string formatted UUID). This value will be automatically assigned on create. | 
 **dev_eui** | **str**| Device EUI (HEX encoded). | 

### Return type

[**ApiGetFUOTADeploymentDeviceResponse**](ApiGetFUOTADeploymentDeviceResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ApiListFUOTADeploymentResponse list(limit=limit, offset=offset, application_id=application_id, dev_eui=dev_eui)

List lists the fuota deployments.

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
api_instance = swagger_client.FUOTADeploymentServiceApi(swagger_client.ApiClient(configuration))
limit = 'limit_example' # str | Max number of deployments to return in the result-set. (optional)
offset = 'offset_example' # str | Offset in the result-set (for pagination). (optional)
application_id = 'application_id_example' # str | Application ID to filter on (optional). (optional)
dev_eui = 'dev_eui_example' # str | Device EUI (HEX encoded) (optional). (optional)

try:
    # List lists the fuota deployments.
    api_response = api_instance.list(limit=limit, offset=offset, application_id=application_id, dev_eui=dev_eui)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FUOTADeploymentServiceApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| Max number of deployments to return in the result-set. | [optional] 
 **offset** | **str**| Offset in the result-set (for pagination). | [optional] 
 **application_id** | **str**| Application ID to filter on (optional). | [optional] 
 **dev_eui** | **str**| Device EUI (HEX encoded) (optional). | [optional] 

### Return type

[**ApiListFUOTADeploymentResponse**](ApiListFUOTADeploymentResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deployment_devices**
> ApiListFUOTADeploymentDevicesResponse list_deployment_devices(fuota_deployment_id, limit=limit, offset=offset)

ListDeploymentDevices lists the devices (and status) for the given fuota deployment ID.

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
api_instance = swagger_client.FUOTADeploymentServiceApi(swagger_client.ApiClient(configuration))
fuota_deployment_id = 'fuota_deployment_id_example' # str | ID of the deployment (string formatted UUID). This value will be automatically assigned on create.
limit = 'limit_example' # str | Max number of items to return. (optional)
offset = 'offset_example' # str | Offset in the result-set (for pagination). (optional)

try:
    # ListDeploymentDevices lists the devices (and status) for the given fuota deployment ID.
    api_response = api_instance.list_deployment_devices(fuota_deployment_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FUOTADeploymentServiceApi->list_deployment_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fuota_deployment_id** | **str**| ID of the deployment (string formatted UUID). This value will be automatically assigned on create. | 
 **limit** | **str**| Max number of items to return. | [optional] 
 **offset** | **str**| Offset in the result-set (for pagination). | [optional] 

### Return type

[**ApiListFUOTADeploymentDevicesResponse**](ApiListFUOTADeploymentDevicesResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

