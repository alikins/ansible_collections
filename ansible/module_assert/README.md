# Ansible module: ansible.module_assert


Asserts given expressions are true

## Description

This module asserts that given expressions are true with an optional custom message.
This module is also supported for Windows targets.

## Requirements

TODO

## Arguments

``` json
{
    "fail_msg": "{'version_added': '2.7', 'description': ['The customized message used for a failing assertion', "This argument was called 'msg' before version 2.7, now it's renamed to 'fail_msg' with alias 'msg'"], 'aliases': ['msg']}",
    "success_msg": "{'version_added': '2.7', 'description': ['The customized message used for a successful assertion']}",
    "that": "{'description': ["A string expression of the same form that can be passed to the 'when' statement", 'Alternatively, a list of string expressions'], 'required': True}",
}
```

## Examples


``` yaml

- assert: { that: "ansible_os_family != 'RedHat'" }

- assert:
    that:
      - "'foo' in some_command_result.stdout"
      - "number_of_the_counting == 3"

- name: after version 2.7 both 'msg' and 'fail_msg' can customize failing assertion message
  assert:
    that:
      - "my_param <= 100"
      - "my_param >= 0"
    fail_msg: "'my_param' must be between 0 and 100"
    success_msg: "'my_param' is between 0 and 100"

- name: please use 'msg' when ansible version is smaller than 2.7
  assert:
    that:
      - "my_param <= 100"
      - "my_param >= 0"
    msg: "'my_param' must be between 0 and 100"

```

## License

TODO

## Author Information
  - ['Ansible Core Team', 'Michael DeHaan']
  - ['Ansible Core Team', 'Michael DeHaan']
