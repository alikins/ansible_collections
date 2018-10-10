# Ansible module: ansible.module_import_role


Import a role into a play

## Description

Much like the `roles:` keyword, this task loads a role, but it allows you to control it when the role tasks run in between other tasks of the play.
Most keywords, loops and conditionals will only be applied to the imported tasks, not to this statement itself. If you want the opposite behavior, use M(include_role) instead. To better understand the difference you can read the L(Including and Importing Guide,../user_guide/playbooks_reuse_includes.html).

## Requirements

TODO

## Arguments

``` json
{
    "allow_duplicates": "{'description': ["Overrides the role's metadata setting to allow using a role more than once with the same parameters."], 'type': 'bool', 'default': True}",
    "defaults_from": "{'description': ["File to load from a role's C(defaults/) directory."], 'default': 'main'}",
    "name": "{'description': ['The name of the role to be executed.'], 'required': True}",
    "tasks_from": "{'description': ["File to load from a role's C(tasks/) directory."], 'default': 'main'}",
    "vars_from": "{'description': ["File to load from a role's C(vars/) directory."], 'default': 'main'}",
}
```

## Examples


``` yaml

- hosts: all
  tasks:
    - import_role:
        name: myrole

    - name: Run tasks/other.yaml instead of 'main'
      import_role:
        name: myrole
        tasks_from: other

    - name: Pass variables to role
      import_role:
        name: myrole
      vars:
        rolevar1: value from task

    - name: Apply condition to each task in role
      import_role:
        name: myrole
      when: not idontwanttorun

```

## License

TODO

## Author Information
  - ['Ansible Core Team (@ansible)']
