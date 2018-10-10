# Ansible module: ansible.module_win_timezone


Sets Windows machine timezone

## Description

Sets machine time to the specified timezone.

## Requirements

TODO

## Arguments

``` json
{
    "timezone": "{'description': ['Timezone to set to.', 'Example: Central Standard Time'], 'required': True}",
}
```

## Examples


``` yaml

- name: Set timezone to 'Romance Standard Time' (GMT+01:00)
  win_timezone:
    timezone: Romance Standard Time

- name: Set timezone to 'GMT Standard Time' (GMT)
  win_timezone:
    timezone: GMT Standard Time

- name: Set timezone to 'Central Standard Time' (GMT-06:00)
  win_timezone:
    timezone: Central Standard Time

```

## License

TODO

## Author Information
  - ['Phil Schwartz (@schwartzmx)']
