# Ansible module: ansible.module_os_client_config


Get OpenStack Client config

## Description

Get I(openstack) client config data from clouds.yaml or environment

## Requirements

TODO

## Arguments

``` json
{
    "clouds": "{'description': ['List of clouds to limit the return list to. No value means return information on all configured clouds'], 'required': False, 'default': []}",
}
```

## Examples


``` yaml

- name: Get list of clouds that do not support security groups
  os_client_config:

- debug:
    var: "{{ item }}"
  with_items: "{{ openstack.clouds | rejectattr('secgroup_source', 'none') | list }}"

- name: Get the information back just about the mordred cloud
  os_client_config:
    clouds:
      - mordred

```

## License

TODO

## Author Information
  - ['Monty Taylor (@emonty)']
