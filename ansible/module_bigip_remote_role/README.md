# Ansible module: ansible.module_bigip_remote_role


Manage remote roles on a BIG-IP

## Description

Manages remote roles on a BIG-IP. Remote roles are used in situations where user authentication is handled off-box. Local access control to the BIG-IP is controlled by the defined remote role. Where-as authentication (and by extension, assignment to the role) is handled off-box.

## Requirements

TODO

## Arguments

``` json
{
    "assigned_role": "{'description': ['Specifies the authorization (level of access) for the account.', 'When creating a new remote role, if this parameter is not provided, the default is C(none).', 'The C(partition_access) parameter controls which partitions the account can access.', 'The chosen role may affect the partitions that one is allowed to specify. Specifically, roles such as C(administrator), C(auditor) and C(resource-administrator) required a C(partition_access) of C(all).', 'A set of pre-existing roles ship with the system. They are C(none), C(guest), C(operator), C(application-editor), C(manager), C(certificate-manager), C(irule-manager), C(user-manager), C(resource-administrator), C(auditor), C(administrator), C(firewall-manager).']}",
    "attribute_string": "{'description': ['Specifies the user account attributes saved in the group, in the format C(cn=, ou=, dc=).', 'When creating a new remote role, this parameter is required.']}",
    "line_order": "{'description': ['Specifies the order of the line in the file C(/config/bigip/auth/remoterole).', 'The LDAP and Active Directory servers read this file line by line.', 'The order of the information is important; therefore, F5 recommends that you set the first line at 1000. This allows you, in the future, to insert lines before the first line.', 'When creating a new remote role, this parameter is required.']}",
    "name": "{'description': ['Specifies the name of the remote role.'], 'required': True}",
    "partition_access": "{'description': ['Specifies the accessible partitions for the account.', 'This parameter supports the reserved names C(all) and C(Common), as well as specific partitions a user may access.', "Users who have access to a partition can operate on objects in that partition, as determined by the permissions conferred by the user's C(assigned_role).", 'When creating a new remote role, if this parameter is not specified, the default is C(all).']}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "remote_access": "{'description': ['Enables or disables remote access for the specified group of remotely authenticated users.', 'When creating a new remote role, if this parameter is not specified, the default is C(yes).'], 'type': 'bool'}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present), guarantees that the remote role exists.', 'When C(absent), removes the remote role from the system.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "terminal_access": "{'description': ['Specifies terminal-based accessibility for remote accounts not already explicitly assigned a user role.', 'Common values for this include C(tmsh) and C(none), however custom values may also be specified.', 'When creating a new remote role, if this parameter is not specified, the default is C(none).']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create a remote role
  bigip_remote_role:
    name: foo
    group_name: ldap_group
    line_order: 1
    attribute_string: memberOf=cn=ldap_group,cn=ldap.group,ou=ldap
    remote_access: enabled
    assigned_role: administrator
    partition_access: all
    terminal_access: none
    state: present
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
