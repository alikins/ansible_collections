# Ansible module: ansible.module_say


Makes a computer to speak

## Description

makes a computer speak! Amuse your friends, annoy your coworkers!

## Requirements

TODO

## Arguments

``` json
{
    "msg": "{'description': ['What to say'], 'required': True}",
    "voice": "{'description': ['What voice to use'], 'required': False}",
}
```

## Examples


``` yaml

- say:
    msg: '{{ inventory_hostname }} is all done'
    voice: Zarvox
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Ansible Core Team', 'Michael DeHaan (@mpdehaan)']
  - ['Ansible Core Team', 'Michael DeHaan (@mpdehaan)']
