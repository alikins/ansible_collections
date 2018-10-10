# Ansible module: ansible.module_bigip_device_connectivity


Manages device IP configuration settings for HA on a BIG-IP

## Description

Manages device IP configuration settings for HA on a BIG-IP. Each BIG-IP device has synchronization and failover connectivity information (IP addresses) that you define as part of HA pairing or clustering. This module allows you to configure that information.

## Requirements

TODO

## Arguments

``` json
{
    "cluster_mirroring": "{'description': ['Specifies whether mirroring occurs within the same cluster or between different clusters on a multi-bladed system.', 'This parameter is only supported on platforms that have multiple blades, such as Viprion hardware. It is not supported on VE.'], 'choices': ['between-clusters', 'within-cluster'], 'version_added': 2.7}",
    "config_sync_ip": "{'description': ['Local IP address that the system uses for ConfigSync operations.']}",
    "failover_multicast": "{'description': ["When C(yes), ensures that the Failover Multicast configuration is enabled and if no further multicast configuration is provided, ensures that C(multicast_interface), C(multicast_address) and C(multicast_port) are the defaults specified in each option's description. When C(no), ensures that Failover Multicast configuration is disabled."], 'type': 'bool'}",
    "mirror_primary_address": "{'description': ['Specifies the primary IP address for the system to use to mirror connections.']}",
    "mirror_secondary_address": "{'description': ['Specifies the secondary IP address for the system to use to mirror connections.']}",
    "multicast_address": "{'description': ['IP address for the system to send multicast messages associated with failover. When C(failover_multicast) is C(yes) and this option is not provided, a default of C(224.0.0.245) will be used.']}",
    "multicast_interface": "{'description': ['Interface over which the system sends multicast messages associated with failover. When C(failover_multicast) is C(yes) and this option is not provided, a default of C(eth0) will be used.']}",
    "multicast_port": "{'description': ['Port for the system to send multicast messages associated with failover. When C(failover_multicast) is C(yes) and this option is not provided, a default of C(62960) will be used. This value must be between 0 and 65535.']}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "unicast_failover": "{'description': ["Desired addresses to use for failover operations. Options C(address) and C(port) are supported with dictionary structure where C(address) is the local IP address that the system uses for failover operations. Port specifies the port that the system uses for failover operations. If C(port) is not specified, the default value C(1026) will be used.  If you are specifying the (recommended) management IP address, use 'management-ip' in the address field."]}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Configure device connectivity for standard HA pair
  bigip_device_connectivity:
    config_sync_ip: 10.1.30.1
    mirror_primary_address: 10.1.30.1
    unicast_failover:
      - address: management-ip
      - address: 10.1.30.1
    server: lb.mydomain.com
    user: admin
    password: secret
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
