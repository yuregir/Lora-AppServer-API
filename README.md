## Metacore Lora Server API client

 For more information about the usage of the LoRa App Server (REST) API, see [https://docs.loraserver.io/lora-app-server/api/](https://docs.loraserver.io/lora-app-server/api/). 

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 or 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/yuregir/Lora-AppServer-API.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/yuregir/Lora-AppServer-API.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *http://api.teke.li:9090*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApplicationServiceApi* | [**create**](docs/ApplicationServiceApi.md#create) | **POST** /api/applications | Create creates the given application.
*ApplicationServiceApi* | [**create_http_integration**](docs/ApplicationServiceApi.md#create_http_integration) | **POST** /api/applications/{integration.application_id}/integrations/http | CreateHTTPIntegration creates a HTTP application-integration.
*ApplicationServiceApi* | [**create_influx_db_integration**](docs/ApplicationServiceApi.md#create_influx_db_integration) | **POST** /api/applications/{integration.application_id}/integrations/influxdb | CreateInfluxDBIntegration create an InfluxDB application-integration.
*ApplicationServiceApi* | [**create_things_board_integration**](docs/ApplicationServiceApi.md#create_things_board_integration) | **POST** /api/applications/{integration.application_id}/integrations/thingsboard | CreateThingsBoardIntegration creates a ThingsBoard application-integration.
*ApplicationServiceApi* | [**delete**](docs/ApplicationServiceApi.md#delete) | **DELETE** /api/applications/{id} | Delete deletes the given application.
*ApplicationServiceApi* | [**delete_http_integration**](docs/ApplicationServiceApi.md#delete_http_integration) | **DELETE** /api/applications/{application_id}/integrations/http | DeleteIntegration deletes the HTTP application-integration.
*ApplicationServiceApi* | [**delete_influx_db_integration**](docs/ApplicationServiceApi.md#delete_influx_db_integration) | **DELETE** /api/applications/{application_id}/integrations/influxdb | DeleteInfluxDBIntegration deletes the InfluxDB application-integration.
*ApplicationServiceApi* | [**delete_things_board_integration**](docs/ApplicationServiceApi.md#delete_things_board_integration) | **DELETE** /api/applications/{application_id}/integrations/thingsboard | DeleteThingsBoardIntegration deletes the ThingsBoard application-integration.
*ApplicationServiceApi* | [**get**](docs/ApplicationServiceApi.md#get) | **GET** /api/applications/{id} | Get returns the requested application.
*ApplicationServiceApi* | [**get_http_integration**](docs/ApplicationServiceApi.md#get_http_integration) | **GET** /api/applications/{application_id}/integrations/http | GetHTTPIntegration returns the HTTP application-integration.
*ApplicationServiceApi* | [**get_influx_db_integration**](docs/ApplicationServiceApi.md#get_influx_db_integration) | **GET** /api/applications/{application_id}/integrations/influxdb | GetInfluxDBIntegration returns the InfluxDB application-integration.
*ApplicationServiceApi* | [**get_things_board_integration**](docs/ApplicationServiceApi.md#get_things_board_integration) | **GET** /api/applications/{application_id}/integrations/thingsboard | GetThingsBoardIntegration returns the ThingsBoard application-integration.
*ApplicationServiceApi* | [**list**](docs/ApplicationServiceApi.md#list) | **GET** /api/applications | List lists the available applications.
*ApplicationServiceApi* | [**list_integrations**](docs/ApplicationServiceApi.md#list_integrations) | **GET** /api/applications/{application_id}/integrations | ListIntegrations lists all configured integrations.
*ApplicationServiceApi* | [**update**](docs/ApplicationServiceApi.md#update) | **PUT** /api/applications/{application.id} | Update updates the given application.
*ApplicationServiceApi* | [**update_http_integration**](docs/ApplicationServiceApi.md#update_http_integration) | **PUT** /api/applications/{integration.application_id}/integrations/http | UpdateHTTPIntegration updates the HTTP application-integration.
*ApplicationServiceApi* | [**update_influx_db_integration**](docs/ApplicationServiceApi.md#update_influx_db_integration) | **PUT** /api/applications/{integration.application_id}/integrations/influxdb | UpdateInfluxDBIntegration updates the InfluxDB application-integration.
*ApplicationServiceApi* | [**update_things_board_integration**](docs/ApplicationServiceApi.md#update_things_board_integration) | **PUT** /api/applications/{integration.application_id}/integrations/thingsboard | UpdateThingsBoardIntegration updates the ThingsBoard application-integration.
*DeviceProfileServiceApi* | [**create**](docs/DeviceProfileServiceApi.md#create) | **POST** /api/device-profiles | Create creates the given device-profile.
*DeviceProfileServiceApi* | [**delete**](docs/DeviceProfileServiceApi.md#delete) | **DELETE** /api/device-profiles/{id} | Delete deletes the device-profile matching the given id.
*DeviceProfileServiceApi* | [**get**](docs/DeviceProfileServiceApi.md#get) | **GET** /api/device-profiles/{id} | Get returns the device-profile matching the given id.
*DeviceProfileServiceApi* | [**list**](docs/DeviceProfileServiceApi.md#list) | **GET** /api/device-profiles | List lists the available device-profiles.
*DeviceProfileServiceApi* | [**update**](docs/DeviceProfileServiceApi.md#update) | **PUT** /api/device-profiles/{device_profile.id} | Update updates the given device-profile.
*DeviceQueueServiceApi* | [**enqueue**](docs/DeviceQueueServiceApi.md#enqueue) | **POST** /api/devices/{device_queue_item.dev_eui}/queue | Enqueue adds the given item to the device-queue.
*DeviceQueueServiceApi* | [**flush**](docs/DeviceQueueServiceApi.md#flush) | **DELETE** /api/devices/{dev_eui}/queue | Flush flushes the downlink device-queue.
*DeviceQueueServiceApi* | [**list**](docs/DeviceQueueServiceApi.md#list) | **GET** /api/devices/{dev_eui}/queue | List lists the items in the device-queue.
*DeviceServiceApi* | [**activate**](docs/DeviceServiceApi.md#activate) | **POST** /api/devices/{device_activation.dev_eui}/activate | Activate (re)activates the device (only when ABP is set to true).
*DeviceServiceApi* | [**create**](docs/DeviceServiceApi.md#create) | **POST** /api/devices | Create creates the given device.
*DeviceServiceApi* | [**create_keys**](docs/DeviceServiceApi.md#create_keys) | **POST** /api/devices/{device_keys.dev_eui}/keys | CreateKeys creates the given device-keys.
*DeviceServiceApi* | [**deactivate**](docs/DeviceServiceApi.md#deactivate) | **DELETE** /api/devices/{dev_eui}/activation | Deactivate de-activates the device.
*DeviceServiceApi* | [**delete**](docs/DeviceServiceApi.md#delete) | **DELETE** /api/devices/{dev_eui} | Delete deletes the device matching the given DevEUI.
*DeviceServiceApi* | [**delete_keys**](docs/DeviceServiceApi.md#delete_keys) | **DELETE** /api/devices/{dev_eui}/keys | DeleteKeys deletes the device-keys for the given DevEUI.
*DeviceServiceApi* | [**get**](docs/DeviceServiceApi.md#get) | **GET** /api/devices/{dev_eui} | Get returns the device matching the given DevEUI.
*DeviceServiceApi* | [**get_activation**](docs/DeviceServiceApi.md#get_activation) | **GET** /api/devices/{dev_eui}/activation | GetActivation returns the current activation details of the device (OTAA and ABP).
*DeviceServiceApi* | [**get_keys**](docs/DeviceServiceApi.md#get_keys) | **GET** /api/devices/{dev_eui}/keys | GetKeys returns the device-keys for the given DevEUI.
*DeviceServiceApi* | [**get_random_dev_addr**](docs/DeviceServiceApi.md#get_random_dev_addr) | **POST** /api/devices/{dev_eui}/getRandomDevAddr | GetRandomDevAddr returns a random DevAddr taking the NwkID prefix into account.
*DeviceServiceApi* | [**list**](docs/DeviceServiceApi.md#list) | **GET** /api/devices | List returns the available devices.
*DeviceServiceApi* | [**stream_event_logs**](docs/DeviceServiceApi.md#stream_event_logs) | **GET** /api/devices/{dev_eui}/events | StreamEventLogs stream the device events (uplink payloads, ACKs, joins, errors).   * This endpoint is intended for debugging only.   * This endpoint does not work from a web-browser.
*DeviceServiceApi* | [**stream_frame_logs**](docs/DeviceServiceApi.md#stream_frame_logs) | **GET** /api/devices/{dev_eui}/frames | StreamFrameLogs streams the uplink and downlink frame-logs for the given DevEUI.   * These are the raw LoRaWAN frames and this endpoint is intended for debugging only.   * This endpoint does not work from a web-browser.
*DeviceServiceApi* | [**update**](docs/DeviceServiceApi.md#update) | **PUT** /api/devices/{device.dev_eui} | Update updates the device matching the given DevEUI.
*DeviceServiceApi* | [**update_keys**](docs/DeviceServiceApi.md#update_keys) | **PUT** /api/devices/{device_keys.dev_eui}/keys | UpdateKeys updates the device-keys.
*FUOTADeploymentServiceApi* | [**create_for_device**](docs/FUOTADeploymentServiceApi.md#create_for_device) | **POST** /api/devices/{dev_eui}/fuota-deployments | CreateForDevice creates a deployment for the given DevEUI.
*FUOTADeploymentServiceApi* | [**get**](docs/FUOTADeploymentServiceApi.md#get) | **GET** /api/fuota-deployments/{id} | Get returns the fuota deployment for the given id.
*FUOTADeploymentServiceApi* | [**get_deployment_device**](docs/FUOTADeploymentServiceApi.md#get_deployment_device) | **GET** /api/fuota-deployments/{fuota_deployment_id}/devices/{dev_eui} | GetDeploymentDevice returns the deployment device.
*FUOTADeploymentServiceApi* | [**list**](docs/FUOTADeploymentServiceApi.md#list) | **GET** /api/fuota-deployments | List lists the fuota deployments.
*FUOTADeploymentServiceApi* | [**list_deployment_devices**](docs/FUOTADeploymentServiceApi.md#list_deployment_devices) | **GET** /api/fuota-deployments/{fuota_deployment_id}/devices | ListDeploymentDevices lists the devices (and status) for the given fuota deployment ID.
*GatewayProfileServiceApi* | [**create**](docs/GatewayProfileServiceApi.md#create) | **POST** /api/gateway-profiles | Create creates the given gateway-profile.
*GatewayProfileServiceApi* | [**delete**](docs/GatewayProfileServiceApi.md#delete) | **DELETE** /api/gateway-profiles/{id} | Delete deletes the gateway-profile matching the given id.
*GatewayProfileServiceApi* | [**get**](docs/GatewayProfileServiceApi.md#get) | **GET** /api/gateway-profiles/{id} | Get returns the gateway-profile matching the given id.
*GatewayProfileServiceApi* | [**list**](docs/GatewayProfileServiceApi.md#list) | **GET** /api/gateway-profiles | List returns the existing gateway-profiles.
*GatewayProfileServiceApi* | [**update**](docs/GatewayProfileServiceApi.md#update) | **PUT** /api/gateway-profiles/{gateway_profile.id} | Update updates the given gateway-profile.
*GatewayServiceApi* | [**create**](docs/GatewayServiceApi.md#create) | **POST** /api/gateways | Create creates the given gateway.
*GatewayServiceApi* | [**delete**](docs/GatewayServiceApi.md#delete) | **DELETE** /api/gateways/{id} | Delete deletes the gateway matching the given mac address.
*GatewayServiceApi* | [**get**](docs/GatewayServiceApi.md#get) | **GET** /api/gateways/{id} | Get returns the gateway for the requested mac address.
*GatewayServiceApi* | [**get_last_ping**](docs/GatewayServiceApi.md#get_last_ping) | **GET** /api/gateways/{gateway_id}/pings/last | GetLastPing returns the last emitted ping and gateways receiving this ping.
*GatewayServiceApi* | [**get_stats**](docs/GatewayServiceApi.md#get_stats) | **GET** /api/gateways/{gateway_id}/stats | GetStats lists the gateway stats given the query parameters.
*GatewayServiceApi* | [**list**](docs/GatewayServiceApi.md#list) | **GET** /api/gateways | List lists the gateways.
*GatewayServiceApi* | [**stream_frame_logs**](docs/GatewayServiceApi.md#stream_frame_logs) | **GET** /api/gateways/{gateway_id}/frames | StreamFrameLogs streams the uplink and downlink frame-logs for the given gateway ID. Notes:   * These are the raw LoRaWAN frames and this endpoint is intended for debugging only.   * This endpoint does not work from a web-browser.
*GatewayServiceApi* | [**update**](docs/GatewayServiceApi.md#update) | **PUT** /api/gateways/{gateway.id} | Update updates the gateway matching the given mac address.
*InternalServiceApi* | [**branding**](docs/InternalServiceApi.md#branding) | **GET** /api/internal/branding | Get the branding for the UI
*InternalServiceApi* | [**global_search**](docs/InternalServiceApi.md#global_search) | **GET** /api/internal/search | Perform a global search.
*InternalServiceApi* | [**login**](docs/InternalServiceApi.md#login) | **POST** /api/internal/login | Log in a user
*InternalServiceApi* | [**profile**](docs/InternalServiceApi.md#profile) | **GET** /api/internal/profile | Get the current user&#39;s profile
*MulticastGroupServiceApi* | [**add_device**](docs/MulticastGroupServiceApi.md#add_device) | **POST** /api/multicast-groups/{multicast_group_id}/devices | AddDevice adds the given device to the multicast-group.
*MulticastGroupServiceApi* | [**create**](docs/MulticastGroupServiceApi.md#create) | **POST** /api/multicast-groups | Create creates the given multicast-group.
*MulticastGroupServiceApi* | [**delete**](docs/MulticastGroupServiceApi.md#delete) | **DELETE** /api/multicast-groups/{id} | Delete deletes a multicast-group given an ID.
*MulticastGroupServiceApi* | [**enqueue**](docs/MulticastGroupServiceApi.md#enqueue) | **POST** /api/multicast-groups/{multicast_queue_item.multicast_group_id}/queue | Enqueue adds the given item to the multicast-queue.
*MulticastGroupServiceApi* | [**flush_queue**](docs/MulticastGroupServiceApi.md#flush_queue) | **DELETE** /api/multicast-groups/{multicast_group_id}/queue | FlushQueue flushes the multicast-group queue.
*MulticastGroupServiceApi* | [**get**](docs/MulticastGroupServiceApi.md#get) | **GET** /api/multicast-groups/{id} | Get returns a multicast-group given an ID.
*MulticastGroupServiceApi* | [**list**](docs/MulticastGroupServiceApi.md#list) | **GET** /api/multicast-groups | List lists the available multicast-groups.
*MulticastGroupServiceApi* | [**list_queue**](docs/MulticastGroupServiceApi.md#list_queue) | **GET** /api/multicast-groups/{multicast_group_id}/queue | ListQueue lists the items in the multicast-group queue.
*MulticastGroupServiceApi* | [**remove_device**](docs/MulticastGroupServiceApi.md#remove_device) | **DELETE** /api/multicast-groups/{multicast_group_id}/devices/{dev_eui} | RemoveDevice removes the given device from the multicast-group.
*MulticastGroupServiceApi* | [**update**](docs/MulticastGroupServiceApi.md#update) | **PUT** /api/multicast-groups/{multicast_group.id} | Update updates the given multicast-group.
*NetworkServerServiceApi* | [**create**](docs/NetworkServerServiceApi.md#create) | **POST** /api/network-servers | Create creates the given network-server.
*NetworkServerServiceApi* | [**delete**](docs/NetworkServerServiceApi.md#delete) | **DELETE** /api/network-servers/{id} | Delete deletes the network-server matching the given id.
*NetworkServerServiceApi* | [**get**](docs/NetworkServerServiceApi.md#get) | **GET** /api/network-servers/{id} | Get returns the network-server matching the given id.
*NetworkServerServiceApi* | [**list**](docs/NetworkServerServiceApi.md#list) | **GET** /api/network-servers | List lists the available network-servers.
*NetworkServerServiceApi* | [**update**](docs/NetworkServerServiceApi.md#update) | **PUT** /api/network-servers/{network_server.id} | Update updates the given network-server.
*OrganizationServiceApi* | [**add_user**](docs/OrganizationServiceApi.md#add_user) | **POST** /api/organizations/{organization_user.organization_id}/users | Add a new user to an organization.
*OrganizationServiceApi* | [**create**](docs/OrganizationServiceApi.md#create) | **POST** /api/organizations | Create a new organization.
*OrganizationServiceApi* | [**delete**](docs/OrganizationServiceApi.md#delete) | **DELETE** /api/organizations/{id} | Delete an organization.
*OrganizationServiceApi* | [**delete_user**](docs/OrganizationServiceApi.md#delete_user) | **DELETE** /api/organizations/{organization_id}/users/{user_id} | Delete a user from an organization.
*OrganizationServiceApi* | [**get**](docs/OrganizationServiceApi.md#get) | **GET** /api/organizations/{id} | Get data for a particular organization.
*OrganizationServiceApi* | [**get_user**](docs/OrganizationServiceApi.md#get_user) | **GET** /api/organizations/{organization_id}/users/{user_id} | Get data for a particular organization user.
*OrganizationServiceApi* | [**list**](docs/OrganizationServiceApi.md#list) | **GET** /api/organizations | Get organization list.
*OrganizationServiceApi* | [**list_users**](docs/OrganizationServiceApi.md#list_users) | **GET** /api/organizations/{organization_id}/users | Get organization&#39;s user list.
*OrganizationServiceApi* | [**update**](docs/OrganizationServiceApi.md#update) | **PUT** /api/organizations/{organization.id} | Update an existing organization.
*OrganizationServiceApi* | [**update_user**](docs/OrganizationServiceApi.md#update_user) | **PUT** /api/organizations/{organization_user.organization_id}/users/{organization_user.user_id} | Update a user in an organization.
*ServiceProfileServiceApi* | [**create**](docs/ServiceProfileServiceApi.md#create) | **POST** /api/service-profiles | Create creates the given service-profile.
*ServiceProfileServiceApi* | [**delete**](docs/ServiceProfileServiceApi.md#delete) | **DELETE** /api/service-profiles/{id} | Delete deletes the service-profile matching the given id.
*ServiceProfileServiceApi* | [**get**](docs/ServiceProfileServiceApi.md#get) | **GET** /api/service-profiles/{id} | Get returns the service-profile matching the given id.
*ServiceProfileServiceApi* | [**list**](docs/ServiceProfileServiceApi.md#list) | **GET** /api/service-profiles | List lists the available service-profiles.
*ServiceProfileServiceApi* | [**update**](docs/ServiceProfileServiceApi.md#update) | **PUT** /api/service-profiles/{service_profile.id} | Update updates the given serviceprofile.
*UserServiceApi* | [**create**](docs/UserServiceApi.md#create) | **POST** /api/users | Create a new user.
*UserServiceApi* | [**delete**](docs/UserServiceApi.md#delete) | **DELETE** /api/users/{id} | Delete a user.
*UserServiceApi* | [**get**](docs/UserServiceApi.md#get) | **GET** /api/users/{id} | Get data for a particular user.
*UserServiceApi* | [**list**](docs/UserServiceApi.md#list) | **GET** /api/users | Get user list.
*UserServiceApi* | [**update**](docs/UserServiceApi.md#update) | **PUT** /api/users/{user.id} | Update an existing user.
*UserServiceApi* | [**update_password**](docs/UserServiceApi.md#update_password) | **PUT** /api/users/{user_id}/password | UpdatePassword updates a password.


## Documentation For Models

 - [ApiActivateDeviceRequest](docs/ApiActivateDeviceRequest.md)
 - [ApiAddDeviceToMulticastGroupRequest](docs/ApiAddDeviceToMulticastGroupRequest.md)
 - [ApiAddOrganizationUserRequest](docs/ApiAddOrganizationUserRequest.md)
 - [ApiApplication](docs/ApiApplication.md)
 - [ApiApplicationListItem](docs/ApiApplicationListItem.md)
 - [ApiBrandingResponse](docs/ApiBrandingResponse.md)
 - [ApiCreateApplicationRequest](docs/ApiCreateApplicationRequest.md)
 - [ApiCreateApplicationResponse](docs/ApiCreateApplicationResponse.md)
 - [ApiCreateDeviceKeysRequest](docs/ApiCreateDeviceKeysRequest.md)
 - [ApiCreateDeviceProfileRequest](docs/ApiCreateDeviceProfileRequest.md)
 - [ApiCreateDeviceProfileResponse](docs/ApiCreateDeviceProfileResponse.md)
 - [ApiCreateDeviceRequest](docs/ApiCreateDeviceRequest.md)
 - [ApiCreateFUOTADeploymentForDeviceRequest](docs/ApiCreateFUOTADeploymentForDeviceRequest.md)
 - [ApiCreateFUOTADeploymentForDeviceResponse](docs/ApiCreateFUOTADeploymentForDeviceResponse.md)
 - [ApiCreateGatewayProfileRequest](docs/ApiCreateGatewayProfileRequest.md)
 - [ApiCreateGatewayProfileResponse](docs/ApiCreateGatewayProfileResponse.md)
 - [ApiCreateGatewayRequest](docs/ApiCreateGatewayRequest.md)
 - [ApiCreateHTTPIntegrationRequest](docs/ApiCreateHTTPIntegrationRequest.md)
 - [ApiCreateInfluxDBIntegrationRequest](docs/ApiCreateInfluxDBIntegrationRequest.md)
 - [ApiCreateMulticastGroupRequest](docs/ApiCreateMulticastGroupRequest.md)
 - [ApiCreateMulticastGroupResponse](docs/ApiCreateMulticastGroupResponse.md)
 - [ApiCreateNetworkServerRequest](docs/ApiCreateNetworkServerRequest.md)
 - [ApiCreateNetworkServerResponse](docs/ApiCreateNetworkServerResponse.md)
 - [ApiCreateOrganizationRequest](docs/ApiCreateOrganizationRequest.md)
 - [ApiCreateOrganizationResponse](docs/ApiCreateOrganizationResponse.md)
 - [ApiCreateServiceProfileRequest](docs/ApiCreateServiceProfileRequest.md)
 - [ApiCreateServiceProfileResponse](docs/ApiCreateServiceProfileResponse.md)
 - [ApiCreateThingsBoardIntegrationRequest](docs/ApiCreateThingsBoardIntegrationRequest.md)
 - [ApiCreateUserRequest](docs/ApiCreateUserRequest.md)
 - [ApiCreateUserResponse](docs/ApiCreateUserResponse.md)
 - [ApiDevice](docs/ApiDevice.md)
 - [ApiDeviceActivation](docs/ApiDeviceActivation.md)
 - [ApiDeviceKeys](docs/ApiDeviceKeys.md)
 - [ApiDeviceListItem](docs/ApiDeviceListItem.md)
 - [ApiDeviceProfile](docs/ApiDeviceProfile.md)
 - [ApiDeviceProfileListItem](docs/ApiDeviceProfileListItem.md)
 - [ApiDeviceQueueItem](docs/ApiDeviceQueueItem.md)
 - [ApiDownlinkFrameLog](docs/ApiDownlinkFrameLog.md)
 - [ApiDownlinkTXInfo](docs/ApiDownlinkTXInfo.md)
 - [ApiEncryptedFineTimestamp](docs/ApiEncryptedFineTimestamp.md)
 - [ApiEnqueueDeviceQueueItemRequest](docs/ApiEnqueueDeviceQueueItemRequest.md)
 - [ApiEnqueueDeviceQueueItemResponse](docs/ApiEnqueueDeviceQueueItemResponse.md)
 - [ApiEnqueueMulticastQueueItemRequest](docs/ApiEnqueueMulticastQueueItemRequest.md)
 - [ApiEnqueueMulticastQueueItemResponse](docs/ApiEnqueueMulticastQueueItemResponse.md)
 - [ApiFUOTADeployment](docs/ApiFUOTADeployment.md)
 - [ApiFUOTADeploymentDeviceListItem](docs/ApiFUOTADeploymentDeviceListItem.md)
 - [ApiFUOTADeploymentDeviceState](docs/ApiFUOTADeploymentDeviceState.md)
 - [ApiFUOTADeploymentListItem](docs/ApiFUOTADeploymentListItem.md)
 - [ApiGateway](docs/ApiGateway.md)
 - [ApiGatewayBoard](docs/ApiGatewayBoard.md)
 - [ApiGatewayListItem](docs/ApiGatewayListItem.md)
 - [ApiGatewayProfile](docs/ApiGatewayProfile.md)
 - [ApiGatewayProfileExtraChannel](docs/ApiGatewayProfileExtraChannel.md)
 - [ApiGatewayProfileListItem](docs/ApiGatewayProfileListItem.md)
 - [ApiGatewayStats](docs/ApiGatewayStats.md)
 - [ApiGetApplicationResponse](docs/ApiGetApplicationResponse.md)
 - [ApiGetDeviceActivationResponse](docs/ApiGetDeviceActivationResponse.md)
 - [ApiGetDeviceKeysResponse](docs/ApiGetDeviceKeysResponse.md)
 - [ApiGetDeviceProfileResponse](docs/ApiGetDeviceProfileResponse.md)
 - [ApiGetDeviceResponse](docs/ApiGetDeviceResponse.md)
 - [ApiGetFUOTADeploymentDeviceResponse](docs/ApiGetFUOTADeploymentDeviceResponse.md)
 - [ApiGetFUOTADeploymentResponse](docs/ApiGetFUOTADeploymentResponse.md)
 - [ApiGetGatewayProfileResponse](docs/ApiGetGatewayProfileResponse.md)
 - [ApiGetGatewayResponse](docs/ApiGetGatewayResponse.md)
 - [ApiGetGatewayStatsResponse](docs/ApiGetGatewayStatsResponse.md)
 - [ApiGetHTTPIntegrationResponse](docs/ApiGetHTTPIntegrationResponse.md)
 - [ApiGetInfluxDBIntegrationResponse](docs/ApiGetInfluxDBIntegrationResponse.md)
 - [ApiGetLastPingResponse](docs/ApiGetLastPingResponse.md)
 - [ApiGetMulticastGroupResponse](docs/ApiGetMulticastGroupResponse.md)
 - [ApiGetNetworkServerResponse](docs/ApiGetNetworkServerResponse.md)
 - [ApiGetOrganizationResponse](docs/ApiGetOrganizationResponse.md)
 - [ApiGetOrganizationUserResponse](docs/ApiGetOrganizationUserResponse.md)
 - [ApiGetRandomDevAddrResponse](docs/ApiGetRandomDevAddrResponse.md)
 - [ApiGetServiceProfileResponse](docs/ApiGetServiceProfileResponse.md)
 - [ApiGetThingsBoardIntegrationResponse](docs/ApiGetThingsBoardIntegrationResponse.md)
 - [ApiGetUserResponse](docs/ApiGetUserResponse.md)
 - [ApiGlobalSearchResponse](docs/ApiGlobalSearchResponse.md)
 - [ApiGlobalSearchResult](docs/ApiGlobalSearchResult.md)
 - [ApiHTTPIntegration](docs/ApiHTTPIntegration.md)
 - [ApiHTTPIntegrationHeader](docs/ApiHTTPIntegrationHeader.md)
 - [ApiInfluxDBIntegration](docs/ApiInfluxDBIntegration.md)
 - [ApiInfluxDBPrecision](docs/ApiInfluxDBPrecision.md)
 - [ApiIntegrationKind](docs/ApiIntegrationKind.md)
 - [ApiIntegrationListItem](docs/ApiIntegrationListItem.md)
 - [ApiListApplicationResponse](docs/ApiListApplicationResponse.md)
 - [ApiListDeviceProfileResponse](docs/ApiListDeviceProfileResponse.md)
 - [ApiListDeviceQueueItemsResponse](docs/ApiListDeviceQueueItemsResponse.md)
 - [ApiListDeviceResponse](docs/ApiListDeviceResponse.md)
 - [ApiListFUOTADeploymentDevicesResponse](docs/ApiListFUOTADeploymentDevicesResponse.md)
 - [ApiListFUOTADeploymentResponse](docs/ApiListFUOTADeploymentResponse.md)
 - [ApiListGatewayProfilesResponse](docs/ApiListGatewayProfilesResponse.md)
 - [ApiListGatewayResponse](docs/ApiListGatewayResponse.md)
 - [ApiListIntegrationResponse](docs/ApiListIntegrationResponse.md)
 - [ApiListMulticastGroupQueueItemsResponse](docs/ApiListMulticastGroupQueueItemsResponse.md)
 - [ApiListMulticastGroupResponse](docs/ApiListMulticastGroupResponse.md)
 - [ApiListNetworkServerResponse](docs/ApiListNetworkServerResponse.md)
 - [ApiListOrganizationResponse](docs/ApiListOrganizationResponse.md)
 - [ApiListOrganizationUsersResponse](docs/ApiListOrganizationUsersResponse.md)
 - [ApiListServiceProfileResponse](docs/ApiListServiceProfileResponse.md)
 - [ApiListUserResponse](docs/ApiListUserResponse.md)
 - [ApiLoginRequest](docs/ApiLoginRequest.md)
 - [ApiLoginResponse](docs/ApiLoginResponse.md)
 - [ApiMulticastGroup](docs/ApiMulticastGroup.md)
 - [ApiMulticastGroupListItem](docs/ApiMulticastGroupListItem.md)
 - [ApiMulticastGroupType](docs/ApiMulticastGroupType.md)
 - [ApiMulticastQueueItem](docs/ApiMulticastQueueItem.md)
 - [ApiNetworkServer](docs/ApiNetworkServer.md)
 - [ApiNetworkServerListItem](docs/ApiNetworkServerListItem.md)
 - [ApiOrganization](docs/ApiOrganization.md)
 - [ApiOrganizationLink](docs/ApiOrganizationLink.md)
 - [ApiOrganizationListItem](docs/ApiOrganizationListItem.md)
 - [ApiOrganizationUser](docs/ApiOrganizationUser.md)
 - [ApiOrganizationUserListItem](docs/ApiOrganizationUserListItem.md)
 - [ApiPingRX](docs/ApiPingRX.md)
 - [ApiProfileResponse](docs/ApiProfileResponse.md)
 - [ApiProfileSettings](docs/ApiProfileSettings.md)
 - [ApiRatePolicy](docs/ApiRatePolicy.md)
 - [ApiServiceProfile](docs/ApiServiceProfile.md)
 - [ApiServiceProfileListItem](docs/ApiServiceProfileListItem.md)
 - [ApiStreamDeviceEventLogsResponse](docs/ApiStreamDeviceEventLogsResponse.md)
 - [ApiStreamDeviceFrameLogsResponse](docs/ApiStreamDeviceFrameLogsResponse.md)
 - [ApiStreamGatewayFrameLogsResponse](docs/ApiStreamGatewayFrameLogsResponse.md)
 - [ApiThingsBoardIntegration](docs/ApiThingsBoardIntegration.md)
 - [ApiUpdateApplicationRequest](docs/ApiUpdateApplicationRequest.md)
 - [ApiUpdateDeviceKeysRequest](docs/ApiUpdateDeviceKeysRequest.md)
 - [ApiUpdateDeviceProfileRequest](docs/ApiUpdateDeviceProfileRequest.md)
 - [ApiUpdateDeviceRequest](docs/ApiUpdateDeviceRequest.md)
 - [ApiUpdateGatewayProfileRequest](docs/ApiUpdateGatewayProfileRequest.md)
 - [ApiUpdateGatewayRequest](docs/ApiUpdateGatewayRequest.md)
 - [ApiUpdateHTTPIntegrationRequest](docs/ApiUpdateHTTPIntegrationRequest.md)
 - [ApiUpdateInfluxDBIntegrationRequest](docs/ApiUpdateInfluxDBIntegrationRequest.md)
 - [ApiUpdateMulticastGroupRequest](docs/ApiUpdateMulticastGroupRequest.md)
 - [ApiUpdateNetworkServerRequest](docs/ApiUpdateNetworkServerRequest.md)
 - [ApiUpdateOrganizationRequest](docs/ApiUpdateOrganizationRequest.md)
 - [ApiUpdateOrganizationUserRequest](docs/ApiUpdateOrganizationUserRequest.md)
 - [ApiUpdateServiceProfileRequest](docs/ApiUpdateServiceProfileRequest.md)
 - [ApiUpdateThingsBoardIntegrationRequest](docs/ApiUpdateThingsBoardIntegrationRequest.md)
 - [ApiUpdateUserPasswordRequest](docs/ApiUpdateUserPasswordRequest.md)
 - [ApiUpdateUserRequest](docs/ApiUpdateUserRequest.md)
 - [ApiUplinkFrameLog](docs/ApiUplinkFrameLog.md)
 - [ApiUplinkRXInfo](docs/ApiUplinkRXInfo.md)
 - [ApiUser](docs/ApiUser.md)
 - [ApiUserListItem](docs/ApiUserListItem.md)
 - [ApiUserOrganization](docs/ApiUserOrganization.md)
 - [CommonLocation](docs/CommonLocation.md)
 - [CommonLocationSource](docs/CommonLocationSource.md)
 - [CommonModulation](docs/CommonModulation.md)
 - [GwDelayTimingInfo](docs/GwDelayTimingInfo.md)
 - [GwDownlinkTiming](docs/GwDownlinkTiming.md)
 - [GwFSKModulationInfo](docs/GwFSKModulationInfo.md)
 - [GwFineTimestampType](docs/GwFineTimestampType.md)
 - [GwGPSEpochTimingInfo](docs/GwGPSEpochTimingInfo.md)
 - [GwImmediatelyTimingInfo](docs/GwImmediatelyTimingInfo.md)
 - [GwLoRaModulationInfo](docs/GwLoRaModulationInfo.md)
 - [GwPlainFineTimestamp](docs/GwPlainFineTimestamp.md)
 - [GwUplinkTXInfo](docs/GwUplinkTXInfo.md)
 - [ProtobufAny](docs/ProtobufAny.md)
 - [RuntimeStreamError](docs/RuntimeStreamError.md)


## Documentation For Authorization


## ApiKeyHeaderAuth

- **Type**: API key
- **API key parameter name**: Grpc-Metadata-Authorization
- **Location**: HTTP header


## Author

Yuregir TEKELI
