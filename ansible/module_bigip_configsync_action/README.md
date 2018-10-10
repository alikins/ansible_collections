# Ansible module: ansible.module_bigip_configsync_action


Perform different actions related to config-sync

## Description

Allows one to run different config-sync actions. These actions allow you to manually sync your configuration across multiple BIG-IPs when those devices are in an HA pair.

## Requirements

TODO

## Arguments

``` json
{
    "device_group": "{'description': ['The device group that you want to perform config-sync actions on.'], 'required': True}",
    "overwrite_config": "{'description': ['Indicates that the sync operation overwrites the configuration on the target.'], 'default': False, 'type': 'bool'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "sync_device_to_group": "{'description': ['Specifies that the system synchronizes configuration data from this device to other members of the device group. In this case, the device will do a "push" to all the other devices in the group. This option is mutually exclusive with the C(sync_group_to_device) option.'], 'type': 'bool'}",
    "sync_most_recent_to_device": "{'description': ['Specifies that the system synchronizes configuration data from the device with the most recent configuration. In this case, the device will do a "pull" from the most recently updated device. This option is mutually exclusive with the C(sync_device_to_group) options.'], 'type': 'bool'}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Sync configuration from device to group
  bigip_configsync_action:
    device_group: foo-group
    sync_device_to_group: yes
    server: lb.mydomain.com
    user: admin
    password: secret
    validate_certs: no
  delegate_to: localhost

- name: Sync configuration from most recent device to the current host
  bigip_configsync_action:
    device_group: foo-group
    sync_most_recent_to_device: yes
    server: lb.mydomain.com
    user: admin
    password: secret
    validate_certs: no
  delegate_to: localhost

- name: Perform an initial sync of a device to a new device group
  bigip_configsync_action:
    device_group: new-device-group
    sync_device_to_group: yes
    server: lb.mydomain.com
    user: admin
    password: secret
    validate_certs: no
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
