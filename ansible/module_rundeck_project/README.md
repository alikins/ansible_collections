# Ansible module: ansible.module_rundeck_project


Manage Rundeck projects

## Description

Create and remove Rundeck projects through HTTP API.

## Requirements

TODO

## Arguments

``` json
{
    "api_version": "{'description': ['Sets the API version used by module.', 'API version must be at least 14.'], 'default': 14}",
    "name": "{'description': ['Sets the project name.'], 'required': True}",
    "state": "{'description': ['Create or remove Rundeck project.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "token": "{'description': ['Sets the token to authenticate against Rundeck API.'], 'required': True}",
    "url": "{'description': ['Sets the rundeck instance URL.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create a rundeck project
  rundeck_project:
    name: "Project_01"
    api_version: 18
    url: "https://rundeck.example.org"
    token: "mytoken"
    state: present

- name: Remove a rundeck project
  rundeck_project:
    name: "Project_02"
    url: "https://rundeck.example.org"
    token: "mytoken"
    state: absent

```

## License

TODO

## Author Information
  - ['Loic Blot (@nerzhul)']
