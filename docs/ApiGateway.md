# ApiGateway

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boards** | [**list[ApiGatewayBoard]**](ApiGatewayBoard.md) | Gateway boards configuration (optional). This is (currently) only needed when the gateway supports the fine-timestamp and you you would like to add the FPGA ID to the gateway meta-data or would like LoRa Server to decrypt the fine-timestamp. | [optional] 
**description** | **str** | Gateway description. | [optional] 
**discovery_enabled** | **bool** | Set to true to enable gateway discovery. | [optional] 
**gateway_profile_id** | **str** | Gateway-profile ID (UUID string, optional). | [optional] 
**id** | **str** | Gateway ID (HEX encoded). | [optional] 
**location** | [**CommonLocation**](CommonLocation.md) | Gateway location. | [optional] 
**name** | **str** | Gateway name. | [optional] 
**network_server_id** | **str** | Network-server ID on which the gateway is provisioned. | [optional] 
**organization_id** | **str** | Organization ID to which the gateway belongs. This can&#39;t be changed after creating the gateway. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


