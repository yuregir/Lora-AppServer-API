# ApiDeviceQueueItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmed** | **bool** | Set this to true when an acknowledgement from the device is required. Please note that this must not be used to guarantee a delivery. | [optional] 
**data** | **str** | Base64 encoded data. Or use the json_object field when an application codec has been configured. | [optional] 
**dev_eui** | **str** | Device EUI (HEX encoded). | [optional] 
**f_cnt** | **int** | Downlink frame-counter. This will be automatically set on enquue. | [optional] 
**f_port** | **int** | FPort used (must be &gt; 0) | [optional] 
**json_object** | **str** | JSON object (string). Only use this when an application codec has been configured that can convert this object into binary form. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


