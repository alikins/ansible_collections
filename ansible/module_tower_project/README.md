# Ansible module: ansible.module_tower_project


create, update, or destroy Ansible Tower projects

## Description

Create, update, or destroy Ansible Tower projects. See U(https://www.ansible.com/tower) for an overview.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['Description to use for the project.']}",
    "local_path": "{'description': ['The server playbook directory for manual projects.']}",
    "name": "{'description': ['Name to use for the project.'], 'required': True}",
    "organization": "{'description': ['Primary key of organization for project.']}",
    "scm_branch": "{'description': ['The branch to use for the SCM resource.']}",
    "scm_clean": "{'description': ['Remove local modifications before updating.'], 'type': 'bool', 'default': False}",
    "scm_credential": "{'description': ['Name of the credential to use with this SCM resource.']}",
    "scm_delete_on_update": "{'description': ['Remove the repository completely before updating.'], 'type': 'bool', 'default': False}",
    "scm_type": "{'description': ['Type of SCM resource.'], 'choices': ['manual', 'git', 'hg', 'svn'], 'default': 'manual'}",
    "scm_update_on_launch": "{'description': ['Before an update to the local repository before launching a job with this project.'], 'type': 'bool', 'default': False}",
    "scm_url": "{'description': ['URL of SCM resource.']}",
    "state": "{'description': ['Desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tower_config_file": "{'description': ['Path to the Tower config file. See notes.']}",
    "tower_host": "{'description': ['URL to your Tower instance.']}",
    "tower_password": "{'description': ['Password for your Tower instance.']}",
    "tower_username": "{'description': ['Username for your Tower instance.']}",
    "tower_verify_ssl": "{'description': ['Dis/allow insecure connections to Tower. If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Add tower project
  tower_project:
    name: "Foo"
    description: "Foo bar project"
    organization: "test"
    state: present
    tower_config_file: "~/tower_cli.cfg"

```

## License

TODO

## Author Information
  - ['Wayne Witzel III (@wwitzel3)']
