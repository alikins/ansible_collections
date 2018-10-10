# Ansible module: ansible.module_win_iis_webapplication


Configures IIS web applications

## Description

Creates, removes, and configures IIS web applications.

## Requirements

TODO

## Arguments

``` json
{
    "application_pool": "{'description': ['The application pool in which the new site executes.']}",
    "name": "{'description': ['Name of the web application.'], 'required': True}",
    "physical_path": "{'description': ['The physical path on the remote host to use for the new application.', 'The specified folder must already exist.']}",
    "site": "{'description': ['Name of the site on which the application is created.'], 'required': True}",
    "state": "{'description': ['State of the web application.'], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Add ACME webapplication on IIS.
  win_iis_webapplication:
    name: api
    site: acme
    state: present
    physical_path: C:\apps\acme\api

```

## License

TODO

## Author Information
  - ['Henrik Wallström']
