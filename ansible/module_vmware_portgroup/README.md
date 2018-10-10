# Ansible module: ansible.module_vmware_portgroup


Create a VMware portgroup

## Description

Create a VMware portgroup on given host/s or hosts of given cluster

## Requirements

TODO

## Arguments

``` json
{
    "cluster_name": "{'description': ['Name of cluster name for host membership.', 'Portgroup will be created on all hosts of the given cluster.', 'This option is required if C(hosts) is not specified.'], 'version_added': '2.5'}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "hosts": "{'description': ['List of name of host or hosts on which portgroup needs to be added.', 'This option is required if C(cluster_name) is not specified.'], 'aliases': ['esxi_hostname'], 'version_added': '2.5'}",
    "network_policy": "{'description': ['Network policy specifies layer 2 security settings for a portgroup such as promiscuous mode, where guest adapter listens to all the packets, MAC address changes and forged transmits.', 'Dict which configures the different security values for portgroup.', 'Valid attributes are:', '- C(promiscuous_mode) (bool): indicates whether promiscuous mode is allowed. (default: false)', '- C(forged_transmits) (bool): indicates whether forged transmits are allowed. (default: false)', '- C(mac_changes) (bool): indicates whether mac changes are allowed. (default: false)'], 'required': False, 'version_added': '2.2', 'default': {'mac_changes': False, 'promiscuous_mode': False, 'forged_transmits': False}}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "portgroup_name": "{'description': ['Portgroup name to add.'], 'required': True}",
    "state": "{'description': ['Determines if the portgroup should be present or not.'], 'choices': ['present', 'absent'], 'version_added': '2.5', 'default': 'present'}",
    "switch_name": "{'description': ['vSwitch to modify.'], 'required': True}",
    "teaming_policy": "{'description': ['Dictionary which configures the different teaming values for portgroup.', 'Valid attributes are:', '- C(load_balance_policy) (string): Network adapter teaming policy. (default: loadbalance_srcid)', '   - choices: [ loadbalance_ip, loadbalance_srcmac, loadbalance_srcid, failover_explicit ]', '- C(inbound_policy) (bool): Indicate whether or not the teaming policy is applied to inbound frames as well. (default: False)', '- C(notify_switches) (bool): Indicate whether or not to notify the physical switch if a link fails. (default: True)', '- C(rolling_order) (bool): Indicate whether or not to use a rolling policy when restoring links. (default: False)'], 'required': False, 'version_added': '2.6', 'default': {'notify_switches': True, 'load_balance_policy': 'loadbalance_srcid', 'inbound_policy': False, 'rolling_order': False}}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
    "vlan_id": "{'description': ['VLAN ID to assign to portgroup.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Add Management Network VM Portgroup
  vmware_portgroup:
    hostname: "{{ esxi_hostname }}"
    username: "{{ esxi_username }}"
    password: "{{ esxi_password }}"
    switch_name: "{{ vswitch_name }}"
    portgroup_name: "{{ portgroup_name }}"
    vlan_id: "{{ vlan_id }}"
  delegate_to: localhost

- name: Add Portgroup with Promiscuous Mode Enabled
  vmware_portgroup:
    hostname: "{{ esxi_hostname }}"
    username: "{{ esxi_username }}"
    password: "{{ esxi_password }}"
    switch_name: "{{ vswitch_name }}"
    portgroup_name: "{{ portgroup_name }}"
    network_policy:
        promiscuous_mode: True
  delegate_to: localhost

- name: Add Management Network VM Portgroup to specific hosts
  vmware_portgroup:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    hosts: [esxi_hostname_one]
    switch_name: "{{ vswitch_name }}"
    portgroup_name: "{{ portgroup_name }}"
    vlan_id: "{{ vlan_id }}"
  delegate_to: localhost

- name: Add Management Network VM Portgroup to all hosts in a cluster
  vmware_portgroup:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    cluster_name: "{{ cluster_name }}"
    switch_name: "{{ vswitch_name }}"
    portgroup_name: "{{ portgroup_name }}"
    vlan_id: "{{ vlan_id }}"
  delegate_to: localhost

- name: Remove Management Network VM Portgroup to all hosts in a cluster
  vmware_portgroup:
    hostname: "{{ vcenter_hostname }}"
    username: "{{ vcenter_username }}"
    password: "{{ vcenter_password }}"
    cluster_name: "{{ cluster_name }}"
    switch_name: "{{ vswitch_name }}"
    portgroup_name: "{{ portgroup_name }}"
    vlan_id: "{{ vlan_id }}"
    state: absent
  delegate_to: localhost

- name: Add Portgroup with teaming policy
  vmware_portgroup:
    hostname: "{{ esxi_hostname }}"
    username: "{{ esxi_username }}"
    password: "{{ esxi_password }}"
    switch_name: "{{ vswitch_name }}"
    portgroup_name: "{{ portgroup_name }}"
    teaming_policy:
      load_balance_policy: 'failover_explicit'
      inbound_policy: True
  delegate_to: localhost
  register: teaming_result

```

## License

TODO

## Author Information
  - ['Joseph Callen (@jcpowermac)', 'Russell Teague (@mtnbikenc)', 'Abhijeet Kasurde (@Akasurde) <akasurde@redhat.com>']
  - ['Joseph Callen (@jcpowermac)', 'Russell Teague (@mtnbikenc)', 'Abhijeet Kasurde (@Akasurde) <akasurde@redhat.com>']
  - ['Joseph Callen (@jcpowermac)', 'Russell Teague (@mtnbikenc)', 'Abhijeet Kasurde (@Akasurde) <akasurde@redhat.com>']
