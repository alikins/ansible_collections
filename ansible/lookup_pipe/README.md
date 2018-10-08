# Ansible lookup: ansible.lookup_pipe


read output from a command

## Description

Run a command and return the output

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['command(s) to run'], 'required': True}",
}
```

## Examples


``` yaml

- name: raw result of running date command"
  debug: msg="{{ lookup('pipe','date') }}"

- name: Always use quote filter to make sure your variables are safe to use with shell
  debug: msg="{{ lookup('pipe','getent ' + myuser|quote ) }}"

```

## License

TODO

## Author Information
  - ['Daniel Hokka Zakrisson <daniel@hozac.com>']
