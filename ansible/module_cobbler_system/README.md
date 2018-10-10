# Ansible module: ansible.module_cobbler_system


Manage system objects in Cobbler

## Description

Add, modify or remove systems in Cobbler

## Requirements

TODO

## Arguments

``` json
{
    "host": "{'description': ['The name or IP address of the Cobbler system.'], 'default': '127.0.0.1'}",
    "interfaces": "{'description': ['A list of dictionaries containing interface options.']}",
    "name": "{'description': ['The system name to manage.']}",
    "password": "{'description': ['The password to log in to Cobbler.'], 'required': True}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter C(use_ssl).']}",
    "properties": "{'description': ['A dictionary with system properties.']}",
    "state": "{'description': ['Whether the system should be present, absent or a query is made.'], 'choices': ['absent', 'present', 'query'], 'default': 'present'}",
    "sync": "{'description': ['Sync on changes.', 'Concurrently syncing Cobbler is bound to fail.'], 'type': 'bool', 'default': False}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['The username to log in to Cobbler.'], 'default': 'cobbler'}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only set to C(no) when used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Ensure the system exists in Cobbler
  cobbler_system:
    host: cobbler01
    username: cobbler
    password: MySuperSecureP4sswOrd
    name: myhost
    properties:
      profile: CentOS6-x86_64
      name_servers: [ 2.3.4.5, 3.4.5.6 ]
      name_servers_search: foo.com, bar.com
    interfaces:
      eth0:
        macaddress: 00:01:02:03:04:05
        ipaddress: 1.2.3.4
  delegate_to: localhost

- name: Enable network boot in Cobbler
  cobbler_system:
    host: bdsol-aci-cobbler-01
    username: cobbler
    password: ins3965!
    name: bdsol-aci51-apic1.cisco.com
    properties:
      netboot_enabled: yes
    state: present
  delegate_to: localhost

- name: Query all systems in Cobbler
  cobbler_system:
    host: cobbler01
    username: cobbler
    password: MySuperSecureP4sswOrd
  register: cobbler_systems
  delegate_to: localhost

- name: Query a specific system in Cobbler
  cobbler_system:
    host: cobbler01
    username: cobbler
    password: MySuperSecureP4sswOrd
    name: '{{ inventory_hostname }}'
  register: cobbler_properties
  delegate_to: localhost

- name: Ensure the system does not exist in Cobbler
  cobbler_system:
    host: cobbler01
    username: cobbler
    password: MySuperSecureP4sswOrd
    name: myhost
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)']
