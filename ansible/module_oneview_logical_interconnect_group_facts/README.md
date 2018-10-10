# Ansible module: ansible.module_oneview_logical_interconnect_group_facts


Retrieve facts about one or more of the OneView Logical Interconnect Groups

## Description

Retrieve facts about one or more of the Logical Interconnect Groups from OneView

## Requirements

TODO

## Arguments

``` json
{
    "config": "{'description': ['Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section.']}",
    "name": "{'description': ['Logical Interconnect Group name.']}",
    "params": "{'description': ['List of params to delimit, filter and sort the list of resources.', 'params allowed: - C(start): The first item to return, using 0-based indexing. - C(count): The number of resources to return. - C(filter): A general filter/query string to narrow the list of items returned. - C(sort): The sort order of the returned data set.']}",
}
```

## Examples


``` yaml

- name: Gather facts about all Logical Interconnect Groups
  oneview_logical_interconnect_group_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
  no_log: true
  delegate_to: localhost

- debug: var=logical_interconnect_groups

- name: Gather paginated, filtered and sorted facts about Logical Interconnect Groups
  oneview_logical_interconnect_group_facts:
    params:
      start: 0
      count: 3
      sort: name:descending
      filter: name=LIGName
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
  no_log: true
  delegate_to: localhost

- debug: var=logical_interconnect_groups

- name: Gather facts about a Logical Interconnect Group by name
  oneview_logical_interconnect_group_facts:
    name: logical lnterconnect group name
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
  no_log: true
  delegate_to: localhost

- debug: var=logical_interconnect_groups

```

## License

TODO

## Author Information
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
