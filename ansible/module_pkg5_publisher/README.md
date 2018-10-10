# Ansible module: ansible.module_pkg5_publisher


Manages Solaris 11 Image Packaging System publishers

## Description

IPS packages are the native packages in Solaris 11 and higher.
This modules will configure which publishers a client will download IPS packages from.

## Requirements

TODO

## Arguments

``` json
{
    "enabled": "{'description': ['Is the repository enabled or disabled?'], 'type': 'bool'}",
    "mirror": "{'description': ['A path or URL to the repository mirror.', 'Multiple values may be provided.']}",
    "name": "{'description': ["The publisher's name."], 'required': True, 'aliases': ['publisher']}",
    "origin": "{'description': ['A path or URL to the repository.', 'Multiple values may be provided.']}",
    "state": "{'description': ['Whether to ensure that a publisher is present or absent.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "sticky": "{'description': ['Packages installed from a sticky repository can only receive updates from that repository.'], 'type': 'bool'}",
}
```

## Examples


``` yaml

# Fetch packages for the solaris publisher direct from Oracle:
- pkg5_publisher:
    name: solaris
    sticky: true
    origin: https://pkg.oracle.com/solaris/support/

# Configure a publisher for locally-produced packages:
- pkg5_publisher:
    name: site
    origin: 'https://pkg.example.com/site/'

```

## License

TODO

## Author Information
  - ['Peter Oliver (@mavit)']
