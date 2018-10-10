# Ansible module: ansible.module_svc


Manage daemontools services

## Description

Controls daemontools services on remote hosts using the svc utility.

## Requirements

TODO

## Arguments

``` json
{
    "downed": "{'description': ["Should a 'down' file exist or not, if it exists it disables auto startup. defaults to no. Downed does not imply stopped."], 'type': 'bool', 'default': False}",
    "enabled": "{'description': ['Wheater the service is enabled or not, if disabled it also implies stopped. Make note that a service can be enabled and downed (no auto restart).'], 'type': 'bool'}",
    "name": "{'description': ['Name of the service to manage.'], 'required': True}",
    "service_dir": "{'description': ['directory svscan watches for services'], 'default': '/service'}",
    "service_src": "{'description': ['directory where services are defined, the source of symlinks to service_dir.']}",
    "state": "{'description': ['C(Started)/C(stopped) are idempotent actions that will not run commands unless necessary.  C(restarted) will always bounce the svc (svc -t) and C(killed) will always bounce the svc (svc -k). C(reloaded) will send a sigusr1 (svc -1). C(once) will run a normally downed svc once (svc -o), not really an idempotent operation.'], 'choices': ['killed', 'once', 'reloaded', 'restarted', 'started', 'stopped']}",
}
```

## Examples


``` yaml

- name: Start svc dnscache, if not running
  svc:
    name: dnscache
    state: started

- name: Stop svc dnscache, if running
  svc:
    name: dnscache
    state: stopped

- name: Kill svc dnscache, in all cases
  svc:
    name: dnscache
    state: killed

- name: Restart svc dnscache, in all cases
  svc:
    name: dnscache
    state: restarted

- name: Reload svc dnscache, in all cases
  svc:
    name: dnscache
    state: reloaded

- name: Using alternative svc directory location
  svc:
    name: dnscache
    state: reloaded
    service_dir: /var/service

```

## License

TODO

## Author Information
  - ['Brian Coca (@bcoca)']
