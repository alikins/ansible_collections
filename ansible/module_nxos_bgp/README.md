# Ansible module: ansible.module_nxos_bgp


Manages BGP configuration

## Description

Manages BGP configurations on NX-OS switches.

## Requirements

TODO

## Arguments

``` json
{
    "asn": "{'description': ['BGP autonomous system number. Valid values are String, Integer in ASPLAIN or ASDOT notation.'], 'required': True}",
    "bestpath_always_compare_med": "{'description': ['Enable/Disable MED comparison on paths from different autonomous systems.'], 'type': 'bool'}",
    "bestpath_aspath_multipath_relax": "{'description': ['Enable/Disable load sharing across the providers with different (but equal-length) AS paths.'], 'type': 'bool'}",
    "bestpath_compare_neighborid": "{'description': ['Enable/Disable neighborid. Use this when more paths available than max path config.'], 'type': 'bool'}",
    "bestpath_compare_routerid": "{'description': ['Enable/Disable comparison of router IDs for identical eBGP paths.'], 'type': 'bool'}",
    "bestpath_cost_community_ignore": "{'description': ['Enable/Disable Ignores the cost community for BGP best-path calculations.'], 'type': 'bool'}",
    "bestpath_med_confed": "{'description': ['Enable/Disable enforcement of bestpath to do a MED comparison only between paths originated within a confederation.'], 'type': 'bool'}",
    "bestpath_med_missing_as_worst": "{'description': ['Enable/Disable assigns the value of infinity to received routes that do not carry the MED attribute, making these routes the least desirable.'], 'type': 'bool'}",
    "bestpath_med_non_deterministic": "{'description': ['Enable/Disable deterministic selection of the best MED pat from among the paths from the same autonomous system.'], 'type': 'bool'}",
    "cluster_id": "{'description': ['Route Reflector Cluster-ID.']}",
    "confederation_id": "{'description': ['Routing domain confederation AS.']}",
    "confederation_peers": "{'description': ['AS confederation parameters.']}",
    "disable_policy_batching": "{'description': ['Enable/Disable the batching evaluation of prefix advertisement to all peers.'], 'type': 'bool'}",
    "disable_policy_batching_ipv4_prefix_list": "{'description': ['Enable/Disable the batching evaluation of prefix advertisements to all peers with prefix list.']}",
    "disable_policy_batching_ipv6_prefix_list": "{'description': ['Enable/Disable the batching evaluation of prefix advertisements to all peers with prefix list.']}",
    "enforce_first_as": "{'description': ['Enable/Disable enforces the neighbor autonomous system to be the first AS number listed in the AS path attribute for eBGP. On NX-OS, this property is only supported in the global BGP context.'], 'type': 'bool'}",
    "event_history_cli": "{'description': ['Enable/Disable cli event history buffer.'], 'choices': ['size_small', 'size_medium', 'size_large', 'size_disable', 'default']}",
    "event_history_detail": "{'description': ['Enable/Disable detail event history buffer.'], 'choices': ['size_small', 'size_medium', 'size_large', 'size_disable', 'default']}",
    "event_history_events": "{'description': ['Enable/Disable event history buffer.'], 'choices': ['size_small', 'size_medium', 'size_large', 'size_disable', 'default']}",
    "event_history_periodic": "{'description': ['Enable/Disable periodic event history buffer.'], 'choices': ['size_small', 'size_medium', 'size_large', 'size_disable', 'default']}",
    "fast_external_fallover": "{'description': ['Enable/Disable immediately reset the session if the link to a directly connected BGP peer goes down.  Only supported in the global BGP context.'], 'type': 'bool'}",
    "flush_routes": "{'description': ['Enable/Disable flush routes in RIB upon controlled restart. On NX-OS, this property is only supported in the global BGP context.'], 'type': 'bool'}",
    "graceful_restart": "{'description': ['Enable/Disable graceful restart.'], 'type': 'bool'}",
    "graceful_restart_helper": "{'description': ['Enable/Disable graceful restart helper mode.'], 'type': 'bool'}",
    "graceful_restart_timers_restart": "{'description': ['Set maximum time for a restart sent to the BGP peer.']}",
    "graceful_restart_timers_stalepath_time": "{'description': ['Set maximum time that BGP keeps the stale routes from the restarting BGP peer.']}",
    "isolate": "{'description': ['Enable/Disable isolate this router from BGP perspective.'], 'type': 'bool'}",
    "local_as": "{'description': ['Local AS number to be used within a VRF instance.']}",
    "log_neighbor_changes": "{'description': ['Enable/Disable message logging for neighbor up/down event.'], 'type': 'bool'}",
    "maxas_limit": "{'description': ['Specify Maximum number of AS numbers allowed in the AS-path attribute. Valid values are between 1 and 512.']}",
    "neighbor_down_fib_accelerate": "{'description': ['Enable/Disable handle BGP neighbor down event, due to various reasons.'], 'type': 'bool'}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using NX-API.', 'For more information please see the L(NXOS Platform Options guide, ../network/user_guide/platform_nxos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(nxapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(nxapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False, 'choices': ['yes', 'no'], 'version_added': '2.5.3'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.'], 'default': 'none', 'version_added': '2.5.3'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc).'], 'default': 10, 'version_added': 2.3}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.  This argument is only used for the I(cli) transport. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.  The transport argument supports connectivity to the device over cli (ssh) or nxapi.'], 'required': True, 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=nxapi), otherwise this value is ignored.'], 'type': 'bool', 'default': 'no'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not nxapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "reconnect_interval": "{'description': ['The BGP reconnection interval for dropped sessions. Valid values are between 1 and 60.']}",
    "router_id": "{'description': ['Router Identifier (ID) of the BGP router VRF instance.']}",
    "shutdown": "{'description': ['Administratively shutdown the BGP protocol.'], 'type': 'bool'}",
    "state": "{'description': ['Determines whether the config should be present or not on the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "suppress_fib_pending": "{'description': ['Enable/Disable advertise only routes programmed in hardware to peers.'], 'type': 'bool'}",
    "timer_bestpath_limit": "{'description': ['Specify timeout for the first best path after a restart, in seconds.']}",
    "timer_bgp_hold": "{'description': ['Set BGP hold timer.']}",
    "timer_bgp_keepalive": "{'description': ['Set BGP keepalive timer.']}",
    "vrf": "{'description': ["Name of the VRF. The name 'default' is a valid VRF representing the global BGP."]}",
}
```

## Examples


``` yaml

- name: Configure a simple ASN
  nxos_bgp:
      asn: 65535
      vrf: test
      router_id: 192.0.2.1
      state: present

```

## License

TODO

## Author Information
  - ['Jason Edelman (@jedelman8)', 'Gabriele Gerbino (@GGabriele)']
  - ['Jason Edelman (@jedelman8)', 'Gabriele Gerbino (@GGabriele)']
