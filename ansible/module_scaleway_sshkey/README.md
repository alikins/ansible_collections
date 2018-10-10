# Ansible module: ansible.module_scaleway_sshkey


Scaleway SSH keys management module

## Description

This module manages SSH keys on Scaleway account U(https://developer.scaleway.com)

## Requirements

TODO

## Arguments

``` json
{
    "api_timeout": "{'description': ['HTTP timeout to Scaleway API in seconds.'], 'default': 30, 'aliases': ['timeout']}",
    "api_token": "{'description': ['Scaleway OAuth token.'], 'aliases': ['oauth_token']}",
    "api_url": "{'description': ['Scaleway API URL'], 'default': 'https://account.scaleway.com', 'aliases': ['base_url']}",
    "ssh_pub_key": "{'description': ['The public SSH key as a string to add.'], 'required': True}",
    "state": "{'description': ['Indicate desired state of the SSH key.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['Validate SSL certs of the Scaleway API.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: "Add SSH key"
  scaleway_sshkey:
    ssh_pub_key: "ssh-rsa AAAA..."
    state: "present"

- name: "Delete SSH key"
  scaleway_sshkey:
    ssh_pub_key: "ssh-rsa AAAA..."
    state: "absent"

- name: "Add SSH key with explicit token"
  scaleway_sshkey:
    ssh_pub_key: "ssh-rsa AAAA..."
    state: "present"
    oauth_token: "6ecd2c9b-6f4f-44d4-a187-61a92078d08c"

```

## License

TODO

## Author Information
  - ['Remy Leone (@sieben)']
