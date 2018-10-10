# Ansible module: ansible.module_bigip_firewall_port_list


Manage port lists on BIG-IP AFM

## Description

Manages the AFM port lists on a BIG-IP. This module can be used to add and remove port list entries.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['Description of the port list']}",
    "name": "{'description': ['Specifies the name of the port list.'], 'required': True}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "port_lists": "{'description': ['Simple list of existing port lists to add to this list. Port lists can be specified in either their fully qualified name (/Common/foo) or their short name (foo). If a short name is used, the C(partition) argument will automatically be prepended to the short name.']}",
    "port_ranges": "{'description': ['A list of port ranges where the range starts with a port number, is followed by a dash (-) and then a second number.', 'If the first number is greater than the second number, the numbers will be reversed so-as to be properly formatted. ie, 90-78 would become 78-90.']}",
    "ports": "{'description': ['Simple list of port values to add to the list']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present), ensures that the address list and entries exists.', 'When C(absent), ensures the address list is removed.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create a simple port list
  bigip_firewall_port_list:
    name: foo
    ports:
      - 80
      - 443
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

- name: Override the above list of ports with a new list
  bigip_firewall_port_list:
    name: foo
    ports:
      - 3389
      - 8080
      - 25
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

- name: Create port list with series of ranges
  bigip_firewall_port_list:
    name: foo
    port_ranges:
      - 25-30
      - 80-500
      - 50-78
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

- name: Use multiple types of port arguments
  bigip_firewall_port_list:
    name: foo
    port_ranges:
      - 25-30
      - 80-500
      - 50-78
    ports:
      - 8080
      - 443
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

- name: Remove port list
  bigip_firewall_port_list:
    name: foo
    password: secret
    server: lb.mydomain.com
    state: absent
    user: admin
  delegate_to: localhost

- name: Create port list from a file with one port per line
  bigip_firewall_port_list:
    name: lot-of-ports
    ports: "{{ lookup('file', 'my-large-port-list.txt').split('\n') }}"
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
