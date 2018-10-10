# Ansible module: ansible.module_svr4pkg


Manage Solaris SVR4 packages

## Description

Manages SVR4 packages on Solaris 10 and 11.
These were the native packages on Solaris <= 10 and are available as a legacy feature in Solaris 11.
Note that this is a very basic packaging system. It will not enforce dependencies on install or remove.

## Requirements

TODO

## Arguments

``` json
{
    "category": "{'description': ['Install/Remove category instead of a single package.'], 'required': False, 'type': 'bool', 'version_added': '1.6'}",
    "name": "{'description': ['Package name, e.g. C(SUNWcsr)'], 'required': True}",
    "proxy": "{'description': ['HTTP[s] proxy to be used if C(src) is a URL.']}",
    "response_file": "{'description': ['Specifies the location of a response file to be used if package expects input on install. (added in Ansible 1.4)'], 'required': False}",
    "src": "{'description': ['Specifies the location to install the package from. Required when C(state=present).', "Can be any path acceptable to the C(pkgadd) command's C(-d) option. e.g.: C(somefile.pkg), C(/dir/with/pkgs), C(http:/server/mypkgs.pkg).", 'If using a file or directory, they must already be accessible by the host. See the M(copy) module for a way to get them there.']}",
    "state": "{'description': ['Whether to install (C(present)), or remove (C(absent)) a package.', 'If the package is to be installed, then I(src) is required.', "The SVR4 package system doesn't provide an upgrade operation. You need to uninstall the old, then install the new package."], 'required': True, 'choices': ['present', 'absent']}",
    "zone": "{'description': ['Whether to install the package only in the current zone, or install it into all zones.', 'The installation into all zones works only if you are working with the global zone.'], 'required': False, 'default': 'all', 'choices': ['current', 'all'], 'version_added': '1.6'}",
}
```

## Examples


``` yaml

# Install a package from an already copied file
- svr4pkg:
    name: CSWcommon
    src: /tmp/cswpkgs.pkg
    state: present

# Install a package directly from an http site
- svr4pkg:
    name: CSWpkgutil
    src: 'http://get.opencsw.org/now'
    state: present
    zone: current

# Install a package with a response file
- svr4pkg:
    name: CSWggrep
    src: /tmp/third-party.pkg
    response_file: /tmp/ggrep.response
    state: present

# Ensure that a package is not installed.
- svr4pkg:
    name: SUNWgnome-sound-recorder
    state: absent

# Ensure that a category is not installed.
- svr4pkg:
    name: FIREFOX
    state: absent
    category: true

```

## License

TODO

## Author Information
  - ['Boyd Adamson (@brontitall)']
