# ApiFUOTADeployment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dr** | **int** | Data-rate. | [optional] 
**frequency** | **int** | Frequency (Hz). | [optional] 
**group_type** | [**ApiMulticastGroupType**](ApiMulticastGroupType.md) | Multicast type. Currently only Class-C is supported! | [optional] 
**id** | **str** | ID of the deployment (string formatted UUID). This value will be automatically assigned on create. | [optional] 
**multicast_timeout** | **int** | Multicast time-out. Please refer to the Remote Multicast Setup specification as this field has a different meaning for Class-B and Class-C groups. | [optional] 
**name** | **str** | Name of the deployment. | [optional] 
**next_step_after** | **datetime** | Next step after. This value will be automatically set on create. | [optional] 
**payload** | **str** | Payload. | [optional] 
**redundancy** | **int** | Redundancy (number of packages). | [optional] 
**state** | **str** | Deployment state. This value will be automatically set on create. | [optional] 
**unicast_timeout** | **str** | Unicast time-out. Set this to the value in which you at least expect an uplink frame from the device. The FUOTA deployment engine will wait at least for the given time before proceeding with the next steps. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


