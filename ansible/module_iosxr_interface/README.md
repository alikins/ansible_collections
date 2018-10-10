# Ansible module: ansible.module_iosxr_interface


Manage Interface on Cisco IOS XR network devices

## Description

This module provides declarative management of Interfaces on Cisco IOS XR network devices.

## Requirements

TODO

## Arguments

``` json
{
    "active": "{'description': ['Whether the interface is C(active) or C(preconfigured). Preconfiguration allows you to configure modular services cards before they are inserted into the router. When the cards are inserted, they are instantly configured. Active cards are the ones already inserted.'], 'choices': ['active', 'preconfigure'], 'default': 'active', 'version_added': 2.5}",
    "aggregate": "{'description': ['List of Interface definitions. Include multiple interface configurations together, one each on a separate line']}",
    "delay": "{'description': ['Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are I(state) with values C(up)/C(down), I(tx_rate) and I(rx_rate).'], 'default': 10}",
    "description": "{'description': ['Description of Interface being configured.']}",
    "duplex": "{'description': ['Configures the interface duplex mode. Default is auto-negotiation when not configured.'], 'choices': ['full', 'half']}",
    "enabled": "{'description': ['Removes the shutdown configuration, which removes the forced administrative down on the interface, enabling it to move to an up or down state.'], 'type': 'bool', 'default': True}",
    "mtu": "{'description': ["Sets the MTU value for the interface. Range is between 64 and 65535'"]}",
    "name": "{'description': ['Name of the interface to configure in C(type + path) format. e.g. C(GigabitEthernet0/0/0/0)'], 'required': True}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli).', 'For more information please see the L(Network Guide, ../network/getting_started/network_differences.html#multiple-communication-protocols).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "rx_rate": "{'description': ['Receiver rate in bits per second (bps).', 'This is state check parameter only.', 'Supports conditionals, see L(Conditionals in Networking Modules,../network/user_guide/network_working_with_command_output.html)']}",
    "speed": "{'description': ['Configure the speed for an interface. Default is auto-negotiation when not configured.'], 'choices': ['10', '100', '1000']}",
    "state": "{'description': ['State of the Interface configuration, C(up) means present and operationally up and C(down) means present and operationally C(down)'], 'default': 'present', 'choices': ['present', 'absent', 'up', 'down']}",
    "tx_rate": "{'description': ['Transmit rate in bits per second (bps).', 'This is state check parameter only.', 'Supports conditionals, see L(Conditionals in Networking Modules,../network/user_guide/network_working_with_command_output.html)']}",
}
```

## Examples


``` yaml

- name: configure interface
  iosxr_interface:
      name: GigabitEthernet0/0/0/2
      description: test-interface
      speed: 100
      duplex: half
      mtu: 512

- name: remove interface
  iosxr_interface:
    name: GigabitEthernet0/0/0/2
    state: absent

- name: make interface up
  iosxr_interface:
    name: GigabitEthernet0/0/0/2
    enabled: True

- name: make interface down
  iosxr_interface:
    name: GigabitEthernet0/0/0/2
    enabled: False

- name: Create interface using aggregate
  iosxr_interface:
    aggregate:
    - name: GigabitEthernet0/0/0/3
    - name: GigabitEthernet0/0/0/2
    speed: 100
    duplex: full
    mtu: 512
    state: present

- name: Create interface using aggregate along with additional params in aggregate
  iosxr_interface:
    aggregate:
    - { name: GigabitEthernet0/0/0/3, description: test-interface 3 }
    - { name: GigabitEthernet0/0/0/2, description: test-interface 2 }
    speed: 100
    duplex: full
    mtu: 512
    state: present

- name: Delete interface using aggregate
  iosxr_interface:
    aggregate:
    - name: GigabitEthernet0/0/0/3
    - name: GigabitEthernet0/0/0/2
    state: absent

- name: Check intent arguments
  iosxr_interface:
    name: GigabitEthernet0/0/0/5
    state: up
    delay: 20

- name: Config + intent
  iosxr_interface:
    name: GigabitEthernet0/0/0/5
    enabled: False
    state: down
    delay: 20

```

## License

TODO

## Author Information
  - ['Ganesh Nalawade (@ganeshrn)', 'Kedar Kekan (@kedarX)']
  - ['Ganesh Nalawade (@ganeshrn)', 'Kedar Kekan (@kedarX)']
