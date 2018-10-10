# Ansible module: ansible.module_cs_facts


Gather facts on instances of Apache CloudStack based clouds

## Description

This module fetches data from the metadata API in CloudStack. The module must be called from within the instance itself.

## Requirements

TODO

## Arguments

``` json
{
    "filter": "{'description': ['Filter for a specific fact.'], 'choices': ['cloudstack_service_offering', 'cloudstack_availability_zone', 'cloudstack_public_hostname', 'cloudstack_public_ipv4', 'cloudstack_local_hostname', 'cloudstack_local_ipv4', 'cloudstack_instance_id', 'cloudstack_user_data']}",
    "meta_data_host": "{'description': ['Host or IP of the meta data API service.', 'If not set, determination by parsing the dhcp lease file.'], 'version_added': '2.4'}",
}
```

## Examples


``` yaml

# Gather all facts on instances
- name: Gather cloudstack facts
  cs_facts:

# Gather specific fact on instances
- name: Gather cloudstack facts
  cs_facts: filter=cloudstack_instance_id

# Gather specific fact on instances with a given meta_data_host
- name: Gather cloudstack facts
  cs_facts:
    filter: cloudstack_instance_id
    meta_data_host: 169.254.169.254

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
