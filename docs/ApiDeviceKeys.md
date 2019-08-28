# ApiDeviceKeys

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_key** | **str** | Application root key (HEX encoded). Note: This field only needs to be set for LoRaWAN 1.1.x devices! | [optional] 
**dev_eui** | **str** | Device EUI (HEX encoded). | [optional] 
**gen_app_key** | **str** | Gen application key (HEX encoded). This is an optional key that only must be set for LORaWAN 1.0.x devices that implement the remote multicast setup specification. | [optional] 
**nwk_key** | **str** | Network root key (HEX encoded). Note: For LoRaWAN 1.0.x, use this field for the LoRaWAN 1.0.x &#39;AppKey&#x60;! | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


