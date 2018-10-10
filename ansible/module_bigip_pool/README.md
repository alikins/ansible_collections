# Ansible module: ansible.module_bigip_pool


Manages F5 BIG-IP LTM pools

## Description

Manages F5 BIG-IP LTM pools via iControl REST API.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['Specifies descriptive text that identifies the pool.'], 'version_added': 2.3}",
    "lb_method": "{'description': ['Load balancing method. When creating a new pool, if this value is not specified, the default of C(round-robin) will be used.'], 'version_added': 1.3, 'choices': ['dynamic-ratio-member', 'dynamic-ratio-node', 'fastest-app-response', 'fastest-node', 'least-connections-member', 'least-connections-node', 'least-sessions', 'observed-member', 'observed-node', 'predictive-member', 'predictive-node', 'ratio-least-connections-member', 'ratio-least-connections-node', 'ratio-member', 'ratio-node', 'ratio-session', 'round-robin', 'weighted-least-connections-member', 'weighted-least-connections-node']}",
    "metadata": "{'description': ['Arbitrary key/value pairs that you can attach to a pool. This is useful in situations where you might want to annotate a pool to me managed by Ansible.', 'Key names will be stored as strings; this includes names that are numbers.', 'Values for all of the keys will be stored as strings; this includes values that are numbers.', 'Data will be persisted, not ephemeral.'], 'version_added': 2.5}",
    "monitor_type": "{'description': ['Monitor rule type when C(monitors) is specified.', "When creating a new pool, if this value is not specified, the default of 'and_list' will be used.", 'When C(single) ensures that all specified monitors are checked, but additionally includes checks to make sure you only specified a single monitor.', 'When C(and_list) ensures that B(all) monitors are checked.', 'When C(m_of_n) ensures that C(quorum) of C(monitors) are checked. C(m_of_n) B(requires) that a C(quorum) of 1 or greater be set either in the playbook, or already existing on the device.', 'Both C(single) and C(and_list) are functionally identical since BIG-IP considers all monitors as "a list".'], 'version_added': 1.3, 'choices': ['and_list', 'm_of_n', 'single']}",
    "monitors": "{'description': ['Monitor template name list. If the partition is not provided as part of the monitor name, then the C(partition) option will be used instead.'], 'version_added': 1.3}",
    "name": "{'description': ['Pool name'], 'required': True, 'aliases': ['pool']}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common', 'version_added': 2.5}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "priority_group_activation": "{'description': ['Specifies whether the system load balances traffic according to the priority number assigned to the pool member.', 'When creating a new pool, if this parameter is not specified, the default of C(0) will be used.', 'To disable this setting, provide the value C(0).', "Once you enable this setting, you can specify pool member priority when you create a new pool or on a pool member's properties screen.", 'The system treats same-priority pool members as a group.', 'To enable priority group activation, provide a number from C(0) to C(65535) that represents the minimum number of members that must be available in one priority group before the system directs traffic to members in a lower priority group.', 'When a sufficient number of members become available in the higher priority group, the system again directs traffic to the higher priority group.'], 'aliases': ['minimum_active_members'], 'version_added': 2.6}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "quorum": "{'description': ['Monitor quorum value when C(monitor_type) is C(m_of_n).', 'Quorum must be a value of 1 or greater when C(monitor_type) is C(m_of_n).'], 'version_added': 1.3}",
    "reselect_tries": "{'description': ['Sets the number of times the system tries to contact a pool member after a passive failure.'], 'version_added': 2.2}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "service_down_action": "{'description': ['Sets the action to take when node goes down in pool.'], 'version_added': 1.3, 'choices': ['none', 'reset', 'drop', 'reselect']}",
    "slow_ramp_time": "{'description': ['Sets the ramp-up time (in seconds) to gradually ramp up the load on newly added or freshly detected up pool members.'], 'version_added': 1.3}",
    "state": "{'description': ['When C(present), guarantees that the pool exists with the provided attributes.', 'When C(absent), removes the pool from the system.'], 'default': 'present', 'choices': ['absent', 'present'], 'version_added': 2.5}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create pool
  bigip_pool:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: present
    name: my-pool
    partition: Common
    lb_method: least-connections-member
    slow_ramp_time: 120
  delegate_to: localhost

- name: Modify load balancer method
  bigip_pool:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: present
    name: my-pool
    partition: Common
    lb_method: round-robin
  delegate_to: localhost

- name: Add pool member
  bigip_pool_member:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: present
    pool: my-pool
    partition: Common
    host: "{{ ansible_default_ipv4['address'] }}"
    port: 80
  delegate_to: localhost

- name: Set a single monitor (with enforcement)
  bigip_pool:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: present
    name: my-pool
    partition: Common
    monitor_type: single
    monitors:
      - http
  delegate_to: localhost

- name: Set a single monitor (without enforcement)
  bigip_pool:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: present
    name: my-pool
    partition: Common
    monitors:
      - http
  delegate_to: localhost

- name: Set multiple monitors (all must succeed)
  bigip_pool:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: present
    name: my-pool
    partition: Common
    monitor_type: and_list
    monitors:
      - http
      - tcp
  delegate_to: localhost

- name: Set multiple monitors (at least 1 must succeed)
  bigip_pool:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: present
    name: my-pool
    partition: Common
    monitor_type: m_of_n
    quorum: 1
    monitors:
      - http
      - tcp
  delegate_to: localhost

- name: Remove pool member from pool
  bigip_pool_member:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: absent
    pool: my-pool
    partition: Common
    host: "{{ ansible_default_ipv4['address'] }}"
    port: 80
  delegate_to: localhost

- name: Delete pool
  bigip_pool:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: absent
    name: my-pool
    partition: Common
  delegate_to: localhost

- name: Add metadata to pool
  bigip_pool:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: absent
    name: my-pool
    partition: Common
    metadata:
      ansible: 2.4
      updated_at: 2017-12-20T17:50:46Z
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)', 'Wojciech Wypior (@wojtek0806)']
  - ['Tim Rupp (@caphrim007)', 'Wojciech Wypior (@wojtek0806)']
