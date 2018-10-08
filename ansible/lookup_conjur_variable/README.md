# Ansible lookup: ansible.lookup_conjur_variable


Fetch credentials from CyberArk Conjur

## Description

Retrieves credentials from Conjur using the controlling host's Conjur identity. Conjur info: U(https://www.conjur.org/).

## Requirements

TODO

## Arguments

``` json
{
    "_term": "{'description': ['Variable path'], 'required': True}",
    "config_file": "{'description': ['Path to the Conjur configuration file. The configuration file is a YAML file.'], 'type': 'path', 'default': '/etc/conjur.conf', 'required': False, 'ini': [{'section': 'conjur,', 'key': 'config_file_path'}], 'env': [{'name': 'CONJUR_CONFIG_FILE'}]}",
    "identity_file": "{'description': ['Path to the Conjur identity file. The identity file follows the netrc file format convention.'], 'type': 'path', 'default': '/etc/conjur.identity', 'required': False, 'ini': [{'section': 'conjur,', 'key': 'identity_file_path'}], 'env': [{'name': 'CONJUR_IDENTITY_FILE'}]}",
}
```

## Examples


``` yaml

  - debug:
      msg: "{{ lookup('conjur_variable', '/path/to/secret') }}"

```

## License

TODO

## Author Information
  - ['UNKNOWN']
