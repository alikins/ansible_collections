# Ansible module: ansible.module_na_elementsw_account


NetApp Element Software Manage Accounts

## Description

Create, destroy, or update accounts on Element SW

## Requirements

TODO

## Arguments

``` json
{
    "account_id": "{'description': ['The ID of the account to manage or update.']}",
    "attributes": "{'description': ['List of Name/Value pairs in JSON object format.']}",
    "element_username": "{'description': ['Unique username for this account. (May be 1 to 64 characters in length).'], 'required': True}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the SolidFire cluster.']}",
    "initiator_secret": "{'description': ['CHAP secret to use for the initiator. Should be 12-16 characters long and impenetrable.', 'The CHAP initiator secrets must be unique and cannot be the same as the target CHAP secret.', 'If not specified, a random secret is created.']}",
    "new_element_username": "{'description': ['New name for the user account.']}",
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
  na_elementsw_account:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    element_username: TenantA

- name: Modify Account
  na_elementsw_account:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: present
    element_username: TenantA
    new_element_username: TenantA-Renamed

- name: Delete Account
  na_elementsw_account:
    hostname: "{{ elementsw_hostname }}"
    username: "{{ elementsw_username }}"
    password: "{{ elementsw_password }}"
    state: absent
    element_username: TenantA-Renamed

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
