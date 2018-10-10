# Ansible module: ansible.module_bigip_vlan


Manage VLANs on a BIG-IP system

## Description

Manage VLANs on a BIG-IP system

## Requirements

TODO

## Arguments

``` json
{
    "cmp_hash": "{'description': ['Specifies how the traffic on the VLAN will be disaggregated. The value selected determines the traffic disaggregation method. You can choose to disaggregate traffic based on C(source-address) (the source IP address), C(destination-address) (destination IP address), or C(default), which specifies that the default CMP hash uses L4 ports.', 'When creating a new VLAN, if this parameter is not specified, the default of C(default) is used.'], 'choices': ['default', 'destination-address', 'source-address', 'dst-ip', 'src-ip', 'dest', 'destination', 'source', 'dst', 'src'], 'version_added': 2.5}",
    "dag_round_robin": "{'description': ['Specifies whether some of the stateless traffic on the VLAN should be disaggregated in a round-robin order instead of using a static hash. The stateless traffic includes non-IP L2 traffic, ICMP, some UDP protocols, and so on.', 'When creating a new VLAN, if this parameter is not specified, the default of (no) is used.'], 'version_added': 2.5, 'type': 'bool'}",
    "dag_tunnel": "{'description': ['Specifies how the disaggregator (DAG) distributes received tunnel-encapsulated packets to TMM instances. Select C(inner) to distribute packets based on information in inner headers. Select C(outer) to distribute packets based on information in outer headers without inspecting inner headers.', 'When creating a new VLAN, if this parameter is not specified, the default of C(outer) is used.', 'This parameter is not supported on Virtual Editions of BIG-IP.'], 'version_added': 2.5, 'choices': ['inner', 'outer']}",
    "description": "{'description': ['The description to give to the VLAN.']}",
    "mtu": "{'description': ['Specifies the maximum transmission unit (MTU) for traffic on this VLAN. When creating a new VLAN, if this parameter is not specified, the default value used will be C(1500).', 'This number must be between 576 to 9198.'], 'version_added': 2.5}",
    "name": "{'description': ['The VLAN to manage. If the special VLAN C(ALL) is specified with the C(state) value of C(absent) then all VLANs will be removed.'], 'required': True}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common', 'version_added': 2.5}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['The state of the VLAN on the system. When C(present), guarantees that the VLAN exists with the provided attributes. When C(absent), removes the VLAN from the system.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tag": "{'description': ['Tag number for the VLAN. The tag number can be any integer between 1 and 4094. The system automatically assigns a tag number if you do not specify a value.']}",
    "tagged_interfaces": "{'description': ['Specifies a list of tagged interfaces and trunks that you want to configure for the VLAN. Use tagged interfaces or trunks when you want to assign a single interface or trunk to multiple VLANs.'], 'aliases': ['tagged_interface']}",
    "untagged_interfaces": "{'description': ['Specifies a list of untagged interfaces and trunks that you want to configure for the VLAN.'], 'aliases': ['untagged_interface']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create VLAN
  bigip_vlan:
      name: "net1"
      password: "secret"
      server: "lb.mydomain.com"
      user: "admin"
      validate_certs: "no"
  delegate_to: localhost

- name: Set VLAN tag
  bigip_vlan:
      name: "net1"
      password: "secret"
      server: "lb.mydomain.com"
      tag: "2345"
      user: "admin"
      validate_certs: "no"
  delegate_to: localhost

- name: Add VLAN 2345 as tagged to interface 1.1
  bigip_vlan:
      tagged_interface: 1.1
      name: "net1"
      password: "secret"
      server: "lb.mydomain.com"
      tag: "2345"
      user: "admin"
      validate_certs: "no"
  delegate_to: localhost

- name: Add VLAN 1234 as tagged to interfaces 1.1 and 1.2
  bigip_vlan:
      tagged_interfaces:
          - 1.1
          - 1.2
      name: "net1"
      password: "secret"
      server: "lb.mydomain.com"
      tag: "1234"
      user: "admin"
      validate_certs: "no"
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)', 'Wojciech Wypior (@wojtek0806)']
  - ['Tim Rupp (@caphrim007)', 'Wojciech Wypior (@wojtek0806)']
