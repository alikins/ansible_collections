# Ansible module: ansible.module_na_elementsw_ldap


NetApp Element Software Manage ldap admin users

## Description

Enable, disable ldap, and add ldap users

## Requirements

TODO

## Arguments

``` json
{
    "authType": "{'description': ['Identifies which user authentication method to use.'], 'choices': ['DirectBind', 'SearchAndBind']}",
    "groupSearchBaseDn": "{'description': ['The base DN of the tree to start the group search (will do a subtree search from here)']}",
    "groupSearchCustomFilter": "{'description': ['For use with the CustomFilter Search type']}",
    "groupSearchType": "{'description': ['Controls the default group search filter used'], 'choices': ['NoGroup', 'ActiveDirectory', 'MemberDN']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the SolidFire cluster.']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "searchBindDN": "{'description': ['A dully qualified DN to log in with to perform an LDAp search for the user (needs read access to the LDAP directory).']}",
    "searchBindPassword": "{'description': ['The password for the searchBindDN account used for searching']}",
    "serverURIs": "{'description': ['A comma-separated list of LDAP server URIs']}",
    "state": "{'description': ['Whether the specified volume should exist or not.'], 'required': True, 'choices': ['present', 'absent']}",
    "userDNTemplate": "{'description': ['A string that is used form a fully qualified user DN.']}",
    "username": "{'required': True, 'description': ['Please ensure that the user has the adequate permissions. For more information, please read the official documentation U(https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US).'], 'aliases': ['user']}",
    "userSearchBaseDN": "{'description': ['The base DN of the tree to start the search (will do a subtree search from here)']}",
    "userSearchFilter": "{'description': ['the LDAP Filter to use']}",
}
```

## Examples


``` yaml

    - name: disable ldap authentication
      na_elementsw_ldap:
        state: absent
        username: "{{ admin username }}"
        password: "{{ admin password }}"
        hostname: "{{ hostname }}"

    - name: Enable ldap authentication
      na_elementsw_ldap:
        state: present
        username: "{{ admin username }}"
        password: "{{ admin password }}"
        hostname: "{{ hostname }}"
        authType: DirectBind
        serverURIs: ldap://svmdurlabesx01spd_ldapclnt
        groupSearchType: MemberDN
        userDNTemplate:  uid=%USERNAME%,cn=users,cn=accounts,dc=corp,dc="{{ company name }}",dc=com



```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
