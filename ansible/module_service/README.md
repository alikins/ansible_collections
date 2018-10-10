# Ansible module: ansible.module_service


Manage services

## Description

Controls services on remote hosts. Supported init systems include BSD init, OpenRC, SysV, Solaris SMF, systemd, upstart.
For Windows targets, use the M(win_service) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "arguments": "{'description': ['Additional arguments provided on the command line'], 'aliases': ['args']}",
    "enabled": "{'description': ['Whether the service should start on boot. B(At least one of state and enabled are required.)'], 'type': 'bool'}",
    "name": "{'description': ['Name of the service.'], 'required': True}",
    "pattern": "{'description': ['If the service does not respond to the status command, name a substring to look for as would be found in the output of the I(ps) command as a stand-in for a status result.  If the string is found, the service will be assumed to be started.']}",
    "runlevel": "{'description': ['For OpenRC init scripts (ex: Gentoo) only.  The runlevel that this service belongs to.'], 'default': 'default'}",
    "sleep": "{'description': ['If the service is being C(restarted) then sleep this many seconds between the stop and start command. This helps to workaround badly behaving init scripts that exit immediately after signaling a process to stop.'], 'version_added': '1.3'}",
    "state": "{'description': ["C(started)/C(stopped) are idempotent actions that will not run commands unless necessary.  C(restarted) will always bounce the service.  C(reloaded) will always reload. B(At least one of state and enabled are required.) Note that reloaded will start the service if it is not already started, even if your chosen init system wouldn't normally."], 'choices': ['reloaded', 'restarted', 'started', 'stopped']}",
    "use": "{'description': ['The service module actually uses system specific modules, normally through auto detection, this setting can force a specific module.', "Normally it uses the value of the 'ansible_service_mgr' fact and falls back to the old 'service' module when none matching is found."], 'default': 'auto', 'version_added': 2.2}",
}
```

## Examples


``` yaml

- name: Start service httpd, if not started
  service:
    name: httpd
    state: started

- name: Stop service httpd, if started
  service:
    name: httpd
    state: stopped

- name: Restart service httpd, in all cases
  service:
    name: httpd
    state: restarted

- name: Reload service httpd, in all cases
  service:
    name: httpd
    state: reloaded

- name: Enable service httpd, and not touch the state
  service:
    name: httpd
    enabled: yes

- name: Start service foo, based on running process /usr/bin/foo
  service:
    name: foo
    pattern: /usr/bin/foo
    state: started

- name: Restart network service for interface eth0
  service:
    name: network
    state: restarted
    args: eth0

```

## License

TODO

## Author Information
  - ['Ansible Core Team', 'Michael DeHaan']
  - ['Ansible Core Team', 'Michael DeHaan']
