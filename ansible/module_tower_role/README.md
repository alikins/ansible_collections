# Ansible module: ansible.module_tower_role


create, update, or destroy Ansible Tower role

## Description

Create, update, or destroy Ansible Tower roles. See U(https://www.ansible.com/tower) for an overview.

## Requirements

TODO

## Arguments

``` json
{
    "credential": "{'description': ['Credential the role acts on.']}",
    "inventory": "{'description': ['Inventory the role acts on.']}",
    "job_template": "{'description': ['The job template the role acts on.']}",
    "organization": "{'description': ['Organization the role acts on.']}",
    "project": "{'description': ['Project the role acts on.']}",
    "role": "{'description': ['The role type to grant/revoke.'], 'required': True, 'choices': ['admin', 'read', 'member', 'execute', 'adhoc', 'update', 'use', 'auditor']}",
    "state": "{'description': ['Desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "target_team": "{'description': ['Team that the role acts on.']}",
    "team": "{'description': ['Team that receives the permissions specified by the role.']}",
    "tower_config_file": "{'description': ['Path to the Tower config file. See notes.']}",
    "tower_host": "{'description': ['URL to your Tower instance.']}",
    "tower_password": "{'description': ['Password for your Tower instance.']}",
    "tower_username": "{'description': ['Username for your Tower instance.']}",
    "tower_verify_ssl": "{'description': ['Dis/allow insecure connections to Tower. If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
    "user": "{'description': ['User that receives the permissions specified by the role.']}",
}
```

## Examples


``` yaml

- name: Add jdoe to the member role of My Team
  tower_role:
    user: jdoe
    target_team: "My Team"
    role: member
    state: present
    tower_config_file: "~/tower_cli.cfg"

```

## License

TODO

## Author Information
  - ['Wayne Witzel III (@wwitzel3)']
