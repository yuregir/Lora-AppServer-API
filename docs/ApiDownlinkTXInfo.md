# ApiDownlinkTXInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**antenna** | **int** | The antenna identifier for emitting the frame. | [optional] 
**board** | **int** | The board identifier for emitting the frame. | [optional] 
**context** | **str** | Gateway specific context. In case of a Class-A downlink, this contains a copy of the uplink context. | [optional] 
**delay_timing_info** | [**GwDelayTimingInfo**](GwDelayTimingInfo.md) | Context based delay timing information. | [optional] 
**frequency** | **int** | TX frequency (in Hz). | [optional] 
**fsk_modulation_info** | [**GwFSKModulationInfo**](GwFSKModulationInfo.md) | FSK modulation information. | [optional] 
**gateway_id** | **str** | Gateway ID. | [optional] 
**gps_epoch_timing_info** | [**GwGPSEpochTimingInfo**](GwGPSEpochTimingInfo.md) | GPS Epoch timing information. | [optional] 
**immediately_timing_info** | [**GwImmediatelyTimingInfo**](GwImmediatelyTimingInfo.md) | Immediately timing information. | [optional] 
**lora_modulation_info** | [**GwLoRaModulationInfo**](GwLoRaModulationInfo.md) | LoRa modulation information. | [optional] 
**modulation** | [**CommonModulation**](CommonModulation.md) | Modulation. | [optional] 
**power** | **int** | TX power (in dBm). | [optional] 
**timing** | [**GwDownlinkTiming**](GwDownlinkTiming.md) | Timing defines the downlink timing to use. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


