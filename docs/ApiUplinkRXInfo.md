# ApiUplinkRXInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**antenna** | **int** | Antenna. | [optional] 
**board** | **int** | Board. | [optional] 
**channel** | **int** | Channel. | [optional] 
**context** | **str** | Gateway specific context. | [optional] 
**encrypted_fine_timestamp** | [**ApiEncryptedFineTimestamp**](ApiEncryptedFineTimestamp.md) | Encrypted fine-timestamp data. | [optional] 
**fine_timestamp_type** | [**GwFineTimestampType**](GwFineTimestampType.md) | Fine-timestamp type. | [optional] 
**gateway_id** | **str** | Gateway ID. | [optional] 
**location** | [**CommonLocation**](CommonLocation.md) | Location. | [optional] 
**lora_snr** | **float** | LoRa SNR. | [optional] 
**plain_fine_timestamp** | [**GwPlainFineTimestamp**](GwPlainFineTimestamp.md) | Plain fine-timestamp data. | [optional] 
**rf_chain** | **int** | RF Chain. | [optional] 
**rssi** | **int** | RSSI. | [optional] 
**time** | **datetime** | RX time (only set when the gateway has a GPS module). | [optional] 
**time_since_gps_epoch** | **str** | RX time since GPS epoch (only set when the gateway has a GPS module). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


