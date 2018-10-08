# Ansible strategy: ansible.strategy_free


Executes tasks without waiting for all hosts

## Description

Task execution is as fast as possible per batch as defined by C(serial) (default all). Ansible will not wait for other hosts to finish the current task before queuing more tasks for other hosts. All hosts are still attempted for the current task, but it prevents blocking new tasks for hosts that have already finished.
With the free strategy, unlike the default linear strategy, a host that is slow or stuck on a specific task won't hold up the rest of the hosts and tasks.

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
