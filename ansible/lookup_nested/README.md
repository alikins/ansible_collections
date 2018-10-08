# Ansible lookup: ansible.lookup_nested


composes a list with nested elements of other lists

## Description

Takes the input lists and returns a list with elements that are lists composed of the elements of the input lists

## Requirements

TODO

## Arguments

``` json
{
    "_raw": "{'description': ['a set of lists'], 'required': True}",
}
```

## Examples


``` yaml

- name: give users access to multiple databases
  mysql_user:
    name: "{{ item[0] }}"
    priv: "{{ item[1] }}.*:ALL"
    append_privs: yes
    password: "foo"
  with_nested:
    - [ 'alice', 'bob' ]
    - [ 'clientdb', 'employeedb', 'providerdb' ]
# As with the case of 'with_items' above, you can use previously defined variables.:

- name: here, 'users' contains the above list of employees
  mysql_user:
    name: "{{ item[0] }}"
    priv: "{{ item[1] }}.*:ALL"
    append_privs: yes
    password: "foo"
  with_nested:
    - "{{ users }}"
    - [ 'clientdb', 'employeedb', 'providerdb' ]

```

## License

TODO

## Author Information
  - ['UNKNOWN']
