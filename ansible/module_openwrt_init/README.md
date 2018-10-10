# Ansible module: ansible.module_openwrt_init


Manage services on OpenWrt

## Description

Controls OpenWrt services on remote hosts.

## Requirements

TODO

## Arguments

``` json
{
    "enabled": "{'description': ['Whether the service should start on boot. B(At least one of state and enabled are required.)'], 'type': 'bool'}",
    "name": "{'description': ['Name of the service.'], 'required': True, 'aliases': ['service']}",
    "pattern": "{'description': ["If the service does not respond to the 'running' command, name a substring to look for as would be found in the output of the I(ps) command as a stand-in for a 'running' result.  If the string is found, the service will be assumed to be running."]}",
    "state": "{'description': ['C(started)/C(stopped) are idempotent actions that will not run commands unless necessary. C(restarted) will always bounce the service. C(reloaded) will always reload.'], 'choices': ['started', 'stopped', 'restarted', 'reloaded']}",
}
```

## Examples


``` yaml

# Example action to start service httpd, if not running
- openwrt_init:
    state: started
    name: httpd

# Example action to stop service cron, if running
- openwrt_init:
    name: cron
    state: stopped

# Example action to reload service httpd, in all cases
- openwrt_init:
    name: httpd
    state: reloaded

# Example action to enable service httpd
- openwrt_init:
    name: httpd
    enabled: yes

```

## License

TODO

## Author Information
  - ['Andrew Gaffney (@agaffney)']
