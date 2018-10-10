# Ansible module: ansible.module_bigmon_chain


Create and remove a bigmon inline service chain

## Description

Create and remove a bigmon inline service chain.

## Requirements

TODO

## Arguments

``` json
{
    "access_token": "{'description': ["Bigmon access token. If this isn't set, the environment variable C(BIGSWITCH_ACCESS_TOKEN) is used."]}",
    "controller": "{'description': ['The controller IP address.'], 'required': True}",
    "name": "{'description': ['The name of the chain.'], 'required': True}",
    "state": "{'description': ['Whether the service chain should be present or absent.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['If C(false), SSL certificates will not be validated. This should only be used on personally controlled devices using self-signed certificates.'], 'required': False, 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: bigmon inline service chain
  bigmon_chain:
    name: MyChain
    controller: '{{ inventory_hostname }}'
    state: present
    validate_certs: false

```

## License

TODO

## Author Information
  - ['Ted (@tedelhourani)']
