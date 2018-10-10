# Ansible module: ansible.module_win_chocolatey


Manage packages using chocolatey

## Description

Manage packages using Chocolatey (U(http://chocolatey.org/)).
If Chocolatey is missing from the system, the module will install it.
List of packages can be found at U(http://chocolatey.org/packages).

## Requirements

TODO

## Arguments

``` json
{
    "allow_empty_checksums": "{'description': ['Allow empty checksums to be used for downloaded resource from non-secure locations.', 'Use M(win_chocolatey_feature) with the name C(allowEmptyChecksums) to control this option globally.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "allow_prerelease": "{'description': ['Allow the installation of pre-release packages.', 'If I(state) is C(latest), the latest pre-release package will be installed.'], 'type': 'bool', 'default': False, 'version_added': '2.6'}",
    "architecture": "{'description': ['Force Chocolatey to install the package of a specific process architecture.', 'When setting C(x86), will ensure Chocolatey installs the x86 package even when on an x64 bit OS.'], 'choices': ['default', 'x86'], 'default': 'default', 'version_added': '2.7'}",
    "force": "{'description': ['Forces the install of a package, even if it already is installed.', 'Using I(force) will cause Ansible to always report that a change was made.'], 'type': 'bool', 'default': False}",
    "ignore_checksums": "{'description': ['Ignore the checksums provided by the package.', 'Use M(win_chocolatey_feature) with the name C(checksumFiles) to control this option globally.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "ignore_dependencies": "{'description': ['Ignore dependencies, only install/upgrade the package itself.'], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "install_args": "{'description': ['Arguments to pass to the native installer.', 'These are arguments that are passed directly to the installer the Chocolatey package runs, this is generally an advanced option.'], 'type': 'str', 'version_added': '2.1'}",
    "name": "{'description': ['Name of the package(s) to be installed.', 'Set to C(all) to run the action on all the installed packages.'], 'required': True, 'type': 'list'}",
    "package_params": "{'description': ['Parameters to pass to the package.', 'These are parameters specific to the Chocolatey package and are generally documented by the package itself.', 'Before Ansible 2.7, this option was just I(params).'], 'type': 'str', 'version_added': '2.1', 'aliases': ['params']}",
    "proxy_password": "{'description': ['Proxy password used to install Chocolatey and the package.', 'This value is exposed as a command argument and any privileged account can see this value when the module is running Chocolatey, define the password on the global config level with M(win_chocolatey_config) with name C(proxyPassword) to avoid this.'], 'type': 'str', 'version_added': '2.4'}",
    "proxy_url": "{'description': ['Proxy URL used to install chocolatey and the package.', 'Use M(win_chocolatey_config) with the name C(proxy) to control this option globally.'], 'type': 'str', 'version_added': '2.4'}",
    "proxy_username": "{'description': ['Proxy username used to install Chocolatey and the package.', 'Before Ansible 2.7, users with double quote characters C(") would need to be escaped with C(\\) beforehand. This is no longer necessary.', 'Use M(win_chocolatey_config) with the name C(proxyUser) to control this option globally.'], 'type': 'str', 'version_added': '2.4'}",
    "skip_scripts": "{'description': ['Do not run I(chocolateyInstall.ps1) or I(chocolateyUninstall.ps1) scripts when installing a package.'], 'type': 'bool', 'default': False, 'version_added': '2.4'}",
    "source": "{'description': ['Specify the source to retrieve the package from.', 'Use M(win_chocolatey_source) to manage global sources.', 'This value can either be the URL to a Chocolatey feed, a path to a folder containing C(.nupkg) packages or the name of a source defined by M(win_chocolatey_source).', 'This value is also used when Chocolatey is not installed as the location of the install.ps1 script and only supports URLs for this case.'], 'type': 'str'}",
    "source_password": "{'description': ['The password for I(source_username).', 'This value is exposed as a command argument and any privileged account can see this value when the module is running Chocolatey, define the credentials with a source with M(win_chocolatey_source) to avoid this.'], 'type': 'str', 'version_added': '2.7'}",
    "source_username": "{'description': ['A username to use with I(source) when accessing a feed that requires authentication.', 'It is recommended you define the credentials on a source with M(win_chocolatey_source) instead of passing it per task.'], 'type': 'str', 'version_added': '2.7'}",
    "state": "{'description': ['State of the package on the system.', 'When C(absent), will ensure the package is not installed.', 'When C(present), will ensure the package is installed.', 'When C(downgrade), will allow Chocolatey to downgrade a package if I(version) is older than the installed version.', 'When C(latest), will ensure the package is installed to the latest available version.', 'When C(reinstalled), will uninstall and reinstall the package.'], 'choices': ['absent', 'downgrade', 'latest', 'present', 'reinstalled'], 'default': 'present', 'type': 'str'}",
    "timeout": "{'description': ['The time to allow chocolatey to finish before timing out.'], 'type': 'int', 'default': 2700, 'version_added': '2.3', 'aliases': ['execution_timeout']}",
    "validate_certs": "{'description': ['Used when downloading the Chocolatey install script if Chocolatey is not already installed, this does not affect the Chocolatey package install process.', 'When C(no), no SSL certificates will be validated.', 'This should only be used on personally controlled sites using self-signed certificate.'], 'type': 'bool', 'default': True, 'version_added': '2.7'}",
    "version": "{'description': ['Specific version of the package to be installed.', 'Ignored when I(state) is set to C(absent).'], 'type': 'str'}",
}
```

## Examples


``` yaml

- name: Install git
  win_chocolatey:
    name: git
    state: present

- name: Upgrade installed packages
  win_chocolatey:
    name: all
    state: latest

- name: Install notepadplusplus version 6.6
  win_chocolatey:
    name: notepadplusplus
    version: '6.6'

- name: Install notepadplusplus 32 bit version
  win_chocolatey:
    name: notepadplusplus
    architecture: x86

- name: Install git from specified repository
  win_chocolatey:
    name: git
    source: https://someserver/api/v2/

- name: Install git from a pre configured source (win_chocolatey_source)
  win_chocolatey:
    name: git
    source: internal_repo

- name: ensure Chocolatey itself is installed and use internal repo as source
  win_chocolatey:
    name: chocolatey
    source: http://someserver/chocolatey

- name: Uninstall git
  win_chocolatey:
    name: git
    state: absent

- name: Install multiple packages
  win_chocolatey:
    name:
    - procexp
    - putty
    - windirstat
    state: present

- name: Install multiple packages sequentially
  win_chocolatey:
    name: '{{ item }}'
    state: present
  with_items:
  - procexp
  - putty
  - windirstat

- name: uninstall multiple packages
  win_chocolatey:
    name:
    - procexp
    - putty
    - windirstat
    state: absent

- name: Install curl using proxy
  win_chocolatey:
    name: curl
    proxy_url: http://proxy-server:8080/
    proxy_username: joe
    proxy_password: p@ssw0rd

- name: Install a package that requires 'become'
  win_chocolatey:
    name: officepro2013
  become: yes
  become_user: Administrator
  become_method: runas

```

## License

TODO

## Author Information
  - ['Trond Hindenes (@trondhindenes)', 'Peter Mounce (@petemounce)', 'Pepe Barbe (@elventear)', 'Adam Keech (@smadam813)', 'Pierre Templier (@ptemplier)', 'Jordan Borean (@jborean93)']
  - ['Trond Hindenes (@trondhindenes)', 'Peter Mounce (@petemounce)', 'Pepe Barbe (@elventear)', 'Adam Keech (@smadam813)', 'Pierre Templier (@ptemplier)', 'Jordan Borean (@jborean93)']
  - ['Trond Hindenes (@trondhindenes)', 'Peter Mounce (@petemounce)', 'Pepe Barbe (@elventear)', 'Adam Keech (@smadam813)', 'Pierre Templier (@ptemplier)', 'Jordan Borean (@jborean93)']
  - ['Trond Hindenes (@trondhindenes)', 'Peter Mounce (@petemounce)', 'Pepe Barbe (@elventear)', 'Adam Keech (@smadam813)', 'Pierre Templier (@ptemplier)', 'Jordan Borean (@jborean93)']
  - ['Trond Hindenes (@trondhindenes)', 'Peter Mounce (@petemounce)', 'Pepe Barbe (@elventear)', 'Adam Keech (@smadam813)', 'Pierre Templier (@ptemplier)', 'Jordan Borean (@jborean93)']
  - ['Trond Hindenes (@trondhindenes)', 'Peter Mounce (@petemounce)', 'Pepe Barbe (@elventear)', 'Adam Keech (@smadam813)', 'Pierre Templier (@ptemplier)', 'Jordan Borean (@jborean93)']
