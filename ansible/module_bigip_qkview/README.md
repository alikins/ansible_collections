# Ansible module: ansible.module_bigip_qkview


Manage qkviews on the device

## Description

Manages creating and downloading qkviews from a BIG-IP. Various options can be provided when creating qkviews. The qkview is important when dealing with F5 support. It may be required that you upload this qkview to the supported channels during resolution of an SRs that you may have opened.

## Requirements

TODO

## Arguments

``` json
{
    "asm_request_log": "{'description': ['When C(True), includes the ASM request log data. When C(False), excludes the ASM request log data.'], 'default': False, 'type': 'bool'}",
    "complete_information": "{'description': ['Include complete information in the qkview.'], 'default': False, 'type': 'bool'}",
    "dest": "{'description': ['Destination on your local filesystem when you want to save the qkview.'], 'required': True}",
    "exclude": "{'description': ['Exclude various file from the qkview.'], 'choices': ['all', 'audit', 'secure', 'bash_history']}",
    "exclude_core": "{'description': ['Exclude core files from the qkview.'], 'default': False, 'type': 'bool'}",
    "filename": "{'description': ['Name of the qkview to create on the remote BIG-IP.'], 'default': 'localhost.localdomain.qkview'}",
    "force": "{'description': ['If C(no), the file will only be transferred if the destination does not exist.'], 'default': True, 'type': 'bool'}",
    "max_file_size": "{'description': ['Max file size, in bytes, of the qkview to create. By default, no max file size is specified.'], 'default': 0}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Fetch a qkview from the remote device
  bigip_qkview:
    asm_request_log: yes
    exclude:
      - audit
      - secure
    dest: /tmp/localhost.localdomain.qkview
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
