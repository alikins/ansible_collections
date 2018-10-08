# Ansible lookup: ansible.lookup_ini


read data from a ini file

## Description

The ini lookup reads the contents of a file in INI format C(key1=value1). This plugin retrieve the value on the right side after the equal sign C('=') of a given section C([section]).
You can also read a property file which - in this case - does not contain section.

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['The key(s) to look up'], 'required': True}",
    "default": "{'description': ['return value if the key is not in the ini file'], 'default': ''}",
    "encoding": "{'default': 'utf-8', 'description': ['Text encoding to use.']}",
    "file": "{'description': ['Name of the file to load'], 'default': 'ansible.ini'}",
    "re": "{'default': False, 'type': 'boolean', 'description': ['Flag to indicate if the key supplied is a regexp.']}",
    "section": "{'default': 'global', 'description': ['section where to lookup for key.']}",
    "type": "{'description': ["ini Type of the file. 'properties' refers to the Java properties files."], 'default': 'ini', 'choices': ['ini', 'properties']}",
}
```

## Examples


``` yaml

- debug: msg="User in integration is {{ lookup('ini', 'user section=integration file=users.ini') }}"

- debug: msg="User in production  is {{ lookup('ini', 'user section=production  file=users.ini') }}"

- debug: msg="user.name is {{ lookup('ini', 'user.name type=properties file=user.properties') }}"

- debug:
    msg: "{{ item }}"
  with_ini:
    - value[1-2]
    - section: section1
    - file: "lookup.ini"
    - re: true

```

## License

TODO

## Author Information
  - ['Yannig Perre <yannig.perre(at)gmail.com>']
