# Ansible module: ansible.module_apt


Manages apt-packages

## Description

Manages I(apt) packages (such as for Debian/Ubuntu).

## Requirements

TODO

## Arguments

``` json
{
    "allow_unauthenticated": "{'description': ['Ignore if packages cannot be authenticated. This is useful for bootstrapping environments that manage their own apt-key setup.', 'C(allow_unauthenticated) is only supported with state: I(install)/I(present)'], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "autoclean": "{'description': ['If C(yes), cleans the local repository of retrieved package files that can no longer be downloaded.'], 'type': 'bool', 'default': False, 'version_added': '2.4'}",
    "autoremove": "{'description': ['If C(yes), remove unused dependency packages for all module states except I(build-dep). It can also be used as the only option.', 'Previous to version 2.4, autoclean was also an alias for autoremove, now it is its own separate command. See documentation for further information.'], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "cache_valid_time": "{'description': ['Update the apt cache if its older than the I(cache_valid_time). This option is set in seconds. As of Ansible 2.4, this sets I(update_cache=yes).'], 'default': 0}",
    "deb": "{'description': ['Path to a .deb package on the remote machine.', 'If :// in the path, ansible will attempt to download deb before installing. (Version added 2.1)'], 'required': False, 'version_added': '1.6'}",
    "default_release": "{'description': ['Corresponds to the C(-t) option for I(apt) and sets pin priorities']}",
    "dpkg_options": "{'description': ['Add dpkg options to apt command. Defaults to \'-o "Dpkg::Options::=--force-confdef" -o "Dpkg::Options::=--force-confold"\'', 'Options should be supplied as comma separated list'], 'default': 'force-confdef,force-confold'}",
    "force": "{'description': ['Corresponds to the C(--force-yes) to I(apt-get) and implies C(allow_unauthenticated: yes)', "This option will disable checking both the packages' signatures and the certificates of the web servers they are downloaded from.", 'This option *is not* the equivalent of passing the C(-f) flag to I(apt-get) on the command line', '**This is a destructive operation with the potential to destroy your system, and it should almost never be used.** Please also see C(man apt-get) for more information.'], 'type': 'bool', 'default': False}",
    "force_apt_get": "{'description': ['Force usage of apt-get instead of aptitude'], 'type': 'bool', 'default': False, 'version_added': '2.4'}",
    "install_recommends": "{'description': ['Corresponds to the C(--no-install-recommends) option for I(apt). C(yes) installs recommended packages.  C(no) does not install recommended packages. By default, Ansible will use the same defaults as the operating system. Suggested packages are never installed.'], 'aliases': ['install-recommends'], 'type': 'bool'}",
    "name": "{'description': ['A list of package names, like C(foo), or package specifier with version, like C(foo=1.0). Name wildcards (fnmatch) like C(apt*) and version wildcards like C(foo=1.0*) are also supported.'], 'aliases': ['package', 'pkg']}",
    "only_upgrade": "{'description': ['Only upgrade a package if it is already installed.'], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "purge": "{'description': ['Will force purging of configuration files if the module state is set to I(absent).'], 'type': 'bool', 'default': False}",
    "state": "{'description': ['Indicates the desired package state. C(latest) ensures that the latest version is installed. C(build-dep) ensures the package build dependencies are installed. C(fixed) attempt to correct a system with broken dependencies in place.'], 'default': 'present', 'choices': ['absent', 'build-dep', 'latest', 'present', 'fixed']}",
    "update_cache": "{'description': ['Run the equivalent of C(apt-get update) before the operation. Can be run as part of the package installation or as a separate step.'], 'type': 'bool', 'default': False}",
    "upgrade": "{'description': ['If yes or safe, performs an aptitude safe-upgrade.', 'If full, performs an aptitude full-upgrade.', 'If dist, performs an apt-get dist-upgrade.', 'Note: This does not upgrade a specific package, use state=latest for that.', 'Note: Since 2.4, apt-get is used as a fall-back if aptitude is not present.'], 'choices': ['dist', 'full', 'no', 'safe', 'yes'], 'default': 'no'}",
}
```

## Examples


``` yaml

- name: Update repositories cache and install "foo" package
  apt:
    name: foo
    update_cache: yes

- name: Install apache httpd but avoid starting it immediately (state=present is optional)
  apt:
    name: apache2
    state: present
  environment:
    RUNLEVEL: 1

- name: Remove "foo" package
  apt:
    name: foo
    state: absent

- name: Install the package "foo"
  apt:
    name: foo

- name: Install a list of packages
  apt:
    name: "{{ packages }}"
  vars:
    packages:
    - foo
    - foo-tools

- name: Install the version '1.00' of package "foo"
  apt:
    name: foo=1.00

- name: Update the repository cache and update package "nginx" to latest version using default release squeeze-backport
  apt:
    name: nginx
    state: latest
    default_release: squeeze-backports
    update_cache: yes

- name: Install latest version of "openjdk-6-jdk" ignoring "install-recommends"
  apt:
    name: openjdk-6-jdk
    state: latest
    install_recommends: no

- name: Upgrade all packages to the latest version
  apt:
    name: "*"
    state: latest

- name: Update all packages to the latest version
  apt:
    upgrade: dist

- name: Run the equivalent of "apt-get update" as a separate step
  apt:
    update_cache: yes

- name: Only run "update_cache=yes" if the last one is more than 3600 seconds ago
  apt:
    update_cache: yes
    cache_valid_time: 3600

- name: Pass options to dpkg on run
  apt:
    upgrade: dist
    update_cache: yes
    dpkg_options: 'force-confold,force-confdef'

- name: Install a .deb package
  apt:
    deb: /tmp/mypackage.deb

- name: Install the build dependencies for package "foo"
  apt:
    pkg: foo
    state: build-dep

- name: Install a .deb package from the internet.
  apt:
    deb: https://example.com/python-ppq_0.1-1_all.deb

- name: Remove useless packages from the cache
  apt:
    autoclean: yes

- name: Remove dependencies that are no longer required
  apt:
    autoremove: yes


```

## License

TODO

## Author Information
  - ['Matthew Williams (@mgwilliams)']
