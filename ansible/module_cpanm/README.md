# Ansible module: ansible.module_cpanm


Manages Perl library dependencies

## Description

Manage Perl library dependencies.

## Requirements

TODO

## Arguments

``` json
{
    "executable": "{'description': ['Override the path to the cpanm executable'], 'version_added': '2.1'}",
    "from_path": "{'description': ['The local directory from where to install']}",
    "installdeps": "{'description': ['Only install dependencies'], 'type': 'bool', 'default': False, 'version_added': '2.0'}",
    "locallib": "{'description': ['Specify the install base to install modules'], 'type': 'bool', 'default': False}",
    "mirror": "{'description': ['Specifies the base URL for the CPAN mirror to use'], 'type': 'bool', 'default': False}",
    "mirror_only": "{'description': ["Use the mirror's index file instead of the CPAN Meta DB"], 'type': 'bool', 'default': False}",
    "name": "{'description': ['The name of the Perl library to install. You may use the "full distribution path", e.g.  MIYAGAWA/Plack-0.99_05.tar.gz'], 'aliases': ['pkg']}",
    "notest": "{'description': ['Do not run unit tests'], 'type': 'bool', 'default': False}",
    "system_lib": "{'description': ['Use this if you want to install modules to the system perl include path. You must be root or have "passwordless" sudo for this to work.', "This uses the cpanm commandline option '--sudo', which has nothing to do with ansible privilege escalation."], 'type': 'bool', 'default': False, 'version_added': '2.0', 'aliases': ['use_sudo']}",
    "version": "{'description': ['minimum version of perl module to consider acceptable'], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
}
```

## Examples


``` yaml

# install Dancer perl package
- cpanm:
    name: Dancer

# install version 0.99_05 of the Plack perl package
- cpanm:
    name: MIYAGAWA/Plack-0.99_05.tar.gz

# install Dancer into the specified locallib
- cpanm:
    name: Dancer
    locallib: /srv/webapps/my_app/extlib

# install perl dependencies from local directory
- cpanm:
    from_path: /srv/webapps/my_app/src/

# install Dancer perl package without running the unit tests in indicated locallib
- cpanm:
    name: Dancer
    notest: True
    locallib: /srv/webapps/my_app/extlib

# install Dancer perl package from a specific mirror
- cpanm:
    name: Dancer
    mirror: 'http://cpan.cpantesters.org/'

# install Dancer perl package into the system root path
- cpanm:
    name: Dancer
    system_lib: yes

# install Dancer if it's not already installed
# OR the installed version is older than version 1.0
- cpanm:
    name: Dancer
    version: '1.0'

```

## License

TODO

## Author Information
  - ['Franck Cuny (@fcuny)']
