# gRPC API Reference

## service `GobgpApi` (api/gobgp.proto)

Interface exported by the server.

| Method | Request Type | Response Type | Description |
| ------ | ------------ | ------------- | ----------- |
| StartServer | StartServerRequest | StartServerResponse |  |
| StopServer | StopServerRequest | StopServerResponse |  |
| GetServer | GetServerRequest | GetServerResponse |  |
| AddNeighbor | AddNeighborRequest | AddNeighborResponse |  |
| DeleteNeighbor | DeleteNeighborRequest | DeleteNeighborResponse |  |
| UpdateNeighbor | UpdateNeighborRequest | UpdateNeighborResponse |  |
| GetNeighbor | GetNeighborRequest | GetNeighborResponse |  |
| ResetNeighbor | ResetNeighborRequest | ResetNeighborResponse |  |
| SoftResetNeighbor | SoftResetNeighborRequest | SoftResetNeighborResponse |  |
| ShutdownNeighbor | ShutdownNeighborRequest | ShutdownNeighborResponse |  |
| EnableNeighbor | EnableNeighborRequest | EnableNeighborResponse |  |
| DisableNeighbor | DisableNeighborRequest | DisableNeighborResponse |  |
| GetRib | GetRibRequest | GetRibResponse |  |
| GetPath | GetPathRequest | Path |  |
| ValidateRib | ValidateRibRequest | ValidateRibResponse |  |
| AddPath | AddPathRequest | AddPathResponse |  |
| DeletePath | DeletePathRequest | DeletePathResponse |  |
| MonitorRib | MonitorRibRequest | Destination |  |
| MonitorPeerState | Arguments | Peer |  |
| EnableMrt | EnableMrtRequest | EnableMrtResponse |  |
| DisableMrt | DisableMrtRequest | DisableMrtResponse |  |
| InjectMrt | InjectMrtRequest | InjectMrtResponse |  |
| AddBmp | AddBmpRequest | AddBmpResponse |  |
| DeleteBmp | DeleteBmpRequest | DeleteBmpResponse |  |
| GetRpki | GetRpkiRequest | GetRpkiResponse |  |
| AddRpki | AddRpkiRequest | AddRpkiResponse |  |
| DeleteRpki | DeleteRpkiRequest | DeleteRpkiResponse |  |
| EnableRpki | EnableRpkiRequest | EnableRpkiResponse |  |
| DisableRpki | DisableRpkiRequest | DisableRpkiResponse |  |
| ResetRpki | ResetRpkiRequest | ResetRpkiResponse |  |
| SoftResetRpki | SoftResetRpkiRequest | SoftResetRpkiResponse |  |
| GetRoa | GetRoaRequest | GetRoaResponse |  |
| EnableZebra | EnableZebraRequest | EnableZebraResponse |  |
| AddVrf | AddVrfRequest | AddVrfResponse |  |
| DeleteVrf | DeleteVrfRequest | DeleteVrfResponse |  |
| GetVrf | GetVrfRequest | GetVrfResponse |  |
| GetDefinedSet | GetDefinedSetRequest | GetDefinedSetResponse |  |
| AddDefinedSet | AddDefinedSetRequest | AddDefinedSetResponse |  |
| DeleteDefinedSet | DeleteDefinedSetRequest | DeleteDefinedSetResponse |  |
| ReplaceDefinedSet | ReplaceDefinedSetRequest | ReplaceDefinedSetResponse |  |
| GetStatement | GetStatementRequest | GetStatementResponse |  |
| AddStatement | AddStatementRequest | AddStatementResponse |  |
| DeleteStatement | DeleteStatementRequest | DeleteStatementResponse |  |
| ReplaceStatement | ReplaceStatementRequest | ReplaceStatementResponse |  |
| GetPolicy | GetPolicyRequest | GetPolicyResponse |  |
| AddPolicy | AddPolicyRequest | AddPolicyResponse |  |
| DeletePolicy | DeletePolicyRequest | DeletePolicyResponse |  |
| ReplacePolicy | ReplacePolicyRequest | ReplacePolicyResponse |  |
| GetPolicyAssignment | GetPolicyAssignmentRequest | GetPolicyAssignmentResponse |  |
| AddPolicyAssignment | AddPolicyAssignmentRequest | AddPolicyAssignmentResponse |  |
| DeletePolicyAssignment | DeletePolicyAssignmentRequest | DeletePolicyAssignmentResponse |  |
| ReplacePolicyAssignment | ReplacePolicyAssignmentRequest | ReplacePolicyAssignmentResponse |  |
| GetRibInfo | GetRibInfoRequest | GetRibInfoResponse |  |

