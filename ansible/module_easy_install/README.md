# Ansible module: ansible.module_easy_install


Installs Python libraries

## Description

Installs Python libraries, optionally in a I(virtualenv)

## Requirements

TODO

## Arguments

``` json
{
    "executable": "{'description': ['The explicit executable or a pathname to the executable to be used to run easy_install for a specific version of Python installed in the system. For example C(easy_install-3.3), if there are both Python 2.7 and 3.3 installations in the system and you want to run easy_install for the Python 3.3 installation.'], 'version_added': '1.3'}",
    "name": "{'description': ['A Python library name'], 'required': True}",
    "state": "{'version_added': '2.0', 'description': ['The desired state of the library. C(latest) ensures that the latest version is installed.'], 'choices': ['present', 'latest'], 'default': 'present'}",
    "virtualenv": "{'description': ['an optional I(virtualenv) directory path to install into. If the I(virtualenv) does not exist, it is created automatically']}",
    "virtualenv_command": "{'description': ['The command to create the virtual environment with. For example C(pyvenv), C(virtualenv), C(virtualenv2).'], 'default': 'virtualenv'}",
    "virtualenv_site_packages": "{'description': ['Whether the virtual environment will inherit packages from the global site-packages directory.  Note that if this setting is changed on an already existing virtual environment it will not have any effect, the environment must be deleted and newly created.'], 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

# Examples from Ansible Playbooks
- easy_install:
    name: pip
    state: latest

# Install Bottle into the specified virtualenv.
- easy_install:
    name: bottle
    virtualenv: /webapps/myapp/venv

```

## License

TODO

## Author Information
  - ['Matt Wright (@mattupstate)']
