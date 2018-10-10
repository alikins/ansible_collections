# Ansible module: ansible.module_raw


Executes a low-down and dirty SSH command

## Description

Executes a low-down and dirty SSH command, not going through the module subsystem. This is useful and should only be done in a few cases. A common case is installing C(python) on a system without python installed by default. Another is speaking to any devices such as routers that do not have any Python installed. In any other case, using the M(shell) or M(command) module is much more appropriate. Arguments given to C(raw) are run directly through the configured remote shell. Standard output, error output and return code are returned when available. There is no change handler support for this module.
This module does not require python on the remote system, much like the M(script) module.
This module is also supported for Windows targets.

## Requirements

TODO

## Arguments

``` json
{
    "executable": "{'description': ['change the shell used to execute the command. Should be an absolute path to the executable.', 'when using privilege escalation (C(become)), a default shell will be assigned if one is not provided as privilege escalation requires a shell.'], 'required': False}",
    "free_form": "{'description': ["the raw module takes a free form command to run. There is no parameter actually named 'free form'; see the examples!"], 'required': True}",
}
```

## Examples


``` yaml

- name: Bootstrap a host without python2 installed
  raw: dnf install -y python2 python2-dnf libselinux-python

- name: Run a command that uses non-posix shell-isms (in this example /bin/sh doesn't handle redirection and wildcards together but bash does)
  raw: cat < /tmp/*txt
  args:
    executable: /bin/bash

- name: safely use templated variables. Always use quote filter to avoid injection issues.
  raw: "{{package_mgr|quote}} {{pkg_flags|quote}} install {{python|quote}}"

```

## License

TODO

## Author Information
  - ['Ansible Core Team', 'Michael DeHaan']
  - ['Ansible Core Team', 'Michael DeHaan']
