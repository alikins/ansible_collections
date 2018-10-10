# Ansible module: ansible.module_win_ping


A windows version of the classic ping module

## Description

Checks management connectivity of a windows host.
This is NOT ICMP ping, this is just a trivial test module.
For non-Windows targets, use the M(ping) module instead.
For Network targets, use the M(net_ping) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "data": "{'description': ["Alternate data to return instead of 'pong'.", 'If this parameter is set to C(crash), the module will cause an exception.'], 'default': 'pong'}",
}
```

## Examples


``` yaml

# Test connectivity to a windows host
# ansible winserver -m win_ping

# Example from an Ansible Playbook
- win_ping:

# Induce an exception to see what happens
- win_ping:
    data: crash

```

## License

TODO

## Author Information
  - ['Chris Church (@cchurch)']
