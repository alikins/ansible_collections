# Ansible module: ansible.module_oneview_fc_network_facts


Retrieve the facts about one or more of the OneView Fibre Channel Networks

## Description

Retrieve the facts about one or more of the Fibre Channel Networks from OneView.

## Requirements

TODO

## Arguments

``` json
{
    "config": "{'description': ['Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section.']}",
    "name": "{'description': ['Fibre Channel Network name.']}",
    "params": "{'description': ['List of params to delimit, filter and sort the list of resources.', 'params allowed: - C(start): The first item to return, using 0-based indexing. - C(count): The number of resources to return. - C(filter): A general filter/query string to narrow the list of items returned. - C(sort): The sort order of the returned data set.']}",
}
```

## Examples


``` yaml

- name: Gather facts about all Fibre Channel Networks
  oneview_fc_network_facts:
    config: /etc/oneview/oneview_config.json
  delegate_to: localhost

- debug: var=fc_networks

- name: Gather paginated, filtered and sorted facts about Fibre Channel Networks
  oneview_fc_network_facts:
    config: /etc/oneview/oneview_config.json
    params:
      start: 1
      count: 3
      sort: 'name:descending'
      filter: 'fabricType=FabricAttach'
  delegate_to: localhost
- debug: var=fc_networks

- name: Gather facts about a Fibre Channel Network by name
  oneview_fc_network_facts:
    config: /etc/oneview/oneview_config.json
    name: network name
  delegate_to: localhost

- debug: var=fc_networks

```

## License

TODO

## Author Information
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
