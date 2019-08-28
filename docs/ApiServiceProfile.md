# ApiServiceProfile

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_gw_meta_data** | **bool** | GW metadata (RSSI, SNR, GW geoloc., etc.) are added to the packet sent to AS. | [optional] 
**channel_mask** | **str** | Channel mask. sNS does not have to obey (i.e., informative). | [optional] 
**dev_status_req_freq** | **int** | Frequency to initiate an End-Device status request (request/day). | [optional] 
**dl_bucket_size** | **int** | Token bucket burst size. | [optional] 
**dl_rate** | **int** | Token bucket filling rate, including ACKs (packet/h). | [optional] 
**dl_rate_policy** | [**ApiRatePolicy**](ApiRatePolicy.md) | Drop or mark when exceeding DLRate. | [optional] 
**dr_max** | **int** | Maximum allowed data rate. Used for ADR. | [optional] 
**dr_min** | **int** | Minimum allowed data rate. Used for ADR. | [optional] 
**hr_allowed** | **bool** | Handover Roaming allowed. | [optional] 
**id** | **str** | Service-profile ID (UUID string). This will be automatically set on create. | [optional] 
**min_gw_diversity** | **int** | Minimum number of receiving GWs (informative). | [optional] 
**name** | **str** | Service-profile name. | [optional] 
**network_server_id** | **str** | Network-server ID on which the service-profile is provisioned. | [optional] 
**nwk_geo_loc** | **bool** | Enable network geolocation service. | [optional] 
**organization_id** | **str** | Organization ID to which the service-profile is assigned. | [optional] 
**pr_allowed** | **bool** | Passive Roaming allowed. | [optional] 
**ra_allowed** | **bool** | Roaming Activation allowed. | [optional] 
**report_dev_status_battery** | **bool** | Report End-Device battery level to AS. | [optional] 
**report_dev_status_margin** | **bool** | Report End-Device margin to AS. | [optional] 
**target_per** | **int** | Target Packet Error Rate. | [optional] 
**ul_bucket_size** | **int** | Token bucket burst size. | [optional] 
**ul_rate** | **int** | Token bucket filling rate, including ACKs (packet/h). | [optional] 
**ul_rate_policy** | [**ApiRatePolicy**](ApiRatePolicy.md) | Drop or mark when exceeding ULRate. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


