# Ansible module: ansible.module_git_config


Read and write git configuration

## Description

The C(git_config) module changes git configuration by invoking 'git config'. This is needed if you don't want to use M(template) for the entire git config file (e.g. because you need to change just C(user.email) in /etc/.git/config).  Solutions involving M(command) are cumbersome or don't work correctly in check mode.

## Requirements

TODO

## Arguments

``` json
{
    "list_all": "{'description': ['List all settings (optionally limited to a given I(scope))'], 'type': 'bool', 'default': False}",
    "name": "{'description': ['The name of the setting. If no value is supplied, the value will be read from the config if it has been set.']}",
    "repo": "{'description': ['Path to a git repository for reading and writing values from a specific repo.']}",
    "scope": "{'description': ['Specify which scope to read/set values from. This is required when setting config values. If this is set to local, you must also specify the repo parameter. It defaults to system only when not using I(list_all)=yes.'], 'choices': ['local', 'global', 'system']}",
    "value": "{'description': ['When specifying the name of a single setting, supply a value to set that setting to the given value.']}",
}
```

## Examples


``` yaml

# Set some settings in ~/.gitconfig
- git_config:
    name: alias.ci
    scope: global
    value: commit

- git_config:
    name: alias.st
    scope: global
    value: status

# Or system-wide:
- git_config:
    name: alias.remotev
    scope: system
    value: remote -v

- git_config:
    name: core.editor
    scope: global
    value: vim

# scope=system is the default
- git_config:
    name: alias.diffc
    value: diff --cached

- git_config:
    name: color.ui
    value: auto

# Make etckeeper not complain when invoked by cron
- git_config:
    name: user.email
    repo: /etc
    scope: local
    value: 'root@{{ ansible_fqdn }}'

# Read individual values from git config
- git_config:
    name: alias.ci
    scope: global

# scope: system is also assumed when reading values, unless list_all=yes
- git_config:
    name: alias.diffc

# Read all values from git config
- git_config:
    list_all: yes
    scope: global

# When list_all=yes and no scope is specified, you get configuration from all scopes
- git_config:
    list_all: yes

# Specify a repository to include local settings
- git_config:
    list_all: yes
    repo: /path/to/repo.git

```

## License

TODO

## Author Information
  - ['Matthew Gamble (@djmattyg007)', 'Marius Gedminas']
  - ['Matthew Gamble (@djmattyg007)', 'Marius Gedminas']
