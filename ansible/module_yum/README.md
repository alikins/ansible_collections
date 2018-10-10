# Ansible module: ansible.module_yum


Manages packages with the *yum* package manager

## Description

Installs, upgrade, downgrades, removes, and lists packages and groups with the I(yum) package manager.
This module only works on Python 2. If you require Python 3 support see the M(dnf) module.

## Requirements

TODO

## Arguments

``` json
{
    "allow_downgrade": "{'description': ['Specify if the named package and version is allowed to downgrade a maybe already installed higher version of that package. Note that setting allow_downgrade=True can make this module behave in a non-idempotent way. The task could end up with a set of packages that does not match the complete list of specified packages to install (because dependencies between the downgraded package and others can cause changes to the packages which were in the earlier transaction).'], 'type': 'bool', 'default': False, 'version_added': '2.4'}",
    "autoremove": "{'description': ['If C(yes), removes all "leaf" packages from the system that were originally installed as dependencies of user-installed packages but which are no longer required by any such package. Should be used alone or when state is I(absent)', 'NOTE: This feature requires yum >= 3.4.3 (RHEL/CentOS 7+)'], 'type': 'bool', 'default': False, 'version_added': '2.7'}",
    "bugfix": "{'description': ['If set to C(yes), and C(state=latest) then only installs updates that have been marked bugfix related.'], 'default': 'no', 'version_added': '2.6'}",
    "conf_file": "{'description': ['The remote yum configuration file to use for the transaction.']}",
    "disable_excludes": "{'description': ['Disable the excludes defined in YUM config files.', 'If set to C(all), disables all excludes.', 'If set to C(main), disable excludes defined in [main] in yum.conf.', 'If set to C(repoid), disable excludes defined for given repo id.'], 'choices': ['all', 'main', 'repoid'], 'version_added': '2.7'}",
    "disable_gpg_check": "{'description': ['Whether to disable the GPG checking of signatures of packages being installed. Has an effect only if state is I(present) or I(latest).'], 'type': 'bool', 'default': False}",
    "disable_plugin": "{'description': ['I(Plugin) name to disable for the install/update operation. The disabled plugins will not persist beyond the transaction.'], 'version_added': '2.5'}",
    "disablerepo": "{'description': ['I(Repoid) of repositories to disable for the install/update operation. These repos will not persist beyond the transaction. When specifying multiple repos, separate them with a C(",").', 'As of Ansible 2.7, this can alternatively be a list instead of C(",") separated string']}",
    "download_only": "{'description': ['Only download the packages, do not install them.'], 'default': False, 'type': 'bool', 'version_added': '2.7'}",
    "enable_plugin": "{'description': ['I(Plugin) name to enable for the install/update operation. The enabled plugin will not persist beyond the transaction.'], 'version_added': '2.5'}",
    "enablerepo": "{'description': ['I(Repoid) of repositories to enable for the install/update operation. These repos will not persist beyond the transaction. When specifying multiple repos, separate them with a C(",").', 'As of Ansible 2.7, this can alternatively be a list instead of C(",") separated string']}",
    "exclude": "{'description': ['Package name(s) to exclude when state=present, or latest'], 'version_added': '2.0'}",
    "installroot": "{'description': ['Specifies an alternative installroot, relative to which all packages will be installed.'], 'default': '/', 'version_added': '2.3'}",
    "list": "{'description': ['Package name to run the equivalent of yum list <package> against. In addition to listing packages, use can also list the following: C(installed), C(updates), C(available) and C(repos).']}",
    "lock_poll": "{'description': ['Poll interval to wait for the yum lockfile to be freed.', 'By default this is set to -1, if you set it to a positive integer it will enable to polling'], 'required': False, 'default': -1, 'type': 'int', 'version_added': '2.8'}",
    "lock_timeout": "{'description': ['Amount of time to wait for the yum lockfile to be freed', 'This should be set along with C(lock_poll) to enable the lockfile polling.'], 'required': False, 'default': 10, 'type': 'int', 'version_added': '2.8'}",
    "name": "{'description': ['A package name or package specifier with version, like C(name-1.0).', 'If a previous version is specified, the task also needs to turn C(allow_downgrade) on. See the C(allow_downgrade) documentation for caveats with downgrading packages.', "When using state=latest, this can be C('*') which means run C(yum -y update).", 'You can also pass a url or a local path to a rpm file (using state=present). To operate on several packages this can accept a comma separated list of packages or (as of 2.0) a list of packages.'], 'aliases': ['pkg']}",
    "releasever": "{'description': ['Specifies an alternative release from which all packages will be installed.'], 'version_added': '2.7'}",
    "security": "{'description': ['If set to C(yes), and C(state=latest) then only installs updates that have been marked security related.'], 'type': 'bool', 'default': False, 'version_added': '2.4'}",
    "skip_broken": "{'description': ['Skip packages with broken dependencies(devsolve) and are causing problems.'], 'type': 'bool', 'default': False, 'version_added': '2.3'}",
    "state": "{'description': ['Whether to install (C(present) or C(installed), C(latest)), or remove (C(absent) or C(removed)) a package.', 'C(present) and C(installed) will simply ensure that a desired package is installed.', "C(latest) will update the specified package if it's not of the latest available version.", 'C(absent) and C(removed) will remove the specified package.'], 'choices': ['absent', 'installed', 'latest', 'present', 'removed'], 'default': 'present'}",
    "update_cache": "{'description': ['Force yum to check if cache is out of date and redownload if needed. Has an effect only if state is I(present) or I(latest).'], 'type': 'bool', 'default': False, 'aliases': ['expire-cache'], 'version_added': '1.9'}",
    "update_only": "{'description': ['When using latest, only update installed packages. Do not install packages.', 'Has an effect only if state is I(latest)'], 'default': False, 'type': 'bool', 'version_added': '2.5'}",
    "use_backend": "{'description': ['This module supports C(yum) (as it always has), this is known as C(yum3)/C(YUM3)/C(yum-deprecated) by upstream yum developers. As of Ansible 2.7+, this module also supports C(YUM4), which is the "new yum" and it has an C(dnf) backend.', 'By default, this module will select the backend based on the C(ansible_pkg_mgr) fact.'], 'default': 'auto', 'choices': ['auto', 'yum', 'yum4', 'dnf'], 'version_added': '2.7'}",
    "validate_certs": "{'description': ['This only applies if using a https url as the source of the rpm. e.g. for localinstall. If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates as it avoids verifying the source site.', 'Prior to 2.1 the code worked as if this was set to C(yes).'], 'type': 'bool', 'default': True, 'version_added': '2.1'}",
}
```

