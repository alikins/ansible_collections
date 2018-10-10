# Ansible module: ansible.module_oneview_fcoe_network_facts


Retrieve the facts about one or more of the OneView FCoE Networks

## Description

Retrieve the facts about one or more of the FCoE Networks from OneView.

## Requirements

TODO

## Arguments

``` json
{
    "config": "{'description': ['Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section.']}",
    "name": "{'description': ['FCoE Network name.']}",
    "params": "{'description': ['List of params to delimit, filter and sort the list of resources.', 'params allowed: - C(start): The first item to return, using 0-based indexing. - C(count): The number of resources to return. - C(filter): A general filter/query string to narrow the list of items returned. - C(sort): The sort order of the returned data set.']}",
}
```

## Examples


``` yaml

- name: Gather facts about all FCoE Networks
  oneview_fcoe_network_facts:
    config: /etc/oneview/oneview_config.json
  delegate_to: localhost

- debug: var=fcoe_networks

- name: Gather paginated, filtered and sorted facts about FCoE Networks
  oneview_fcoe_network_facts:
    config: /etc/oneview/oneview_config.json
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: 'vlanId=2'
  delegate_to: localhost

- debug: var=fcoe_networks

- name: Gather facts about a FCoE Network by name
  oneview_fcoe_network_facts:
    config: /etc/oneview/oneview_config.json
    name: Test FCoE Network Facts
  delegate_to: localhost

- debug: var=fcoe_networks

```

## License

TODO

## Author Information
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