## message `Actions` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| route_action |  | RouteAction |
| community |  | CommunityAction |
| med |  | MedAction |
| as_prepend |  | AsPrependAction |
| ext_community |  | CommunityAction |
| nexthop |  | NexthopAction |
| local_pref |  | LocalPrefAction |
| large_community |  | CommunityAction |

## message `AddBmpRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| address |  | string |
| port |  | uint32 |
| type |  | MonitoringPolicy |

## message `AddBmpResponse` (api/gobgp.proto)

Empty field.

## message `AddDefinedSetRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| set |  | DefinedSet |

## message `AddDefinedSetResponse` (api/gobgp.proto)

Empty field.

## message `AddNeighborRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| peer |  | Peer |

## message `AddNeighborResponse` (api/gobgp.proto)

Empty field.

## message `AddPathRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| resource |  | Resource |
| vrf_id |  | string |
| path |  | Path |

## message `AddPathResponse` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| uuid |  | bytes |

## message `AddPaths` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| config |  | AddPathsConfig |
| state |  | AddPathsState |

## message `AddPathsConfig` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| receive |  | bool |
| send_max |  | uint32 |

## message `AddPathsState` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| receive |  | bool |
| send_max |  | uint32 |

## message `AddPolicyAssignmentRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| assignment |  | PolicyAssignment |

## message `AddPolicyAssignmentResponse` (api/gobgp.proto)

Empty field.

## message `AddPolicyRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| policy |  | Policy |
| refer_existing_statements | if this flag is set, gobgpd won't define new statements but refer existing statements using statement's names in this arguments. | bool |

## message `AddPolicyResponse` (api/gobgp.proto)

Empty field.

## message `AddRpkiRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| address |  | string |
| port |  | uint32 |
| lifetime |  | int64 |

## message `AddRpkiResponse` (api/gobgp.proto)

Empty field.

## message `AddStatementRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| statement |  | Statement |

## message `AddStatementResponse` (api/gobgp.proto)

Empty field.

## message `AddVrfRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| vrf |  | Vrf |

## message `AddVrfResponse` (api/gobgp.proto)

Empty field.

## message `AfiSafi` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| mp_graceful_restart |  | MpGracefulRestart |
| config |  | AfiSafiConfig |
| apply_policy |  | ApplyPolicy |
| route_selection_options | TODO: Support the following structures: - Ipv4Unicast - Ipv6Unicast - Ipv4LabelledUnicast - Ipv6LabelledUnicast - L3vpnIpv4Unicast - L3vpnIpv6Unicast - L3vpnIpv4Multicast - L3vpnIpv6Multicast - L2vpnVpls - L2vpnEvpn | RouteSelectionOptions |
| use_multiple_paths |  | UseMultiplePaths |
| prefix_limits |  | PrefixLimit |
| route_target_membership |  | RouteTargetMembership |
| long_lived_graceful_restart |  | LongLivedGracefulRestart |
| add_paths |  | AddPaths |

## message `AfiSafiConfig` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| family |  | uint32 |
| enabled |  | bool |

## message `AfiSafiState` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| family |  | uint32 |
| enabled |  | bool |
| total_paths |  | uint32 |
| total_prefixes |  | uint32 |

