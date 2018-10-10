# Ansible module: ansible.module_zypper


Manage packages on SUSE and openSUSE

## Description

Manage packages on SUSE and openSUSE using the zypper and rpm tools.

## Requirements

TODO

## Arguments

``` json
{
    "disable_gpg_check": "{'description': ['Whether to disable to GPG signature checking of the package signature being installed. Has an effect only if state is I(present) or I(latest).'], 'required': False, 'default': False, 'type': 'bool'}",
    "disable_recommends": "{'version_added': '1.8', 'description': ["Corresponds to the C(--no-recommends) option for I(zypper). Default behavior (C(yes)) modifies zypper's default behavior; C(no) does install recommended packages."], 'required': False, 'default': True, 'type': 'bool'}",
    "extra_args": "{'version_added': '2.4', 'required': False, 'description': ['Add additional options to C(zypper) command.', 'Options should be supplied in a single line as if given in the command line.']}",
    "extra_args_precommand": "{'version_added': '2.6', 'required': False, 'description': ['Add additional global target options to C(zypper).', 'Options should be supplied in a single line as if given in the command line.']}",
    "force": "{'version_added': '2.2', 'description': ['Adds C(--force) option to I(zypper). Allows to downgrade packages and change vendor or architecture.'], 'required': False, 'default': False, 'type': 'bool'}",
    "name": "{'description': ['Package name C(name) or package specifier or a list of either.', 'Can include a version like C(name=1.0), C(name>3.4) or C(name<=2.7). If a version is given, C(oldpackage) is implied and zypper is allowed to update the package within the version range given.', 'You can also pass a url or a local path to a rpm file.', "When using state=latest, this can be '*', which updates all installed packages."], 'required': True, 'aliases': ['pkg']}",
    "oldpackage": "{'version_added': '2.2', 'description': ['Adds C(--oldpackage) option to I(zypper). Allows to downgrade packages with less side-effects than force. This is implied as soon as a version is specified as part of the package name.'], 'required': False, 'default': False, 'type': 'bool'}",
    "state": "{'description': ['C(present) will make sure the package is installed. C(latest)  will make sure the latest version of the package is installed. C(absent)  will make sure the specified package is not installed. C(dist-upgrade) will make sure the latest version of all installed packages from all enabled repositories is installed.', "When using C(dist-upgrade), I(name) should be C('*')."], 'required': False, 'choices': ['present', 'latest', 'absent', 'dist-upgrade'], 'default': 'present'}",
    "type": "{'description': ['The type of package to be operated on.'], 'required': False, 'choices': ['package', 'patch', 'pattern', 'product', 'srcpackage', 'application'], 'default': 'package', 'version_added': '2.0'}",
    "update_cache": "{'version_added': '2.2', 'description': ['Run the equivalent of C(zypper refresh) before the operation. Disabled in check mode.'], 'required': False, 'default': False, 'type': 'bool', 'aliases': ['refresh']}",
}
```

## Examples


``` yaml

# Install "nmap"
- zypper:
    name: nmap
    state: present

# Install apache2 with recommended packages
- zypper:
    name: apache2
    state: present
    disable_recommends: no

# Apply a given patch
- zypper:
    name: openSUSE-2016-128
    state: present
    type: patch

# Remove the "nmap" package
- zypper:
    name: nmap
    state: absent

# Install the nginx rpm from a remote repo
- zypper:
    name: 'http://nginx.org/packages/sles/12/x86_64/RPMS/nginx-1.8.0-1.sles12.ngx.x86_64.rpm'
    state: present

# Install local rpm file
- zypper:
    name: /tmp/fancy-software.rpm
    state: present

# Update all packages
- zypper:
    name: '*'
    state: latest

# Apply all available patches
- zypper:
    name: '*'
    state: latest
    type: patch

# Perform a dist-upgrade with additional arguments
- zypper:
    name: '*'
    state: dist-upgrade
    extra_args: '--no-allow-vendor-change --allow-arch-change'

# Refresh repositories and update package "openssl"
- zypper:
    name: openssl
    state: present
    update_cache: yes

# Install specific version (possible comparisons: <, >, <=, >=, =)
- zypper:
    name: 'docker>=1.10'
    state: present

# Wait 20 seconds to acquire the lock before failing
- zypper:
    name: mosh
    state: present
  environment:
    ZYPP_LOCK_TIMEOUT: 20

```

## License

TODO

## Author Information
  - ['Patrick Callahan (@dirtyharrycallahan)', 'Alexander Gubin (@alxgu)', "Thomas O'Donnell (@andytom)", 'Robin Roth (@robinro)', 'Andrii Radyk (@AnderEnder)']
  - ['Patrick Callahan (@dirtyharrycallahan)', 'Alexander Gubin (@alxgu)', "Thomas O'Donnell (@andytom)", 'Robin Roth (@robinro)', 'Andrii Radyk (@AnderEnder)']
  - ['Patrick Callahan (@dirtyharrycallahan)', 'Alexander Gubin (@alxgu)', "Thomas O'Donnell (@andytom)", 'Robin Roth (@robinro)', 'Andrii Radyk (@AnderEnder)']
  - ['Patrick Callahan (@dirtyharrycallahan)', 'Alexander Gubin (@alxgu)', "Thomas O'Donnell (@andytom)", 'Robin Roth (@robinro)', 'Andrii Radyk (@AnderEnder)']
  - ['Patrick Callahan (@dirtyharrycallahan)', 'Alexander Gubin (@alxgu)', "Thomas O'Donnell (@andytom)", 'Robin Roth (@robinro)', 'Andrii Radyk (@AnderEnder)']
