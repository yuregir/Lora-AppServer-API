# swagger_client.ApplicationServiceApi

All URIs are relative to *http://api.teke.li:9090*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ApplicationServiceApi.md#create) | **POST** /api/applications | Create creates the given application.
[**create_http_integration**](ApplicationServiceApi.md#create_http_integration) | **POST** /api/applications/{integration.application_id}/integrations/http | CreateHTTPIntegration creates a HTTP application-integration.
[**create_influx_db_integration**](ApplicationServiceApi.md#create_influx_db_integration) | **POST** /api/applications/{integration.application_id}/integrations/influxdb | CreateInfluxDBIntegration create an InfluxDB application-integration.
[**create_things_board_integration**](ApplicationServiceApi.md#create_things_board_integration) | **POST** /api/applications/{integration.application_id}/integrations/thingsboard | CreateThingsBoardIntegration creates a ThingsBoard application-integration.
[**delete**](ApplicationServiceApi.md#delete) | **DELETE** /api/applications/{id} | Delete deletes the given application.
[**delete_http_integration**](ApplicationServiceApi.md#delete_http_integration) | **DELETE** /api/applications/{application_id}/integrations/http | DeleteIntegration deletes the HTTP application-integration.
[**delete_influx_db_integration**](ApplicationServiceApi.md#delete_influx_db_integration) | **DELETE** /api/applications/{application_id}/integrations/influxdb | DeleteInfluxDBIntegration deletes the InfluxDB application-integration.
[**delete_things_board_integration**](ApplicationServiceApi.md#delete_things_board_integration) | **DELETE** /api/applications/{application_id}/integrations/thingsboard | DeleteThingsBoardIntegration deletes the ThingsBoard application-integration.
[**get**](ApplicationServiceApi.md#get) | **GET** /api/applications/{id} | Get returns the requested application.
[**get_http_integration**](ApplicationServiceApi.md#get_http_integration) | **GET** /api/applications/{application_id}/integrations/http | GetHTTPIntegration returns the HTTP application-integration.
[**get_influx_db_integration**](ApplicationServiceApi.md#get_influx_db_integration) | **GET** /api/applications/{application_id}/integrations/influxdb | GetInfluxDBIntegration returns the InfluxDB application-integration.
[**get_things_board_integration**](ApplicationServiceApi.md#get_things_board_integration) | **GET** /api/applications/{application_id}/integrations/thingsboard | GetThingsBoardIntegration returns the ThingsBoard application-integration.
[**list**](ApplicationServiceApi.md#list) | **GET** /api/applications | List lists the available applications.
[**list_integrations**](ApplicationServiceApi.md#list_integrations) | **GET** /api/applications/{application_id}/integrations | ListIntegrations lists all configured integrations.
[**update**](ApplicationServiceApi.md#update) | **PUT** /api/applications/{application.id} | Update updates the given application.
[**update_http_integration**](ApplicationServiceApi.md#update_http_integration) | **PUT** /api/applications/{integration.application_id}/integrations/http | UpdateHTTPIntegration updates the HTTP application-integration.
[**update_influx_db_integration**](ApplicationServiceApi.md#update_influx_db_integration) | **PUT** /api/applications/{integration.application_id}/integrations/influxdb | UpdateInfluxDBIntegration updates the InfluxDB application-integration.
[**update_things_board_integration**](ApplicationServiceApi.md#update_things_board_integration) | **PUT** /api/applications/{integration.application_id}/integrations/thingsboard | UpdateThingsBoardIntegration updates the ThingsBoard application-integration.


# **create**
> ApiCreateApplicationResponse create(body)

Create creates the given application.

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
api_instance = swagger_client.ApplicationServiceApi(swagger_client.ApiClient(configuration))
body = swagger_client.ApiCreateApplicationRequest() # ApiCreateApplicationRequest | 

try:
    # Create creates the given application.
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiCreateApplicationRequest**](ApiCreateApplicationRequest.md)|  | 

### Return type

[**ApiCreateApplicationResponse**](ApiCreateApplicationResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_http_integration**
> object create_http_integration(integration_application_id, body)

CreateHTTPIntegration creates a HTTP application-integration.

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
api_instance = swagger_client.ApplicationServiceApi(swagger_client.ApiClient(configuration))
integration_application_id = 'integration_application_id_example' # str | The id of the application.
body = swagger_client.ApiCreateHTTPIntegrationRequest() # ApiCreateHTTPIntegrationRequest | 

try:
    # CreateHTTPIntegration creates a HTTP application-integration.
    api_response = api_instance.create_http_integration(integration_application_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->create_http_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_application_id** | **str**| The id of the application. | 
 **body** | [**ApiCreateHTTPIntegrationRequest**](ApiCreateHTTPIntegrationRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_influx_db_integration**
> object create_influx_db_integration(integration_application_id, body)

CreateInfluxDBIntegration create an InfluxDB application-integration.

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
api_instance = swagger_client.ApplicationServiceApi(swagger_client.ApiClient(configuration))
integration_application_id = 'integration_application_id_example' # str | Application ID.
body = swagger_client.ApiCreateInfluxDBIntegrationRequest() # ApiCreateInfluxDBIntegrationRequest | 

try:
    # CreateInfluxDBIntegration create an InfluxDB application-integration.
    api_response = api_instance.create_influx_db_integration(integration_application_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->create_influx_db_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_application_id** | **str**| Application ID. | 
 **body** | [**ApiCreateInfluxDBIntegrationRequest**](ApiCreateInfluxDBIntegrationRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_things_board_integration**
> object create_things_board_integration(integration_application_id, body)

CreateThingsBoardIntegration creates a ThingsBoard application-integration.

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
api_instance = swagger_client.ApplicationServiceApi(swagger_client.ApiClient(configuration))
integration_application_id = 'integration_application_id_example' # str | Application ID.
body = swagger_client.ApiCreateThingsBoardIntegrationRequest() # ApiCreateThingsBoardIntegrationRequest | 

try:
    # CreateThingsBoardIntegration creates a ThingsBoard application-integration.
    api_response = api_instance.create_things_board_integration(integration_application_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->create_things_board_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_application_id** | **str**| Application ID. | 
 **body** | [**ApiCreateThingsBoardIntegrationRequest**](ApiCreateThingsBoardIntegrationRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> object delete(id)

Delete deletes the given application.

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
api_instance = swagger_client.ApplicationServiceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Application ID.

try:
    # Delete deletes the given application.
    api_response = api_instance.delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Application ID. | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_http_integration**
> object delete_http_integration(application_id)

DeleteIntegration deletes the HTTP application-integration.

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
api_instance = swagger_client.ApplicationServiceApi(swagger_client.ApiClient(configuration))
application_id = 'application_id_example' # str | The id of the application.

try:
    # DeleteIntegration deletes the HTTP application-integration.
    api_response = api_instance.delete_http_integration(application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->delete_http_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The id of the application. | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_influx_db_integration**
> object delete_influx_db_integration(application_id)

DeleteInfluxDBIntegration deletes the InfluxDB application-integration.

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
api_instance = swagger_client.ApplicationServiceApi(swagger_client.ApiClient(configuration))
application_id = 'application_id_example' # str | Application ID.

try:
    # DeleteInfluxDBIntegration deletes the InfluxDB application-integration.
    api_response = api_instance.delete_influx_db_integration(application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->delete_influx_db_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID. | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_things_board_integration**
> object delete_things_board_integration(application_id)

DeleteThingsBoardIntegration deletes the ThingsBoard application-integration.

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
api_instance = swagger_client.ApplicationServiceApi(swagger_client.ApiClient(configuration))
application_id = 'application_id_example' # str | Application ID.

try:
    # DeleteThingsBoardIntegration deletes the ThingsBoard application-integration.
    api_response = api_instance.delete_things_board_integration(application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->delete_things_board_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID. | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ApiGetApplicationResponse get(id)

Get returns the requested application.

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
api_instance = swagger_client.ApplicationServiceApi(swagger_client.ApiClient(configuration))
id = 'id_example' # str | Application ID.

try:
    # Get returns the requested application.
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Application ID. | 

### Return type

[**ApiGetApplicationResponse**](ApiGetApplicationResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_http_integration**
> ApiGetHTTPIntegrationResponse get_http_integration(application_id)

GetHTTPIntegration returns the HTTP application-integration.

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
api_instance = swagger_client.ApplicationServiceApi(swagger_client.ApiClient(configuration))
application_id = 'application_id_example' # str | Application ID.

try:
    # GetHTTPIntegration returns the HTTP application-integration.
    api_response = api_instance.get_http_integration(application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->get_http_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID. | 

### Return type

[**ApiGetHTTPIntegrationResponse**](ApiGetHTTPIntegrationResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_influx_db_integration**
> ApiGetInfluxDBIntegrationResponse get_influx_db_integration(application_id)

GetInfluxDBIntegration returns the InfluxDB application-integration.

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
api_instance = swagger_client.ApplicationServiceApi(swagger_client.ApiClient(configuration))
application_id = 'application_id_example' # str | Application ID.

try:
    # GetInfluxDBIntegration returns the InfluxDB application-integration.
    api_response = api_instance.get_influx_db_integration(application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->get_influx_db_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID. | 

### Return type

[**ApiGetInfluxDBIntegrationResponse**](ApiGetInfluxDBIntegrationResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_things_board_integration**
> ApiGetThingsBoardIntegrationResponse get_things_board_integration(application_id)

GetThingsBoardIntegration returns the ThingsBoard application-integration.

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
api_instance = swagger_client.ApplicationServiceApi(swagger_client.ApiClient(configuration))
application_id = 'application_id_example' # str | Application ID.

try:
    # GetThingsBoardIntegration returns the ThingsBoard application-integration.
    api_response = api_instance.get_things_board_integration(application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->get_things_board_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID. | 

### Return type

[**ApiGetThingsBoardIntegrationResponse**](ApiGetThingsBoardIntegrationResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> ApiListApplicationResponse list(limit=limit, offset=offset, organization_id=organization_id, search=search)

List lists the available applications.

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
api_instance = swagger_client.ApplicationServiceApi(swagger_client.ApiClient(configuration))
limit = 'limit_example' # str | Max number of applications to return in the result-test. (optional)
offset = 'offset_example' # str | Offset in the result-set (for pagination). (optional)
organization_id = 'organization_id_example' # str | ID of the organization to filter on. (optional)
search = 'search_example' # str | Search on name (optional). (optional)

try:
    # List lists the available applications.
    api_response = api_instance.list(limit=limit, offset=offset, organization_id=organization_id, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| Max number of applications to return in the result-test. | [optional] 
 **offset** | **str**| Offset in the result-set (for pagination). | [optional] 
 **organization_id** | **str**| ID of the organization to filter on. | [optional] 
 **search** | **str**| Search on name (optional). | [optional] 

### Return type

[**ApiListApplicationResponse**](ApiListApplicationResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_integrations**
> ApiListIntegrationResponse list_integrations(application_id)

ListIntegrations lists all configured integrations.

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
api_instance = swagger_client.ApplicationServiceApi(swagger_client.ApiClient(configuration))
application_id = 'application_id_example' # str | The id of the application.

try:
    # ListIntegrations lists all configured integrations.
    api_response = api_instance.list_integrations(application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->list_integrations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| The id of the application. | 

### Return type

[**ApiListIntegrationResponse**](ApiListIntegrationResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> object update(application_id, body)

Update updates the given application.

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
api_instance = swagger_client.ApplicationServiceApi(swagger_client.ApiClient(configuration))
application_id = 'application_id_example' # str | Application ID. This will be automatically assigned on create.
body = swagger_client.ApiUpdateApplicationRequest() # ApiUpdateApplicationRequest | 

try:
    # Update updates the given application.
    api_response = api_instance.update(application_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID. This will be automatically assigned on create. | 
 **body** | [**ApiUpdateApplicationRequest**](ApiUpdateApplicationRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_http_integration**
> object update_http_integration(integration_application_id, body)

UpdateHTTPIntegration updates the HTTP application-integration.

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
api_instance = swagger_client.ApplicationServiceApi(swagger_client.ApiClient(configuration))
integration_application_id = 'integration_application_id_example' # str | The id of the application.
body = swagger_client.ApiUpdateHTTPIntegrationRequest() # ApiUpdateHTTPIntegrationRequest | 

try:
    # UpdateHTTPIntegration updates the HTTP application-integration.
    api_response = api_instance.update_http_integration(integration_application_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->update_http_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_application_id** | **str**| The id of the application. | 
 **body** | [**ApiUpdateHTTPIntegrationRequest**](ApiUpdateHTTPIntegrationRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_influx_db_integration**
> object update_influx_db_integration(integration_application_id, body)

UpdateInfluxDBIntegration updates the InfluxDB application-integration.

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
api_instance = swagger_client.ApplicationServiceApi(swagger_client.ApiClient(configuration))
integration_application_id = 'integration_application_id_example' # str | Application ID.
body = swagger_client.ApiUpdateInfluxDBIntegrationRequest() # ApiUpdateInfluxDBIntegrationRequest | 

try:
    # UpdateInfluxDBIntegration updates the InfluxDB application-integration.
    api_response = api_instance.update_influx_db_integration(integration_application_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->update_influx_db_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_application_id** | **str**| Application ID. | 
 **body** | [**ApiUpdateInfluxDBIntegrationRequest**](ApiUpdateInfluxDBIntegrationRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_things_board_integration**
> object update_things_board_integration(integration_application_id, body)

UpdateThingsBoardIntegration updates the ThingsBoard application-integration.

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
api_instance = swagger_client.ApplicationServiceApi(swagger_client.ApiClient(configuration))
integration_application_id = 'integration_application_id_example' # str | Application ID.
body = swagger_client.ApiUpdateThingsBoardIntegrationRequest() # ApiUpdateThingsBoardIntegrationRequest | 

try:
    # UpdateThingsBoardIntegration updates the ThingsBoard application-integration.
    api_response = api_instance.update_things_board_integration(integration_application_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationServiceApi->update_things_board_integration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_application_id** | **str**| Application ID. | 
 **body** | [**ApiUpdateThingsBoardIntegrationRequest**](ApiUpdateThingsBoardIntegrationRequest.md)|  | 

### Return type

**object**

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

