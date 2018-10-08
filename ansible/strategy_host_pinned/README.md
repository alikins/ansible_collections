# Ansible strategy: ansible.strategy_host_pinned


Executes tasks on each host without interruption

## Description

Task execution is as fast as possible per host in batch as defined by C(serial) (default all). Ansible will not start a play for a host unless the play can be finished without interruption by tasks for another host, i.e. the number of hosts with an active play does not exceed the number of forks. Ansible will not wait for other hosts to finish the current task before queuing the next task for a host that has finished. Once a host is done with the play, it opens it's slot to a new host that was waiting to start. Other than that, it behaves just like the "free" strategy.

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
