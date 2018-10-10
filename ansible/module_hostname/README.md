# Ansible module: ansible.module_hostname


Manage hostname

## Description

Set system's hostname, supports most OSs/Distributions, including those using systemd.
Note, this module does *NOT* modify C(/etc/hosts). You need to modify it yourself using other modules like template or replace.
Windows, HP-UX and AIX are not currently supported.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['Name of the host'], 'required': True}",
}
```

## Examples


``` yaml

- hostname:
    name: web01

```

## License

TODO

## Author Information
  - ['Adrian Likins (@alikins)', 'Hideki Saito (@saito-hideki)']
  - ['Adrian Likins (@alikins)', 'Hideki Saito (@saito-hideki)']
