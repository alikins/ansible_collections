# Ansible module: ansible.module_portinstall


Installing packages from FreeBSD's ports system

## Description

Manage packages for FreeBSD using 'portinstall'.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['name of package to install/remove'], 'required': True}",
    "state": "{'description': ['state of the package'], 'choices': ['present', 'absent'], 'required': False, 'default': 'present'}",
    "use_packages": "{'description': ['use packages instead of ports whenever available'], 'type': 'bool', 'required': False, 'default': True}",
}
```

## Examples


``` yaml

# Install package foo
- portinstall:
    name: foo
    state: present

# Install package security/cyrus-sasl2-saslauthd
- portinstall:
    name: security/cyrus-sasl2-saslauthd
    state: present

# Remove packages foo and bar
- portinstall:
    name: foo,bar
    state: absent

```

## License

TODO

## Author Information
  - ['berenddeboer (@berenddeboer)']
