# ApiGetDeviceResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | [**ApiDevice**](ApiDevice.md) | Device object. | [optional] 
**device_status_battery** | **int** | The device battery status 0:      The end-device is connected to an external power source 1..254: The battery level, 1 being at minimum and 254 being at maximum 255:    The end-device was not able to measure the battery level 256:    The device-status is not available. | [optional] 
**device_status_margin** | **int** | The device margin status -32..32: The demodulation SNR ration in dB 256:     The device-status is not available. | [optional] 
**last_seen_at** | **datetime** | Last seen timestamp. | [optional] 
**location** | [**CommonLocation**](CommonLocation.md) | Device location. This will set when the network-server was able to resolve the location using the geolocation-server. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


