# Ansible module: ansible.module_dnf


Manages packages with the *dnf* package manager

## Description

Installs, upgrade, removes, and lists packages and groups with the I(dnf) package manager.

## Requirements

TODO

## Arguments

``` json
{
    "allow_downgrade": "{'description': ['Specify if the named package and version is allowed to downgrade a maybe already installed higher version of that package. Note that setting allow_downgrade=True can make this module behave in a non-idempotent way. The task could end up with a set of packages that does not match the complete list of specified packages to install (because dependencies between the downgraded package and others can cause changes to the packages which were in the earlier transaction).'], 'type': 'bool', 'default': False, 'version_added': '2.7'}",
    "autoremove": "{'description': ['If C(yes), removes all "leaf" packages from the system that were originally installed as dependencies of user-installed packages but which are no longer required by any such package. Should be used alone or when state is I(absent)'], 'type': 'bool', 'default': False, 'version_added': '2.4'}",
    "bugfix": "{'description': ['If set to C(yes), and C(state=latest) then only installs updates that have been marked bugfix related.'], 'default': False, 'type': 'bool', 'version_added': '2.7'}",
    "conf_file": "{'description': ['The remote dnf configuration file to use for the transaction.']}",
    "disable_excludes": "{'description': ['Disable the excludes defined in DNF config files.', 'If set to C(all), disables all excludes.', 'If set to C(main), disable excludes defined in [main] in yum.conf.', 'If set to C(repoid), disable excludes defined for given repo id.'], 'choices': ['all', 'main', 'repoid'], 'version_added': '2.7'}",
    "disable_gpg_check": "{'description': ['Whether to disable the GPG checking of signatures of packages being installed. Has an effect only if state is I(present) or I(latest).'], 'type': 'bool', 'default': False}",
    "disable_plugin": "{'description': ['I(Plugin) name to disable for the install/update operation. The disabled plugins will not persist beyond the transaction.'], 'version_added': '2.7'}",
    "disablerepo": "{'description': ['I(Repoid) of repositories to disable for the install/update operation. These repos will not persist beyond the transaction. When specifying multiple repos, separate them with a ",".']}",
    "download_only": "{'description': ['Only download the packages, do not install them.'], 'default': False, 'type': 'bool', 'version_added': '2.7'}",
    "enable_plugin": "{'description': ['I(Plugin) name to enable for the install/update operation. The enabled plugin will not persist beyond the transaction.'], 'version_added': '2.7'}",
    "enablerepo": "{'description': ['I(Repoid) of repositories to enable for the install/update operation. These repos will not persist beyond the transaction. When specifying multiple repos, separate them with a ",".']}",
    "exclude": "{'description': ['Package name(s) to exclude when state=present, or latest. This can be a list or a comma separated string.'], 'version_added': '2.7'}",
    "install_repoquery": "{'description': ['This is effectively a no-op in DNF as it is not needed with DNF, but is an accepted parameter for feature parity/compatibility with the I(yum) module.'], 'type': 'bool', 'default': True, 'version_added': '2.7'}",
    "installroot": "{'description': ['Specifies an alternative installroot, relative to which all packages will be installed.'], 'version_added': '2.3', 'default': '/'}",
    "list": "{'description': ['Various (non-idempotent) commands for usage with C(/usr/bin/ansible) and I(not) playbooks. See examples.']}",
    "lock_poll": "{'description': ['Poll interval to wait for the dnf lockfile to be freed.', 'By default this is set to -1, if you set it to a positive integer it will enable to polling'], 'required': False, 'default': -1, 'type': 'int', 'version_added': '2.8'}",
    "lock_timeout": "{'description': ['Amount of time to wait for the dnf lockfile to be freed', 'This should be set along with C(lock_poll) to enable the lockfile polling.'], 'required': False, 'default': 10, 'type': 'int', 'version_added': '2.8'}",
    "name": "{'description': ["A list of package names, or package specifier with version, like C(name-1.0) When using state=latest, this can be '*' which means run: dnf -y update. You can also pass a url or a local path to a rpm file."], 'required': True, 'aliases': ['pkg']}",
    "releasever": "{'description': ['Specifies an alternative release from which all packages will be installed.'], 'version_added': '2.6'}",
    "security": "{'description': ['If set to C(yes), and C(state=latest) then only installs updates that have been marked security related.'], 'type': 'bool', 'default': False, 'version_added': '2.7'}",
    "skip_broken": "{'description': ['Skip packages with broken dependencies(devsolve) and are causing problems.'], 'type': 'bool', 'default': False, 'version_added': '2.7'}",
    "state": "{'description': ['Whether to install (C(present), C(latest)), or remove (C(absent)) a package.'], 'choices': ['absent', 'present', 'installed', 'removed', 'latest'], 'default': 'present'}",
    "update_cache": "{'description': ['Force yum to check if cache is out of date and redownload if needed. Has an effect only if state is I(present) or I(latest).'], 'type': 'bool', 'default': False, 'aliases': ['expire-cache'], 'version_added': '2.7'}",
    "update_only": "{'description': ['When using latest, only update installed packages. Do not install packages.', 'Has an effect only if state is I(latest)'], 'default': False, 'type': 'bool', 'version_added': '2.7'}",
    "validate_certs": "{'description': ['This only applies if using a https url as the source of the rpm. e.g. for localinstall. If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates as it avoids verifying the source site.'], 'type': 'bool', 'default': True, 'version_added': '2.7'}",
}
```

