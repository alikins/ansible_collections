# Ansible module: ansible.module_dconf


Modify and read dconf database

## Description

This module allows modifications and reading of dconf database. The module is implemented as a wrapper around dconf tool. Please see the dconf(1) man page for more details.
Since C(dconf) requires a running D-Bus session to change values, the module will try to detect an existing session and reuse it, or run the tool via C(dbus-run-session).

## Requirements

TODO

## Arguments

``` json
{
    "key": "{'required': True, 'description': ['A dconf key to modify or read from the dconf database.']}",
    "state": "{'required': False, 'default': 'present', 'choices': ['read', 'present', 'absent'], 'description': ['The action to take upon the key/value.']}",
    "value": "{'required': False, 'description': ['Value to set for the specified dconf key. Value should be specified in GVariant format. Due to complexity of this format, it is best to have a look at existing values in the dconf database. Required for C(state=present).']}",
}
```

## Examples


``` yaml

- name: Configure available keyboard layouts in Gnome
  dconf:
    key: "/org/gnome/desktop/input-sources/sources"
    value: "[('xkb', 'us'), ('xkb', 'se')]"
    state: present

- name: Read currently available keyboard layouts in Gnome
  dconf:
    key: "/org/gnome/desktop/input-sources/sources"
    state: read
  register: keyboard_layouts

- name: Reset the available keyboard layouts in Gnome
  dconf:
    key: "/org/gnome/desktop/input-sources/sources"
    state: absent

- name: Configure available keyboard layouts in Cinnamon
  dconf:
    key: "/org/gnome/libgnomekbd/keyboard/layouts"
    value: "['us', 'se']"
    state: present

- name: Read currently available keyboard layouts in Cinnamon
  dconf:
    key: "/org/gnome/libgnomekbd/keyboard/layouts"
    state: read
  register: keyboard_layouts

- name: Reset the available keyboard layouts in Cinnamon
  dconf:
    key: "/org/gnome/libgnomekbd/keyboard/layouts"
    state: absent

- name: Disable desktop effects in Cinnamon
  dconf:
    key: "/org/cinnamon/desktop-effects"
    value: "false"
    state: present

```

## License

TODO

## Author Information
  - ['Branko Majic (@azaghal)']
