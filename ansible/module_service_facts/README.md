# Ansible module: ansible.module_service_facts


Return service state information as fact data

## Description

Return service state information as fact data for various service management utilities

## Requirements

TODO

## Arguments

}
```

## Examples


``` yaml

- name: populate service facts
  service_facts:

- debug:
    var: ansible_facts.services


```

## License

TODO

## Author Information
  - ['Matthew Jones', 'Adam Miller (@maxamillion)']
  - ['Matthew Jones', 'Adam Miller (@maxamillion)']