## Examples


``` yaml

- name: install the latest version of Apache
  dnf:
    name: httpd
    state: latest

- name: install the latest version of Apache and MariaDB
  dnf:
    name:
      - httpd
      - mariadb-server
    state: latest

- name: remove the Apache package
  dnf:
    name: httpd
    state: absent

- name: install the latest version of Apache from the testing repo
  dnf:
    name: httpd
    enablerepo: testing
    state: present

- name: upgrade all packages
  dnf:
    name: "*"
    state: latest

- name: install the nginx rpm from a remote repo
  dnf:
    name: 'http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm'
    state: present

- name: install nginx rpm from a local file
  dnf:
    name: /usr/local/src/nginx-release-centos-6-0.el6.ngx.noarch.rpm
    state: present

- name: install the 'Development tools' package group
  dnf:
    name: '@Development tools'
    state: present

- name: Autoremove unneeded packages installed as dependencies
  dnf:
    autoremove: yes

- name: Uninstall httpd but keep its dependencies
  dnf:
    name: httpd
    state: absent
    autoremove: no

```

## License

TODO

## Author Information
  - ['Igor Gnatenko (@ignatenkobrain) <i.gnatenko.brain@gmail.com>', 'Cristian van Ee (@DJMuggs) <cristian at cvee.org>', 'Berend De Schouwer (@berenddeschouwer)', 'Adam Miller (@maxamillion) <admiller@redhat.com>']
  - ['Igor Gnatenko (@ignatenkobrain) <i.gnatenko.brain@gmail.com>', 'Cristian van Ee (@DJMuggs) <cristian at cvee.org>', 'Berend De Schouwer (@berenddeschouwer)', 'Adam Miller (@maxamillion) <admiller@redhat.com>']
  - ['Igor Gnatenko (@ignatenkobrain) <i.gnatenko.brain@gmail.com>', 'Cristian van Ee (@DJMuggs) <cristian at cvee.org>', 'Berend De Schouwer (@berenddeschouwer)', 'Adam Miller (@maxamillion) <admiller@redhat.com>']
  - ['Igor Gnatenko (@ignatenkobrain) <i.gnatenko.brain@gmail.com>', 'Cristian van Ee (@DJMuggs) <cristian at cvee.org>', 'Berend De Schouwer (@berenddeschouwer)', 'Adam Miller (@maxamillion) <admiller@redhat.com>']
