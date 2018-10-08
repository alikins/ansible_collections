# Ansible lookup: ansible.lookup_hiera


get info from hiera data

## Description

Retrieves data from an Puppetmaster node using Hiera as ENC

## Requirements

TODO

## Arguments

``` json
{
    "_bin_file": "{'description': ['Binary file to execute Hiera'], 'default': '/usr/bin/hiera', 'env': [{'name': 'ANSIBLE_HIERA_BIN'}]}",
    "_hiera_key": "{'description': ['The list of keys to lookup on the Puppetmaster'], 'type': 'list', 'element_type': 'string', 'required': True}",
    "_hierarchy_file": "{'description': ['File that describes the hierarchy of Hiera'], 'default': '/etc/hiera.yaml', 'env': [{'name': 'ANSIBLE_HIERA_CFG'}]}",
}
```

## Examples


``` yaml

# All this examples depends on hiera.yml that describes the hierarchy

- name: "a value from Hiera 'DB'"
  debug: msg={{ lookup('hiera', 'foo') }}

- name: "a value from a Hiera 'DB' on other environment"
  debug: msg={{ lookup('hiera', 'foo environment=production') }}

- name: "a value from a Hiera 'DB' for a concrete node"
  debug: msg={{ lookup('hiera', 'foo fqdn=puppet01.localdomain') }}

```

## License

TODO

## Author Information
  - ['Juan Manuel Parrilla (@jparrill)']
