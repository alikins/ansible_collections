# Ansible module: ansible.module_set_fact


Set host facts from a task

## Description

This module allows setting new variables.  Variables are set on a host-by-host basis just like facts discovered by the setup module.
These variables will be available to subsequent plays during an ansible-playbook run, but will not be saved across executions even if you use a fact cache.
Per the standard Ansible variable precedence rules, many other types of variables have a higher priority, so this value may be overridden. See L(Variable Precedence Guide,../user_guide/playbooks_variables.html#variable-precedence-where-should-i-put-a-variable) for more information.
This module is also supported for Windows targets.

## Requirements

TODO

## Arguments

``` json
{
    "cacheable": "{'description': ['This boolean indicates if the facts set will also be added to the fact cache, if fact caching is enabled.'], 'type': 'bool', 'default': False, 'version_added': '2.4'}",
    "key_value": "{'description': ['The C(set_fact) module takes key=value pairs as variables to set in the playbook scope. Or alternatively, accepts complex arguments using the C(args:) statement.'], 'required': True}",
}
```

## Examples


``` yaml

# Example setting host facts using key=value pairs, note that this always creates strings or booleans
- set_fact: one_fact="something" other_fact="{{ local_var }}"

# Example setting host facts using complex arguments
- set_fact:
     one_fact: something
     other_fact: "{{ local_var * 2 }}"
     another_fact: "{{ some_registered_var.results | map(attribute='ansible_facts.some_fact') | list }}"

# Example setting facts so that they will be persisted in the fact cache
- set_fact:
    one_fact: something
    other_fact: "{{ local_var * 2 }}"
    cacheable: true

# As of 1.8, Ansible will convert boolean strings ('true', 'false', 'yes', 'no')
# to proper boolean values when using the key=value syntax, however it is still
# recommended that booleans be set using the complex argument style:
- set_fact:
    one_fact: true
    other_fact: false


```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)']
