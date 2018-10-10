# Ansible module: ansible.module_oneview_san_manager_facts


Retrieve facts about one or more of the OneView SAN Managers

## Description

Retrieve facts about one or more of the SAN Managers from OneView

## Requirements

TODO

## Arguments

``` json
{
    "config": "{'description': ['Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section.']}",
    "params": "{'description': ['List of params to delimit, filter and sort the list of resources.', 'params allowed: - C(start): The first item to return, using 0-based indexing. - C(count): The number of resources to return. - C(query): A general query string to narrow the list of resources returned. - C(sort): The sort order of the returned data set.']}",
    "provider_display_name": "{'description': ['Provider Display Name.']}",
}
```

## Examples


``` yaml

- name: Gather facts about all SAN Managers
  oneview_san_manager_facts:
    config: /etc/oneview/oneview_config.json
  delegate_to: localhost

- debug: var=san_managers

- name: Gather paginated, filtered and sorted facts about SAN Managers
  oneview_san_manager_facts:
    config: /etc/oneview/oneview_config.json
    params:
      start: 0
      count: 3
      sort: name:ascending
      query: isInternal eq false
  delegate_to: localhost

- debug: var=san_managers

- name: Gather facts about a SAN Manager by provider display name
  oneview_san_manager_facts:
    config: /etc/oneview/oneview_config.json
    provider_display_name: Brocade Network Advisor
  delegate_to: localhost

- debug: var=san_managers

```

## License

TODO

## Author Information
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
