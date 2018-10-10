# Ansible module: ansible.module_bigip_device_group


Manage device groups on a BIG-IP

## Description

Managing device groups allows you to create HA pairs and clusters of BIG-IP devices. Usage of this module should be done in conjunction with the C(bigip_configsync_actions) to sync configuration across the pair or cluster if auto-sync is disabled.

## Requirements

TODO

## Arguments

``` json
{
    "auto_sync": "{'description': ['Indicates whether configuration synchronization occurs manually or automatically.', 'When creating a new device group, this option will default to C(no).'], 'type': 'bool'}",
    "description": "{'description': ['Description of the device group.']}",
    "full_sync": "{'description': ['Specifies whether the system synchronizes the entire configuration during synchronization operations.', 'When C(no), the system performs incremental synchronization operations, based on the cache size specified in C(max_incremental_sync_size).', "Incremental configuration synchronization is a mechanism for synchronizing a device-group's configuration among its members, without requiring a full configuration load for each configuration change.", 'In order for this to work, all devices in the device-group must initially agree on the configuration. Typically this requires at least one full configuration load to each device.', 'When creating a new device group, this option will default to C(no).'], 'type': 'bool'}",
    "max_incremental_sync_size": "{'description': ['Specifies the size of the changes cache for incremental sync.', 'For example, using the default, if you make more than 1024 KB worth of incremental changes, the system performs a full synchronization operation.', 'Using incremental synchronization operations can reduce the per-device sync/load time for configuration changes.', 'This setting is relevant only when C(full_sync) is C(no).']}",
    "name": "{'description': ['Specifies the name of the device group.'], 'required': True}",
    "network_failover": "{'description': ['Indicates whether failover occurs over the network or is hard-wired.', "This parameter is only valid for C(type)'s that are C(sync-failover)."], 'type': 'bool', 'version_added': 2.7}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "save_on_auto_sync": "{'description': ['When performing an auto-sync, specifies whether the configuration will be saved or not.', 'When C(no), only the running configuration will be changed on the device(s) being synced to.', 'When creating a new device group, this option will default to C(no).'], 'type': 'bool'}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(state) is C(present), ensures the device group exists.', 'When C(state) is C(absent), ensures that the device group is removed.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "type": "{'description': ['Specifies that the type of group.', 'A C(sync-failover) device group contains devices that synchronize their configuration data and fail over to one another when a device becomes unavailable.', 'A C(sync-only) device group has no such failover. When creating a new device group, this option will default to C(sync-only).', 'This setting cannot be changed once it has been set.'], 'choices': ['sync-failover', 'sync-only']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create a sync-only device group
  bigip_device_group:
    name: foo-group
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

- name: Create a sync-only device group with auto-sync enabled
  bigip_device_group:
    name: foo-group
    auto_sync: yes
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
