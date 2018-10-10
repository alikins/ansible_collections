# Ansible module: ansible.module_ping


Try to connect to host, verify a usable python and return ``pong`` on success

## Description

A trivial test module, this module always returns C(pong) on successful contact. It does not make sense in playbooks, but it is useful from C(/usr/bin/ansible) to verify the ability to login and that a usable Python is configured.
This is NOT ICMP ping, this is just a trivial test module that requires Python on the remote-node.
For Windows targets, use the M(win_ping) module instead.
For Network targets, use the M(net_ping) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "data": "{'description': ['Data to return for the C(ping) return value.', 'If this parameter is set to C(crash), the module will cause an exception.'], 'default': 'pong'}",
}
```

## Examples


``` yaml

# Test we can logon to 'webservers' and execute python with json lib.
# ansible webservers -m ping

# Example from an Ansible Playbook
- ping:

# Induce an exception to see what happens
- ping:
    data: crash

```

## License

TODO

## Author Information
  - ['Ansible Core Team', 'Michael DeHaan']
  - ['Ansible Core Team', 'Michael DeHaan']
