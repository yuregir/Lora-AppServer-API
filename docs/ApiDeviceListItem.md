# ApiDeviceListItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | Application ID. | [optional] 
**description** | **str** | Description of the device. | [optional] 
**dev_eui** | **str** | Device EUI (HEX encoded). | [optional] 
**device_profile_id** | **str** | Device-profile ID attached to the device. | [optional] 
**device_profile_name** | **str** | Device-profile name. | [optional] 
**device_status_battery** | **int** | The device battery status (deprecated, use device_status_battery_level). 0:      The end-device is connected to an external power source 1..254: The battery level, 1 being at minimum and 254 being at maximum 255:    The end-device was not able to measure the battery level 256:    The device-status is not available. | [optional] 
**device_status_battery_level** | **float** | Device battery level as a percentage. | [optional] 
**device_status_battery_level_unavailable** | **bool** | Device battery status is unavailable. | [optional] 
**device_status_external_power_source** | **bool** | Device is connected to an external power source. | [optional] 
**device_status_margin** | **int** | The device margin status -32..32: The demodulation SNR ration in dB 256:     The device-status is not available. | [optional] 
**last_seen_at** | **datetime** | The last time the application-server received any data from the device, or an empty string when the device never sent any data. | [optional] 
**name** | **str** | Name of the device. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


