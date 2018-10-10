# Ansible module: ansible.module_shell


Execute shell commands on targets

## Description

The C(shell) module takes the command name followed by a list of space-delimited arguments.
It is almost exactly like the M(command) module but runs the command through a shell (C(/bin/sh)) on the remote node.
For Windows targets, use the M(win_shell) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "chdir": "{'description': ['Change into this directory before running the command.']}",
    "creates": "{'description': ['A filename, when it already exists, this step will B(not) be run.']}",
    "executable": "{'description': ['Change the shell used to execute the command.', 'This expects an absolute path to the executable.']}",
    "free_form": "{'description': ['The shell module takes a free form command to run, as a string.', "There is no actual parameter named 'free form'.", 'See the examples on how to use this module.'], 'required': True}",
    "removes": "{'description': ['A filename, when it does not exist, this step will B(not) be run.']}",
    "stdin": "{'description': ['Set the stdin of the command directly to the specified value.'], 'version_added': '2.4'}",
    "warn": "{'description': ['Enable or disable task warnings.'], 'type': 'bool', 'default': True, 'version_added': '1.8'}",
}
```

## Examples


``` yaml

- name: Execute the command in remote shell; stdout goes to the specified file on the remote.
  shell: somescript.sh >> somelog.txt

- name: Change the working directory to somedir/ before executing the command.
  shell: somescript.sh >> somelog.txt
  args:
    chdir: somedir/

# You can also use the 'args' form to provide the options.
- name: This command will change the working directory to somedir/ and will only run when somedir/somelog.txt doesn't exist.
  shell: somescript.sh >> somelog.txt
  args:
    chdir: somedir/
    creates: somelog.txt

- name: Run a command that uses non-posix shell-isms (in this example /bin/sh doesn't handle redirection and wildcards together but bash does)
  shell: cat < /tmp/*txt
  args:
    executable: /bin/bash

- name: Run a command using a templated variable (always use quote filter to avoid injection)
  shell: cat {{ myfile|quote }}

# You can use shell to run other executables to perform actions inline
- name: Run expect to wait for a successful PXE boot via out-of-band CIMC
  shell: |
    set timeout 300
    spawn ssh admin@{{ cimc_host }}

    expect "password:"
    send "{{ cimc_password }}\n"

    expect "\n{{ cimc_name }}"
    send "connect host\n"

    expect "pxeboot.n12"
    send "\n"

    exit 0
  args:
    executable: /usr/bin/expect
  delegate_to: localhost

# Disabling warnings
- name: Using curl to connect to a host via SOCKS proxy (unsupported in uri). Ordinarily this would throw a warning.
  shell: curl --socks5 localhost:9000 http://www.ansible.com
  args:
    warn: no

```

## License

TODO

## Author Information
  - ['Ansible Core Team', 'Michael DeHaan']
  - ['Ansible Core Team', 'Michael DeHaan']
