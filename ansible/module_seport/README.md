# Ansible module: ansible.module_seport


Manages SELinux network port type definitions

## Description

Manages SELinux network port type definitions.

## Requirements

TODO

## Arguments

``` json
{
    "ports": "{'description': ['Ports or port ranges. Can be a list (since 2.6) or comma separated string.'], 'required': True}",
    "proto": "{'description': ['Protocol for the specified port.'], 'required': True, 'choices': ['tcp', 'udp']}",
    "reload": "{'description': ['Reload SELinux policy after commit.'], 'type': 'bool', 'default': True}",
    "setype": "{'description': ['SELinux type for the specified port.'], 'required': True}",
    "state": "{'description': ['Desired boolean value.'], 'required': True, 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Allow Apache to listen on tcp port 8888
  seport:
    ports: 8888
    proto: tcp
    setype: http_port_t
    state: present

- name: Allow sshd to listen on tcp port 8991
  seport:
    ports: 8991
    proto: tcp
    setype: ssh_port_t
    state: present

- name: Allow memcached to listen on tcp ports 10000-10100 and 10112
  seport:
    ports: 10000-10100,10112
    proto: tcp
    setype: memcache_port_t
    state: present

- name: Allow memcached to listen on tcp ports 10000-10100 and 10112
  seport:
    ports:
      - 10000-10100
      - 10112
    proto: tcp
    setype: memcache_port_t
    state: present

```

## License

TODO

## Author Information
  - ['Dan Keder (@dankeder)']
