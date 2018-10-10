# Ansible module: ansible.module_gem


Manage Ruby gems

## Description

Manage installation and uninstallation of Ruby gems.

## Requirements

TODO

## Arguments

``` json
{
    "build_flags": "{'description': ['Allow adding build flags for gem compilation'], 'required': False, 'version_added': '2.0'}",
    "env_shebang": "{'description': ['Rewrite the shebang line on installed scripts to use /usr/bin/env.'], 'required': False, 'default': 'no', 'version_added': '2.2'}",
    "executable": "{'description': ['Override the path to the gem executable'], 'required': False, 'version_added': '1.4'}",
    "gem_source": "{'description': ['The path to a local gem used as installation source.'], 'required': False}",
    "include_dependencies": "{'description': ['Whether to include dependencies or not.'], 'required': False, 'type': 'bool', 'default': True}",
    "include_doc": "{'description': ['Install with or without docs.'], 'required': False, 'default': 'no', 'version_added': '2.0'}",
    "install_dir": "{'description': ['Install the gems into a specific directory. These gems will be independant from the global installed ones. Specifying this requires user_install to be false.'], 'required': False, 'version_added': '2.6'}",
    "name": "{'description': ['The name of the gem to be managed.'], 'required': True}",
    "pre_release": "{'description': ['Allow installation of pre-release versions of the gem.'], 'required': False, 'default': 'no', 'version_added': '1.6'}",
    "repository": "{'description': ['The repository from which the gem will be installed'], 'required': False, 'aliases': ['source']}",
    "state": "{'description': ['The desired state of the gem. C(latest) ensures that the latest version is installed.'], 'required': False, 'choices': ['present', 'absent', 'latest'], 'default': 'present'}",
    "user_install": "{'description': ["Install gem in user's local gems cache or for all users"], 'required': False, 'type': 'bool', 'default': True, 'version_added': '1.3'}",
    "version": "{'description': ['Version of the gem to be installed/removed.'], 'required': False}",
}
```

## Examples


``` yaml

# Installs version 1.0 of vagrant.
- gem:
    name: vagrant
    version: 1.0
    state: present

# Installs latest available version of rake.
- gem:
    name: rake
    state: latest

# Installs rake version 1.0 from a local gem on disk.
- gem:
    name: rake
    gem_source: /path/to/gems/rake-1.0.gem
    state: present

```

## License

TODO

## Author Information
  - ['Ansible Core Team', 'Johan Wiren']
  - ['Ansible Core Team', 'Johan Wiren']
