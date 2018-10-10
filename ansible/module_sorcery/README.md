# Ansible module: ansible.module_sorcery


Package manager for Source Mage GNU/Linux

## Description

Manages "spells" on Source Mage GNU/Linux using I(sorcery) toolchain

## Requirements

TODO

## Arguments

``` json
{
    "cache_valid_time": "{'description': ['Time in seconds to invalidate grimoire collection on update', 'especially useful for SCM and rsync grimoires', 'makes sense only in pair with C(update_cache)']}",
    "depends": "{'description': ["Comma-separated list of _optional_ dependencies to build a spell (or make sure it is built) with; use +/- in front of dependency to turn it on/off ('+' is optional though)", "this option is ignored if C(name) parameter is equal to '*' or contains more than one spell", "providers must be supplied in the form recognized by Sorcery, e.g. 'openssl(SSL)'"]}",
    "name": "{'description': ['Name of the spell', 'multiple names can be given, separated by commas', "special value '*' in conjunction with states C(latest) or C(rebuild) will update or rebuild the whole system respectively"], 'aliases': ['spell']}",
    "state": "{'description': ['Whether to cast, dispel or rebuild a package', 'state C(cast) is an equivalent of C(present), not C(latest)', 'state C(latest) always triggers C(update_cache=yes)', 'state C(rebuild) implies cast of all specified spells, not only those existed before'], 'choices': ['present', 'latest', 'absent', 'cast', 'dispelled', 'rebuild'], 'default': 'present'}",
    "update": "{'description': ['Whether or not to update sorcery scripts at the very first stage'], 'type': 'bool', 'default': False}",
    "update_cache": "{'description': ['Whether or not to update grimoire collection before casting spells'], 'type': 'bool', 'default': False, 'aliases': ['update_codex']}",
}
```

## Examples


``` yaml

# Make sure spell 'foo' is installed
- sorcery:
    spell: foo
    state: present

# Make sure spells 'foo', 'bar' and 'baz' are removed
- sorcery:
    spell: foo,bar,baz
    state: absent

# Make sure spell 'foo' with dependencies 'bar' and 'baz' is installed
- sorcery:
    spell: foo
    depends: bar,baz
    state: present

# Make sure spell 'foo' with 'bar' and without 'baz' dependencies is installed
- sorcery:
    spell: foo
    depends: +bar,-baz
    state: present

# Make sure spell 'foo' with libressl (providing SSL) dependency is installed
- sorcery:
    spell: foo
    depends: libressl(SSL)
    state: present

# Playbook: make sure spells with/without required dependencies (if any) are installed
- sorcery:
    name: "{{ item.spell }}"
    depends: "{{ item.depends | default(None) }}"
    state: present
  with_items:
    - { spell: 'vifm', depends: '+file,-gtk+2' }
    - { spell: 'fwknop', depends: 'gpgme' }
    - { spell: 'pv,tnftp,tor' }

# Install the latest version of spell 'foo' using regular glossary
- sorcery:
    name: foo
    state: latest

# Rebuild spell 'foo'
- sorcery:
    spell: foo
    state: rebuild

# Rebuild the whole system, but update Sorcery and Codex first
- sorcery:
    spell: '*'
    state: rebuild
    update: yes
    update_cache: yes

# Refresh the grimoire collection if it's 1 day old using native sorcerous alias
- sorcery:
    update_codex: yes
    cache_valid_time: 86400

# Update only Sorcery itself
- sorcery:
    update: yes

```

## License

TODO

## Author Information
  - ['Vlad Glagolev (@vaygr)']
