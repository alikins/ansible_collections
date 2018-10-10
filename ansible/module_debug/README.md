# Ansible module: ansible.module_debug


Print statements during execution

## Description

This module prints statements during execution and can be useful for debugging variables or expressions without necessarily halting the playbook. Useful for debugging together with the 'when:' directive.
This module is also supported for Windows targets.

## Requirements

TODO

## Arguments

``` json
{
    "msg": "{'description': ['The customized message that is printed. If omitted, prints a generic message.'], 'required': False, 'default': 'Hello world!'}",
    "var": "{'description': ["A variable name to debug.  Mutually exclusive with the 'msg' option."]}",
    "verbosity": "{'description': ['A number that controls when the debug is run, if you set to 3 it will only run debug when -vvv or above'], 'required': False, 'default': 0, 'version_added': '2.1'}",
}
```

## Examples


``` yaml

# Example that prints the loopback address and gateway for each host
- debug:
    msg: "System {{ inventory_hostname }} has uuid {{ ansible_product_uuid }}"

- debug:
    msg: "System {{ inventory_hostname }} has gateway {{ ansible_default_ipv4.gateway }}"
  when: ansible_default_ipv4.gateway is defined

- shell: /usr/bin/uptime
  register: result

- debug:
    var: result
    verbosity: 2

- name: Display all variables/facts known for a host
  debug:
    var: hostvars[inventory_hostname]
    verbosity: 4

# Example that prints two lines of messages, but only if there's an environment value set
- debug:
    msg:
      - "Provisioning based on YOUR_KEY which is: '{{ lookup('env', 'YOUR_KEY') }}"
      - "These servers were built using the password of '{{ password_used }}'. Please retain this for later use."

```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)', 'Michael DeHaan']
  - ['Dag Wieers (@dagwieers)', 'Michael DeHaan']
