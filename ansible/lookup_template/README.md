# Ansible lookup: ansible.lookup_template


retrieve contents of file after templating with Jinja2

## Description

this is mostly a noop, to be used as a with_list loop when you dont want the content transformed in any way.

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['list of files to template']}",
}
```

## Examples


``` yaml

- name: show templating results
  debug: msg="{{ lookup('template', './some_template.j2') }}

```

## License

TODO

## Author Information
  - ['Michael DeHaan <michael.dehaan@gmail.com>']
