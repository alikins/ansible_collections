# Ansible module: ansible.module_oneview_enclosure_facts


Retrieve facts about one or more Enclosures

## Description

Retrieve facts about one or more of the Enclosures from OneView.

## Requirements

TODO

## Arguments

``` json
{
    "config": "{'description': ['Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section.']}",
    "name": "{'description': ['Enclosure name.']}",
    "options": "{'description': ['List with options to gather additional facts about an Enclosure and related resources. Options allowed: C(script), C(environmentalConfiguration), and C(utilization). For the option C(utilization), you can provide specific parameters.']}",
    "params": "{'description': ['List of params to delimit, filter and sort the list of resources.', 'params allowed: - C(start): The first item to return, using 0-based indexing. - C(count): The number of resources to return. - C(filter): A general filter/query string to narrow the list of items returned. - C(sort): The sort order of the returned data set.']}",
}
```

## Examples


``` yaml

- name: Gather facts about all Enclosures
  oneview_enclosure_facts:
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
  no_log: true
  delegate_to: localhost
- debug: var=enclosures

- name: Gather paginated, filtered and sorted facts about Enclosures
  oneview_enclosure_facts:
    params:
      start: 0
      count: 3
      sort: name:descending
      filter: status=OK
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
  no_log: true
  delegate_to: localhost
- debug: var=enclosures

- name: Gather facts about an Enclosure by name
  oneview_enclosure_facts:
    name: Enclosure-Name
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
  no_log: true
  delegate_to: localhost
- debug: var=enclosures

- name: Gather facts about an Enclosure by name with options
  oneview_enclosure_facts:
    name: Test-Enclosure
    options:
      - script                       # optional
      - environmentalConfiguration   # optional
      - utilization                  # optional
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
  no_log: true
  delegate_to: localhost
- debug: var=enclosures
- debug: var=enclosure_script
- debug: var=enclosure_environmental_configuration
- debug: var=enclosure_utilization

- name: "Gather facts about an Enclosure with temperature data at a resolution of one sample per day, between two
         specified dates"
  oneview_enclosure_facts:
    name: Test-Enclosure
    options:
      - utilization:                   # optional
          fields: AmbientTemperature
          filter:
            - startDate=2016-07-01T14:29:42.000Z
            - endDate=2017-07-01T03:29:42.000Z
          view: day
          refresh: false
    hostname: 172.16.101.48
    username: administrator
    password: my_password
    api_version: 500
  no_log: true
  delegate_to: localhost
- debug: var=enclosures
- debug: var=enclosure_utilization

```

## License

TODO

## Author Information
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
