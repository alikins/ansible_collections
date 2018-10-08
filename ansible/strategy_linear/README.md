# Ansible strategy: ansible.strategy_linear


Executes tasks in a linear fashion

## Description

Task execution is in lockstep per host batch as defined by C(serial) (default all). Up to the fork limit of hosts will execute each task at the same time and then the next series of hosts until the batch is done, before going on to the next task.

## Requirements

TODO

## Arguments

}
```

## Examples



## License

TODO

## Author Information
  - ['Ansible Core Team']
