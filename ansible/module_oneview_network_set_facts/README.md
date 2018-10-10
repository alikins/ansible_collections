# Ansible module: ansible.module_oneview_network_set_facts


Retrieve facts about the OneView Network Sets

## Description

Retrieve facts about the Network Sets from OneView.

## Requirements

TODO

## Arguments

``` json
{
    "config": "{'description': ['Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section.']}",
    "name": "{'description': ['Network Set name.']}",
    "options": "{'description': ['List with options to gather facts about Network Set. Option allowed: C(withoutEthernet). The option C(withoutEthernet) retrieves the list of network_sets excluding Ethernet networks.']}",
    "params": "{'description': ['List of params to delimit, filter and sort the list of resources.', 'params allowed: - C(start): The first item to return, using 0-based indexing. - C(count): The number of resources to return. - C(filter): A general filter/query string to narrow the list of items returned. - C(sort): The sort order of the returned data set.']}",
}
```

## Examples


``` yaml

- name: Gather facts about all Network Sets
  oneview_network_set_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
  no_log: true
  delegate_to: localhost

- debug: var=network_sets

- name: Gather paginated, filtered, and sorted facts about Network Sets
  oneview_network_set_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: name='netset001'
  no_log: true
  delegate_to: localhost

- debug: var=network_sets

- name: Gather facts about all Network Sets, excluding Ethernet networks
  oneview_network_set_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
    options:
        - withoutEthernet
  no_log: true
  delegate_to: localhost

- debug: var=network_sets


- name: Gather facts about a Network Set by name
  oneview_network_set_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
    name: Name of the Network Set
  no_log: true
  delegate_to: localhost

- debug: var=network_sets


- name: Gather facts about a Network Set by name, excluding Ethernet networks
  oneview_network_set_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
    name: Name of the Network Set
    options:
        - withoutEthernet
  no_log: true
  delegate_to: localhost

- debug: var=network_sets

```

## License

TODO

## Author Information
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
