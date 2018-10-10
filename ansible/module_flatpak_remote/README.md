# Ansible module: ansible.module_flatpak_remote


Manage flatpak repository remotes

## Description

Allows users to add or remove flatpak remotes.
The flatpak remotes concept is comparable to what is called repositories in other packaging formats.
Currently, remote addition is only supported via I(flatpakrepo) file URLs.
Existing remotes will not be updated.
See the M(flatpak) module for managing flatpaks.

## Requirements

TODO

## Arguments

``` json
{
    "executable": "{'description': ['The path to the C(flatpak) executable to use.', 'By default, this module looks for the C(flatpak) executable on the path.'], 'default': 'flatpak'}",
    "flatpakrepo_url": "{'description': ['The URL to the I(flatpakrepo) file representing the repository remote to add.', 'When used with I(state=present), the flatpak remote specified under the I(flatpakrepo_url) is added using the specified installation C(method).', 'When used with I(state=absent), this is not required.', 'Required when I(state=present).']}",
    "method": "{'description': ['The installation method to use.', 'Defines if the I(flatpak) is supposed to be installed globally for the whole C(system) or only for the current C(user).'], 'choices': ['system', 'user'], 'default': 'system'}",
    "name": "{'description': ['The desired name for the flatpak remote to be registered under on the managed host.', 'When used with I(state=present), the remote will be added to the managed host under the specified I(name).', 'When used with I(state=absent) the remote with that name will be removed.'], 'required': True}",
    "state": "{'description': ['Indicates the desired package state.'], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Add the Gnome flatpak remote to the system installation
  flatpak_remote:
    name: gnome
    state: present
    flatpakrepo_url: https://sdk.gnome.org/gnome-apps.flatpakrepo

- name: Add the flathub flatpak repository remote to the user installation
  flatpak_remote:
    name: flathub
    state: present
    flatpakrepo_url: https://dl.flathub.org/repo/flathub.flatpakrepo
    method: user

- name: Remove the Gnome flatpak remote from the user installation
  flatpak_remote:
    name: gnome
    state: absent
    method: user

- name: Remove the flathub remote from the system installation
  flatpak_remote:
    name: flathub
    state: absent

```

## License

TODO

## Author Information
  - ['John Kwiatkoski (@jaykayy)', 'Alexander Bethke (@oolongbrothers)']
  - ['John Kwiatkoski (@jaykayy)', 'Alexander Bethke (@oolongbrothers)']
