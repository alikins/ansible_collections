# Ansible module: ansible.module_nxos_bgp_af


Manages BGP Address-family configuration

## Description

Manages BGP Address-family configurations on NX-OS switches.

## Requirements

TODO

## Arguments

``` json
{
    "additional_paths_install": "{'description': ['Install a backup path into the forwarding table and provide prefix independent convergence (PIC) in case of a PE-CE link failure.'], 'type': 'bool'}",
    "additional_paths_receive": "{'description': ['Enables the receive capability of additional paths for all of the neighbors under this address family for which the capability has not been disabled.'], 'type': 'bool'}",
    "additional_paths_selection": "{'description': ['Configures the capability of selecting additional paths for a prefix. Valid values are a string defining the name of the route-map.']}",
    "additional_paths_send": "{'description': ['Enables the send capability of additional paths for all of the neighbors under this address family for which the capability has not been disabled.'], 'type': 'bool'}",
    "advertise_l2vpn_evpn": "{'description': ['Advertise evpn routes.'], 'type': 'bool'}",
    "afi": "{'description': ['Address Family Identifier.'], 'required': True, 'choices': ['ipv4', 'ipv6', 'vpnv4', 'vpnv6', 'l2vpn']}",
    "asn": "{'description': ['BGP autonomous system number. Valid values are String, Integer in ASPLAIN or ASDOT notation.'], 'required': True}",
    "client_to_client": "{'description': ['Configure client-to-client route reflection.'], 'type': 'bool'}",
    "dampen_igp_metric": "{'description': ["Specify dampen value for IGP metric-related changes, in seconds. Valid values are integer and keyword 'default'."]}",
    "dampening_half_time": "{'description': ["Specify decay half-life in minutes for route-flap dampening. Valid values are integer and keyword 'default'."]}",
    "dampening_max_suppress_time": "{'description': ["Specify max suppress time for route-flap dampening stable route. Valid values are integer and keyword 'default'."]}",
    "dampening_reuse_time": "{'description': ["Specify route reuse time for route-flap dampening. Valid values are integer and keyword 'default'."]}",
    "dampening_routemap": "{'description': ['Specify route-map for route-flap dampening. Valid values are a string defining the name of the route-map.']}",
    "dampening_state": "{'description': ['Enable/disable route-flap dampening.'], 'type': 'bool'}",
    "dampening_suppress_time": "{'description': ["Specify route suppress time for route-flap dampening. Valid values are integer and keyword 'default'."]}",
    "default_information_originate": "{'description': ['Default information originate.'], 'type': 'bool'}",
    "default_metric": "{'description': ["Sets default metrics for routes redistributed into BGP. Valid values are Integer or keyword 'default'"]}",
    "distance_ebgp": "{'description': ["Sets the administrative distance for eBGP routes. Valid values are Integer or keyword 'default'."]}",
    "distance_ibgp": "{'description': ["Sets the administrative distance for iBGP routes. Valid values are Integer or keyword 'default'."]}",
    "distance_local": "{'description': ["Sets the administrative distance for local BGP routes. Valid values are Integer or keyword 'default'."]}",
    "inject_map": "{'description': ["An array of route-map names which will specify prefixes to inject. Each array entry must first specify the inject-map name, secondly an exist-map name, and optionally the copy-attributes keyword which indicates that attributes should be copied from the aggregate. For example [['lax_inject_map', 'lax_exist_map'], ['nyc_inject_map', 'nyc_exist_map', 'copy-attributes'], ['fsd_inject_map', 'fsd_exist_map']]."]}",
    "maximum_paths": "{'description': ['Configures the maximum number of equal-cost paths for load sharing. Valid value is an integer in the range 1-64.']}",
    "maximum_paths_ibgp": "{'description': ['Configures the maximum number of ibgp equal-cost paths for load sharing. Valid value is an integer in the range 1-64.']}",
    "networks": "{'description': ["Networks to configure. Valid value is a list of network prefixes to advertise. The list must be in the form of an array. Each entry in the array must include a prefix address and an optional route-map. For example [['10.0.0.0/16', 'routemap_LA'], ['192.168.1.1', 'Chicago'], ['192.168.2.0/24'], ['192.168.3.0/24', 'routemap_NYC']]."]}",
    "next_hop_route_map": "{'description': ['Configure a route-map for valid nexthops. Valid values are a string defining the name of the route-map.']}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'This option is only required if you are using NX-API.', 'For more information please see the L(NXOS Platform Options guide, ../network/user_guide/platform_nxos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  This value applies to either I(cli) or I(nxapi).  The port value will default to the appropriate transport common port if none is provided in the task.  (cli=22, http=80, https=443).'], 'default': '0 (use common port)'}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.  This is a common argument used for either I(cli) or I(nxapi) transports. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'authorize': {'description': ['Instructs the module to enter privileged mode on the remote device before sending any commands.  If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTHORIZE) will be used instead.'], 'type': 'bool', 'default': False, 'choices': ['yes', 'no'], 'version_added': '2.5.3'}, 'auth_pass': {'description': ['Specifies the password to use if required to enter privileged mode on the remote device.  If I(authorize) is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_AUTH_PASS) will be used instead.'], 'default': 'none', 'version_added': '2.5.3'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc).'], 'default': 10, 'version_added': 2.3}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.  This argument is only used for the I(cli) transport. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.  The transport argument supports connectivity to the device over cli (ssh) or nxapi.'], 'required': True, 'default': 'cli'}, 'use_ssl': {'description': ['Configures the I(transport) to use SSL if set to true only when the C(transport=nxapi), otherwise this value is ignored.'], 'type': 'bool', 'default': 'no'}, 'validate_certs': {'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  If the transport argument is not nxapi, this value is ignored.'], 'type': 'bool'}, 'use_proxy': {'description': ['If C(no), the environment variables C(http_proxy) and C(https_proxy) will be ignored.'], 'type': 'bool', 'default': 'yes', 'version_added': '2.5'}}}",
    "redistribute": "{'description': ["A list of redistribute directives. Multiple redistribute entries are allowed. The list must be in the form of a nested array. the first entry of each array defines the source-protocol to redistribute from; the second entry defines a route-map name. A route-map is highly advised but may be optional on some platforms, in which case it may be omitted from the array list. For example [['direct', 'rm_direct'], ['lisp', 'rm_lisp']]."]}",
    "safi": "{'description': ['Sub Address Family Identifier.'], 'required': True, 'choices': ['unicast', 'multicast', 'evpn']}",
    "state": "{'description': ['Determines whether the config should be present or not on the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "suppress_inactive": "{'description': ['Advertises only active routes to peers.'], 'type': 'bool'}",
    "table_map": "{'description': ['Apply table-map to filter routes downloaded into URIB. Valid values are a string.']}",
    "table_map_filter": "{'description': ['Filters routes rejected by the route-map and does not download them to the RIB.'], 'type': 'bool'}",
    "vrf": "{'description': ["Name of the VRF. The name 'default' is a valid VRF representing the global bgp."], 'required': True}",
}
```

## Examples


``` yaml

# configure a simple address-family
- nxos_bgp_af:
    asn: 65535
    vrf: TESTING
    afi: ipv4
    safi: unicast
    advertise_l2vpn_evpn: true
    state: present

```

## License

TODO

## Author Information
  - ['Gabriele Gerbino (@GGabriele)']
