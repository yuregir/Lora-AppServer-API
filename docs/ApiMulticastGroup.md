# ApiMulticastGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dr** | **int** | Data-rate. | [optional] 
**f_cnt** | **int** | Frame-counter. | [optional] 
**frequency** | **int** | Frequency (Hz). | [optional] 
**group_type** | [**ApiMulticastGroupType**](ApiMulticastGroupType.md) | Multicast type. | [optional] 
**id** | **str** | ID (string formatted UUID). This will be generated automatically on create. | [optional] 
**mc_addr** | **str** | Multicast address (HEX encoded DevAddr). | [optional] 
**mc_app_s_key** | **str** | Multicast application session key (HEX encoded AES128 key). | [optional] 
**mc_nwk_s_key** | **str** | Multicast network session key (HEX encoded AES128 key). | [optional] 
**name** | **str** | Multicast-group name. | [optional] 
**ping_slot_period** | **int** | Ping-slot period. Mandatory for Class-B multicast groups. | [optional] 
**service_profile_id** | **str** | Service-profile ID. After creation, this can not be updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


