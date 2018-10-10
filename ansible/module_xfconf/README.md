# Ansible module: ansible.module_xfconf


Edit XFCE4 Configurations

## Description

This module allows for the manipulation of Xfce 4 Configuration via xfconf-query.  Please see the xfconf-query(1) man pages for more details.

## Requirements

TODO

## Arguments

``` json
{
    "channel": "{'description': ['A Xfconf preference channel is a top-level tree key, inside of the Xfconf repository that corresponds to the location for which all application properties/keys are stored. See man xfconf-query(1)'], 'required': True}",
    "property": "{'description': ['A Xfce preference key is an element in the Xfconf repository that corresponds to an application preference. See man xfconf-query(1)'], 'required': True}",
    "state": "{'description': ['The action to take upon the property/value.'], 'choices': ['get', 'present', 'absent'], 'default': 'present'}",
    "value": "{'description': ['Preference properties typically have simple values such as strings, integers, or lists of strings and integers. This is ignored if the state is "get". See man xfconf-query(1)']}",
    "value_type": "{'description': ['The type of value being set. This is ignored if the state is "get".'], 'choices': ['int', 'bool', 'float', 'string']}",
}
```

## Examples


``` yaml

- name: Change the DPI to "192"
  xfconf:
    channel: "xsettings"
    property: "/Xft/DPI"
    value_type: "int"
    value: "192"
  become: True
  become_user: johnsmith


```

## License

TODO

## Author Information
  - ['Joseph Benden (@jbenden)']