## message `ApplyPolicy` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| in_policy |  | PolicyAssignment |
| export_policy |  | PolicyAssignment |
| import_policy |  | PolicyAssignment |

## message `Arguments` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| resource |  | Resource |
| family |  | uint32 |
| name |  | string |
| current |  | bool |

## message `AsPathLength` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| type |  | AsPathLengthType |
| length |  | uint32 |

## message `AsPrependAction` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| asn |  | uint32 |
| repeat |  | uint32 |
| use_left_most |  | bool |

## message `CommunityAction` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| type |  | CommunityActionType |
| communities |  | (slice of) string |

## message `Conditions` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| prefix_set |  | MatchSet |
| neighbor_set |  | MatchSet |
| as_path_length |  | AsPathLength |
| as_path_set |  | MatchSet |
| community_set |  | MatchSet |
| ext_community_set |  | MatchSet |
| rpki_result |  | int32 |
| route_type |  | RouteType |
| large_community_set |  | MatchSet |
| next_hop_in_list |  | (slice of) string |

## message `DefinedSet` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| type |  | DefinedType |
| name |  | string |
| list |  | (slice of) string |
| prefixes |  | (slice of) Prefix |

## message `DeleteBmpRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| address |  | string |
| port |  | uint32 |

## message `DeleteBmpResponse` (api/gobgp.proto)

Empty field.

## message `DeleteDefinedSetRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| set |  | DefinedSet |
| all |  | bool |

## message `DeleteDefinedSetResponse` (api/gobgp.proto)

Empty field.

## message `DeleteNeighborRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| peer |  | Peer |

## message `DeleteNeighborResponse` (api/gobgp.proto)

Empty field.

## message `DeletePathRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| resource |  | Resource |
| vrf_id |  | string |
| family |  | uint32 |
| path |  | Path |
| uuid |  | bytes |

## message `DeletePathResponse` (api/gobgp.proto)

Empty field.

## message `DeletePolicyAssignmentRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| assignment |  | PolicyAssignment |
| all |  | bool |

## message `DeletePolicyAssignmentResponse` (api/gobgp.proto)

Empty field.

## message `DeletePolicyRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| policy |  | Policy |
| preserve_statements | if this flag is set, gobgpd won't delete any statements even if some statements get not used by any policy by this operation. | bool |
| all |  | bool |

## message `DeletePolicyResponse` (api/gobgp.proto)

Empty field.

## message `DeleteRpkiRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| address |  | string |
| port |  | uint32 |

## message `DeleteRpkiResponse` (api/gobgp.proto)

Empty field.

## message `DeleteStatementRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| statement |  | Statement |
| all |  | bool |

## message `DeleteStatementResponse` (api/gobgp.proto)

Empty field.

## message `DeleteVrfRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| vrf |  | Vrf |

## message `DeleteVrfResponse` (api/gobgp.proto)

Empty field.

## message `Destination` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| prefix |  | string |
| paths |  | (slice of) Path |
| longer_prefixes |  | bool |
| shorter_prefixes |  | bool |

## message `DisableMrtRequest` (api/gobgp.proto)

Empty field.

## message `DisableMrtResponse` (api/gobgp.proto)

Empty field.

## message `DisableNeighborRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| address |  | string |
| communication |  | string |

## message `DisableNeighborResponse` (api/gobgp.proto)

Empty field.

## message `DisableRpkiRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| address |  | string |

## message `DisableRpkiResponse` (api/gobgp.proto)

Empty field.

## message `Ebgp` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| config |  | EbgpConfig |
| state |  | EbgpState |

## message `EbgpConfig` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| allow_multiple_as |  | bool |
| maximum_paths |  | uint32 |

## message `EbgpMultihop` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| enabled |  | bool |
| multihop_ttl |  | uint32 |

## message `EbgpState` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| allow_multiple_as |  | bool |
| maximum_paths |  | uint32 |

