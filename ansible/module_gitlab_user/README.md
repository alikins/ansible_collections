# Ansible module: ansible.module_gitlab_user


Creates/updates/deletes Gitlab Users

## Description

When the user does not exist in Gitlab, it will be created.
When the user does exists and state=absent, the user will be deleted.
When changes are made to user, the user will be updated.

## Requirements

TODO

## Arguments

``` json
{
    "access_level": "{'description': ['The access level to the group. One of the following can be used.', 'guest', 'reporter', 'developer', 'master', 'owner']}",
    "confirm": "{'description': ['Require confirmation.'], 'type': 'bool', 'default': True, 'version_added': '2.4'}",
    "email": "{'description': ['The email that belongs to the user.'], 'required': True}",
    "group": "{'description': ['Add user as an member to this group.']}",
    "login_password": "{'description': ['Gitlab password for login_user']}",
    "login_token": "{'description': ['Gitlab token for logging in.']}",
    "login_user": "{'description': ['Gitlab user name.']}",
    "name": "{'description': ['Name of the user you want to create'], 'required': True}",
    "password": "{'description': ['The password of the user.', 'GitLab server enforces minimum password length to 8, set this value with 8 or more characters.'], 'required': True}",
    "server_url": "{'description': ['Url of Gitlab server, with protocol (http or https).'], 'required': True}",
    "sshkey_file": "{'description': ['The ssh key itself.']}",
    "sshkey_name": "{'description': ['The name of the sshkey']}",
    "state": "{'description': ['create or delete group.', 'Possible values are present and absent.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "username": "{'description': ['The username of the user.'], 'required': True}",
    "validate_certs": "{'description': ['When using https if SSL certificate needs to be verified.'], 'type': 'bool', 'default': True, 'aliases': ['verify_ssl']}",
}
```

## Examples


``` yaml

- name: Delete Gitlab User
  gitlab_user:
    server_url: http://gitlab.example.com
    validate_certs: False
    login_token: WnUzDsxjy8230-Dy_k
    username: myusername
    state: absent
  delegate_to: localhost

- name: Create Gitlab User
  gitlab_user:
    server_url: https://gitlab.dj-wasabi.local
    validate_certs: True
    login_user: dj-wasabi
    login_password: MySecretPassword
    name: My Name
    username: myusername
    password: mysecretpassword
    email: me@example.com
    sshkey_name: MySSH
    sshkey_file: ssh-rsa AAAAB3NzaC1yc...
    state: present
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Werner Dijkerman (@dj-wasabi)']
