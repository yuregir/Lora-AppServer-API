# ApiApplication

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the application. | [optional] 
**id** | **str** | Application ID. This will be automatically assigned on create. | [optional] 
**name** | **str** | Name of the application (must be unique). | [optional] 
**organization_id** | **str** | ID of the organization to which the application belongs. After create, this can not be modified. | [optional] 
**payload_codec** | **str** | Payload codec. NOTE: These field have moved to the device-profile and will be removed in the next major release. When set, the device-profile payload_ fields have priority over the application payload_ fields. | [optional] 
**payload_decoder_script** | **str** | Payload decoder script. NOTE: These field have moved to the device-profile and will be removed in the next major release. When set, the device-profile payload_ fields have priority over the application payload_ fields. | [optional] 
**payload_encoder_script** | **str** | Payload encoder script. NOTE: These field have moved to the device-profile and will be removed in the next major release. When set, the device-profile payload_ fields have priority over the application payload_ fields. | [optional] 
**service_profile_id** | **str** | ID of the service profile. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