## message `EnableMrtRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| dump_type |  | int32 |
| filename |  | string |
| interval |  | uint64 |

## message `EnableMrtResponse` (api/gobgp.proto)

Empty field.

## message `EnableNeighborRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| address |  | string |

## message `EnableNeighborResponse` (api/gobgp.proto)

Empty field.

## message `EnableRpkiRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| address |  | string |

## message `EnableRpkiResponse` (api/gobgp.proto)

Empty field.

## message `EnableZebraRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| url |  | string |
| route_types |  | (slice of) string |
| version |  | uint32 |
| nexthop_trigger_enable |  | bool |
| nexthop_trigger_delay |  | uint32 |

## message `EnableZebraResponse` (api/gobgp.proto)

Empty field.

## message `GetDefinedSetRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| type |  | DefinedType |
| name |  | string |

## message `GetDefinedSetResponse` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| sets |  | (slice of) DefinedSet |

## message `GetNeighborRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| enableAdvertised |  | bool |
| address |  | string |

## message `GetNeighborResponse` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| peers |  | (slice of) Peer |

## message `GetPathRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| type |  | Resource |
| name |  | string |
| family |  | uint32 |
| prefixes |  | (slice of) TableLookupPrefix |

## message `GetPolicyAssignmentRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| assignment |  | PolicyAssignment |

## message `GetPolicyAssignmentResponse` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| assignment |  | PolicyAssignment |

## message `GetPolicyRequest` (api/gobgp.proto)

Empty field.

## message `GetPolicyResponse` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| policies |  | (slice of) Policy |

## message `GetRibInfoRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| info |  | TableInfo |

## message `GetRibInfoResponse` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| info |  | TableInfo |

## message `GetRibRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| table |  | Table |

## message `GetRibResponse` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| table |  | Table |

## message `GetRoaRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| family |  | uint32 |

## message `GetRoaResponse` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| roas |  | (slice of) Roa |

## message `GetRpkiRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| family |  | uint32 |

## message `GetRpkiResponse` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| servers |  | (slice of) Rpki |

## message `GetServerRequest` (api/gobgp.proto)

Empty field.

## message `GetServerResponse` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| global |  | Global |

## message `GetStatementRequest` (api/gobgp.proto)

Empty field.

## message `GetStatementResponse` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| statements |  | (slice of) Statement |

## message `GetVrfRequest` (api/gobgp.proto)

Empty field.

## message `GetVrfResponse` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| vrfs |  | (slice of) Vrf |

## message `Global` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| as |  | uint32 |
| router_id |  | string |
| listen_port |  | int32 |
| listen_addresses |  | (slice of) string |
| families |  | (slice of) uint32 |
| use_multiple_paths |  | bool |

## message `GracefulRestart` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| enabled |  | bool |
| restart_time |  | uint32 |
| helper_only |  | bool |
| deferral_time |  | uint32 |
| notification_enabled |  | bool |
| longlived_enabled |  | bool |

## message `Ibgp` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| config |  | IbgpConfig |
| state |  | IbgpState |

## message `IbgpConfig` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| maximum_paths |  | uint32 |

## message `IbgpState` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| maximum_paths |  | uint32 |

## message `InjectMrtRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| resource |  | Resource |
| vrf_id |  | string |
| paths |  | (slice of) Path |

## message `InjectMrtResponse` (api/gobgp.proto)

Empty field.

## message `LocalPrefAction` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| value |  | uint32 |

## message `LongLivedGracefulRestart` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| config |  | LongLivedGracefulRestartConfig |
| state |  | LongLivedGracefulRestartState |

## message `LongLivedGracefulRestartConfig` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| enabled |  | bool |
| restart_time |  | uint32 |

## message `LongLivedGracefulRestartState` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| enabled |  | bool |
| received |  | bool |
| advertised |  | bool |
| peer_restart_time |  | uint32 |
| peer_restart_timer_expired |  | bool |

