# Ansible module: ansible.module_flatpak


Manage flatpaks

## Description

Allows users to add or remove flatpaks.
See the M(flatpak_remote) module for managing flatpak remotes.

## Requirements

TODO

## Arguments

``` json
{
    "executable": "{'description': ['The path to the C(flatpak) executable to use.', 'By default, this module looks for the C(flatpak) executable on the path.'], 'default': 'flatpak'}",
    "method": "{'description': ['The installation method to use.', 'Defines if the I(flatpak) is supposed to be installed globally for the whole C(system) or only for the current C(user).'], 'choices': ['system', 'user'], 'default': 'system'}",
    "name": "{'description': ['The name of the flatpak to manage.', 'When used with I(state=present), I(name) can be specified as an C(http(s)) URL to a C(flatpakref) file or the unique reverse DNS name that identifies a flatpak.', 'When suppying a reverse DNS name, you can use the I(remote) option to specify on what remote to look for the flatpak. An example for a reverse DNS name is C(org.gnome.gedit).', 'When used with I(state=absent), it is recommended to specify the name in the reverse DNS format.', 'When supplying an C(http(s)) URL with I(state=absent), the module will try to match the installed flatpak based on the name of the flatpakref to remove it. However, there is no guarantee that the names of the flatpakref file and the reverse DNS name of the installed flatpak do match.'], 'required': True}",
    "remote": "{'description': ['The flatpak remote (repository) to install the flatpak from.', 'By default, C(flathub) is assumed, but you do need to add the flathub flatpak_remote before you can use this.', 'See the M(flatpak_remote) module for managing flatpak remotes.'], 'default': 'flathub'}",
    "state": "{'description': ['Indicates the desired package state.'], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Install the spotify flatpak
  flatpak:
    name:  https://s3.amazonaws.com/alexlarsson/spotify-repo/spotify.flatpakref
    state: present

- name: Install the gedit flatpak package
  flatpak:
    name: https://git.gnome.org/browse/gnome-apps-nightly/plain/gedit.flatpakref
    state: present

- name: Install the gedit package from flathub for current user
  flatpak:
    name: org.gnome.gedit
    state: present
  method: user

- name: Install the Gnome Calendar flatpak from the gnome remote system-wide
  flatpak:
    name: org.gnome.Calendar
    state: present
    remote: gnome

- name: Remove the gedit flatpak
  flatpak:
    name: org.gnome.gedit
    state: absent

```

## License

TODO

## Author Information
  - ['John Kwiatkoski (@jaykayy)', 'Alexander Bethke (@oolongbrothers)']
  - ['John Kwiatkoski (@jaykayy)', 'Alexander Bethke (@oolongbrothers)']
