# Ansible module: ansible.module_systemd


Manage services

## Description

Controls systemd services on remote hosts.

## Requirements

TODO

## Arguments

``` json
{
    "daemon_reexec": "{'description': ['run daemon_reexec command before doing any other operations, the systemd manager will serialize the manager state.'], 'type': 'bool', 'default': False, 'aliases': ['daemon-reexec'], 'version_added': '2.8'}",
    "daemon_reload": "{'description': ['run daemon-reload before doing any other operations, to make sure systemd has read any changes.'], 'type': 'bool', 'default': False, 'aliases': ['daemon-reload']}",
    "enabled": "{'description': ['Whether the service should start on boot. B(At least one of state and enabled are required.)'], 'type': 'bool'}",
    "force": "{'description': ['Whether to override existing symlinks.'], 'type': 'bool', 'version_added': 2.6}",
    "masked": "{'description': ['Whether the unit should be masked or not, a masked unit is impossible to start.'], 'type': 'bool'}",
    "name": "{'description': ['Name of the service. When using in a chroot environment you always need to specify the full name i.e. (crond.service).'], 'aliases': ['service', 'unit']}",
    "no_block": "{'description': ['Do not synchronously wait for the requested operation to finish. Enqueued job will continue without Ansible blocking on its completion.'], 'type': 'bool', 'default': False, 'version_added': '2.3'}",
    "scope": "{'description': ["run systemctl within a given service manager scope, either as the default system scope (system), the current user's scope (user), or the scope of all users (global)."], 'choices': ['system', 'user', 'global'], 'default': 'system', 'version_added': '2.7'}",
    "state": "{'description': ['C(started)/C(stopped) are idempotent actions that will not run commands unless necessary. C(restarted) will always bounce the service. C(reloaded) will always reload.'], 'choices': ['reloaded', 'restarted', 'started', 'stopped']}",
    "user": "{'description': ['(deprecated) run ``systemctl`` talking to the service manager of the calling user, rather than the service manager of the system.', 'This option is deprecated and will eventually be removed in 2.11. The ``scope`` option should be used instead.'], 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

- name: Make sure a service is running
  systemd:
    state: started
    name: httpd

- name: stop service cron on debian, if running
  systemd:
    name: cron
    state: stopped

- name: restart service cron on centos, in all cases, also issue daemon-reload to pick up config changes
  systemd:
    state: restarted
    daemon_reload: yes
    name: crond

- name: reload service httpd, in all cases
  systemd:
    name: httpd
    state: reloaded

- name: enable service httpd and ensure it is not masked
  systemd:
    name: httpd
    enabled: yes
    masked: no

- name: enable a timer for dnf-automatic
  systemd:
    name: dnf-automatic.timer
    state: started
    enabled: yes

- name: just force systemd to reread configs (2.4 and above)
  systemd:
    daemon_reload: yes

```

## License

TODO

## Author Information
  - ['Ansible Core Team']
