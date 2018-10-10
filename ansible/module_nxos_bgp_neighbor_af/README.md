# Ansible module: ansible.module_nxos_bgp_neighbor_af


Manages BGP address-family's neighbors configuration

## Description

Manages BGP address-family's neighbors configurations on NX-OS switches.

## Requirements

TODO

## Arguments

``` json
{
    "additional_paths_receive": "{'description': ['Valid values are enable for basic command enablement; disable for disabling the command at the neighbor af level (it adds the disable keyword to the basic command); and inherit to remove the command at this level (the command value is inherited from a higher BGP layer).'], 'choices': ['enable', 'disable', 'inherit']}",
    "additional_paths_send": "{'description': ['Valid values are enable for basic command enablement; disable for disabling the command at the neighbor af level (it adds the disable keyword to the basic command); and inherit to remove the command at this level (the command value is inherited from a higher BGP layer).'], 'choices': ['enable', 'disable', 'inherit']}",
    "advertise_map_exist": "{'description': ["Conditional route advertisement. This property requires two route maps, an advertise-map and an exist-map. Valid values are an array specifying both the advertise-map name and the exist-map name, or simply 'default' e.g. ['my_advertise_map', 'my_exist_map']. This command is mutually exclusive with the advertise_map_non_exist property."]}",
    "advertise_map_non_exist": "{'description': ["Conditional route advertisement. This property requires two route maps, an advertise-map and an exist-map. Valid values are an array specifying both the advertise-map name and the non-exist-map name, or simply 'default' e.g. ['my_advertise_map', 'my_non_exist_map']. This command is mutually exclusive with the advertise_map_exist property."]}",
    "afi": "{'description': ['Address Family Identifier.'], 'required': True, 'choices': ['ipv4', 'ipv6', 'vpnv4', 'vpnv6', 'l2vpn']}",
    "allowas_in": "{'description': ['Activate allowas-in property']}",
    "allowas_in_max": "{'description': ["Max-occurrences value for allowas_in. Valid values are an integer value or 'default'. This is mutually exclusive with allowas_in."]}",
    "as_override": "{'description': ['Activate the as-override feature.'], 'type': 'bool'}",
    "asn": "{'description': ['BGP autonomous system number. Valid values are String, Integer in ASPLAIN or ASDOT notation.'], 'required': True}",
    "default_originate": "{'description': ['Activate the default-originate feature.'], 'type': 'bool'}",
    "default_originate_route_map": "{'description': ["Route-map for the default_originate property. Valid values are a string defining a route-map name, or 'default'. This is mutually exclusive with default_originate."]}",
    "disable_peer_as_check": "{'description': ['Disable checking of peer AS-number while advertising'], 'type': 'bool', 'version_added': 2.5}",
    "filter_list_in": "{'description': ["Valid values are a string defining a filter-list name, or 'default'."]}",
    "filter_list_out": "{'description': ["Valid values are a string defining a filter-list name, or 'default'."]}",
    "max_prefix_interval": "{'description': ['Optional restart interval. Valid values are an integer. Requires max_prefix_limit. May not be combined with max_prefix_warning.']}",
    "max_prefix_limit": "{'description': ["maximum-prefix limit value. Valid values are an integer value or 'default'."]}",
    "max_prefix_threshold": "{'description': ['Optional threshold percentage at which to generate a warning. Valid values are an integer value. Requires max_prefix_limit.']}",
    "max_prefix_warning": "{'description': ['Optional warning-only keyword. Requires max_prefix_limit. May not be combined with max_prefix_interval.'], 'type': 'bool'}",
    "neighbor": "{'description': ['Neighbor Identifier. Valid values are string. Neighbors may use IPv4 or IPv6 notation, with or without prefix length.'], 'required': True}",
    "next_hop_self": "{'description': ['Activate the next-hop-self feature.'], 'type': 'bool'}",
    "next_hop_third_party": "{'description': ['Activate the next-hop-third-party feature.'], 'type': 'bool'}",
    "prefix_list_in": "{'description': ["Valid values are a string defining a prefix-list name, or 'default'."]}",
    "prefix_list_out": "{'description': ["Valid values are a string defining a prefix-list name, or 'default'."]}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using NX-API.', 'For more information please see the L(NXOS Platform Options guide, ../network/user_guide/platform_nxos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(nxapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(nxapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False, 'choices': ['yes', 'no'], 'version_added': '2.5.3'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.'], 'default': 'none', 'version_added': '2.5.3'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc).'], 'default': 10, 'version_added': 2.3}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.  This argument is only used for the I(cli) transport. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.  The transport argument supports connectivity to the device over cli (ssh) or nxapi.'], 'required': True, 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=nxapi), otherwise this value is ignored.'], 'type': 'bool', 'default': 'no'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not nxapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "route_map_in": "{'description': ["Valid values are a string defining a route-map name, or 'default'."]}",
    "route_map_out": "{'description': ["Valid values are a string defining a route-map name, or 'default'."]}",
    "route_reflector_client": "{'description': ['Router reflector client.'], 'type': 'bool'}",
    "safi": "{'description': ['Sub Address Family Identifier.'], 'required': True, 'choices': ['unicast', 'multicast', 'evpn']}",
    "send_community": "{'description': ['send-community attribute.'], 'choices': ['none', 'both', 'extended', 'standard', 'default']}",
    "soft_reconfiguration_in": "{'description': ["Valid values are 'enable' for basic command enablement; 'always' to add the always keyword to the basic command; and 'inherit' to remove the command at this level (the command value is inherited from a higher BGP layer)."], 'choices': ['enable', 'always', 'inherit']}",
    "soo": "{'description': ["Site-of-origin. Valid values are a string defining a VPN extcommunity or 'default'."]}",
    "state": "{'description': ['Determines whether the config should be present or not on the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "suppress_inactive": "{'description': ['suppress-inactive feature.'], 'type': 'bool'}",
    "unsuppress_map": "{'description': ["unsuppress-map. Valid values are a string defining a route-map name or 'default'."]}",
    "vrf": "{'description': ["Name of the VRF. The name 'default' is a valid VRF representing the global bgp."], 'default': 'default'}",
    "weight": "{'description': ["Weight value. Valid values are an integer value or 'default'."]}",
}
```

## Examples


``` yaml

- name: configure RR client
  nxos_bgp_neighbor_af:
    asn: 65535
    neighbor: '192.0.2.3'
    afi: ipv4
    safi: unicast
    route_reflector_client: true
    state: present

```

## License

TODO

## Author Information
  - ['Gabriele Gerbino (@GGabriele)']
