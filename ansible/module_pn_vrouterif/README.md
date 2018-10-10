# Ansible module: ansible.module_pn_vrouterif


CLI command to add/remove/modify vrouter-interface

## Description

Execute vrouter-interface-add, vrouter-interface-remove, vrouter-interface-modify command.
You configure interfaces to vRouter services on a fabric, cluster, standalone switch or virtual network(VNET).

## Requirements

TODO

## Arguments

``` json
{
    "pn_alias": "{'description': ['Specify an alias for the interface.']}",
    "pn_assignment": "{'description': ['Specify the DHCP method for IP address assignment.'], 'choices': ['none', 'dhcp', 'dhcpv6', 'autov6']}",
    "pn_clipassword": "{'description': ['Provide login password if user is not root.'], 'required': False}",
    "pn_cliswitch": "{'description': ['Target switch to run the cli on.'], 'required': False}",
    "pn_cliusername": "{'description': ['Provide login username if user is not root.'], 'required': False}",
    "pn_exclusive": "{'description': ['Specify if the interface is exclusive to the configuration. Exclusive means that other configurations cannot use the interface. Exclusive is specified when you configure the interface as span interface and allows higher throughput through the interface.']}",
    "pn_interface": "{'description': ['Specify if the interface is management, data or span interface.'], 'choices': ['mgmt', 'data', 'span']}",
    "pn_interface_ip": "{'description': ['Specify the IP address of the interface in x.x.x.x/n format.']}",
    "pn_l3port": "{'description': ['Specify a Layer 3 port for the interface.']}",
    "pn_nic_enable": "{'description': ['Specify if the NIC is enabled or not']}",
    "pn_nic_str": "{'description': ['Specify the type of NIC. Used for vrouter-interface remove/modify.']}",
    "pn_secondary_macs": "{'description': ['Specify a secondary MAC address for the interface.']}",
    "pn_vlan": "{'description': ['Specify the VLAN identifier. This is a value between 1 and 4092.']}",
    "pn_vrouter_name": "{'description': ['Specify the name of the vRouter interface.'], 'required': True}",
    "pn_vrrp_adv_int": "{'description': ['Specify a VRRP advertisement interval in milliseconds. The range is from 30 to 40950 with a default value of 1000.']}",
    "pn_vrrp_id": "{'description': ['Specify the ID for the VRRP interface. The IDs on both vRouters must be the same IS number.']}",
    "pn_vrrp_priority": "{'description': ['Specify the priority for the VRRP interface. This is a value between 1 (lowest) and 255 (highest).']}",
    "pn_vxlan": "{'description': ['Specify the VXLAN identifier. This is a value between 1 and 16777215.']}",
    "state": "{'description': ["State the action to perform. Use 'present' to add vrouter interface, 'absent' to remove vrouter interface and 'update' to modify vrouter interface."], 'required': True, 'choices': ['present', 'absent', 'update']}",
}
```

## Examples


``` yaml

- name: Add vrouter-interface
  pn_vrouterif:
    pn_cliusername: admin
    pn_clipassword: admin
    state: 'present'
    pn_vrouter_name: 'ansible-vrouter'
    pn_interface_ip: 101.101.101.2/24
    pn_vlan: 101

- name: Add VRRP..
  pn_vrouterif:
    pn_cliusername: admin
    pn_clipassword: admin
    state: 'present'
    pn_vrouter_name: 'ansible-vrouter'
    pn_interface_ip: 101.101.101.2/24
    pn_vrrp_ip: 101.101.101.1/24
    pn_vrrp_priority: 100
    pn_vlan: 101

- name: Remove vrouter-interface
  pn_vrouterif:
    pn_cliusername: admin
    pn_clipassword: admin
    state: 'absent'
    pn_vrouter_name: 'ansible-vrouter'
    pn_interface_ip: 101.101.101.2/24

```

## License

TODO

## Author Information
  - ['Pluribus Networks (@amitsi)']