## message `MatchSet` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| type |  | MatchType |
| name |  | string |

## message `MedAction` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| type |  | MedActionType |
| value |  | int64 |

## message `Message` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| NOTIFICATION |  | uint64 |
| UPDATE |  | uint64 |
| OPEN |  | uint64 |
| KEEPALIVE |  | uint64 |
| REFRESH |  | uint64 |
| DISCARDED |  | uint64 |
| TOTAL |  | uint64 |

## message `Messages` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| received |  | Message |
| sent |  | Message |

## message `MonitorRibRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| table |  | Table |
| current |  | bool |

## message `MpGracefulRestart` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| config |  | MpGracefulRestartConfig |
| state |  | MpGracefulRestartState |

## message `MpGracefulRestartConfig` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| enabled |  | bool |

## message `MpGracefulRestartState` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| enabled |  | bool |
| received |  | bool |
| advertised |  | bool |
| end_of_rib_received |  | bool |
| end_of_rib_sent |  | bool |

## message `NexthopAction` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| address |  | string |
| self |  | bool |

## message `Path` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| nlri |  | bytes |
| pattrs |  | (slice of) bytes |
| age |  | int64 |
| best |  | bool |
| is_withdraw |  | bool |
| validation |  | int32 |
| validation_detail | remains for backword compatibility | RPKIValidation |
| no_implicit_withdraw |  | bool |
| family |  | uint32 |
| source_asn |  | uint32 |
| source_id |  | string |
| filtered |  | bool |
| stale |  | bool |
| is_from_external |  | bool |
| neighbor_ip |  | string |
| uuid |  | bytes |
| is_nexthop_invalid | only paths installed by AddPath API have this | bool |
| identifier |  | uint32 |
| local_identifier |  | uint32 |

## message `Peer` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| families | Note: Regarding to the consistency with OpenConfig model, a list of address family should be removed from here, and should be configured with the list of AfiSafi instead. | (slice of) uint32 |
| apply_policy |  | ApplyPolicy |
| conf |  | PeerConf |
| ebgp_multihop |  | EbgpMultihop |
| route_reflector |  | RouteReflector |
| info |  | PeerState |
| timers |  | Timers |
| transport |  | Transport |
| route_server |  | RouteServer |
| graceful_restart |  | GracefulRestart |
| afi_safis |  | (slice of) AfiSafi |
| add_paths |  | AddPaths |

## message `PeerConf` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| auth_password |  | string |
| description |  | string |
| local_as |  | uint32 |
| neighbor_address |  | string |
| peer_as |  | uint32 |
| peer_group |  | string |
| peer_type |  | uint32 |
| remove_private_as |  | RemovePrivateAs |
| route_flap_damping |  | bool |
| send_community |  | uint32 |
| remote_cap |  | (slice of) bytes |
| local_cap |  | (slice of) bytes |
| id |  | string |
| prefix_limits | Note: Regarding to the consistency with OpenConfig model, list of PrefixLimit should be removed from here, and list of PrefixLimit in AfiSafi should be used instead. | (slice of) PrefixLimit |
| local_address |  | string |
| neighbor_interface |  | string |
| vrf |  | string |
| allow_own_as |  | uint32 |
| replace_peer_as |  | bool |

## message `PeerState` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| auth_password |  | string |
| description |  | string |
| local_as |  | uint32 |
| messages |  | Messages |
| neighbor_address |  | string |
| peer_as |  | uint32 |
| peer_group |  | string |
| peer_type |  | uint32 |
| queues |  | Queues |
| remove_private_as |  | uint32 |
| route_flap_damping |  | bool |
| send_community |  | uint32 |
| session_state |  | uint32 |
| supported_capabilities |  | (slice of) string |
| bgp_state |  | string |
| admin_state |  | AdminState |
| received |  | uint32 |
| accepted |  | uint32 |
| advertised |  | uint32 |
| out_q |  | uint32 |
| flops |  | uint32 |

