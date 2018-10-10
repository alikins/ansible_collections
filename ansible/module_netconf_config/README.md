# Ansible module: ansible.module_netconf_config


netconf device configuration

## Description

Netconf is a network management protocol developed and standardized by the IETF. It is documented in RFC 6241.
This module allows the user to send a configuration XML file to a netconf device, and detects if there was a configuration change.

## Requirements

TODO

## Arguments

``` json
{
    "backup": "{'description': ['This argument will cause the module to create a full backup of the current C(running-config) from the remote device before any changes are made.  The backup file is written to the C(backup) folder in the playbook root directory or role root directory, if playbook is part of an ansible role. If the directory does not exist, it is created.'], 'type': 'bool', 'default': False, 'version_added': '2.7'}",
    "commit": "{'description': ["This boolean flag controls if the configuration changes should be committed or not after editing the candidate datastore. This oprion is supported only if remote Netconf server supports :candidate capability. If the value is set to I(False) commit won't be issued after edit-config operation and user needs to handle commit or discard-changes explicitly."], 'type': 'bool', 'default': True, 'version_added': '2.7'}",
    "confirm": "{'description': ['This argument will configure a timeout value for the commit to be confirmed before it is automatically rolled back. If the C(confirm_commit) argument is set to False, this argument is silently ignored. If the value of this argument is set to 0, the commit is confirmed immediately. The remote host MUST support :candidate and :confirmed-commit capability for this option to .'], 'default': 0, 'version_added': '2.7'}",
    "confirm_commit": "{'description': ['This argument will execute commit operation on remote device. It can be used to confirm a previous commit.'], 'type': 'bool', 'default': False, 'version_added': '2.7'}",
    "content": "{'description': ["The configuration data as defined by the device's data models, the value can be either in xml string format or text format. The format of the configuration should be supported by remote Netconf server"], 'aliases': ['xml']}",
    "default_operation": "{'description': ['The default operation for <edit-config> rpc, valid values are I(merge), I(replace) and I(none). If the default value is merge, the configuration data in the C(content) option is merged at the corresponding level in the C(target) datastore. If the value is replace the data in the C(content) option completely replaces the configuration in the C(target) datastore. If the value is none the C(target) datastore is unaffected by the configuration in the config option, unless and until the incoming configuration data uses the C(operation) operation to request a different operation.'], 'choices': ['merge', 'replace', 'none'], 'version_added': '2.7'}",
    "delete": "{'description': ['It instructs the module to delete the configuration from value mentioned in C(target) datastore.'], 'type': 'bool', 'default': False, 'version_added': '2.7'}",
    "error_option": "{'description': ['This option control the netconf server action after a error is occured while editing the configuration. If the value is I(stop-on-error) abort the config edit on first error, if value is I(continue-on-error) it continues to process configuration data on error, error is recorded and negative response is generated if any errors occur. If value is C(rollback-on-error) it rollback to the original configuration in case any error occurs, this requires the remote Netconf server to support the :rollback-on-error capability.'], 'default': 'stop-on-error', 'choices': ['stop-on-error', 'continue-on-error', 'rollback-on-error'], 'version_added': '2.7'}",
    "format": "{'description': ['The format of the configuration provided as value of C(content). Accepted values are I(xml) and I(text) and the given configuration format should be supported by remote Netconf server.'], 'default': 'xml', 'choices': ['xml', 'text'], 'version_added': '2.7'}",
    "host": "{'description': ['Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host is used as the destination address for the transport.'], 'required': True}",
    "hostkey_verify": "{'description': ['If set to true, the ssh host key of the device must match a ssh key present on the host if false, the ssh host key of the device is not checked.'], 'type': 'bool', 'default': True}",
    "lock": "{'description': ['Instructs the module to explicitly lock the datastore specified as C(target). By setting the option value I(always) is will explicitly lock the datastore mentioned in C(target) option. It the value is I(never) it will not lock the C(target) datastore. The value I(if-supported) lock the C(target) datastore only if it is supported by the remote Netconf server.'], 'default': 'always', 'choices': ['never', 'always', 'if-supported'], 'version_added': '2.7'}",
    "look_for_keys": "{'description': ['Enables looking in the usual locations for the ssh keys (e.g. :file:`~/.ssh/id_*`)'], 'type': 'bool', 'default': True}",
    "password": "{'description': ['Specifies the password to use to authenticate the connection to the remote device.   This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_PASSWORD) will be used instead.']}",
    "port": "{'description': ['Specifies the port to use when building the connection to the remote device.  The port value will default to port 830.'], 'type': 'int', 'default': 830}",
    "save": "{'description': ['The C(save) argument instructs the module to save the configuration in C(target) datastore to the startup-config if changed and if :startup capability is supported by Netconf server.'], 'default': False, 'version_added': '2.4'}",
    "source_datastore": "{'description': ['Name of the configuration datastore to use as the source to copy the configuration to the datastore mentioned by C(target) option. The values can be either I(running), I(candidate), I(startup) or a remote URL'], 'version_added': '2.7', 'aliases': ['source']}",
    "src": "{'description': ['Specifies the source path to the xml file that contains the configuration or configuration template to load. The path to the source file can either be the full path on the Ansible control host or a relative path from the playbook or role root directory. This argument is mutually exclusive with I(xml).'], 'version_added': '2.4'}",
    "ssh_keyfile": "{'description': ['Specifies the SSH key to use to authenticate the connection to the remote device.   This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_SSH_KEYFILE) will be used instead.'], 'type': 'path'}",
    "target": "{'description': ['Name of the configuration datastore to be edited. - auto, uses candidate and fallback to running - candidate, edit <candidate/> datastore and then commit - running, edit <running/> datastore directly'], 'default': 'auto', 'version_added': '2.4', 'aliases': ['datastore']}",
    "timeout": "{'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'type': 'int', 'default': 10}",
    "username": "{'description': ['Configures the username to use to authenticate the connection to the remote device.  This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable C(ANSIBLE_NET_USERNAME) will be used instead.']}",
    "validate": "{'description': ['This boolean flag if set validates the content of datastore given in C(target) option. For this option to work remote Netconf server shoule support :validate capability.'], 'type': 'bool', 'default': False, 'version_added': '2.7'}",
}
```

## Examples


``` yaml

- name: use lookup filter to provide xml configuration
  netconf_config:
    content: "{{ lookup('file', './config.xml') }}"

- name: set ntp server in the device
  netconf_config:
    content: |
        <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
            <system xmlns="urn:ietf:params:xml:ns:yang:ietf-system">
                <ntp>
                    <enabled>true</enabled>
                    <server>
                        <name>ntp1</name>
                        <udp><address>127.0.0.1</address></udp>
                    </server>
                </ntp>
            </system>
        </config>

- name: wipe ntp configuration
  netconf_config:
    content: |
        <config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0">
            <system xmlns="urn:ietf:params:xml:ns:yang:ietf-system">
                <ntp>
                    <enabled>false</enabled>
                    <server operation="remove">
                        <name>ntp1</name>
                    </server>
                </ntp>
            </system>
        </config>

- name: configure interface while providing different private key file path (for connection=netconf)
  netconf_config:
    backup: yes
  register: backup_junos_location
  vars:
    ansible_private_key_file: /home/admin/.ssh/newprivatekeyfile

```

## License

TODO

## Author Information
  - ['Leandro Lisboa Penz (@lpenz)']
