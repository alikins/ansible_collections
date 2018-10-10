# Ansible module: ansible.module_manageiq_user


Management of users in ManageIQ

## Description

The manageiq_user module supports adding, updating and deleting users in ManageIQ.

## Requirements

TODO

## Arguments

``` json
{
    "email": "{'description': ["The users' E-mail address."]}",
    "group": "{'description': ['The name of the group to which the user belongs.']}",
    "manageiq_connection": "{'required': True, 'description': ['ManageIQ connection configuration information.'], 'suboptions': {'url': {'required': True, 'description': ['ManageIQ environment url. C(MIQ_URL) env var if set. otherwise, it is required to pass it.']}, 'username': {'description': ['ManageIQ username. C(MIQ_USERNAME) env var if set. otherwise, required if no token is passed in.']}, 'password': {'description': ['ManageIQ password. C(MIQ_PASSWORD) env var if set. otherwise, required if no token is passed in.']}, 'token': {'description': ['ManageIQ token. C(MIQ_TOKEN) env var if set. otherwise, required if no username or password is passed in.']}, 'verify_ssl': {'description': ['Whether SSL certificates should be verified for HTTPS requests. defaults to True.'], 'default': True}, 'ca_bundle_path': {'description': ['The path to a CA bundle file or directory with certificates. defaults to None.']}}}",
    "name": "{'description': ["The users' full name."]}",
    "password": "{'description': ["The users' password."]}",
    "state": "{'description': ['absent - user should not exist, present - user should be.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "update_password": "{'default': 'always', 'choices': ['always', 'on_create'], 'description': ['C(always) will update passwords unconditionally.  C(on_create) will only set the password for a newly created user.'], 'version_added': '2.5'}",
    "userid": "{'description': ['The unique userid in manageiq, often mentioned as username.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create a new user in ManageIQ
  manageiq_user:
    userid: 'jdoe'
    name: 'Jane Doe'
    password: 'VerySecret'
    group: 'EvmGroup-user'
    email: 'jdoe@example.com'
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      verify_ssl: False

- name: Create a new user in ManageIQ using a token
  manageiq_user:
    userid: 'jdoe'
    name: 'Jane Doe'
    password: 'VerySecret'
    group: 'EvmGroup-user'
    email: 'jdoe@example.com'
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      token: 'sometoken'
      verify_ssl: False

- name: Delete a user in ManageIQ
  manageiq_user:
    state: 'absent'
    userid: 'jdoe'
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      verify_ssl: False

- name: Delete a user in ManageIQ using a token
  manageiq_user:
    state: 'absent'
    userid: 'jdoe'
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      token: 'sometoken'
      verify_ssl: False

- name: Update email of user in ManageIQ
  manageiq_user:
    userid: 'jdoe'
    email: 'jaustine@example.com'
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      verify_ssl: False

- name: Update email of user in ManageIQ using a token
  manageiq_user:
    userid: 'jdoe'
    email: 'jaustine@example.com'
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      token: 'sometoken'
      verify_ssl: False

```

## License

TODO

## Author Information
  - ['Daniel Korn (@dkorn)']
