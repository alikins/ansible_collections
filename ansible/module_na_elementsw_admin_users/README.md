# Ansible module: ansible.module_na_elementsw_admin_users


NetApp Element Software Manage Admin Users

## Description

Create, destroy, or update admin users on SolidFire

## Requirements

TODO

## Arguments

``` json
{
    "acceptEula": "{'description': ['Boolean, true for accepting Eula, False Eula'], 'type': 'bool'}",
    "access": "{'description': ['A list of type the admin has access to']}",
    "element_password": "{'description': ['The password for the new admin account. Setting the password attribute will always reset your password, even if the password is the same']}",
    "element_username": "{'description': ['Unique username for this account. (May be 1 to 64 characters in length).'], 'required': True}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the SolidFire cluster.']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "state": "{'description': ['Whether the specified account should exist or not.'], 'required': True, 'choices': ['present', 'absent']}",
    "username": "{'required': True, 'description': ['Please ensure that the user has the adequate permissions. For more information, please read the official documentation U(https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US).'], 'aliases': ['user']}",
}
```

## Examples


``` yaml

    - name: Add admin user
      na_elementsw_admin_users:
        state: present
        username: "{{ admin_user_name }}"
        password: "{{ admin_password }}"
        hostname: "{{ hostname }}"
        element_username: carchi8py
        element_password: carchi8py
        acceptEula: True
        access: accounts,drives

    - name: modify admin user
      na_elementsw_admin_users:
        state: present
        username: "{{ admin_user_name }}"
        password: "{{ admin_password }}"
        hostname: "{{ hostname }}"
        element_username: carchi8py
        element_password: carchi8py12
        acceptEula: True
        access: accounts,drives,nodes

    - name: delete admin user
      na_elementsw_admin_users:
        state: absent
        username: "{{ admin_user_name }}"
        password: "{{ admin_password }}"
        hostname: "{{ hostname }}"
        element_username: carchi8py

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
