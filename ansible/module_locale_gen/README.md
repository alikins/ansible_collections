# Ansible module: ansible.module_locale_gen


Creates or removes locales

## Description

Manages locales by editing /etc/locale.gen and invoking locale-gen.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['Name and encoding of the locale, such as "en_GB.UTF-8".'], 'required': True}",
    "state": "{'description': ['Whether the locale shall be present.'], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Ensure a locale exists
  locale_gen:
    name: de_CH.UTF-8
    state: present

```

## License

TODO

## Author Information
  - ['Augustus Kling (@AugustusKling)']
