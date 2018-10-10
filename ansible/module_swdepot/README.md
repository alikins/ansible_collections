# Ansible module: ansible.module_swdepot


Manage packages with swdepot package manager (HP-UX)

## Description

Will install, upgrade and remove packages with swdepot package manager (HP-UX)

## Requirements

TODO

## Arguments

``` json
{
    "depot": "{'description': ['The source repository from which install or upgrade a package.'], 'version_added': 1.4}",
    "name": "{'description': ['package name.'], 'required': True, 'version_added': 1.4}",
    "state": "{'description': ['whether to install (C(present), C(latest)), or remove (C(absent)) a package.'], 'required': True, 'choices': ['present', 'latest', 'absent'], 'version_added': 1.4}",
}
```

## Examples


``` yaml

- swdepot:
    name: unzip-6.0
    state: installed
    depot: 'repository:/path'

- swdepot:
    name: unzip
    state: latest
    depot: 'repository:/path'

- swdepot:
    name: unzip
    state: absent

```

## License

TODO

## Author Information
  - ['Raul Melo (@melodous)']
