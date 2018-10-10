# Ansible module: ansible.module_na_cdot_user


useradmin configuration and management

## Description

Create or destroy users.

## Requirements

TODO

## Arguments

``` json
{
    "application": "{'description': ['Applications to grant access to.'], 'required': True, 'choices': ['console', 'http', 'ontapi', 'rsh', 'snmp', 'sp', 'ssh', 'telnet']}",
    "authentication_method": "{'description': ['Authentication method for the application.', 'Not all authentication methods are valid for an application.', 'Valid authentication methods for each application are as denoted in I(authentication_choices_description).', 'password for console application', 'password, domain, nsswitch, cert for http application.', 'password, domain, nsswitch, cert for ontapi application.', 'community for snmp application (when creating SNMPv1 and SNMPv2 users).', 'usm and community for snmp application (when creating SNMPv3 users).', 'password for sp application.', 'password for rsh application.', 'password for telnet application.', 'password, publickey, domain, nsswitch for ssh application.'], 'required': True, 'choices': ['community', 'password', 'publickey', 'domain', 'nsswitch', 'usm']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "name": "{'description': ['The name of the user to manage.'], 'required': True}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "role_name": "{'description': ['The name of the role. Required when C(state=present)']}",
    "set_password": "{'description': ['Password for the user account.', 'It is ignored for creating snmp users, but is required for creating non-snmp users.', 'For an existing user, this value will be used as the new password.']}",
    "state": "{'description': ['Whether the specified user should exist or not.'], 'required': True, 'choices': ['present', 'absent']}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "vserver": "{'description': ['The name of the vserver to use.'], 'required': True}",
}
```

## Examples


``` yaml


    - name: Create User
      na_cdot_user:
        state: present
        name: SampleUser
        application: ssh
        authentication_method: password
        set_password: apn1242183u1298u41
        role_name: vsadmin
        vserver: ansibleVServer
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"


```

## License

TODO

## Author Information
  - ['Sumit Kumar (sumit4@netapp.com)']
