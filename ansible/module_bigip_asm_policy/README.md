# Ansible module: ansible.module_bigip_asm_policy


Manage BIG-IP ASM policies

## Description

Manage BIG-IP ASM policies.

## Requirements

TODO

## Arguments

``` json
{
    "active": "{'description': ['If C(yes) will apply and activate existing inactive policy. If C(no), it will deactivate existing active policy. Generally should be C(yes) only in cases where you want to activate new or existing policy.'], 'default': False, 'type': 'bool'}",
    "file": "{'description': ['Full path to a policy file to be imported into the BIG-IP ASM.', 'Policy files exported from newer versions of BIG-IP cannot be imported into older versions of BIG-IP. The opposite, however, is true; you can import older into newer.']}",
    "name": "{'description': ['The ASM policy to manage or create.'], 'required': True}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(state) is C(present), and C(file) or C(template) parameter is provided, new ASM policy is imported and created with the given C(name).', 'When C(state) is present and no C(file) or C(template) parameter is provided new blank ASM policy is created with the given C(name).', 'When C(state) is C(absent), ensures that the policy is removed, even if it is currently active.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "template": "{'description': ['An ASM policy built-in template. If the template does not exist we will raise an error.', 'Once the policy has been created, this value cannot change.', 'The C(Comprehensive), C(Drupal), C(Fundamental), C(Joomla), C(Vulnerability Assessment Baseline), and C(Wordpress) templates are only available on BIG-IP versions >= 13.'], 'choices': ['ActiveSync v1.0 v2.0 (http)', 'ActiveSync v1.0 v2.0 (https)', 'Comprehensive', 'Drupal', 'Fundamental', 'Joomla', 'LotusDomino 6.5 (http)', 'LotusDomino 6.5 (https)', 'OWA Exchange 2003 (http)', 'OWA Exchange 2003 (https)', 'OWA Exchange 2003 with ActiveSync (http)', 'OWA Exchange 2003 with ActiveSync (https)', 'OWA Exchange 2007 (http)', 'OWA Exchange 2007 (https)', 'OWA Exchange 2007 with ActiveSync (http)', 'OWA Exchange 2007 with ActiveSync (https)', 'OWA Exchange 2010 (http)', 'OWA Exchange 2010 (https)', 'Oracle 10g Portal (http)', 'Oracle 10g Portal (https)', 'Oracle Applications 11i (http)', 'Oracle Applications 11i (https)', 'PeopleSoft Portal 9 (http)', 'PeopleSoft Portal 9 (https)', 'Rapid Deployment Policy', 'SAP NetWeaver 7 (http)', 'SAP NetWeaver 7 (https)', 'SharePoint 2003 (http)', 'SharePoint 2003 (https)', 'SharePoint 2007 (http)', 'SharePoint 2007 (https)', 'SharePoint 2010 (http)', 'SharePoint 2010 (https)', 'Vulnerability Assessment Baseline', 'Wordpress']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Import and activate ASM policy
  bigip_asm_policy:
    server: lb.mydomain.com
    user: admin
    password: secret
    name: new_asm_policy
    file: /root/asm_policy.xml
    active: yes
    state: present
  delegate_to: localhost

- name: Import ASM policy from template
  bigip_asm_policy:
    server: lb.mydomain.com
    user: admin
    password: secret
    name: new_sharepoint_policy
    template: SharePoint 2007 (http)
    state: present
  delegate_to: localhost

- name: Create blank ASM policy
  bigip_asm_policy:
    server: lb.mydomain.com
    user: admin
    password: secret
    name: new_blank_policy
    state: present
  delegate_to: localhost

- name: Create blank ASM policy and activate
  bigip_asm_policy:
    server: lb.mydomain.com
    user: admin
    password: secret
    name: new_blank_policy
    active: yes
    state: present
  delegate_to: localhost

- name: Activate ASM policy
  bigip_asm_policy:
    server: lb.mydomain.com
    user: admin
    password: secret
    name: inactive_policy
    active: yes
    state: present
  delegate_to: localhost

- name: Deactivate ASM policy
  bigip_asm_policy:
    server: lb.mydomain.com
    user: admin
    password: secret
    name: active_policy
    state: present
  delegate_to: localhost

- name: Import and activate ASM policy in Role
  bigip_asm_policy:
    server: lb.mydomain.com
    user: admin
    password: secret
    name: new_asm_policy
    file: "{{ role_path }}/files/asm_policy.xml"
    active: yes
    state: present
  delegate_to: localhost

- name: Import ASM binary policy
  bigip_asm_policy:
    server: lb.mydomain.com
    user: admin
    password: secret
    name: new_asm_policy
    file: "/root/asm_policy.plc"
    active: yes
    state: present
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Wojciech Wypior (@wojtek0806)', 'Tim Rupp (@caphrim007)']
  - ['Wojciech Wypior (@wojtek0806)', 'Tim Rupp (@caphrim007)']
