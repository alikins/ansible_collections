# Ansible module: ansible.module_gconftool2


Edit GNOME Configurations

## Description

This module allows for the manipulation of GNOME 2 Configuration via gconftool-2.  Please see the gconftool-2(1) man pages for more details.

## Requirements

TODO

## Arguments

``` json
{
    "config_source": "{'description': ['Specify a configuration source to use rather than the default path. See man gconftool-2(1)']}",
    "direct": "{'description': ['Access the config database directly, bypassing server.  If direct is specified then the config_source must be specified as well. See man gconftool-2(1)'], 'type': 'bool', 'default': False}",
    "key": "{'description': ['A GConf preference key is an element in the GConf repository that corresponds to an application preference. See man gconftool-2(1)'], 'required': True}",
    "state": "{'description': ['The action to take upon the key/value.'], 'required': True, 'choices': ['absent', 'get', 'present']}",
    "value": "{'description': ['Preference keys typically have simple values such as strings, integers, or lists of strings and integers. This is ignored if the state is "get". See man gconftool-2(1)']}",
    "value_type": "{'description': ['The type of value being set. This is ignored if the state is "get".'], 'choices': ['bool', 'float', 'int', 'string']}",
}
```

## Examples


``` yaml

- name: Change the widget font to "Serif 12"
  gconftool2:
    key: "/desktop/gnome/interface/font_name"
    value_type: "string"
    value: "Serif 12"

```

## License

TODO

## Author Information
  - ['Kenneth D. Evensen (@kevensen)']
