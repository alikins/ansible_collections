# Ansible module: ansible.module_command


Execute commands on targets

## Description

The C(command) module takes the command name followed by a list of space-delimited arguments.
The given command will be executed on all selected nodes. It will not be processed through the shell, so variables like C($HOME) and operations like C("<"), C(">"), C("|"), C(";") and C("&") will not work (use the M(shell) module if you need these features).
For Windows targets, use the M(win_command) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "argv": "{'description': ['Allows the user to provide the command as a list vs. a string.  Only the string or the list form can be provided, not both.  One or the other must be provided.'], 'version_added': '2.6'}",
    "chdir": "{'description': ['Change into this directory before running the command.']}",
    "creates": "{'description': ["A filename or (since 2.0) glob pattern. If it already exists, this step B(won't) be run."]}",
    "free_form": "{'description': ['The command module takes a free form command to run.', "There is no actual parameter named 'free form'.", 'See the examples on how to use this module.'], 'required': True}",
    "removes": "{'description': ['A filename or (since 2.0) glob pattern. If it already exists, this step B(will) be run.']}",
    "stdin": "{'description': ['Set the stdin of the command directly to the specified value.'], 'version_added': '2.4'}",
    "warn": "{'description': ['Enable or disable task warnings.'], 'type': 'bool', 'default': True, 'version_added': '1.8'}",
}
```

## Examples


``` yaml

- name: return motd to registered var
  command: cat /etc/motd
  register: mymotd

- name: Run the command if the specified file does not exist.
  command: /usr/bin/make_database.sh arg1 arg2
  args:
    creates: /path/to/database

# You can also use the 'args' form to provide the options.
- name: This command will change the working directory to somedir/ and will only run when /path/to/database doesn't exist.
  command: /usr/bin/make_database.sh arg1 arg2
  args:
    chdir: somedir/
    creates: /path/to/database

- name: use argv to send the command as a list.  Be sure to leave command empty
  command:
  args:
    argv:
      - echo
      - testing

- name: safely use templated variable to run command. Always use the quote filter to avoid injection issues.
  command: cat {{ myfile|quote }}
  register: myoutput

```

## License

TODO

## Author Information
  - ['Ansible Core Team', 'Michael DeHaan']
  - ['Ansible Core Team', 'Michael DeHaan']
