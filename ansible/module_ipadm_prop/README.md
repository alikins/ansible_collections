# Ansible module: ansible.module_ipadm_prop


Manage protocol properties on Solaris/illumos systems

## Description

Modify protocol properties on Solaris/illumos systems.

## Requirements

TODO

## Arguments

``` json
{
    "property": "{'description': ['Specifies the name of property we want to manage.'], 'required': True}",
    "protocol": "{'description': ['Specifies the procotol for which we want to manage properties.'], 'required': True}",
    "state": "{'description': ['Set or reset the property value.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent', 'reset']}",
    "temporary": "{'description': ['Specifies that the property value is temporary. Temporary property values do not persist across reboots.'], 'required': False, 'default': False, 'type': 'bool'}",
    "value": "{'description': ['Specifies the value we want to set for the property.'], 'required': False}",
}
```

## Examples


``` yaml

# Set TCP receive buffer size
- ipadm_prop: protocol=tcp property=recv_buf value=65536

# Reset UDP send buffer size to the default value
- ipadm_prop: protocol=udp property=send_buf state=reset

```

## License

TODO

## Author Information
  - ['Adam Števko (@xen0l)']
