# Ansible module: ansible.module_panos_set


Execute arbitrary commands on a PAN-OS device using XPath and element

## Description

Run an arbitrary 'xapi' command taking an XPath (i.e get) or XPath and element (i.e set).
See https://github.com/kevinsteves/pan-python/blob/master/doc/pan.xapi.rst for details
Runs a 'set' command by default
This should support _all_ commands that your PAN-OS device accepts vi it's cli
cli commands are found as
Once logged in issue 'debug cli on'
Enter configuration mode by issuing 'configure'
Enter your set (or other) command, for example 'set deviceconfig system timezone Australia/Melbourne'
returns
"<request cmd="set" obj="/config/devices/entry[@name='localhost.localdomain']/deviceconfig/system" cookie=XXXX><timezone>Australia/Melbourne</timezone></request>

The 'xpath' is  "/config/devices/entry[@name='localhost.localdomain']/deviceconfig/system"
The 'element' is "<timezone>Australia/Melbourne</timezone>"

## Requirements

TODO

## Arguments

``` json
{
    "command": "{'description': ["Xapi method name which supports 'xpath' or 'xpath' and 'element'"], 'choices': ['set', 'edit', 'delete', 'get', 'show', 'override'], 'default': 'set'}",
    "element": "{'description': ["The 'element' for the 'xpath' if required"]}",
    "ip_address": "{'description': ['IP address or host FQDN of the target PAN-OS NVA'], 'required': True}",
    "password": "{'description': ["Password for the given 'username'"], 'required': True}",
    "username": "{'description': ['User name for a user with admin rights on the PAN-OS NVA'], 'default': 'admin'}",
    "xpath": "{'description': ["The 'xpath' for the commands configurable"], 'required': True}",
}
```

## Examples


``` yaml


- name: Set timezone on PA NVA
  panos_set:
    ip_address: "192.168.1.1"
    username: "my-random-admin"
    password: "admin1234"
    xpath: "/config/devices/entry/deviceconfig/system"
    element: "<timezone>Australia/Melbourne</timezone>"

- name: Commit configuration
  panos_commit:
    ip_address: "192.168.1.1"
    username: "my-random-admin"
    password: "admin1234"

```

## License

TODO

## Author Information
  - ['Jasper Mackenzie']
