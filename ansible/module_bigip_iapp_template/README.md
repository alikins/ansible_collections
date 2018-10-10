# Ansible module: ansible.module_bigip_iapp_template


Manages TCL iApp templates on a BIG-IP

## Description

Manages TCL iApp templates on a BIG-IP. This module will allow you to deploy iApp templates to the BIG-IP and manage their lifecycle. The conventional way to use this module is to import new iApps as needed or by extracting the contents of the iApp archive that is provided at downloads.f5.com and then importing all the iApps with this module. This module can also update existing iApps provided that the source of the iApp changed while the name stayed the same. Note however that this module will not reconfigure any services that may have been created using the C(bigip_iapp_service) module. iApps are normally not updated in production. Instead, new versions are deployed and then existing services are changed to consume that new template. As such, the ability to update templates in-place requires the C(force) option to be used.

## Requirements

TODO

## Arguments

``` json
{
    "content": "{'description': ['Sets the contents of an iApp template directly to the specified value. This is for simple values, but can be used with lookup plugins for anything complex or with formatting. C(content) must be provided when creating new templates.']}",
    "force": "{'description': ['Specifies whether or not to force the uploading of an iApp. When C(yes), will force update the iApp even if there are iApp services using it. This will not update the running service though. Use C(bigip_iapp_service) to do that. When C(no), will update the iApp only if there are no iApp services using the template.'], 'type': 'bool'}",
    "name": "{'description': ['The name of the iApp template that you want to delete. This option is only available when specifying a C(state) of C(absent) and is provided as a way to delete templates that you may no longer have the source of.']}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['Whether the iApp template should exist or not.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Add the iApp contained in template iapp.tmpl
  bigip_iapp_template:
    content: "{{ lookup('template', 'iapp.tmpl') }}"
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

- name: Update a template in place
  bigip_iapp_template:
    content: "{{ lookup('template', 'iapp-new.tmpl') }}"
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

- name: Update a template in place that has existing services created from it.
  bigip_iapp_template:
    content: "{{ lookup('template', 'iapp-new.tmpl') }}"
    force: yes
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
