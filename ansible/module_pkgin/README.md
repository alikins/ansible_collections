# Ansible module: ansible.module_pkgin


Package manager for SmartOS, NetBSD, et al

## Description

The standard package manager for SmartOS, but also usable on NetBSD or any OS that uses C(pkgsrc).  (Home: U(http://pkgin.net/))

## Requirements

TODO

## Arguments

``` json
{
    "clean": "{'description': ['Clean packages cache'], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "force": "{'description': ['Force package reinstall'], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "full_upgrade": "{'description': ['Upgrade all packages to their newer versions'], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "name": "{'description': ['Name of package to install/remove;', 'multiple names may be given, separated by commas']}",
    "state": "{'description': ['Intended state of the package'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "update_cache": "{'description': ["Update repository database. Can be run with other steps or on it's own."], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "upgrade": "{'description': ['Upgrade main packages to their newer versions'], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
}
```

## Examples


``` yaml

# install package foo
- pkgin:
    name: foo
    state: present

# Update database and install "foo" package
- pkgin:
    name: foo
    update_cache: yes

# remove package foo
- pkgin:
    name: foo
    state: absent

# remove packages foo and bar
- pkgin:
    name: foo,bar
    state: absent

# Update repositories as a separate step
- pkgin:
    update_cache: yes

# Upgrade main packages (equivalent to C(pkgin upgrade))
- pkgin:
    upgrade: yes

# Upgrade all packages (equivalent to C(pkgin full-upgrade))
- pkgin:
    full_upgrade: yes

# Force-upgrade all packages (equivalent to C(pkgin -F full-upgrade))
- pkgin:
    full_upgrade: yes
    force: yes

# clean packages cache (equivalent to C(pkgin clean))
- pkgin:
    clean: yes

```

## License

TODO

## Author Information
  - ['Larry Gilbert (L2G)', 'Shaun Zinck (@szinck)', 'Jasper Lievisse Adriaanse (@jasperla)']
  - ['Larry Gilbert (L2G)', 'Shaun Zinck (@szinck)', 'Jasper Lievisse Adriaanse (@jasperla)']
  - ['Larry Gilbert (L2G)', 'Shaun Zinck (@szinck)', 'Jasper Lievisse Adriaanse (@jasperla)']
