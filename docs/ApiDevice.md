# ApiDevice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | ID of the application to which the device must be added. It is possible to move a device to a different application on update, given that both the old and the new application share the same service-profile. | [optional] 
**description** | **str** | Description of the device. | [optional] 
**dev_eui** | **str** | Device EUI (HEX encoded). | [optional] 
**device_profile_id** | **str** | DeviceProfileID attached to the device. | [optional] 
**name** | **str** | Name of the device (if left blank, it will be set to the DevEUI). | [optional] 
**reference_altitude** | **float** | Reference altitude. When using geolocation, this altitude will be used as a reference (when supported by the geolocation-server) to increase geolocation accuracy. | [optional] 
**skip_f_cnt_check** | **bool** | Skip frame-counter checks (this is insecure, but could be helpful for debugging). | [optional] 
**tags** | **dict(str, str)** | Tags (user defined). These tags are exposed in the event payloads or to integration. Tags are intended for aggregation and filtering. | [optional] 
**variables** | **dict(str, str)** | Variables (user defined). These variables can be used together with integrations to store tokens / secrets that must be configured per device. These variables are not exposed in the event payloads. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