## message `Policy` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| name |  | string |
| statements |  | (slice of) Statement |

## message `PolicyAssignment` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| type |  | PolicyType |
| resource |  | Resource |
| name |  | string |
| policies |  | (slice of) Policy |
| default |  | RouteAction |

## message `Prefix` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| ip_prefix |  | string |
| mask_length_min |  | uint32 |
| mask_length_max |  | uint32 |

## message `PrefixLimit` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| family |  | uint32 |
| max_prefixes |  | uint32 |
| shutdown_threshold_pct |  | uint32 |

## message `Queues` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| input |  | uint32 |
| output |  | uint32 |

## message `RPKIConf` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| address |  | string |
| remote_port |  | string |

## message `RPKIState` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| uptime |  | int64 |
| downtime |  | int64 |
| up |  | bool |
| record_ipv4 |  | uint32 |
| record_ipv6 |  | uint32 |
| prefix_ipv4 |  | uint32 |
| prefix_ipv6 |  | uint32 |
| serial |  | uint32 |
| received_ipv4 |  | int64 |
| received_ipv6 |  | int64 |
| serial_notify |  | int64 |
| cache_reset |  | int64 |
| cache_response |  | int64 |
| end_of_data |  | int64 |
| error |  | int64 |
| serial_query |  | int64 |
| reset_query |  | int64 |

## message `RPKIValidation` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| state |  | State |
| reason |  | Reason |
| matched |  | (slice of) Roa |
| unmatched_as |  | (slice of) Roa |
| unmatched_length |  | (slice of) Roa |

## message `ReplaceDefinedSetRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| set |  | DefinedSet |

## message `ReplaceDefinedSetResponse` (api/gobgp.proto)

Empty field.

## message `ReplacePolicyAssignmentRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| assignment |  | PolicyAssignment |

## message `ReplacePolicyAssignmentResponse` (api/gobgp.proto)

Empty field.

## message `ReplacePolicyRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| policy |  | Policy |
| refer_existing_statements | if this flag is set, gobgpd won't define new statements but refer existing statements using statement's names in this arguments. | bool |
| preserve_statements | if this flag is set, gobgpd won't delete any statements even if some statements get not used by any policy by this operation. | bool |

## message `ReplacePolicyResponse` (api/gobgp.proto)

Empty field.

## message `ReplaceStatementRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| statement |  | Statement |

## message `ReplaceStatementResponse` (api/gobgp.proto)

Empty field.

## message `ResetNeighborRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| address |  | string |
| communication |  | string |

## message `ResetNeighborResponse` (api/gobgp.proto)

Empty field.

## message `ResetRpkiRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| address |  | string |

## message `ResetRpkiResponse` (api/gobgp.proto)

Empty field.

## message `Roa` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| as |  | uint32 |
| prefixlen |  | uint32 |
| maxlen |  | uint32 |
| prefix |  | string |
| conf |  | RPKIConf |

## message `RouteReflector` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| route_reflector_client |  | bool |
| route_reflector_cluster_id |  | string |

## message `RouteSelectionOptions` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| config |  | RouteSelectionOptionsConfig |
| state |  | RouteSelectionOptionsState |

## message `RouteSelectionOptionsConfig` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| always_compare_med |  | bool |
| ignore_as_path_length |  | bool |
| external_compare_router_id |  | bool |
| advertise_inactive_routes |  | bool |
| enable_aigp |  | bool |
| ignore_next_hop_igp_metric |  | bool |

## message `RouteSelectionOptionsState` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| always_compare_med |  | bool |
| ignore_as_path_length |  | bool |
| external_compare_router_id |  | bool |
| advertise_inactive_routes |  | bool |
| enable_aigp |  | bool |
| ignore_next_hop_igp_metric |  | bool |

## message `RouteServer` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| route_server_client |  | bool |

## message `RouteTargetMembership` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| config |  | RouteTargetMembershipConfig |
| state |  | RouteTargetMembershipState |

