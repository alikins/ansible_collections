# Ansible module: ansible.module_runit


Manage runit services

## Description

Controls runit services on remote hosts using the sv utility.

## Requirements

TODO

## Arguments

``` json
{
    "enabled": "{'description': ['Whether the service is enabled or not, if disabled it also implies stopped.'], 'type': 'bool'}",
    "name": "{'description': ['Name of the service to manage.'], 'required': True}",
    "service_dir": "{'description': ['directory runsv watches for services'], 'default': '/var/service'}",
    "service_src": "{'description': ['directory where services are defined, the source of symlinks to service_dir.'], 'default': '/etc/sv'}",
    "state": "{'description': ['C(started)/C(stopped) are idempotent actions that will not run commands unless necessary.  C(restarted) will always bounce the service (sv restart) and C(killed) will always bounce the service (sv force-stop). C(reloaded) will send a HUP (sv reload). C(once) will run a normally downed sv once (sv once), not really an idempotent operation.'], 'choices': ['killed', 'once', 'reloaded', 'restarted', 'started', 'stopped']}",
}
```

## Examples


``` yaml

- name: Start sv dnscache, if not running
  runit:
    name: dnscache
    state: started

- name: Stop sv dnscache, if running
  runit:
    name: dnscache
    state: stopped

- name: Kill sv dnscache, in all cases
  runit:
    name: dnscache
    state: killed

- name: Restart sv dnscache, in all cases
  runit:
    name: dnscache
    state: restarted

- name: Reload sv dnscache, in all cases
  runit:
    name: dnscache
    state: reloaded

- name: Use alternative sv directory location
  runit:
    name: dnscache
    state: reloaded
    service_dir: /run/service

```

## License

TODO

## Author Information
  - ['James Sumners (@jsumners)']
