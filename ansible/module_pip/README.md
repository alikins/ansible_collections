# Ansible module: ansible.module_pip


Manages Python library dependencies

## Description

Manage Python library dependencies. To use this module, one of the following keys is required: C(name) or C(requirements).

## Requirements

TODO

## Arguments

``` json
{
    "chdir": "{'description': ['cd into this directory before running the command'], 'version_added': '1.3'}",
    "editable": "{'description': ['Pass the editable flag.'], 'type': 'bool', 'default': False, 'version_added': '2.0'}",
    "executable": "{'description': ["The explicit executable or a pathname to the executable to be used to run pip for a specific version of Python installed in the system. For example C(pip-3.3), if there are both Python 2.7 and 3.3 installations in the system and you want to run pip for the Python 3.3 installation. It cannot be specified together with the 'virtualenv' parameter (added in 2.1). By default, it will take the appropriate version for the python interpreter use by ansible, e.g. pip3 on python 3, and pip2 or pip on python 2."], 'version_added': '1.3'}",
    "extra_args": "{'description': ['Extra arguments passed to pip.']}",
    "name": "{'description': ['The name of a Python library to install or the url(bzr+,hg+,git+,svn+) of the remote package.', 'This can be a list (since 2.2) and contain version specifiers (since 2.7).']}",
    "requirements": "{'description': ['The path to a pip requirements file, which should be local to the remote system. File can be specified as a relative path if using the chdir option.']}",
    "state": "{'description': ['The state of module', "The 'forcereinstall' option is only available in Ansible 2.1 and above."], 'choices': ['absent', 'forcereinstall', 'latest', 'present'], 'default': 'present'}",
    "umask": "{'description': ['The system umask to apply before installing the pip package. This is useful, for example, when installing on systems that have a very restrictive umask by default (e.g., 0077) and you want to pip install packages which are to be used by all users. Note that this requires you to specify desired umask mode in octal, with a leading 0 (e.g., 0077).'], 'version_added': '2.1'}",
    "version": "{'description': ['The version number to install of the Python library specified in the I(name) parameter.']}",
    "virtualenv": "{'description': ["An optional path to a I(virtualenv) directory to install into. It cannot be specified together with the 'executable' parameter (added in 2.1). If the virtualenv does not exist, it will be created before installing packages. The optional virtualenv_site_packages, virtualenv_command, and virtualenv_python options affect the creation of the virtualenv."]}",
    "virtualenv_command": "{'description': ['The command or a pathname to the command to create the virtual environment with. For example C(pyvenv), C(virtualenv), C(virtualenv2), C(~/bin/virtualenv), C(/usr/local/bin/virtualenv).'], 'default': 'virtualenv'}",
    "virtualenv_python": "{'description': ['The Python executable used for creating the virtual environment. For example C(python3.5), C(python2.7). When not specified, the Python version used to run the ansible module is used. This parameter should not be used when C(virtualenv_command) is using C(pyvenv) or the C(-m venv) module.'], 'version_added': '2.0'}",
    "virtualenv_site_packages": "{'description': ['Whether the virtual environment will inherit packages from the global site-packages directory.  Note that if this setting is changed on an already existing virtual environment it will not have any effect, the environment must be deleted and newly created.'], 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

# Install (Bottle) python package.
- pip:
    name: bottle

# Install (Bottle) python package on version 0.11.
- pip:
    name: bottle==0.11

# Install (bottle) python package with version specifiers
- pip:
    name: bottle>0.10,<0.20,!=0.11

# Install multi python packages with version specifiers
- pip:
    name:
      - django>1.11.0,<1.12.0
      - bottle>0.10,<0.20,!=0.11

# Install (MyApp) using one of the remote protocols (bzr+,hg+,git+,svn+). You do not have to supply '-e' option in extra_args.
- pip:
    name: svn+http://myrepo/svn/MyApp#egg=MyApp

# Install MyApp using one of the remote protocols (bzr+,hg+,git+).
- pip:
    name: git+http://myrepo/app/MyApp

# Install (MyApp) from local tarball
- pip:
    name: file:///path/to/MyApp.tar.gz

# Install (Bottle) into the specified (virtualenv), inheriting none of the globally installed modules
- pip:
    name: bottle
    virtualenv: /my_app/venv

# Install (Bottle) into the specified (virtualenv), inheriting globally installed modules
- pip:
    name: bottle
    virtualenv: /my_app/venv
    virtualenv_site_packages: yes

# Install (Bottle) into the specified (virtualenv), using Python 2.7
- pip:
    name: bottle
    virtualenv: /my_app/venv
    virtualenv_command: virtualenv-2.7

# Install (Bottle) within a user home directory.
- pip:
    name: bottle
    extra_args: --user

# Install specified python requirements.
- pip:
    requirements: /my_app/requirements.txt

# Install specified python requirements in indicated (virtualenv).
- pip:
    requirements: /my_app/requirements.txt
    virtualenv: /my_app/venv

# Install specified python requirements and custom Index URL.
- pip:
    requirements: /my_app/requirements.txt
    extra_args: -i https://example.com/pypi/simple

# Install (Bottle) for Python 3.3 specifically,using the 'pip-3.3' executable.
- pip:
    name: bottle
    executable: pip-3.3

# Install (Bottle), forcing reinstallation if it's already installed
- pip:
    name: bottle
    state: forcereinstall

# Install (Bottle) while ensuring the umask is 0022 (to ensure other users can use it)
- pip:
    name: bottle
    umask: "0022"
  become: True

```

## License

TODO

## Author Information
  - ['Matt Wright (@mattupstate)']
