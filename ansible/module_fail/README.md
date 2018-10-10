# Ansible module: ansible.module_fail


Fail with custom message

## Description

This module fails the progress with a custom message. It can be useful for bailing out when a certain condition is met using C(when).
This module is also supported for Windows targets.

## Requirements

TODO

## Arguments

``` json
{
    "msg": "{'description': ['The customized message used for failing execution. If omitted, fail will simply bail out with a generic message.'], 'required': False, 'default': "'Failed as requested from task'"}",
}
```

## Examples


``` yaml

# Example playbook using fail and when together
- fail:
    msg: "The system may not be provisioned according to the CMDB status."
  when: cmdb_status != "to-be-staged"

```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)']
