# Ansible module: ansible.module_expect


Executes a command and responds to prompts

## Description

The C(expect) module executes a command and responds to prompts.
The given command will be executed on all selected nodes. It will not be processed through the shell, so variables like C($HOME) and operations like C("<"), C(">"), C("|"), and C("&") will not work.

## Requirements

TODO

## Arguments

``` json
{
    "chdir": "{'description': ['Change into this directory before running the command.']}",
    "command": "{'description': ['The command module takes command to run.'], 'required': True}",
    "creates": "{'description': ['A filename, when it already exists, this step will B(not) be run.']}",
    "echo": "{'description': ['Whether or not to echo out your response strings.'], 'default': False}",
    "removes": "{'description': ['A filename, when it does not exist, this step will B(not) be run.']}",
    "responses": "{'description': ['Mapping of expected string/regex and string to respond with. If the response is a list, successive matches return successive responses. List functionality is new in 2.1.'], 'required': True}",
    "timeout": "{'description': ['Amount of time in seconds to wait for the expected strings. Use C(null) to disable timeout.'], 'default': 30}",
}
```

## Examples


``` yaml

- name: Case insensitive password string match
  expect:
    command: passwd username
    responses:
      (?i)password: "MySekretPa$$word"
  # you don't want to show passwords in your logs
  no_log: true

- name: Generic question with multiple different responses
  expect:
    command: /path/to/custom/command
    responses:
      Question:
        - response1
        - response2
        - response3

```

## License

TODO

## Author Information
  - ['Matt Martz (@sivel)']
