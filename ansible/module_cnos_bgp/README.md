# Ansible module: ansible.module_cnos_bgp


Manage BGP resources and attributes on devices running CNOS

## Description

This module allows you to work with Border Gateway Protocol (BGP) related configurations. The operators used are overloaded to ensure control over switch BGP configurations. This module is invoked using method with asNumber as one of its arguments. The first level of the BGP configuration allows to set up an AS number, with the following attributes going into various configuration operations under the context of BGP. After passing this level, there are eight BGP arguments that will perform further configurations. They are bgpArg1, bgpArg2, bgpArg3, bgpArg4, bgpArg5, bgpArg6, bgpArg7, and bgpArg8. For more details on how to use these arguments, see [Overloaded Variables]. This module uses SSH to manage network device configuration. The results of the operation will be placed in a directory named 'results' that must be created by the user in their local directory to where the playbook is run. For more information about this module from Lenovo and customizing it usage for your use cases, please visit U(http://systemx.lenovofiles.com/help/index.jsp?topic=%2Fcom.lenovo.switchmgt.ansible.doc%2Fcnos_bgp.html)

## Requirements

TODO

## Arguments

``` json
{
    "asNum": "{'description': ['AS number'], 'required': True, 'default': None}",
    "bgpArg1": "{'description': ['This is an overloaded bgp first argument. Usage of this argument can be found is the User Guide referenced above.'], 'required': True, 'default': None, 'choices': ['address-family', 'bestpath', 'bgp', 'cluster-id', 'confederation', 'enforce-first-as', 'fast-external-failover', 'graceful-restart', 'graceful-restart-helper', 'log-neighbor-changes', 'maxas-limit', 'neighbor', 'router-id', 'shutdown', 'synchronization', 'timers', 'vrf']}",
    "bgpArg2": "{'description': ['This is an overloaded bgp second argument. Usage of this argument can be found is the User Guide referenced above.'], 'required': False, 'default': None, 'choices': ['ipv4 or ipv6', 'always-compare-med', 'compare-confed-aspath', 'compare-routerid', 'dont-compare-originator-id', 'tie-break-on-age', 'as-path', 'med', 'identifier', 'peers']}",
    "bgpArg3": "{'description': ['This is an overloaded bgp third argument. Usage of this argument can be found is the User Guide referenced above.'], 'required': False, 'default': None, 'choices': ['aggregate-address', 'client-to-client', 'dampening', 'distance', 'maximum-paths', 'network', 'nexthop', 'redistribute', 'save', 'synchronization', 'ignore or multipath-relax', 'confed or missing-as-worst or non-deterministic or remove-recv-med or remove-send-med']}",
    "bgpArg4": "{'description': ['This is an overloaded bgp fourth argument. Usage of this argument can be found is the User Guide referenced above.'], 'required': False, 'default': None, 'choices': ['Aggregate prefix', 'Reachability Half-life time', 'route-map', 'Distance for routes ext', 'ebgp or ibgp', 'IP prefix <network>', 'IP prefix <network>/<length>', 'synchronization', 'Delay value', 'direct', 'ospf', 'static', 'memory']}",
    "bgpArg5": "{'description': ['This is an overloaded bgp fifth argument. Usage of this argument can be found is the User Guide referenced above.'], 'required': False, 'default': None, 'choices': ['as-set', 'summary-only', 'Value to start reusing a route', 'Distance for routes internal', 'Supported multipath numbers', 'backdoor', 'map', 'route-map']}",
    "bgpArg6": "{'description': ['This is an overloaded bgp sixth argument. Usage of this argument can be found is the User Guide referenced above.'], 'required': False, 'default': None, 'choices': ['summary-only', 'as-set', 'route-map name', 'Value to start suppressing a route', 'Distance local routes', 'Network mask', 'Pointer to route-map entries']}",
    "bgpArg7": "{'description': ['This is an overloaded bgp seventh argument. Use of this argument can be found is the User Guide referenced above.'], 'required': False, 'default': None, 'choices': ['Maximum duration to suppress a stable route(minutes)', 'backdoor', 'route-map', 'Name of the route map']}",
    "bgpArg8": "{'description': ['This is an overloaded bgp eigth argument. Usage of this argument can be found is the User Guide referenced above.'], 'required': False, 'default': None, 'choices': ['Un-reachability Half-life time for the penalty(minutes)', 'backdoor']}",
    "deviceType": "{'description': ['This specifies the type of device where the method is executed. The choices NE1072T,NE1032,NE1032T,NE10032, NE2572 are added since version 2.4'], 'required': True, 'choices': ['g8272_cnos', 'g8296_cnos', 'g8332_cnos', 'NE1072T', 'NE1032', 'NE1032T', 'NE10032', 'NE2572'], 'version_added': 2.3}",
    "enablePassword": "{'description': ['Configures the password used to enter Global Configuration command mode on the switch. If the switch does not request this password, the parameter is ignored.While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used.'], 'version_added': 2.3}",
    "host": "{'description': ['This is the variable used to search the hosts file at /etc/ansible/hosts and identify the IP address of the device on which the template is going to be applied. Usually the Ansible keyword {{ inventory_hostname }} is specified in the playbook as an abstraction of the group of network elements that need to be configured.'], 'required': True, 'version_added': 2.3}",
    "outputfile": "{'description': ['This specifies the file path where the output of each command execution is saved. Each command that is specified in the merged template file and each response from the device are saved here. Usually the location is the results folder, but you can choose another location based on your write permission.'], 'required': True, 'version_added': 2.3}",
    "password": "{'description': ['Configures the password used to authenticate the connection to the remote device. The value of the password parameter is used to authenticate the SSH session. While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used.'], 'required': True, 'version_added': 2.3}",
    "username": "{'description': ['Configures the username used to authenticate the connection to the remote device. The value of the username parameter is used to authenticate the SSH session. While generally the value should come from the inventory file, you can also specify it as a variable. This parameter is optional. If it is not specified, no default value will be used.'], 'required': True, 'version_added': 2.3}",
}
```

## Examples


``` yaml

Tasks: The following are examples of using the module cnos_bgp. These are
 written in the main.yml file of the tasks directory.
---
- name: Test BGP  - neighbor
  cnos_bgp:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "neighbor"
      bgpArg2: "10.241.107.40"
      bgpArg3: 13
      bgpArg4: "address-family"
      bgpArg5: "ipv4"
      bgpArg6: "next-hop-self"

- name: Test BGP  - BFD
  cnos_bgp:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "neighbor"
      bgpArg2: "10.241.107.40"
      bgpArg3: 13
      bgpArg4: "bfd"

- name: Test BGP  - address-family - dampening
  cnos_bgp:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "address-family"
      bgpArg2: "ipv4"
      bgpArg3: "dampening"
      bgpArg4: 13
      bgpArg5: 233
      bgpArg6: 333
      bgpArg7: 15
      bgpArg8: 33

- name: Test BGP  - address-family - network
  cnos_bgp:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "address-family"
      bgpArg2: "ipv4"
      bgpArg3: "network"
      bgpArg4: "1.2.3.4/5"
      bgpArg5: "backdoor"

- name: Test BGP - bestpath - always-compare-med
  cnos_bgp:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "bestpath"
      bgpArg2: "always-compare-med"

- name: Test BGP - bestpath-compare-confed-aspat
  cnos_bgp:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "bestpath"
      bgpArg2: "compare-confed-aspath"

- name: Test BGP - bgp
  cnos_bgp:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "bgp"
      bgpArg2: 33

- name: Test BGP  - cluster-id
  cnos_bgp:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "cluster-id"
      bgpArg2: "1.2.3.4"

- name: Test BGP - confederation-identifier
  cnos_bgp:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "confederation"
      bgpArg2: "identifier"
      bgpArg3: 333

- name: Test BGP - enforce-first-as
  cnos_bgp:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "enforce-first-as"

- name: Test BGP - fast-external-failover
  cnos_bgp:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "fast-external-failover"

- name: Test BGP  - graceful-restart
  cnos_bgp:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "graceful-restart"
      bgpArg2: 333

- name: Test BGP - graceful-restart-helper
  cnos_bgp:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "graceful-restart-helper"

- name: Test BGP - maxas-limit
  cnos_bgp:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "maxas-limit"
      bgpArg2: 333

- name: Test BGP  - neighbor
  cnos_bgp:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "neighbor"
      bgpArg2: "10.241.107.40"
      bgpArg3: 13
      bgpArg4: "address-family"
      bgpArg5: "ipv4"
      bgpArg6: "next-hop-self"

- name: Test BGP - router-id
  cnos_bgp:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "router-id"
      bgpArg2: "1.2.3.4"

- name: Test BGP - synchronization
  cnos_bgp:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "synchronization"

- name: Test BGP - timers
  cnos_bgp:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "timers"
      bgpArg2: 333
      bgpArg3: 3333

- name: Test BGP - vrf
  cnos_bgp:
      host: "{{ inventory_hostname }}"
      username: "{{ hostvars[inventory_hostname]['ansible_ssh_user'] }}"
      password: "{{ hostvars[inventory_hostname]['ansible_ssh_pass'] }}"
      deviceType: "{{ hostvars[inventory_hostname]['deviceType'] }}"
      enablePassword: "{{ hostvars[inventory_hostname]['enablePassword'] }}"
      outputfile: "./results/test_bgp_{{ inventory_hostname }}_output.txt"
      asNum: 33
      bgpArg1: "vrf"


```

## License

TODO

## Author Information
  - ['Anil Kumar Muraleedharan (@amuraleedhar)']
