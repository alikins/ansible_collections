# Ansible module: ansible.module_bigip_trunk


Manage trunks on a BIG-IP

## Description

Manages trunks on a BIG-IP.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['Description of the trunk.'], 'version_added': 2.7}",
    "frame_distribution_hash": "{'description': ['Specifies the basis for the hash that the system uses as the frame distribution algorithm. The system uses the resulting hash to determine which interface to use for forwarding traffic.', 'When creating a new trunk, if this parameter is not specified, the default is C(source-destination-ip).', 'When C(source-destination-mac), specifies that the system bases the hash on the combined MAC addresses of the source and the destination.', 'When C(destination-mac), specifies that the system bases the hash on the MAC address of the destination.', 'When C(source-destination-ip), specifies that the system bases the hash on the combined IP addresses of the source and the destination.'], 'choices': ['destination-mac', 'source-destination-ip', 'source-destination-mac']}",
    "interfaces": "{'description': ['The interfaces that are part of the trunk.', 'To clear the list of interfaces, specify an empty list.']}",
    "lacp_enabled": "{'description': ['When C(yes), specifies that the system supports the link aggregation control protocol (LACP), which monitors the trunk by exchanging control packets over the member links to determine the health of the links.', 'If LACP detects a failure in a member link, it removes the link from the link aggregation.', 'When creating a new trunk, if this parameter is not specified, LACP is C(no).', 'LACP is disabled by default for backward compatibility. If this does not apply to your network, we recommend that you enable LACP.'], 'type': 'bool'}",
    "lacp_mode": "{'description': ['Specifies the operation mode for link aggregation control protocol (LACP), if LACP is enabled for the trunk.', 'When creating a new trunk, if this parameter is not specified, the default is C(active).', 'When C(active), specifies that the system periodically sends control packets regardless of whether the partner system has issued a request.', 'When C(passive), specifies that the system sends control packets only when the partner system has issued a request.'], 'choices': ['active', 'passive']}",
    "lacp_timeout": "{'description': ['Specifies the rate at which the system sends the LACP control packets.', 'When creating a new trunk, if this parameter is not specified, the default is C(long).', 'When C(long), specifies that the system sends an LACP control packet every 30 seconds.', 'When C(short), specifies that the system sends an LACP control packet every 1 seconds.'], 'choices': ['long', 'short']}",
    "link_selection_policy": "{'description': ['Specifies, once the trunk is configured, the policy that the trunk uses to determine which member link (interface) can handle new traffic.', 'When creating a new trunk, if this value is not specific, the default is C(auto).', 'When C(auto), specifies that the system automatically determines which interfaces can handle new traffic. For the C(auto) option, the member links must all be the same media type and speed.', "When C(maximum-bandwidth), specifies that the system determines which interfaces can handle new traffic based on the members' maximum bandwidth."], 'choices': ['auto', 'maximum-bandwidth']}",
    "name": "{'description': ['Specifies the name of the trunk.'], 'required': True}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "qinq_ethertype": "{'description': ['Specifies the ether-type value used for the packets handled on this trunk when it is a member in a QinQ vlan.', 'The ether-type can be set to any string containing a valid hexadecimal 16 bits number, or any of the well known ether-types; C(0x8100), C(0x9100), C(0x88a8).', 'This parameter is not supported on Virtual Editions.', 'You should always wrap this value in quotes to prevent Ansible from interpreting the value as a literal hexadecimal number and converting it to an integer.'], 'version_added': 2.7}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present), ensures that the resource exists.', 'When C(absent), ensures the resource is removed.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create a trunk on hardware
  bigip_trunk:
    name: trunk1
    interfaces:
      - 1.1
      - 1.2
    link_selection_policy: maximum-bandwidth
    frame_distribution_hash: destination-mac
    lacp_enabled: yes
    lacp_mode: passive
    lacp_timeout: short
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
