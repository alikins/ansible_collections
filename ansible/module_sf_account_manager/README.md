# Ansible module: ansible.module_sf_account_manager


Manage SolidFire accounts

## Description

Create, destroy, or update accounts on SolidFire

## Requirements

TODO

## Arguments

``` json
{
    "account_id": "{'description': ['The ID of the account to manage or update.']}",
    "attributes": "{'description': ['List of Name/Value pairs in JSON object format.']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the SolidFire cluster.']}",
    "initiator_secret": "{'description': ['CHAP secret to use for the initiator. Should be 12-16 characters long and impenetrable.', 'The CHAP initiator secrets must be unique and cannot be the same as the target CHAP secret.', 'If not specified, a random secret is created.']}",
    "name": "{'description': ['Unique username for this account. (May be 1 to 64 characters in length).'], 'required': True}",
    "new_name": "{'description': ['New name for the user account.']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "state": "{'description': ['Whether the specified account should exist or not.'], 'required': True, 'choices': ['present', 'absent']}",
    "status": "{'description': ['Status of the account.']}",
    "target_secret": "{'description': ['CHAP secret to use for the target (mutual CHAP authentication).', 'Should be 12-16 characters long and impenetrable.', 'The CHAP target secrets must be unique and cannot be the same as the initiator CHAP secret.', 'If not specified, a random secret is created.']}",
    "username": "{'required': True, 'description': ['Please ensure that the user has the adequate permissions. For more information, please read the official documentation U(https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US).'], 'aliases': ['user']}",
}
```

## Examples


``` yaml

- name: Create Account
  sf_account_manager:
    hostname: "{{ solidfire_hostname }}"
    username: "{{ solidfire_username }}"
    password: "{{ solidfire_password }}"
    state: present
    name: TenantA

- name: Modify Account
  sf_account_manager:
    hostname: "{{ solidfire_hostname }}"
    username: "{{ solidfire_username }}"
    password: "{{ solidfire_password }}"
    state: present
    name: TenantA
    new_name: TenantA-Renamed

- name: Delete Account
  sf_account_manager:
    hostname: "{{ solidfire_hostname }}"
    username: "{{ solidfire_username }}"
    password: "{{ solidfire_password }}"
    state: absent
    name: TenantA-Renamed

```

## License

TODO

## Author Information
  - ['Sumit Kumar (sumit4@netapp.com)']
