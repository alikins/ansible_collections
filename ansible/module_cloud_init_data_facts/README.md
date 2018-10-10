# Ansible module: ansible.module_cloud_init_data_facts


Retrieve facts of cloud-init

## Description

Gathers facts by reading the status.json and result.json of cloud-init.

## Requirements

TODO

## Arguments

``` json
{
    "filter": "{'description': ['Filter facts'], 'choices': ['status', 'result']}",
}
```

## Examples


``` yaml

- name: Gather all facts of cloud init
  cloud_init_data_facts:
  register: result

- debug:
    var: result

- name: Wait for cloud init to finish
  cloud_init_data_facts:
    filter: status
  register: res
  until: "res.cloud_init_data_facts.status.v1.stage is defined and not res.cloud_init_data_facts.status.v1.stage"
  retries: 50
  delay: 5

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
