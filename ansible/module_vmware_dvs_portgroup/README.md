# Ansible module: ansible.module_vmware_dvs_portgroup


Create or remove a Distributed vSwitch portgroup

## Description

Create or remove a Distributed vSwitch portgroup.

## Requirements

TODO

## Arguments

``` json
{
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "network_policy": "{'description': ['Dictionary which configures the different security values for portgroup.', 'Valid attributes are:', '- C(promiscuous) (bool): indicates whether promiscuous mode is allowed. (default: false)', '- C(forged_transmits) (bool): indicates whether forged transmits are allowed. (default: false)', '- C(mac_changes) (bool): indicates whether mac changes are allowed. (default: false)'], 'required': False, 'version_added': '2.5', 'default': {'promiscuous': False, 'forged_transmits': False, 'mac_changes': False}}",
    "num_ports": "{'description': ['The number of ports the portgroup should contain.'], 'required': True}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "port_policy": "{'description': ['Dictionary which configures the advanced policy settings for the portgroup.', 'Valid attributes are:', '- C(block_override) (bool): indicates if the block policy can be changed per port. (default: true)', '- C(ipfix_override) (bool): indicates if the ipfix policy can be changed per port. (default: false)', '- C(live_port_move) (bool): indicates if a live port can be moved in or out of the portgroup. (default: false)', '- C(network_rp_override) (bool): indicates if the network resource pool can be changed per port. (default: false)', '- C(port_config_reset_at_disconnect) (bool): indicates if the configuration of a port is reset automatically after disconnect. (default: true)', '- C(security_override) (bool): indicates if the security policy can be changed per port. (default: false)', '- C(shaping_override) (bool): indicates if the shaping policy can be changed per port. (default: false)', '- C(traffic_filter_override) (bool): indicates if the traffic filter can be changed per port. (default: false)', '- C(uplink_teaming_override) (bool): indicates if the uplink teaming policy can be changed per port. (default: false)', '- C(vendor_config_override) (bool): indicates if the vendor config can be changed per port. (default: false)', '- C(vlan_override) (bool): indicates if the vlan can be changed per port. (default: false)'], 'required': False, 'version_added': '2.5', 'default': {'traffic_filter_override': False, 'network_rp_override': False, 'live_port_move': False, 'security_override': False, 'vendor_config_override': False, 'port_config_reset_at_disconnect': True, 'uplink_teaming_override': False, 'block_override': True, 'shaping_override': False, 'vlan_override': False, 'ipfix_override': False}}",
    "portgroup_name": "{'description': ['The name of the portgroup that is to be created or deleted.'], 'required': True}",
    "portgroup_type": "{'description': ['See VMware KB 1022312 regarding portgroup types.'], 'required': True, 'choices': ['earlyBinding', 'lateBinding', 'ephemeral']}",
    "state": "{'description': ['Determines if the portgroup should be present or not.'], 'required': True, 'type': 'bool', 'choices': ['present', 'absent'], 'version_added': '2.5'}",
    "switch_name": "{'description': ['The name of the distributed vSwitch the port group should be created on.'], 'required': True}",
    "teaming_policy": "{'description': ['Dictionary which configures the different teaming values for portgroup.', 'Valid attributes are:', '- C(load_balance_policy) (string): Network adapter teaming policy. (default: loadbalance_srcid)', '   - choices: [ loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, loadbalance_loadbased, failover_explicit]', '   - "loadbalance_loadbased" is available from version 2.6 and onwards', '- C(inbound_policy) (bool): Indicate whether or not the teaming policy is applied to inbound frames as well. (default: False)', '- C(notify_switches) (bool): Indicate whether or not to notify the physical switch if a link fails. (default: True)', '- C(rolling_order) (bool): Indicate whether or not to use a rolling policy when restoring links. (default: False)'], 'required': False, 'version_added': '2.5', 'default': {'notify_switches': True, 'load_balance_policy': 'loadbalance_srcid', 'inbound_policy': False, 'rolling_order': False}}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
    "vlan_id": "{'description': ['The VLAN ID that should be configured with the portgroup, use 0 for no VLAN.', 'If C(vlan_trunk) is configured to be I(true), this can be a range, example: 1-4094.'], 'required': True}",
    "vlan_trunk": "{'description': ['Indicates whether this is a VLAN trunk or not.'], 'required': False, 'default': False, 'type': 'bool', 'version_added': '2.5'}",
}
```

## Examples


``` yaml

- name: Create vlan portgroup
  vmware_dvs_portgroup:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    portgroup_name: vlan-123-portrgoup
    switch_name: dvSwitch
    vlan_id: 123
    num_ports: 120
    portgroup_type: earlyBinding
    state: present
  delegate_to: localhost

- name: Create vlan trunk portgroup
  vmware_dvs_portgroup:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    portgroup_name: vlan-trunk-portrgoup
    switch_name: dvSwitch
    vlan_id: 1-1000
    vlan_trunk: True
    num_ports: 120
    portgroup_type: earlyBinding
    state: present
  delegate_to: localhost

- name: Create no-vlan portgroup
  vmware_dvs_portgroup:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    portgroup_name: no-vlan-portrgoup
    switch_name: dvSwitch
    vlan_id: 0
    num_ports: 120
    portgroup_type: earlyBinding
    state: present
  delegate_to: localhost

- name: Create vlan portgroup with all security and port policies
  vmware_dvs_portgroup:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    portgroup_name: vlan-123-portrgoup
    switch_name: dvSwitch
    vlan_id: 123
    num_ports: 120
    portgroup_type: earlyBinding
    state: present
    network_policy:
      promiscuous: yes
      forged_transmits: yes
      mac_changes: yes
    port_policy:
      block_override: yes
      ipfix_override: yes
      live_port_move: yes
      network_rp_override: yes
      port_config_reset_at_disconnect: yes
      security_override: yes
      shaping_override: yes
      traffic_filter_override: yes
      uplink_teaming_override: yes
      vendor_config_override: yes
      vlan_override: yes
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Joseph Callen (@jcpowermac)', 'Philippe Dellaert (@pdellaert) <philippe@dellaert.org>']
  - ['Joseph Callen (@jcpowermac)', 'Philippe Dellaert (@pdellaert) <philippe@dellaert.org>']
