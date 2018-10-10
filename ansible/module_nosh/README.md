# Ansible module: ansible.module_nosh


Manage services with nosh

## Description

Control running and enabled state for system-wide or user services.
BSD and Linux systems are supported.

## Requirements

TODO

## Arguments

``` json
{
    "enabled": "{'required': False, 'type': 'bool', 'description': ['Enable or disable the service, independently of C(*.preset) file preference or running state. Mutually exclusive with I(preset). Will take effect prior to I(state=reset).']}",
    "name": "{'required': True, 'description': ['Name of the service to manage.']}",
    "preset": "{'required': False, 'type': 'bool', 'description': ['Enable or disable the service according to local preferences in *.preset files. Mutually exclusive with I(enabled). Only has an effect if set to true. Will take effect prior to I(state=reset).']}",
    "state": "{'required': False, 'choices': ['started', 'stopped', 'reset', 'restarted', 'reloaded'], 'description': ['C(started)/C(stopped) are idempotent actions that will not run commands unless necessary. C(restarted) will always bounce the service. C(reloaded) will send a SIGHUP or start the service. C(reset) will start or stop the service according to whether it is enabled or not.']}",
    "user": "{'required': False, 'default': False, 'type': 'bool', 'description': ["Run system-control talking to the calling user's service manager, rather than the system-wide service manager."]}",
}
```

## Examples


``` yaml

- name: start dnscache if not running
  nosh: name=dnscache state=started

- name: stop mpd, if running
  nosh: name=mpd state=stopped

- name: restart unbound or start it if not already running
  nosh:
    name: unbound
    state: restarted

- name: reload fail2ban or start it if not already running
  nosh:
    name: fail2ban
    state: reloaded

- name: disable nsd
  nosh: name=nsd enabled=no

- name: for package installers, set nginx running state according to local enable settings, preset and reset
  nosh: name=nginx preset=True state=reset

- name: reboot the host if nosh is the system manager, would need a "wait_for*" task at least, not recommended as-is
  nosh: name=reboot state=started

- name: using conditionals with the module facts
  tasks:
    - name: obtain information on tinydns service
      nosh: name=tinydns
      register: result

    - name: fail if service not loaded
      fail: msg="The {{ result.name }} service is not loaded"
      when: not result.status

    - name: fail if service is running
      fail: msg="The {{ result.name }} service is running"
      when: result.status and result.status['DaemontoolsEncoreState'] == "running"

```

## License

TODO

## Author Information
  - ['Thomas Caravia']
