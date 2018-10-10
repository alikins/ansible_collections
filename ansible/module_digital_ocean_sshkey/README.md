# Ansible module: ansible.module_digital_ocean_sshkey


Manage DigitalOcean SSH keys

## Description

Create/delete DigitalOcean SSH keys.

## Requirements

TODO

## Arguments

``` json
{
    "fingerprint": "{'description': ['This is a unique identifier for the SSH key used to delete a key'], 'version_added': 2.4, 'aliases': ['id']}",
    "name": "{'description': ['The name for the SSH key']}",
    "oauth_token": "{'description': ['DigitalOcean OAuth token.'], 'required': True, 'version_added': 2.4}",
    "ssh_pub_key": "{'description': ['The Public SSH key to add.']}",
    "state": "{'description': ['Indicate desired state of the target.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: "Create ssh key"
  digital_ocean_sshkey:
    oauth_token: "{{ oauth_token }}"
    name: "My SSH Public Key"
    ssh_pub_key: "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAQQDDHr/jh2Jy4yALcK4JyWbVkPRaWmhck3IgCoeOO3z1e2dBowLh64QAM+Qb72pxekALga2oi4GvT+TlWNhzPH4V example"
    state: present
  register: result

- name: "Delete ssh key"
  digital_ocean_sshkey:
    oauth_token: "{{ oauth_token }}"
    state: "absent"
    fingerprint: "3b:16:bf:e4:8b:00:8b:b8:59:8c:a9:d3:f0:19:45:fa"

```

## License

TODO

## Author Information
  - ['Patrick Marques (@pmarques)']
