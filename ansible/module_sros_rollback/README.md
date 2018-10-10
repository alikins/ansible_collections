# Ansible module: ansible.module_sros_rollback


Configure Nokia SR OS rollback

## Description

Configure the rollback feature on remote Nokia devices running the SR OS operating system.  this module provides a stateful implementation for managing the configuration of the rollback feature

## Requirements

TODO

## Arguments

``` json
{
    "local_max_checkpoints": "{'description': ['The I(local_max_checkpoints) argument configures the maximum number of rollback files that can be saved on the devices local compact flash.  Valid values for this argument are in the range of 1 to 50']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "remote_max_checkpoints": "{'description': ['The I(remote_max_checkpoints) argument configures the maximum number of rollback files that can be transferred and saved to a remote location.  Valid values for this argument are in the range of 1 to 50']}",
    "rescue_location": "{'description': ['The I(rescue_location) specifies the location of the rescue file.  This argument supports any valid local or remote URL as specified in SR OS']}",
    "rollback_location": "{'description': ['The I(rollback_location) specifies the location and filename of the rollback checkpoint files.   This argument supports any valid local or remote URL as specified in SR OS']}",
    "state": "{'description': ['The I(state) argument specifies the state of the configuration entries in the devices active configuration.  When the state value is set to C(true) the configuration is present in the devices active configuration.  When the state value is set to C(false) the configuration values are removed from the devices active configuration.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

# Note: examples below use the following provider dict to handle
#       transport and authentication to the node.
---
vars:
  cli:
    host: "{{ inventory_hostname }}"
    username: admin
    password: admin
    transport: cli

---
- name: configure rollback location
  sros_rollback:
    rollback_location: "cb3:/ansible"
    provider: "{{ cli }}"

- name: remove all rollback configuration
  sros_rollback:
    state: absent
    provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Peter Sprygada (@privateip)']
