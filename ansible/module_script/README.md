# Ansible module: ansible.module_script


Runs a local script on a remote node after transferring it

## Description

The C(script) module takes the script name followed by a list of space-delimited arguments.
The local script at path will be transferred to the remote node and then executed.
The given script will be processed through the shell environment on the remote node.
This module does not require python on the remote system, much like the M(raw) module.
This module is also supported for Windows targets.

## Requirements

TODO

## Arguments

``` json
{
    "chdir": "{'description': ['Change into this directory on the remote node before running the script.'], 'version_added': '2.4'}",
    "creates": "{'description': ['A filename on the remote node, when it already exists, this step will B(not) be run.'], 'version_added': '1.5'}",
    "decrypt": "{'description': ['This option controls the autodecryption of source files using vault.'], 'required': False, 'type': 'bool', 'default': True, 'version_added': '2.4'}",
    "executable": "{'description': ['Name or path of a executable to invoke the script with.'], 'version_added': '2.6'}",
    "free_form": "{'description': ['Path to the local script file followed by optional arguments.', "There is no parameter actually named 'free form', see the examples!"], 'required': True}",
    "removes": "{'description': ['A filename on the remote node, when it does not exist, this step will B(not) be run.'], 'version_added': '1.5'}",
}
```

## Examples


``` yaml

- name: Run a script with arguments
  script: /some/local/script.sh --some-argument 1234

- name: Run a script only if file.txt does not exist on the remote node
  script: /some/local/create_file.sh --some-argument 1234
  args:
    creates: /the/created/file.txt

- name: Run a script only if file.txt exists on the remote node
  script: /some/local/remove_file.sh --some-argument 1234
  args:
    removes: /the/removed/file.txt

- name: Run a script using an executable in a non-system path
  script: /some/local/script
  args:
    executable: /some/remote/executable

- name: Run a script using an executable in a system path
  script: /some/local/script.py
  args:
    executable: python3

```

## License

TODO

## Author Information
  - ['Ansible Core Team', 'Michael DeHaan']
  - ['Ansible Core Team', 'Michael DeHaan']
