# Ansible module: ansible.module_junos_package


Installs packages on remote devices running Junos

## Description

This module can install new and updated packages on remote devices running Junos.  The module will compare the specified package with the one running on the remote device and install the specified version if there is a mismatch

## Requirements

TODO

## Arguments

``` json
{
    "force": "{'description': ['The I(force) argument instructs the module to bypass the package version check and install the packaged identified in I(src) on the remote device.'], 'required': True, 'type': 'bool', 'default': False}",
    "no_copy": "{'description': ['The I(no_copy) argument is responsible for instructing the remote device on where to install the package from.  When enabled, the package is transferred to the remote device prior to installing.'], 'type': 'bool', 'default': False}",
    "provider": "{'description': ['B(Deprecated)', 'Starting with Ansible 2.5 we recommend using C(connection: network_cli) or C(connection: netconf).', 'For more information please see the L(Junos OS Platform Options guide, ../network/user_guide/platform_junos.html).', 'HORIZONTALLINE', 'A dict object containing connection details.'], 'suboptions': {'host': {'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}, 'port': {'description': ['Specifies the port to use when building the connection to the remote device.  The port value will default to the well known SSH port of 22 (for C(transport=cli)) or port 830 (for C(transport=netconf)) device.'], 'default': 22}, 'username': {'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}, 'password': {'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.']}}}",
    "reboot": "{'description': ['In order for a package to take effect, the remote device must be restarted.  When enabled, this argument will instruct the module to reboot the device once the updated package has been installed. If disabled or the remote package does not need to be changed, the device will not be started.'], 'required': True, 'type': 'bool', 'default': True}",
    "src": "{'description': ['The I(src) argument specifies the path to the source package to be installed on the remote device in the advent of a version mismatch. The I(src) argument can be either a localized path or a full path to the package file to install.'], 'required': True, 'aliases': ['package']}",
    "validate": "{'description': ['The I(validate) argument is responsible for instructing the remote device to skip checking the current device configuration compatibility with the package being installed. When set to false validation is not performed.'], 'version_added': 2.5, 'type': 'bool', 'default': True}",
    "version": "{'description': ['The I(version) argument can be used to explicitly specify the version of the package that should be installed on the remote device.  If the I(version) argument is not specified, then the version is extracts from the I(src) filename.']}",
}
```

## Examples


``` yaml

# the required set of connection arguments have been purposely left off
# the examples for brevity

- name: install local package on remote device
  junos_package:
    src: junos-vsrx-12.1X46-D10.2-domestic.tgz

- name: install local package on remote device without rebooting
  junos_package:
    src: junos-vsrx-12.1X46-D10.2-domestic.tgz
    reboot: no

```

## License

TODO

## Author Information
  - ['Peter Sprygada (@privateip)']
