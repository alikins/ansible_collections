# Ansible lookup: ansible.lookup_env


read the value of environment variables

## Description

Allows you to query the environment variables available on the controller when you invoked Ansible.

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['Environment variable or list of them to lookup the values for'], 'required': True}",
}
```

## Examples


``` yaml

- debug: msg="{{ lookup('env','HOME') }} is an environment variable"

```

## License

TODO

## Author Information
  - ['Jan-Piet Mens (@jpmens) <jpmens(at)gmail.com>']
