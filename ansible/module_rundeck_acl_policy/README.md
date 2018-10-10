# Ansible module: ansible.module_rundeck_acl_policy


Manage Rundeck ACL policies

## Description

Create, update and remove Rundeck ACL policies through HTTP API.

## Requirements

TODO

## Arguments

``` json
{
    "api_version": "{'description': ['Sets the API version used by module.', 'API version must be at least 14.'], 'default': 14}",
    "name": "{'description': ['Sets the project name.'], 'required': True}",
    "policy": "{'description': ['Sets the ACL policy content.', 'ACL policy content is a YAML object as described in http://rundeck.org/docs/man5/aclpolicy.html.', 'It can be a YAML string or a pure Ansible inventory YAML object.']}",
    "project": "{'description': ['Sets the project which receive the ACL policy.', "If unset, it's a system ACL policy."]}",
    "state": "{'description': ['Create or remove Rundeck project.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "token": "{'description': ['Sets the token to authenticate against Rundeck API.'], 'required': True}",
    "url": "{'description': ['Sets the rundeck instance URL.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create or update a rundeck ACL policy in project Ansible
  rundeck_acl_policy:
    name: "Project_01"
    api_version: 18
    url: "https://rundeck.example.org"
    token: "mytoken"
    state: present
    project: "Ansible"
    policy:
      description: "my policy"
      context:
        application: rundeck
      for:
        project:
          - allow: read
      by:
        group: "build"

- name: Remove a rundeck system policy
  rundeck_acl_policy:
    name: "Project_02"
    url: "https://rundeck.example.org"
    token: "mytoken"
    state: absent

```

## License

TODO

## Author Information
  - ['Loic Blot (@nerzhul)']
