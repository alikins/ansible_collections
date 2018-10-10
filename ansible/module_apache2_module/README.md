# Ansible module: ansible.module_apache2_module


Enables/disables a module of the Apache2 webserver

## Description

Enables or disables a specified module of the Apache2 webserver.

## Requirements

TODO

## Arguments

``` json
{
    "force": "{'description': ['Force disabling of default modules and override Debian warnings.'], 'required': False, 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "identifier": "{'description': ['Identifier of the module as listed by C(apache2ctl -M). This is optional and usually determined automatically by the common convention of appending C(_module) to I(name) as well as custom exception for popular modules.'], 'required': False, 'version_added': '2.5'}",
    "ignore_configcheck": "{'description': ['Ignore configuration checks about inconsistent module configuration. Especially for mpm_* modules.'], 'type': 'bool', 'default': False, 'version_added': '2.3'}",
    "name": "{'description': ['Name of the module to enable/disable as given to C(a2enmod/a2dismod).'], 'required': True}",
    "state": "{'description': ['Desired state of the module.'], 'choices': ['present', 'absent'], 'default': 'present'}",
}
```

## Examples


``` yaml

# enables the Apache2 module "wsgi"
- apache2_module:
    state: present
    name: wsgi
# disables the Apache2 module "wsgi"
- apache2_module:
    state: absent
    name: wsgi
# disable default modules for Debian
- apache2_module:
    state: absent
    name: autoindex
    force: True
# disable mpm_worker and ignore warnings about missing mpm module
- apache2_module:
    state: absent
    name: mpm_worker
    ignore_configcheck: True
# enable dump_io module, which is identified as dumpio_module inside apache2
- apache2_module:
    state: present
    name: dump_io
    identifier: dumpio_module

```

## License

TODO

## Author Information
  - ['Christian Berendt (@berendt)', 'Ralf Hertel (@n0trax)', 'Robin Roth (@robinro)']
  - ['Christian Berendt (@berendt)', 'Ralf Hertel (@n0trax)', 'Robin Roth (@robinro)']
  - ['Christian Berendt (@berendt)', 'Ralf Hertel (@n0trax)', 'Robin Roth (@robinro)']
