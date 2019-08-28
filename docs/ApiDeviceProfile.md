# ApiDeviceProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_b_timeout** | **int** | Maximum delay for the End-Device to answer a MAC request or a confirmed DL frame (mandatory if class B mode supported). | [optional] 
**class_c_timeout** | **int** | Maximum delay for the End-Device to answer a MAC request or a confirmed DL frame (mandatory if class C mode supported). | [optional] 
**factory_preset_freqs** | **list[int]** | List of factory-preset frequencies (mandatory for ABP). | [optional] 
**geoloc_buffer_ttl** | **int** | Geolocation buffer TTL (in seconds). When &gt; 0, uplink RX meta-data will be stored in a buffer so that the meta-data of multiple uplinks can be used for geolocation. | [optional] 
**geoloc_min_buffer_size** | **int** | Geolocation minimum buffer size. When &gt; 0, geolocation will only be performed when the buffer has at least the given size. | [optional] 
**id** | **str** | Device-profile ID (UUID string). | [optional] 
**mac_version** | **str** | Version of the LoRaWAN supported by the End-Device. | [optional] 
**max_duty_cycle** | **int** | Maximum duty cycle supported by the End-Device. | [optional] 
**max_eirp** | **int** | Maximum EIRP supported by the End-Device. | [optional] 
**name** | **str** | Device-profile name. | [optional] 
**network_server_id** | **str** | Network-server ID on which the service-profile is provisioned. | [optional] 
**organization_id** | **str** | Organization ID to which the service-profile is assigned. | [optional] 
**payload_codec** | **str** | Payload codec. Leave blank to disable the codec feature. | [optional] 
**payload_decoder_script** | **str** | Payload decoder script. Depending the codec, it is possible to provide a script which implements the decoder function. | [optional] 
**payload_encoder_script** | **str** | Payload encoder script. Depending the codec, it is possible to provide a script which implements the encoder function. | [optional] 
**ping_slot_dr** | **int** | Mandatory if class B mode supported. | [optional] 
**ping_slot_freq** | **int** | Mandatory if class B mode supported. | [optional] 
**ping_slot_period** | **int** | Mandatory if class B mode supported. | [optional] 
**reg_params_revision** | **str** | Revision of the Regional Parameters document supported by the End-Device. | [optional] 
**rf_region** | **str** | RF region name. | [optional] 
**rx_dr_offset1** | **int** | RX1 data rate offset (mandatory for ABP). | [optional] 
**rx_data_rate2** | **int** | RX2 data rate (mandatory for ABP). | [optional] 
**rx_delay1** | **int** | Class A RX1 delay (mandatory for ABP). | [optional] 
**rx_freq2** | **int** | RX2 channel frequency (mandatory for ABP). | [optional] 
**supports32_bit_f_cnt** | **bool** | End-Device uses 32bit FCnt (mandatory for LoRaWAN 1.0 End-Device). | [optional] 
**supports_class_b** | **bool** | End-Device supports Class B. | [optional] 
**supports_class_c** | **bool** | End-Device supports Class C. | [optional] 
**supports_join** | **bool** | End-Device supports Join (OTAA) or not (ABP). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


