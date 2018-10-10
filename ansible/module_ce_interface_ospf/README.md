# Ansible module: ansible.module_ce_interface_ospf


Manages configuration of an OSPF interface instanceon HUAWEI CloudEngine switches

## Description

Manages configuration of an OSPF interface instanceon HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "area": "{'description': ['Ospf area associated with this ospf process. Valid values are a string, formatted as an IP address (i.e. "0.0.0.0") or as an integer between 1 and 4294967295.'], 'required': True}",
    "auth_key_id": "{'description': ["Authentication key id when C(auth_mode) is 'hmac-sha256', 'md5' or 'hmac-md5. Valid value is an integer is in the range from 1 to 255."]}",
    "auth_mode": "{'description': ['Specifies the authentication type.'], 'choices': ['none', 'null', 'hmac-sha256', 'md5', 'hmac-md5', 'simple']}",
    "auth_text_md5": "{'description': ['Specifies a password for MD5, HMAC-MD5, or HMAC-SHA256 authentication. The value is a string of 1 to 255 case-sensitive characters, spaces not supported.']}",
    "auth_text_simple": "{'description': ['Specifies a password for simple authentication. The value is a string of 1 to 8 characters.']}",
    "cost": "{'description': ['The cost associated with this interface. Valid values are an integer in the range from 1 to 65535.']}",
    "dead_interval": "{'description': ['Time interval an ospf neighbor waits for a hello packet before tearing down adjacencies. Valid values are an integer in the range from 1 to 235926000.']}",
    "hello_interval": "{'description': ['Time between sending successive hello packets. Valid values are an integer in the range from 1 to 65535.']}",
    "interface": "{'description': ['Full name of interface, i.e. 40GE1/0/10.'], 'required': True}",
    "process_id": "{'description': ['Specifies a process ID. The value is an integer ranging from 1 to 4294967295.'], 'required': True}",
    "silent_interface": "{'description': ["Setting to true will prevent this interface from receiving HELLO packets. Valid values are 'true' and 'false'."], 'type': 'bool', 'default': False}",
    "state": "{'description': ['Determines whether the config should be present or not on the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: eth_trunk module test
  hosts: cloudengine
  connection: local
  gather_facts: no
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:
  - name: Enables OSPF and sets the cost on an interface
    ce_interface_ospf:
      interface: 10GE1/0/30
      process_id: 1
      area: 100
      cost: 100
      provider: '{{ cli }}'

  - name: Sets the dead interval of the OSPF neighbor
    ce_interface_ospf:
      interface: 10GE1/0/30
      process_id: 1
      area: 100
      dead_interval: 100
      provider: '{{ cli }}'

  - name: Sets the interval for sending Hello packets on an interface
    ce_interface_ospf:
      interface: 10GE1/0/30
      process_id: 1
      area: 100
      hello_interval: 2
      provider: '{{ cli }}'

  - name: Disables an interface from receiving and sending OSPF packets
    ce_interface_ospf:
      interface: 10GE1/0/30
      process_id: 1
      area: 100
      silent_interface: true
      provider: '{{ cli }}'

```

## License

TODO

## Author Information
  - ['QijunPan (@CloudEngine-Ansible)']