## Examples


``` yaml

- name: install the latest version of Apache
  yum:
    name: httpd
    state: latest

- name: ensure a list of packages installed
  yum:
    name: "{{ packages }}"
  vars:
    packages:
    - httpd
    - httpd-tools

- name: remove the Apache package
  yum:
    name: httpd
    state: absent

- name: install the latest version of Apache from the testing repo
  yum:
    name: httpd
    enablerepo: testing
    state: present

- name: install one specific version of Apache
  yum:
    name: httpd-2.2.29-1.4.amzn1
    state: present

- name: upgrade all packages
  yum:
    name: '*'
    state: latest

- name: upgrade all packages, excluding kernel & foo related packages
  yum:
    name: '*'
    state: latest
    exclude: kernel*,foo*

- name: install the nginx rpm from a remote repo
  yum:
    name: http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm
    state: present

- name: install nginx rpm from a local file
  yum:
    name: /usr/local/src/nginx-release-centos-6-0.el6.ngx.noarch.rpm
    state: present

- name: install the 'Development tools' package group
  yum:
    name: "@Development tools"
    state: present

- name: install the 'Gnome desktop' environment group
  yum:
    name: "@^gnome-desktop-environment"
    state: present

- name: List ansible packages and register result to print with debug later.
  yum:
    list: ansible
  register: result

- name: Install package with multiple repos enabled
  yum:
    name: sos
    enablerepo: "epel,ol7_latest"

- name: Install package with multiple repos disabled
  yum:
    name: sos
    disablerepo: "epel,ol7_latest"

- name: Install a list of packages
  yum:
    name:
      - nginx
      - postgresql
      - postgresql-server
    state: present

- name: Download the nginx package but do not install it
  yum:
    name:
      - nginx
    state: latest
    download_only: true

```

## License

TODO

## Author Information
  - ['Ansible Core Team', 'Seth Vidal', 'Eduard Snesarev (@verm666)', 'Berend De Schouwer (@berenddeschouwer)', 'Abhijeet Kasurde (@Akasurde)', 'Adam Miller (@maxamillion)']
  - ['Ansible Core Team', 'Seth Vidal', 'Eduard Snesarev (@verm666)', 'Berend De Schouwer (@berenddeschouwer)', 'Abhijeet Kasurde (@Akasurde)', 'Adam Miller (@maxamillion)']
  - ['Ansible Core Team', 'Seth Vidal', 'Eduard Snesarev (@verm666)', 'Berend De Schouwer (@berenddeschouwer)', 'Abhijeet Kasurde (@Akasurde)', 'Adam Miller (@maxamillion)']
  - ['Ansible Core Team', 'Seth Vidal', 'Eduard Snesarev (@verm666)', 'Berend De Schouwer (@berenddeschouwer)', 'Abhijeet Kasurde (@Akasurde)', 'Adam Miller (@maxamillion)']
  - ['Ansible Core Team', 'Seth Vidal', 'Eduard Snesarev (@verm666)', 'Berend De Schouwer (@berenddeschouwer)', 'Abhijeet Kasurde (@Akasurde)', 'Adam Miller (@maxamillion)']
  - ['Ansible Core Team', 'Seth Vidal', 'Eduard Snesarev (@verm666)', 'Berend De Schouwer (@berenddeschouwer)', 'Abhijeet Kasurde (@Akasurde)', 'Adam Miller (@maxamillion)']
