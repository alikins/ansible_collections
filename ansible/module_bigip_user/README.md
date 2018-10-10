# Ansible module: ansible.module_bigip_user


Manage user accounts and user attributes on a BIG-IP

## Description

Manage user accounts and user attributes on a BIG-IP. Typically this module operates only on the REST API users and not the CLI users. When specifying C(root), you may only change the password. Your other parameters will be ignored in this case. Changing the C(root) password is not an idempotent operation. Therefore, it will change it every time this module attempts to change it.

## Requirements

TODO

## Arguments

``` json
{
    "full_name": "{'description': ['Full name of the user.']}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common', 'version_added': 2.5}",
    "partition_access": "{'description': ['Specifies the administrative partition to which the user has access. C(partition_access) is required when creating a new account. Should be in the form "partition:role". Valid roles include C(acceleration-policy-editor), C(admin), C(application-editor), C(auditor) C(certificate-manager), C(guest), C(irule-manager), C(manager), C(no-access) C(operator), C(resource-admin), C(user-manager), C(web-application-security-administrator), and C(web-application-security-editor). Partition portion of tuple should be an existing partition or the value \'all\'.']}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "password_credential": "{'description': ['Set the users password to this unencrypted value. C(password_credential) is required when creating a new account.']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "shell": "{'description': ['Optionally set the users shell.'], 'choices': ['bash', 'none', 'tmsh']}",
    "state": "{'description': ['Whether the account should exist or not, taking action if the state is different from what is stated.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "update_password": "{'description': ['C(always) will allow to update passwords if the user chooses to do so. C(on_create) will only set the password for newly created users. When C(username_credential) is C(root), this value will be forced to C(always).'], 'default': 'always', 'choices': ['always', 'on_create']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "username_credential": "{'description': ['Name of the user to create, remove or modify.', 'The C(root) user may not be removed.'], 'required': True, 'aliases': ['name']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Add the user 'johnd' as an admin
  bigip_user:
    server: lb.mydomain.com
    user: admin
    password: secret
    username_credential: johnd
    password_credential: password
    full_name: John Doe
    partition_access: all:admin
    update_password: on_create
    state: present
  delegate_to: localhost

- name: Change the user "johnd's" role and shell
  bigip_user:
    server: lb.mydomain.com
    user: admin
    password: secret
    username_credential: johnd
    partition_access: NewPartition:manager
    shell: tmsh
    state: present
  delegate_to: localhost

- name: Make the user 'johnd' an admin and set to advanced shell
  bigip_user:
    server: lb.mydomain.com
    user: admin
    password: secret
    name: johnd
    partition_access: all:admin
    shell: bash
    state: present
  delegate_to: localhost

- name: Remove the user 'johnd'
  bigip_user:
    server: lb.mydomain.com
    user: admin
    password: secret
    name: johnd
    state: absent
  delegate_to: localhost

- name: Update password
  bigip_user:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: present
    username_credential: johnd
    password_credential: newsupersecretpassword
  delegate_to: localhost

# Note that the second time this task runs, it would fail because
# The password has been changed. Therefore, it is recommended that
# you either,
#
#   * Put this in its own playbook that you run when you need to
#   * Put this task in a `block`
#   * Include `ignore_errors` on this task
- name: Change the Admin password
  bigip_user:
    server: lb.mydomain.com
    user: admin
    password: secret
    state: present
    username_credential: admin
    password_credential: NewSecretPassword
  delegate_to: localhost

- name: Change the root user's password
  bigip_user:
    server: lb.mydomain.com
    user: admin
    password: secret
    username_credential: root
    password_credential: secret
    state: present
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)', 'Wojciech Wypior (@wojtek0806)']
  - ['Tim Rupp (@caphrim007)', 'Wojciech Wypior (@wojtek0806)']
