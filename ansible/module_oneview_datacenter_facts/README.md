# Ansible module: ansible.module_oneview_datacenter_facts


Retrieve facts about the OneView Data Centers

## Description

Retrieve facts about the OneView Data Centers.

## Requirements

TODO

## Arguments

``` json
{
    "config": "{'description': ['Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section.']}",
    "name": "{'description': ['Data Center name.']}",
    "options": "{'description': ["Retrieve additional facts. Options available: 'visualContent'."]}",
    "params": "{'description': ['List of params to delimit, filter and sort the list of resources.', 'params allowed: - C(start): The first item to return, using 0-based indexing. - C(count): The number of resources to return. - C(filter): A general filter/query string to narrow the list of items returned. - C(sort): The sort order of the returned data set.']}",
}
```

## Examples


``` yaml

- name: Gather facts about all Data Centers
  oneview_datacenter_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
  delegate_to: localhost
- debug: var=datacenters

- name: Gather paginated, filtered and sorted facts about Data Centers
  oneview_datacenter_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
    params:
      start: 0
      count: 3
      sort: 'name:descending'
      filter: 'state=Unmanaged'
- debug: var=datacenters

- name: Gather facts about a Data Center by name
  oneview_datacenter_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
    name: "My Data Center"
  delegate_to: localhost
- debug: var=datacenters

- name: Gather facts about the Data Center Visual Content
  oneview_datacenter_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
    name: "My Data Center"
    options:
      - visualContent
  delegate_to: localhost
- debug: var=datacenters
- debug: var=datacenter_visual_content

```

## License

TODO

## Author Information
  - ['Alex Monteiro (@aalexmonteiro)', 'Madhav Bharadwaj (@madhav-bharadwaj)', 'Priyanka Sood (@soodpr)', 'Ricardo Galeno (@ricardogpsf)']
  - ['Alex Monteiro (@aalexmonteiro)', 'Madhav Bharadwaj (@madhav-bharadwaj)', 'Priyanka Sood (@soodpr)', 'Ricardo Galeno (@ricardogpsf)']
  - ['Alex Monteiro (@aalexmonteiro)', 'Madhav Bharadwaj (@madhav-bharadwaj)', 'Priyanka Sood (@soodpr)', 'Ricardo Galeno (@ricardogpsf)']
  - ['Alex Monteiro (@aalexmonteiro)', 'Madhav Bharadwaj (@madhav-bharadwaj)', 'Priyanka Sood (@soodpr)', 'Ricardo Galeno (@ricardogpsf)']
