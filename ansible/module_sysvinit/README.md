# Ansible module: ansible.module_sysvinit


Manage SysV services

## Description

Controls services on target hosts that use the SysV init system.

## Requirements

TODO

## Arguments

``` json
{
    "arguments": "{'description': ['Additional arguments provided on the command line that some init scripts accept.'], 'aliases': ['args']}",
    "daemonize": "{'type': 'bool', 'description': ['Have the module daemonize as the service itself might not do so properly.', 'This is useful with badly written init scripts or deamons, which commonly manifests as the task hanging as it is still holding the tty or the service dying when the task is over as the connection closes the session.'], 'default': False}",
    "enabled": "{'type': 'bool', 'description': ['Whether the service should start on boot. B(At least one of state and enabled are required.)']}",
    "name": "{'required': True, 'description': ['Name of the service.'], 'aliases': ['service']}",
    "pattern": "{'description': ['A substring to look for as would be found in the output of the I(ps) command as a stand-in for a status result.', 'If the string is found, the service will be assumed to be running.', "This option is mainly for use with init scripts that don't support the 'status' option."]}",
    "runlevels": "{'description': ['The runlevels this script should be enabled/disabled from.', 'Use this to override the defaults set by the package or init script itself.']}",
    "sleep": "{'default': 1, 'description': ['If the service is being C(restarted) or C(reloaded) then sleep this many seconds between the stop and start command. This helps to workaround badly behaving services.']}",
    "state": "{'choices': ['started', 'stopped', 'restarted', 'reloaded'], 'description': ['C(started)/C(stopped) are idempotent actions that will not run commands unless necessary. Not all init scripts support C(restarted) nor C(reloaded) natively, so these will both trigger a stop and start as needed.']}",
}
```

## Examples


``` yaml

- name: make sure apache2 is started
  sysvinit:
      name: apache2
      state: started
      enabled: yes

- name: make sure apache2 is started on runlevels 3 and 5
  sysvinit:
      name: apache2
      state: started
      enabled: yes
      runlevels:
        - 3
        - 5

```

## License

TODO

## Author Information
  - ['Ansible Core Team']
