# Ansible module: ansible.module_cli_command


Run a cli command on cli-based network devices

## Description

Sends a command to a network device and returns the result read from the device.

## Requirements

TODO

## Arguments

``` json
{
    "answer": "{'description': ['The answer to reply with if I(prompt) is matched. The value can be a single answer or a list of answer for multiple prompts. In case the command execution results in multiple prompts the sequence of the prompt and excepted answer should be in same order.'], 'required': False, 'type': 'list'}",
    "check_all": "{'description': ["By default if any one of the prompts mentioned in C(prompt) option is matched it won't check for other prompts. This boolean flag, that when set to I(True) will check for all the prompts mentioned in C(prompt) option in the given order. If the option is set to I(True) all the prompts should be received from remote host if not it will result in timeout."], 'type': 'bool', 'default': False}",
    "command": "{'description': ['The command to send to the remote network device.  The resulting output from the command is returned, unless I(sendonly) is set.'], 'required': True}",
    "prompt": "{'description': ['A single regex pattern or a sequence of patterns to evaluate the expected prompt from I(command).'], 'required': False, 'type': 'list'}",
    "sendonly": "{'description': ['The boolean value, that when set to true will send I(command) to the device but not wait for a result.'], 'type': 'bool', 'default': False, 'required': False}",
}
```

## Examples


``` yaml

- name: run show version on remote devices
  cli_command:
    command: show version

- name: run command with json formatted output
  cli_command:
    command: show version | json

- name: run command expecting user confirmation
  cli_command:
    command: commit replace
    prompt: This commit will replace or remove the entire running configuration
    answer: yes

- name: run config mode command and handle prompt/answer
  cli_command:
    command: "{{ item }}"
    prompt:
      - "Exit with uncommitted changes"
    answer: 'y'
  loop:
    - configure
    - set system syslog file test any any
    - exit

- name: multiple prompt, multiple answer (mandatory check for all prompts)
  cli_command:
    command: "copy sftp sftp://user@host//user/test.img"
    check_all: True
    prompt:
      - "Confirm download operation"
      - "Password"
      - "Do you want to change that to the standby image"
    answer:
      - 'y'
      - <password>
      - 'y'

```

## License

TODO

## Author Information
  - ['Nathaniel Case (@qalthos)']
