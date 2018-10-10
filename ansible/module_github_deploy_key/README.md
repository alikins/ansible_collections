# Ansible module: ansible.module_github_deploy_key


Manages deploy keys for GitHub repositories

## Description

Adds or removes deploy keys for GitHub repositories. Supports authentication using username and password, username and password and 2-factor authentication code (OTP), OAuth2 token, or personal access token.

## Requirements

TODO

## Arguments

``` json
{
    "force": "{'description': ['If C(true), forcefully adds the deploy key by deleting any existing deploy key with the same public key or title.'], 'type': 'bool', 'default': False}",
    "key": "{'description': ['The SSH public key to add to the repository as a deploy key.'], 'required': True}",
    "name": "{'description': ['The name for the deploy key.'], 'required': True, 'aliases': ['title', 'label']}",
    "otp": "{'description': ['The 6 digit One Time Password for 2-Factor Authentication. Required together with I(username) and I(password).'], 'aliases': ['2fa_token']}",
    "owner": "{'description': ['The name of the individual account or organization that owns the GitHub repository.'], 'required': True, 'aliases': ['account', 'organization']}",
    "password": "{'description': ['The password to authenticate with. A personal access token can be used here in place of a password.']}",
    "read_only": "{'description': ['If C(true), the deploy key will only be able to read repository contents. Otherwise, the deploy key will be able to read and write.'], 'type': 'bool', 'default': True}",
    "repo": "{'description': ['The name of the GitHub repository.'], 'required': True, 'aliases': ['repository']}",
    "state": "{'description': ['The state of the deploy key.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "token": "{'description': ['The OAuth2 token or personal access token to authenticate with. Mutually exclusive with I(password).']}",
    "username": "{'description': ['The username to authenticate with.']}",
}
```

## Examples


``` yaml

# add a new read-only deploy key to a GitHub repository using basic authentication
- github_deploy_key:
    owner: "johndoe"
    repo: "example"
    name: "new-deploy-key"
    key: "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAwXxn7kIMNWzcDfou..."
    read_only: yes
    username: "johndoe"
    password: "supersecretpassword"

# remove an existing deploy key from a GitHub repository
- github_deploy_key:
    owner: "johndoe"
    repository: "example"
    name: "new-deploy-key"
    key: "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAwXxn7kIMNWzcDfou..."
    force: yes
    username: "johndoe"
    password: "supersecretpassword"
    state: absent

# add a new deploy key to a GitHub repository, replace an existing key, use an OAuth2 token to authenticate
- github_deploy_key:
    owner: "johndoe"
    repository: "example"
    name: "new-deploy-key"
    key: "{{ lookup('file', '~/.ssh/github.pub') }}"
    force: yes
    token: "ABAQDAwXxn7kIMNWzcDfo..."

# re-add a deploy key to a GitHub repository but with a different name
- github_deploy_key:
    owner: "johndoe"
    repository: "example"
    name: "replace-deploy-key"
    key: "{{ lookup('file', '~/.ssh/github.pub') }}"
    username: "johndoe"
    password: "supersecretpassword"

# add a new deploy key to a GitHub repository using 2FA
- github_deploy_key:
    owner: "johndoe"
    repo: "example"
    name: "new-deploy-key-2"
    key: "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAwXxn7kIMNWzcDfou..."
    username: "johndoe"
    password: "supersecretpassword"
    otp: 123456

```

## License

TODO

## Author Information
  - ['Ali (@bincyber)']
