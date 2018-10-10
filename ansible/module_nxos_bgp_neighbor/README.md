# Ansible module: ansible.module_nxos_bgp_neighbor


Manages BGP neighbors configurations

## Description

Manages BGP neighbors configurations on NX-OS switches.

## Requirements

TODO

## Arguments

``` json
{
    "asn": "{'description': ['BGP autonomous system number. Valid values are string, Integer in ASPLAIN or ASDOT notation.'], 'required': True}",
    "capability_negotiation": "{'description': ['Configure whether or not to negotiate capability with this neighbor.'], 'type': 'bool'}",
    "connected_check": "{'description': ['Configure whether or not to check for directly connected peer.'], 'type': 'bool'}",
    "description": "{'description': ['Description of the neighbor.']}",
    "dynamic_capability": "{'description': ['Configure whether or not to enable dynamic capability.'], 'type': 'bool'}",
    "ebgp_multihop": "{'description': ["Specify multihop TTL for a remote peer. Valid values are integers between 2 and 255, or keyword 'default' to disable this property."]}",
    "local_as": "{'description': ["Specify the local-as number for the eBGP neighbor. Valid values are String or Integer in ASPLAIN or ASDOT notation, or 'default', which means not to configure it."]}",
    "log_neighbor_changes": "{'description': ['Specify whether or not to enable log messages for neighbor up/down event.'], 'choices': ['enable', 'disable', 'inherit']}",
    "low_memory_exempt": "{'description': ['Specify whether or not to shut down this neighbor under memory pressure.'], 'type': 'bool'}",
    "maximum_peers": "{'description': ["Specify Maximum number of peers for this neighbor prefix Valid values are between 1 and 1000, or 'default', which does not impose the limit. Note that this parameter is accepted only on neighbors with address/prefix."]}",
    "neighbor": "{'description': ['Neighbor Identifier. Valid values are string. Neighbors may use IPv4 or IPv6 notation, with or without prefix length.'], 'required': True}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using NX-API.', 'For more information please see the L(NXOS Platform Options guide, ../network/user_guide/platform_nxos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(nxapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(nxapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False, 'choices': ['yes', 'no'], 'version_added': '2.5.3'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.'], 'default': 'none', 'version_added': '2.5.3'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc).'], 'default': 10, 'version_added': 2.3}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.  This argument is only used for the I(cli) transport. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.  The transport argument supports connectivity to the device over cli (ssh) or nxapi.'], 'required': True, 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=nxapi), otherwise this value is ignored.'], 'type': 'bool', 'default': 'no'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not nxapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "pwd": "{'description': ['Specify the password for neighbor. Valid value is string.']}",
    "pwd_type": "{'description': ["Specify the encryption type the password will use. Valid values are '3des' or 'cisco_type_7' encryption or keyword 'default'."], 'choices': ['3des', 'cisco_type_7', 'default']}",
    "remote_as": "{'description': ["Specify Autonomous System Number of the neighbor. Valid values are String or Integer in ASPLAIN or ASDOT notation, or 'default', which means not to configure it."]}",
    "remove_private_as": "{'description': ["Specify the config to remove private AS number from outbound updates. Valid values are 'enable' to enable this config, 'disable' to disable this config, 'all' to remove all private AS number, or 'replace-as', to replace the private AS number."], 'choices': ['enable', 'disable', 'all', 'replace-as']}",
    "shutdown": "{'description': ['Configure to administratively shutdown this neighbor.'], 'type': 'bool'}",
    "state": "{'description': ['Determines whether the config should be present or not on the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "suppress_4_byte_as": "{'description': ['Configure to suppress 4-byte AS Capability.'], 'type': 'bool'}",
    "timers_holdtime": "{'description': ["Specify holdtime timer value. Valid values are integers between 0 and 3600 in terms of seconds, or 'default', which is 180."]}",
    "timers_keepalive": "{'description': ["Specify keepalive timer value. Valid values are integers between 0 and 3600 in terms of seconds, or 'default', which is 60."]}",
    "transport_passive_only": "{'description': ["Specify whether or not to only allow passive connection setup. Valid values are 'true', 'false', and 'default', which defaults to 'false'. This property can only be configured when the neighbor is in 'ip' address format without prefix length."], 'type': 'bool'}",
    "update_source": "{'description': ['Specify source interface of BGP session and updates.']}",
    "vrf": "{'description': ["Name of the VRF. The name 'default' is a valid VRF representing the global bgp."], 'default': 'default'}",
}
```

## Examples


``` yaml

# create a new neighbor
- nxos_bgp_neighbor:
    asn: 65535
    neighbor: 192.0.2.3
    local_as: 20
    remote_as: 30
    description: "just a description"
    update_source: Ethernet1/3
    state: present

```

## License

TODO

## Author Information
  - ['Gabriele Gerbino (@GGabriele)']
