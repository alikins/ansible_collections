# Ansible module: ansible.module_portage


Package manager for Gentoo

## Description

Manages Gentoo packages

## Requirements

TODO

## Arguments

``` json
{
    "changed_use": "{'description': ['Include installed packages where USE flags have changed, except when', 'flags that the user has not enabled are added or removed', '(--changed-use)'], 'type': 'bool', 'default': False, 'version_added': 1.8}",
    "deep": "{'description': ['Consider the entire dependency tree of packages (--deep)'], 'type': 'bool', 'default': False}",
    "depclean": "{'description': ['Remove packages not needed by explicitly merged packages (--depclean)', "If no package is specified, clean up the world's dependencies", 'Otherwise, --depclean serves as a dependency aware version of --unmerge'], 'type': 'bool', 'default': False}",
    "getbinpkg": "{'description': ['Prefer packages specified at PORTAGE_BINHOST in make.conf'], 'type': 'bool', 'default': False}",
    "jobs": "{'description': ['Specifies the number of packages to build simultaneously.', 'Since version 2.6: Value of 0 or False resets any previously added', '--jobs setting values'], 'version_added': 2.3}",
    "keepgoing": "{'description': ['Continue as much as possible after an error.'], 'type': 'bool', 'default': False, 'version_added': 2.3}",
    "loadavg": "{'description': ['Specifies that no new builds should be started if there are', 'other builds running and the load average is at least LOAD', 'Since version 2.6: Value of 0 or False resets any previously added', '--load-average setting values'], 'version_added': 2.3}",
    "newuse": "{'description': ['Include installed packages where USE flags have changed (--newuse)'], 'type': 'bool', 'default': False}",
    "nodeps": "{'description': ['Only merge packages but not their dependencies (--nodeps)'], 'type': 'bool', 'default': False}",
    "noreplace": "{'description': ['Do not re-emerge installed packages (--noreplace)'], 'type': 'bool', 'default': False}",
    "oneshot": "{'description': ['Do not add the packages to the world file (--oneshot)'], 'type': 'bool', 'default': False}",
    "onlydeps": "{'description': ["Only merge packages' dependencies but not the packages (--onlydeps)"], 'type': 'bool', 'default': False}",
    "package": "{'description': ['Package atom or set, e.g. C(sys-apps/foo) or C(>foo-2.13) or C(@world)']}",
    "quiet": "{'description': ['Run emerge in quiet mode (--quiet)'], 'type': 'bool', 'default': False}",
    "quietbuild": "{'description': ['Redirect all build output to logs alone, and do not display it', 'on stdout (--quiet-build)'], 'type': 'bool', 'default': False, 'version_added': 2.6}",
    "quietfail": "{'description': ['Suppresses display of the build log on stdout (--quiet-fail)', 'Only the die message and the path of the build log will be', 'displayed on stdout.'], 'type': 'bool', 'default': False, 'version_added': 2.6}",
    "state": "{'description': ['State of the package atom'], 'default': 'present', 'choices': ['present', 'installed', 'emerged', 'absent', 'removed', 'unmerged', 'latest']}",
    "sync": "{'description': ['Sync package repositories first', 'If yes, perform "emerge --sync"', 'If web, perform "emerge-webrsync"'], 'choices': ['web', 'yes', 'no']}",
    "update": "{'description': ['Update packages to the best version available (--update)'], 'type': 'bool', 'default': False}",
    "usepkgonly": "{'description': ['Merge only binaries (no compiling). This sets getbinpkg=yes.'], 'type': 'bool', 'default': False}",
    "verbose": "{'description': ['Run emerge in verbose mode (--verbose)'], 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

# Make sure package foo is installed
- portage:
    package: foo
    state: present

# Make sure package foo is not installed
- portage:
    package: foo
    state: absent

# Update package foo to the "latest" version ( os specific alternative to latest )
- portage:
    package: foo
    update: yes

# Install package foo using PORTAGE_BINHOST setup
- portage:
    package: foo
    getbinpkg: yes

# Re-install world from binary packages only and do not allow any compiling
- portage:
    package: '@world'
    usepkgonly: yes

# Sync repositories and update world
- portage:
    package: '@world'
    update: yes
    deep: yes
    sync: yes

# Remove unneeded packages
- portage:
    depclean: yes

# Remove package foo if it is not explicitly needed
- portage:
    package: foo
    state: absent
    depclean: yes

```

## License

TODO

## Author Information
  - ['William L Thomson Jr (@wltjr)', 'Yap Sok Ann (@sayap)', 'Andrew Udvare']
  - ['William L Thomson Jr (@wltjr)', 'Yap Sok Ann (@sayap)', 'Andrew Udvare']
  - ['William L Thomson Jr (@wltjr)', 'Yap Sok Ann (@sayap)', 'Andrew Udvare']
