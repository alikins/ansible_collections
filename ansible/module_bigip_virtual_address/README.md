# Ansible module: ansible.module_bigip_virtual_address


Manage LTM virtual addresses on a BIG-IP

## Description

Manage LTM virtual addresses on a BIG-IP.

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'description': ['Virtual address. This value cannot be modified after it is set.', 'If you never created a virtual address, but did create virtual servers, then a virtual address for each virtual server was created automatically. The name of this virtual address is its IP address value.']}",
    "arp": "{'description': ['Specifies whether the system accepts ARP requests.', 'When C(no), specifies that the system does not accept ARP requests.', 'When C(yes), then the packets are dropped.', 'Note that both ARP and ICMP Echo must be disabled in order for forwarding virtual servers using that virtual address to forward ICMP packets.', 'When creating a new virtual address, if this parameter is not specified, the default value is C(yes).'], 'type': 'bool', 'version_added': 2.7}",
    "arp_state": "{'description': ['Specifies whether the system accepts ARP requests. When (disabled), specifies that the system does not accept ARP requests. Note that both ARP and ICMP Echo must be disabled in order for forwarding virtual servers using that virtual address to forward ICMP packets. If (enabled), then the packets are dropped.', 'Deprecated. Use the C(arp) parameter instead.', 'When creating a new virtual address, if this parameter is not specified, the default value is C(enabled).'], 'choices': ['enabled', 'disabled']}",
    "auto_delete": "{'description': ['Specifies whether the system automatically deletes the virtual address with the deletion of the last associated virtual server. When C(disabled), specifies that the system leaves the virtual address even when all associated virtual servers have been deleted. When creating the virtual address, the default value is C(enabled).', 'C(enabled) and C(disabled) are deprecated and will be removed in Ansible 2.11. Instead, use known Ansible booleans such as C(yes) and C(no)']}",
    "availability_calculation": "{'description': ['Specifies what routes of the virtual address the system advertises. When C(when_any_available), advertises the route when any virtual server is available. When C(when_all_available), advertises the route when all virtual servers are available. When (always), always advertises the route regardless of the virtual servers available.'], 'choices': ['always', 'when_all_available', 'when_any_available'], 'aliases': ['advertise_route'], 'version_added': 2.6}",
    "connection_limit": "{'description': ['Specifies the number of concurrent connections that the system allows on this virtual address.']}",
    "icmp_echo": "{'description': ['Specifies how the systems sends responses to (ICMP) echo requests on a per-virtual address basis for enabling route advertisement. When C(enabled), the BIG-IP system intercepts ICMP echo request packets and responds to them directly. When C(disabled), the BIG-IP system passes ICMP echo requests through to the backend servers. When (selective), causes the BIG-IP system to internally enable or disable responses based on virtual server state; C(when_any_available), C(when_all_available, or C(always), regardless of the state of any virtual servers.'], 'choices': ['enabled', 'disabled', 'selective']}",
    "name": "{'description': ['Name of the virtual address.', 'If this parameter is not provided, then the value of C(address) will be used.'], 'version_added': 2.6}",
    "netmask": "{'description': ['Netmask of the provided virtual address. This value cannot be modified after it is set.'], 'default': '255.255.255.255'}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common', 'version_added': 2.5}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "route_advertisement": "{'description': ['Specifies whether the system uses route advertisement for this virtual address.', 'When disabled, the system does not advertise routes for this virtual address.', 'The majority of these options are only supported on versions 13.0.0-HF1 or higher. On versions less than this, all choices expect C(disabled) will translate to C(enabled).', 'When C(always), the BIG-IP system will always advertise the route for the virtual address, regardless of availability status. This requires an C(enabled) virtual address.', 'When C(enabled), the BIG-IP system will advertise the route for the available virtual address, based on the calculation method in the availability calculation.', 'When C(disabled), the BIG-IP system will not advertise the route for the virtual address, regardless of the availability status.', 'When C(selective), you can also selectively enable ICMP echo responses, which causes the BIG-IP system to internally enable or disable responses based on virtual server state. Either C(any) virtual server, C(all) virtual servers, or C(always), regardless of the state of any virtual server.', 'When C(any), the BIG-IP system will advertise the route for the virtual address when any virtual server is available.', 'When C(all), the BIG-IP system will advertise the route for the virtual address when all virtual servers are available.'], 'choices': ['disabled', 'enabled', 'always', 'selective', 'any', 'all'], 'version_added': 2.6}",
    "route_domain": "{'description': ['The route domain of the C(address) that you want to use.', 'This value cannot be modified after it is set.'], 'version_added': 2.6}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "spanning": "{'description': ['Enables all BIG-IP systems in a device group to listen for and process traffic on the same virtual address.', 'Spanning for a virtual address occurs when you enable the C(spanning) option on a device and then sync the virtual address to the other members of the device group.', 'Spanning also relies on the upstream router to distribute application flows to the BIG-IP systems using ECMP routes. ECMP defines a route to the virtual address using distinct Floating self-IP addresses configured on each BIG-IP system.', 'You must also configure MAC masquerade addresses and disable C(arp) on the virtual address when Spanning is enabled.', 'When creating a new virtual address, if this parameter is not specified, the default valus is C(no).'], 'version_added': 2.7, 'type': 'bool'}",
    "state": "{'description': ['The virtual address state. If C(absent), an attempt to delete the virtual address will be made. This will only succeed if this virtual address is not in use by a virtual server. C(present) creates the virtual address and enables it. If C(enabled), enable the virtual address if it exists. If C(disabled), create the virtual address if needed, and set state to C(disabled).'], 'default': 'present', 'choices': ['present', 'absent', 'enabled', 'disabled']}",
    "traffic_group": "{'description': ['The traffic group for the virtual address. When creating a new address, if this value is not specified, the default of C(/Common/traffic-group-1) will be used.'], 'version_added': 2.5}",
    "use_route_advertisement": "{'description': ['Specifies whether the system uses route advertisement for this virtual address.', 'When disabled, the system does not advertise routes for this virtual address.', 'Deprecated. Use the C(route_advertisement) parameter instead.'], 'type': 'bool'}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Add virtual address
  bigip_virtual_address:
    server: lb.mydomain.net
    user: admin
    password: secret
    state: present
    partition: Common
    address: 10.10.10.10
  delegate_to: localhost

- name: Enable route advertisement on the virtual address
  bigip_virtual_address:
    server: lb.mydomain.net
    user: admin
    password: secret
    state: present
    address: 10.10.10.10
    use_route_advertisement: yes
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
