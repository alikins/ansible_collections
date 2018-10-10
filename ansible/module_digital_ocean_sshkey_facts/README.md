# Ansible module: ansible.module_digital_ocean_sshkey_facts


DigitalOcean SSH keys facts

## Description

Fetch DigitalOcean SSH keys facts.

## Requirements

TODO

## Arguments

``` json
{
    "oauth_token": "{'description': ['DigitalOcean OAuth token.', 'There are several other environment variables which can be used to provide this value.', "i.e., - 'DO_API_TOKEN', 'DO_API_KEY', 'DO_OAUTH_TOKEN' and 'OAUTH_TOKEN'"], 'required': False, 'aliases': ['api_token']}",
    "timeout": "{'description': ["The timeout in seconds used for polling DigitalOcean's API."], 'default': 30}",
    "validate_certs": "{'description': ['If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- digital_ocean_sshkey_facts:
    oauth_token: "{{ my_do_key }}"

- set_fact:
    pubkey: "{{ item.public_key }}"
  with_items: "{{ ssh_keys|json_query(ssh_pubkey) }}"
  vars:
    ssh_pubkey: "[?name=='ansible_ctrl']"

- debug:
    msg: "{{ pubkey }}"

```

## License

TODO

## Author Information
  - ['Patrick Marques (@pmarques)']