## message `RouteTargetMembershipConfig` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| deferral_time |  | uint32 |

## message `RouteTargetMembershipState` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| deferral_time |  | uint32 |

## message `Rpki` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| conf |  | RPKIConf |
| state |  | RPKIState |

## message `ShutdownNeighborRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| address |  | string |
| communication |  | string |

## message `ShutdownNeighborResponse` (api/gobgp.proto)

Empty field.

## message `SoftResetNeighborRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| address |  | string |
| direction |  | SoftResetDirection |

## message `SoftResetNeighborResponse` (api/gobgp.proto)

Empty field.

## message `SoftResetRpkiRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| address |  | string |

## message `SoftResetRpkiResponse` (api/gobgp.proto)

Empty field.

## message `StartServerRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| global |  | Global |

## message `StartServerResponse` (api/gobgp.proto)

Empty field.

## message `Statement` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| name |  | string |
| conditions |  | Conditions |
| actions |  | Actions |

## message `StopServerRequest` (api/gobgp.proto)

Empty field.

## message `StopServerResponse` (api/gobgp.proto)

Empty field.

## message `Table` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| type |  | Resource |
| name |  | string |
| family |  | uint32 |
| destinations |  | (slice of) Destination |
| post_policy |  | bool |

## message `TableInfo` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| type |  | Resource |
| name |  | string |
| family |  | uint32 |
| num_destination |  | uint64 |
| num_path |  | uint64 |
| num_accepted |  | uint64 |

## message `TableLookupPrefix` (api/gobgp.proto)

API representation of table.LookupPrefix

| Field | Description | Type |
| ----- | ----------- | ---- |
| prefix |  | string |
| lookup_option |  | TableLookupOption |

## message `Timers` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| config |  | TimersConfig |
| state |  | TimersState |

## message `TimersConfig` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| connect_retry |  | uint64 |
| hold_time |  | uint64 |
| keepalive_interval |  | uint64 |
| minimum_advertisement_interval |  | uint64 |

## message `TimersState` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| connect_retry |  | uint64 |
| hold_time |  | uint64 |
| keepalive_interval |  | uint64 |
| minimum_advertisement_interval |  | uint64 |
| negotiated_hold_time |  | uint64 |
| uptime |  | uint64 |
| downtime |  | uint64 |

## message `Transport` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| local_address |  | string |
| local_port |  | uint32 |
| mtu_discovery |  | bool |
| passive_mode |  | bool |
| remote_address |  | string |
| remote_port |  | uint32 |
| tcp_mss |  | uint32 |

## message `UpdateNeighborRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| peer |  | Peer |
| do_soft_reset_in | Calls SoftResetIn after updating the neighbor configuration if needed. | bool |

## message `UpdateNeighborResponse` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| needs_soft_reset_in | Indicates whether calling SoftResetIn is required due to this update. If "true" is set, the client should call SoftResetIn manually. If "do_soft_reset_in = true" is set in the request, always returned with "false". | bool |

## message `UseMultiplePaths` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| config |  | UseMultiplePathsConfig |
| state |  | UseMultiplePathsState |
| ebgp |  | Ebgp |
| ibgp |  | Ibgp |

## message `UseMultiplePathsConfig` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| enabled |  | bool |

## message `UseMultiplePathsState` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| enabled |  | bool |

## message `ValidateRibRequest` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| type |  | Resource |
| family |  | uint32 |
| prefix |  | string |

## message `ValidateRibResponse` (api/gobgp.proto)

Empty field.

## message `Vrf` (api/gobgp.proto)

| Field | Description | Type |
| ----- | ----------- | ---- |
| name |  | string |
| rd |  | bytes |
| import_rt |  | (slice of) bytes |
| export_rt |  | (slice of) bytes |
| id |  | uint32 |

> This document is generated by [`protodoc.sh`](../../tools/docs/protodoc.sh).
