# Ansible module: ansible.module_win_iis_virtualdirectory


Configures a virtual directory in IIS

## Description

Creates, Removes and configures a virtual directory in IIS.

## Requirements

TODO

## Arguments

``` json
{
    "application": "{'description': ['The application under which the virtual directory is created or exists.']}",
    "name": "{'description': ['The name of the virtual directory to create or remove.'], 'required': True}",
    "physical_path": "{'description': ['The physical path to the folder in which the new virtual directory is created.', 'The specified folder must already exist.']}",
    "site": "{'description': ['The site name under which the virtual directory is created or exists.'], 'required': True}",
    "state": "{'description': ['Whether to add or remove the specified virtual directory.'], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Create a virtual directory if it does not exist
  win_iis_virtualdirectory:
    name: somedirectory
    site: somesite
    state: present
    physical_path: C:\virtualdirectory\some

- name: Remove a virtual directory if it exists
  win_iis_virtualdirectory:
    name: somedirectory
    site: somesite
    state: absent

- name: Create a virtual directory on an application if it does not exist
  win_iis_virtualdirectory:
    name: somedirectory
    site: somesite
    application: someapp
    state: present
    physical_path: C:\virtualdirectory\some

```

## License

TODO

## Author Information
  - ['Henrik Wallström']
