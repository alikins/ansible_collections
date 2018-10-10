# Ansible module: ansible.module_homebrew_tap


Tap a Homebrew repository

## Description

Tap external Homebrew repositories.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['The GitHub user/organization repository to tap.'], 'required': True, 'aliases': ['tap']}",
    "state": "{'description': ['state of the repository.'], 'choices': ['present', 'absent'], 'required': False, 'default': 'present'}",
    "url": "{'description': ["The optional git URL of the repository to tap. The URL is not assumed to be on GitHub, and the protocol doesn't have to be HTTP. Any location and protocol that git can handle is fine.", 'I(name) option may not be a list of multiple taps (but a single tap instead) when this option is provided.'], 'required': False, 'version_added': '2.2'}",
}
```

## Examples


``` yaml

- homebrew_tap:
    name: homebrew/dupes

- homebrew_tap:
    name: homebrew/dupes
    state: absent

- homebrew_tap:
    name: homebrew/dupes,homebrew/science
    state: present

- homebrew_tap:
    name: telemachus/brew
    url: 'https://bitbucket.org/telemachus/brew'

```

## License

TODO

## Author Information
  - ['Indrajit Raychaudhuri (@indrajitr)', 'Daniel Jaouen (@danieljaouen)']
  - ['Indrajit Raychaudhuri (@indrajitr)', 'Daniel Jaouen (@danieljaouen)']
