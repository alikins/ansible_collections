# Ansible module: ansible.module_bigip_ucs


Manage upload, installation and removal of UCS files

## Description

Manage upload, installation and removal of UCS files.

## Requirements

TODO

## Arguments

``` json
{
    "force": "{'description': ['If C(yes) will upload the file every time and replace the file on the device. If C(no), the file will only be uploaded if it does not already exist. Generally should be C(yes) only in cases where you have reason to believe that the image was corrupted during upload.'], 'type': 'bool', 'default': False}",
    "include_chassis_level_config": "{'description': ['During restore of the UCS file, include chassis level configuration that is shared among boot volume sets. For example, cluster default configuration.'], 'type': 'bool'}",
    "no_license": "{'description': ['Performs a full restore of the UCS file and all the files it contains, with the exception of the license file. The option must be used to restore a UCS on RMA devices (Returned Materials Authorization).'], 'type': 'bool'}",
    "no_platform_check": "{'description': ['Bypasses the platform check and allows a UCS that was created using a different platform to be installed. By default (without this option), a UCS created from a different platform is not allowed to be installed.'], 'type': 'bool'}",
    "passphrase": "{'description': ['Specifies the passphrase that is necessary to load the specified UCS file.'], 'type': 'bool'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "reset_trust": "{'description': ['When specified, the device and trust domain certs and keys are not loaded from the UCS. Instead, a new set is regenerated.'], 'type': 'bool'}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(installed), ensures that the UCS is uploaded and installed, on the system. When C(present), ensures that the UCS is uploaded. When C(absent), the UCS will be removed from the system. When C(installed), the uploading of the UCS is idempotent, however the installation of that configuration is not idempotent.'], 'default': 'present', 'choices': ['absent', 'installed', 'present']}",
    "ucs": "{'description': ['The path to the UCS file to install. The parameter must be provided if the C(state) is either C(installed) or C(activated). When C(state) is C(absent), the full path for this parameter will be ignored and only the filename will be used to select a UCS for removal. Therefore you could specify C(/mickey/mouse/test.ucs) and this module would only look for C(test.ucs).']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Upload UCS
  bigip_ucs:
    server: lb.mydomain.com
    user: admin
    password: secret
    ucs: /root/bigip.localhost.localdomain.ucs
    state: present
  delegate_to: localhost

- name: Install (upload, install) UCS.
  bigip_ucs:
    server: lb.mydomain.com
    user: admin
    password: secret
    ucs: /root/bigip.localhost.localdomain.ucs
    state: installed
  delegate_to: localhost

- name: Install (upload, install) UCS without installing the license portion
  bigip_ucs:
    server: lb.mydomain.com
    user: admin
    password: secret
    ucs: /root/bigip.localhost.localdomain.ucs
    state: installed
    no_license: yes
  delegate_to: localhost

- name: Install (upload, install) UCS except the license, and bypassing the platform check
  bigip_ucs:
    server: lb.mydomain.com
    user: admin
    password: secret
    ucs: /root/bigip.localhost.localdomain.ucs
    state: installed
    no_license: yes
    no_platform_check: yes
  delegate_to: localhost

- name: Install (upload, install) UCS using a passphrase necessary to load the UCS
  bigip_ucs:
    server: lb.mydomain.com
    user: admin
    password: secret
    ucs: /root/bigip.localhost.localdomain.ucs
    state: installed
    passphrase: MyPassphrase1234
  delegate_to: localhost

- name: Remove uploaded UCS file
  bigip_ucs:
    server: lb.mydomain.com
    user: admin
    password: secret
    ucs: bigip.localhost.localdomain.ucs
    state: absent
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
