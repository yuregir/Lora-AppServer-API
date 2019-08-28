# ApiNetworkServer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_cert** | **str** | CA certificate (optional). | [optional] 
**gateway_discovery_dr** | **int** | The data-rate of the gateway discovery &#39;ping&#39;. | [optional] 
**gateway_discovery_enabled** | **bool** | Enable gateway discovery for this network-server. | [optional] 
**gateway_discovery_interval** | **int** | The number of times per day the gateway discovery &#39;ping&#39; must be broadcasted per gateway. | [optional] 
**gateway_discovery_tx_frequency** | **int** | The frequency (Hz) of the gateway discovery &#39;ping&#39;. | [optional] 
**id** | **str** | Network-server ID. | [optional] 
**name** | **str** | Network-server name. | [optional] 
**routing_profile_ca_cert** | **str** | Routing-profile ca certificate (used by the network-server to connect back to the application-server) (optional). | [optional] 
**routing_profile_tls_cert** | **str** | Routing-profile TLS certificate (used by the network-server to connect back to the application-server) (optional). | [optional] 
**routing_profile_tls_key** | **str** | Routing-profile TLS key (used by the network-server to connect back to the application-server) (optional). | [optional] 
**server** | **str** | Network-server server. Format: hostname:ip (e.g. localhost:8000). | [optional] 
**tls_cert** | **str** | TLS (client) certificate for connecting to the network-server (optional). | [optional] 
**tls_key** | **str** | TLS (client) key for connecting to the network-server (optional). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


