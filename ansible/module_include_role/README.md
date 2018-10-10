# Ansible module: ansible.module_include_role


Load and execute a role

## Description

Loads and executes a role as a task dynamically. This frees roles from the `roles:` directive and allows them to be treated more as tasks.
Unlike M(import_role), most keywords, including loops and conditionals, apply to this statement.
This module is also supported for Windows targets.

## Requirements

TODO

## Arguments

``` json
{
    "allow_duplicates": "{'description': ["Overrides the role's metadata setting to allow using a role more than once with the same parameters."], 'type': 'bool', 'default': True}",
    "apply": "{'description': ['Accepts a hash of task keywords (e.g. C(tags), C(become)) that will be applied to the tasks within the include.'], 'version_added': '2.7'}",
    "defaults_from": "{'description': ["File to load from a role's C(defaults/) directory."], 'default': 'main'}",
    "name": "{'description': ['The name of the role to be executed.'], 'required': True}",
    "public": "{'description': ["This option dictates whether the role's C(vars) and C(defaults) are exposed to the playbook. If set to C(yes) the variables will be available to tasks following the C(include_role) task. This functionality differs from standard variable exposure for roles listed under the C(roles) header or C(import_role) as they are exposed at playbook parsing time, and available to earlier roles and tasks as well."], 'type': 'bool', 'default': False, 'version_added': '2.7'}",
    "tasks_from": "{'description': ["File to load from a role's C(tasks/) directory."], 'default': 'main'}",
    "vars_from": "{'description': ["File to load from a role's C(vars/) directory."], 'default': 'main'}",
}
```

## Examples


``` yaml

- include_role:
    name: myrole

- name: Run tasks/other.yaml instead of 'main'
  include_role:
    name: myrole
    tasks_from: other

- name: Pass variables to role
  include_role:
    name: myrole
  vars:
    rolevar1: value from task

- name: Use role in loop
  include_role:
    name: '{{ roleinputvar }}'
  with_items:
    - '{{ roleinput1 }}'
    - '{{ roleinput2 }}'
  loop_control:
    loop_var: roleinputvar

- name: Conditional role
  include_role:
    name: myrole
  when: not idontwanttorun

- name: Apply tags to tasks within included file
  include_role:
    name: install
    apply:
      tags:
        - install
  tags:
    - always

```

## License

TODO

## Author Information
  - ['Ansible Core Team (@ansible)']
