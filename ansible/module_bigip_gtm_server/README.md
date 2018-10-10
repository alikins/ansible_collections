# Ansible module: ansible.module_bigip_gtm_server


Manages F5 BIG-IP GTM servers

## Description

Manage BIG-IP server configuration. This module is able to manipulate the server definitions in a BIG-IP.

## Requirements

TODO

## Arguments

``` json
{
    "datacenter": "{'description': ['Data center the server belongs to. When creating a new GTM server, this value is required.']}",
    "devices": "{'description': ['Lists the self IP addresses and translations for each device. When creating a new GTM server, this value is required. This list is a complex list that specifies a number of keys.', 'The C(name) key specifies a name for the device. The device name must be unique per server. This key is required.', 'The C(address) key contains an IP address, or list of IP addresses, for the destination server. This key is required.', 'The C(translation) key contains an IP address to translate the C(address) value above to. This key is optional.', "Specifying duplicate C(name) fields is a supported means of providing device addresses. In this scenario, the addresses will be assigned to the C(name)'s list of addresses."]}",
    "iquery_options": "{'description': ['Specifies whether the Global Traffic Manager uses this BIG-IP system to conduct a variety of probes before delegating traffic to it.'], 'suboptions': {'allow_path': {'description': ['Specifies that the system verifies the logical network route between a data center server and a local DNS server.'], 'type': 'bool'}, 'allow_service_check': {'description': ['Specifies that the system verifies that an application on a server is running, by remotely running the application using an external service checker program.'], 'type': 'bool'}, 'allow_snmp': {'description': ['Specifies that the system checks the performance of a server running an SNMP agent.'], 'type': 'bool'}}, 'version_added': 2.7}",
    "link_discovery": "{'description': ['Specifies whether the system auto-discovers the links for this server. When creating a new GTM server, if this parameter is not specified, the default value C(disabled) is used.', 'If you set this parameter to C(enabled) or C(enabled-no-delete), you must also ensure that the C(virtual_server_discovery) parameter is also set to C(enabled) or C(enabled-no-delete).'], 'choices': ['enabled', 'disabled', 'enabled-no-delete']}",
    "name": "{'description': ['The name of the server.'], 'required': True}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common', 'version_added': 2.5}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "server_type": "{'description': ['Specifies the server type. The server type determines the metrics that the system can collect from the server. When creating a new GTM server, the default value C(bigip) is used.'], 'choices': ['alteon-ace-director', 'cisco-css', 'cisco-server-load-balancer', 'generic-host', 'radware-wsd', 'windows-nt-4.0', 'bigip', 'cisco-local-director-v2', 'extreme', 'generic-load-balancer', 'sun-solaris', 'cacheflow', 'cisco-local-director-v3', 'foundry-server-iron', 'netapp', 'windows-2000-server'], 'aliases': ['product']}",
    "state": "{'description': ['The server state. If C(absent), an attempt to delete the server will be made. This will only succeed if this server is not in use by a virtual server. C(present) creates the server and enables it. If C(enabled), enable the server if it exists. If C(disabled), create the server if needed, and set state to C(disabled).'], 'default': 'present', 'choices': ['present', 'absent', 'enabled', 'disabled']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
    "virtual_server_discovery": "{'description': ['Specifies whether the system auto-discovers the virtual servers for this server. When creating a new GTM server, if this parameter is not specified, the default value C(disabled) is used.'], 'choices': ['enabled', 'disabled', 'enabled-no-delete']}",
}
```

## Examples


``` yaml

- name: Create server "GTM_Server"
  bigip_gtm_server:
    server: lb.mydomain.com
    user: admin
    password: secret
    name: GTM_Server
    datacenter: /Common/New York
    server_type: bigip
    link_discovery: disabled
    virtual_server_discovery: disabled
    devices:
      - {'name': 'server_1', 'address': '1.1.1.1'}
      - {'name': 'server_2', 'address': '2.2.2.1', 'translation':'192.168.2.1'}
      - {'name': 'server_2', 'address': '2.2.2.2'}
      - {'name': 'server_3', 'addresses': [{'address':'3.3.3.1'},{'address':'3.3.3.2'}]}
      - {'name': 'server_4', 'addresses': [{'address':'4.4.4.1','translation':'192.168.14.1'}, {'address':'4.4.4.2'}]}
  delegate_to: localhost

- name: Create server "GTM_Server" with expanded keys
  bigip_gtm_server:
    server: lb.mydomain.com
    user: admin
    password: secret
    name: GTM_Server
    datacenter: /Common/New York
    server_type: bigip
    link_discovery: disabled
    virtual_server_discovery: disabled
    devices:
      - name: server_1
        address: 1.1.1.1
      - name: server_2
        address: 2.2.2.1
        translation: 192.168.2.1
      - name: server_2
        address: 2.2.2.2
      - name: server_3
        addresses:
          - address: 3.3.3.1
          - address: 3.3.3.2
      - name: server_4
        addresses:
          - address: 4.4.4.1
            translation: 192.168.14.1
          - address: 4.4.4.2
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Robert Teller', 'Tim Rupp (@caphrim007)']
  - ['Robert Teller', 'Tim Rupp (@caphrim007)']
