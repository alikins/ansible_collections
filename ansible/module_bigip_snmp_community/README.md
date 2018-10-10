# Ansible module: ansible.module_bigip_snmp_community


Manages SNMP communities on a BIG-IP

## Description

Assists in managing SNMP communities on a BIG-IP. Different SNMP versions are supported by this module. Take note of the different parameters offered by this module, as different parameters work for different versions of SNMP. Typically this becomes an interest if you are mixing versions C(v2c) and C(3).

## Requirements

TODO

## Arguments

``` json
{
    "access": "{'description': ["Specifies the user's access level to the MIB.", 'When creating a new community, if this parameter is not specified, the default is C(ro).', 'When C(ro), specifies that the user can view the MIB, but cannot modify the MIB.', 'When C(rw), specifies that the user can view and modify the MIB.'], 'choices': ['ro', 'rw', 'read-only', 'read-write']}",
    "community": "{'description': ['Specifies the community string (password) for access to the MIB.', 'This parameter is only relevant when C(version) is C(v1), or C(v2c). If C(version) is something else, this parameter is ignored.']}",
    "ip_version": "{'description': ['Specifies whether the record applies to IPv4 or IPv6 addresses.', 'When creating a new community, if this value is not specified, the default of C(4) will be used.', 'This parameter is only relevant when C(version) is C(v1), or C(v2c). If C(version) is something else, this parameter is ignored.'], 'choices': ['4', '6']}",
    "name": "{'description': ['Name that identifies the SNMP community.', 'When C(version) is C(v1) or C(v2c), this parameter is required.', 'The name C(public) is a reserved name on the BIG-IP. This module handles that name differently than others. Functionally, you should not see a difference however.']}",
    "oid": "{'description': ['Specifies the object identifier (OID) for the record.', 'When C(version) is C(v3), this parameter is required.', 'When C(version) is either C(v1) or C(v2c), if this value is specified, then C(source) must not be set to C(all).']}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['Specifies the port for the trap destination.', 'This parameter is only relevant when C(version) is C(v1), or C(v2c). If C(version) is something else, this parameter is ignored.']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "snmp_auth_password": "{'description': ['Specifies the password for the user.', 'When creating a new SNMP C(v3) community, this parameter is required.', 'This value must be at least 8 characters long.']}",
    "snmp_auth_protocol": "{'description': ['Specifies the authentication method for the user.', 'When C(md5), specifies that the system uses the MD5 algorithm to authenticate the user.', 'When C(sha), specifies that the secure hash algorithm (SHA) to authenticate the user.', 'When C(none), specifies that user does not require authentication.', 'When creating a new SNMP C(v3) community, if this parameter is not specified, the default of C(sha) will be used.'], 'choices': ['md5', 'sha', 'none']}",
    "snmp_privacy_password": "{'description': ['Specifies the password for the user.', 'When creating a new SNMP C(v3) community, this parameter is required.', 'This value must be at least 8 characters long.']}",
    "snmp_privacy_protocol": "{'description': ['Specifies the encryption protocol.', 'When C(aes), specifies that the system encrypts the user information using AES (Advanced Encryption Standard).', 'When C(des), specifies that the system encrypts the user information using DES (Data Encryption Standard).', 'When C(none), specifies that the system does not encrypt the user information.', 'When creating a new SNMP C(v3) community, if this parameter is not specified, the default of C(aes) will be used.'], 'choices': ['aes', 'des', 'none']}",
    "snmp_username": "{'description': ['Specifies the name of the user for whom you want to grant access to the SNMP v3 MIB.', 'This parameter is only relevant when C(version) is C(v3). If C(version) is something else, this parameter is ignored.', 'When creating a new SNMP C(v3) community, this parameter is required.', 'This parameter cannot be changed once it has been set.']}",
    "source": "{'description': ['Specifies the source address for access to the MIB.', 'This parameter can accept a value of C(all).', 'If this parameter is not specified, the value C(all) is used.', 'This parameter is only relevant when C(version) is C(v1), or C(v2c). If C(version) is something else, this parameter is ignored.', 'If C(source) is set to C(all), then it is not possible to specify an C(oid). This will raise an error.', 'This parameter should be provided when C(state) is C(absent), so that the correct community is removed. To remove the C(public) SNMP community that comes with a BIG-IP, this parameter should be set to C(default).']}",
    "state": "{'description': ['When C(present), ensures that the address list and entries exists.', 'When C(absent), ensures the address list is removed.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "update_password": "{'description': ['C(always) will allow to update passwords if the user chooses to do so. C(on_create) will only set the password for newly created resources.'], 'default': 'always', 'choices': ['always', 'on_create']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
    "version": "{'description': ['Specifies to which Simple Network Management Protocol (SNMP) version the trap destination applies.'], 'choices': ['v1', 'v2c', 'v3'], 'default': 'v2c'}",
}
```

## Examples


``` yaml

- name: Create an SMNP v2c read-only community
  bigip_snmp_community:
    name: foo
    version: v2c
    source: all
    oid: .1
    access: ro
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

- name: Create an SMNP v3 read-write community
  bigip_snmp_community:
    name: foo
    version: v3
    snmp_username: foo
    snmp_auth_protocol: sha
    snmp_auth_password: secret
    snmp_privacy_protocol: aes
    snmp_privacy_password: secret
    oid: .1
    access: rw
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

- name: Remove the default 'public' SNMP community
  bigip_snmp_community:
    name: public
    source: default
    password: secret
    server: lb.mydomain.com
    state: absent
    user: admin
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
