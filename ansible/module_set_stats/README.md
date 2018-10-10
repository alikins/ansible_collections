# Ansible module: ansible.module_set_stats


Set stats for the current ansible run

## Description

This module allows setting/accumulating stats on the current ansible run, either per host or for all hosts in the run.
This module is also supported for Windows targets.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['boolean that indicates if the provided value is aggregated to the existing stat C(yes) or will replace it C(no)'], 'required': False, 'default': True}",
    "data": "{'description': ['A dictionary of which each key represents a stat (or variable) you want to keep track of'], 'required': True}",
    "per_host": "{'description': ['boolean that indicates if the stats is per host or for all hosts in the run.'], 'required': False, 'default': False}",
}
```

## Examples


``` yaml

# Aggregating packages_installed stat per host
- set_stats:
    data:
      packages_installed: 31

# Aggregating random stats for all hosts using complex arguments
- set_stats:
    data:
      one_stat: 11
      other_stat: "{{ local_var * 2 }}"
      another_stat: "{{ some_registered_var.results | map(attribute='ansible_facts.some_fact') | list }}"
    per_host: no


# setting stats (not aggregating)
- set_stats:
    data:
      the_answer: 42
    aggregate: no

```

## License

TODO

## Author Information
  - ['Brian Coca (@bcoca)']
