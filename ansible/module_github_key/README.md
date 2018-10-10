# Ansible module: ansible.module_github_key


Manage GitHub access keys

## Description

Creates, removes, or updates GitHub access keys.

## Requirements

TODO

## Arguments

``` json
{
    "force": "{'description': ["The default is C(yes), which will replace the existing remote key if it's different than C(pubkey). If C(no), the key will only be set if no key with the given C(name) exists."], 'type': 'bool', 'default': True}",
    "name": "{'description': ['SSH key name'], 'required': True}",
    "pubkey": "{'description': ['SSH public key value. Required when C(state=present).']}",
    "state": "{'description': ['Whether to remove a key, ensure that it exists, or update its value.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "token": "{'description': ['GitHub Access Token with permission to list and create public keys.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Read SSH public key to authorize
  shell: cat /home/foo/.ssh/id_rsa.pub
  register: ssh_pub_key

- name: Authorize key with GitHub
  local_action:
    module: github_key
    name: Access Key for Some Machine
    token: '{{ github_access_token }}'
    pubkey: '{{ ssh_pub_key.stdout }}'

```

## License

TODO

## Author Information
  - ['Robert Estelle (@erydo)']
