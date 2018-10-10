# Ansible module: ansible.module_cnos_interface


Manage interface configuration on devices running Lenovo CNOS

## Description

This module allows you to work with interface related configurations. The operators used are overloaded to ensure control over switch interface configurations. Apart from the regular device connection related attributes, there are seven interface arguments that will perform further configurations. They are interfaceArg1, interfaceArg2, interfaceArg3, interfaceArg4, interfaceArg5, interfaceArg6, and interfaceArg7. For more details on how to use these arguments, see [Overloaded Variables]. Interface configurations are taken care at six contexts in a regular CLI. They are 1. Interface Name - Configurations 2. Ethernet Interface - Configurations 3. Loopback Interface Configurations 4. Management Interface Configurations 5. Port Aggregation - Configurations 6. VLAN Configurations This module uses SSH to manage network device configuration. The results of the operation will be placed in a directory named 'results' that must be created by the user in their local directory to where the playbook is run. For more information about this module from Lenovo and customizing it usage for your use cases, please visit U(http://systemx.lenovofiles.com/help/index.jsp?topic=%2Fcom.lenovo.switchmgt.ansible.doc%2Fcnos_interface.html)

## Requirements

TODO

## Arguments

``` json
{
    "deviceType": "{'description': ['This specifies the type of device where the method is executed. The choices NE1072T,NE1032,NE1032T,NE10032, NE2572 are added since version 2.4'], 'required': True, 'choices': ['g8272_cnos', 'g8296_cnos', 'g8332_cnos', 'NE1072T', 'NE1032', 'NE1032T', 'NE10032', 'NE2572'], 'version_added': 2.3}",
    "enablePassword": "{'description': ['Configures the password used to enter Global Configuration command mode on the switch. If the switch does not request this password, the parameter is ignored.While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used.'], 'version_added': 2.3}",
    "host": "{'description': ['This is the variable used to search the hosts file at /etc/ansible/hosts and identify the IP address of the device on which the template is going to be applied. Usually the Ansible keyword {{ inventory_hostname }} is specified in the playbook as an abstraction of the group of network elements that need to be configured.'], 'required': True, 'version_added': 2.3}",
    "interfaceArg1": "{'description': ['This is an overloaded interface first argument. Usage of this argument can be found is the User Guide referenced above.'], 'required': True, 'default': None, 'choices': ['channel-group', 'bfd', 'switchport', 'description', 'duplex', 'flowcontrol', 'ip', 'ipv6', 'lacp', 'lldp', 'load-interval', 'mac', 'mac-address', 'mac-learn', 'microburst-detection', 'mtu', 'service', 'service-policy', 'shutdown', 'snmp', 'spanning-tree', 'speed', 'storm-control', 'vlan', 'vrrp', 'port-channel']}",
    "interfaceArg2": "{'description': ['This is an overloaded interface second argument. Usage of this argument can be found is the User Guide referenced above.'], 'required': False, 'default': None, 'choices': ['channel-group number', 'access or mode or trunk', 'description', 'auto or full or half', 'receive or send', 'port-priority', 'suspend-individual', 'timeout', 'receive or transmit or trap-notification', 'tlv-select', 'Load interval delay in seconds', 'counter', 'Name for the MAC Access List', 'mac-address in HHHH.HHHH.HHHH format', 'THRESHOLD  Value in unit of buffer cell', '<64-9216>  MTU in bytes-<64-9216> for L2 packet', '<576-9216> for L3 IPv4 packet', '<1280-9216> for L3 IPv6 packet', 'enter the instance id', 'input or output', 'copp-system-policy', 'type', '1000  or  10000  or   40000 or   auto', 'broadcast or multicast or unicast', 'disable or enable or egress-only', 'Virtual router identifier', 'destination-ip or destination-mac or destination-port or source-dest-ip or source-dest-mac or source-dest-port or source-interface or source-ip or source-mac or source-port']}",
    "interfaceArg3": "{'description': ['This is an overloaded interface third argument. Usage of this argument can be found is the User Guide referenced above.'], 'required': False, 'default': None, 'choices': ['active or on or passive', 'on or off', 'LACP port priority', 'long or short', 'link-aggregation or mac-phy-status or management-address or max-frame-size or port-description or port-protocol-vlan or port-vlan or power-mdi or protocol-identity or system-capabilities or system-description or system-name or vid-management or vlan-name', 'counter for load interval', 'policy input name', 'all or Copp class name to attach', 'qos', 'queueing', 'Enter the allowed traffic level', 'ipv6']}",
    "interfaceArg4": "{'description': ['This is an overloaded interface fourth argument. Usage of this argument can be found is the User Guide referenced above.'], 'required': False, 'default': None, 'choices': ['key-chain', 'key-id', 'keyed-md5 or keyed-sha1 or meticulous-keyed-md5 or meticulous-keyed-sha1 or simple', 'Interval value in milliseconds', 'Destination IP (Both IPV4 and IPV6)', 'in or out', 'MAC address', 'Time-out value in seconds', 'class-id', 'request', 'Specify the IPv4 address', 'OSPF area ID as a decimal value', 'OSPF area ID in IP address format', 'anycast or secondary', 'ethernet', 'vlan', 'MAC (hardware) address in HHHH.HHHH.HHHH format', 'Load interval delay in seconds', 'Specify policy input name', 'input or output', 'cost', 'port-priority', 'BFD minimum receive interval', 'source-interface']}",
    "interfaceArg5": "{'description': ['This is an overloaded interface fifth argument. Usage of this argument can be found is the User Guide referenced above.'], 'required': False, 'default': None, 'choices': ['name of key-chain', 'key-Id Value', 'key-chain', 'key-id', 'BFD minimum receive interval', 'Value of Hello Multiplier', 'admin-down or multihop or non-persistent', 'Vendor class-identifier name', 'bootfile-name or host-name or log-server or ntp-server or tftp-server-name', 'Slot/chassis number', 'Vlan interface', 'Specify policy input name', 'Port path cost or auto', 'Port priority increments of 32']}",
    "interfaceArg6": "{'description': ['This is an overloaded interface sixth argument. Usage of this argument can be found is the User Guide referenced above.'], 'required': False, 'default': None, 'choices': ['Authentication key string', 'name of key-chain', 'key-Id Value', 'Value of Hello Multiplier', 'admin-down or non-persistent']}",
    "interfaceArg7": "{'description': ['This is an overloaded interface seventh argument. Usage of this argument can be found is the User Guide referenced above.'], 'required': False, 'default': None, 'choices': ['Authentication key string', 'admin-down']}",
    "interfaceOption": "{'description': ['This specifies the attribute you specify subsequent to interface command'], 'required': True, 'default': None, 'choices': ['None', 'ethernet', 'loopback', 'mgmt', 'port-channel', 'vlan']}",
    "interfaceRange": "{'description': ['This specifies the interface range in which the port channel is envisaged'], 'required': True, 'default': None}",
    "outputfile": "{'description': ['This specifies the file path where the output of each command execution is saved. Each command that is specified in the merged template file and each response from the device are saved here. Usually the location is the results folder, but you can choose another location based on your write permission.'], 'required': True, 'version_added': 2.3}",
    "password": "{'description': ['Configures the password used to authenticate the connection to the remote device. The value of the password parameter is used to authenticate the SSH session. While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used.'], 'required': True, 'version_added': 2.3}",
    "username": "{'description': ['Configures the username used to authenticate the connection to the remote device. The value of the username parameter is used to authenticate the SSH session. While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used.'], 'required': True, 'version_added': 2.3}",
}
```

## Examples


``` yaml

Tasks : The following are examples of using the module cnos_interface. These are written in the main.yml file of the tasks directory.
---
- name: Test Interface Ethernet - channel-group
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 1
      interfaceArg1: "channel-group"
      interfaceArg2: 33
      interfaceArg3: "on"

- name: Test Interface Ethernet - switchport
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 33
      interfaceArg1: "switchport"
      interfaceArg2: "access"
      interfaceArg3: 33

- name: Test Interface Ethernet - switchport mode
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 33
      interfaceArg1: "switchport"
      interfaceArg2: "mode"
      interfaceArg3: "access"

- name: Test Interface Ethernet  - Description
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 33
      interfaceArg1: "description"
      interfaceArg2: "Hentammoo "

- name: Test Interface Ethernet - Duplex
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 1
      interfaceArg1: "duplex"
      interfaceArg2: "auto"

- name: Test Interface Ethernet - flowcontrol
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 33
      interfaceArg1: "flowcontrol"
      interfaceArg2: "send"
      interfaceArg3: "off"

- name: Test Interface Ethernet - lacp
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 33
      interfaceArg1: "lacp"
      interfaceArg2: "port-priority"
      interfaceArg3: 33

- name: Test Interface Ethernet  - lldp
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 33
      interfaceArg1: "lldp"
      interfaceArg2: "tlv-select"
      interfaceArg3: "max-frame-size"

- name: Test Interface Ethernet - load-interval
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 33
      interfaceArg1: "load-interval"
      interfaceArg2: "counter"
      interfaceArg3: 2
      interfaceArg4: 33

- name: Test Interface Ethernet - mac
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 33
      interfaceArg1: "mac"
      interfaceArg2: "copp-system-acl-vlag-hc"

- name: Test Interface Ethernet - microburst-detection
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 33
      interfaceArg1: "microburst-detection"
      interfaceArg2: 25

- name: Test Interface Ethernet  - mtu
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 33
      interfaceArg1: "mtu"
      interfaceArg2: 66

- name: Test Interface Ethernet - service-policy
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 33
      interfaceArg1: "service-policy"
      interfaceArg2: "input"
      interfaceArg3: "Anil"

- name: Test Interface Ethernet - speed
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 1
      interfaceArg1: "speed"
      interfaceArg2: "auto"

- name: Test Interface Ethernet - storm
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 33
      interfaceArg1: "storm-control"
      interfaceArg2: "broadcast"
      interfaceArg3: 12.5

- name: Test Interface Ethernet - vlan
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 33
      interfaceArg1: "vlan"
      interfaceArg2: "disable"

- name: Test Interface Ethernet - vrrp
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 33
      interfaceArg1: "vrrp"
      interfaceArg2: 33

- name: Test Interface Ethernet - spanning tree1
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 33
      interfaceArg1: "spanning-tree"
      interfaceArg2: "bpduguard"
      interfaceArg3: "enable"

- name: Test Interface Ethernet - spanning tree 2
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 33
      interfaceArg1: "spanning-tree"
      interfaceArg2: "mst"
      interfaceArg3: "33-35"
      interfaceArg4: "cost"
      interfaceArg5: 33

- name: Test Interface Ethernet - ip1
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 33
      interfaceArg1: "ip"
      interfaceArg2: "access-group"
      interfaceArg3: "anil"
      interfaceArg4: "in"

- name: Test Interface Ethernet - ip2
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 33
      interfaceArg1: "ip"
      interfaceArg2: "port"
      interfaceArg3: "anil"

- name: Test Interface Ethernet - bfd
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 33
      interfaceArg1: "bfd"
      interfaceArg2: "interval"
      interfaceArg3: 55
      interfaceArg4: 55
      interfaceArg5: 33

- name: Test Interface Ethernet - bfd
  cnos_interface:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_interface_{{ inventory_hostname }}_output.txt"
      interfaceOption: 'ethernet'
      interfaceRange: 33
      interfaceArg1: "bfd"
      interfaceArg2: "ipv4"
      interfaceArg3: "authentication"
      interfaceArg4: "meticulous-keyed-md5"
      interfaceArg5: "key-chain"
      interfaceArg6: "mychain"


```

## License

TODO

## Author Information
  - ['Anil Kumar Muraleedharan (@amuraleedhar)']
