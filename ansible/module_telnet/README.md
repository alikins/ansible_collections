# Ansible module: ansible.module_telnet


Executes a low-down and dirty telnet command

## Description

Executes a low-down and dirty telnet command, not going through the module subsystem.
This is mostly to be used for enabling ssh on devices that only have telnet enabled by default.

## Requirements

TODO

## Arguments

``` json
{
    "command": "{'description': ['List of commands to be executed in the telnet session.'], 'required': True, 'aliases': ['commands']}",
    "host": "{'description': ['The host/target on which to execute the command'], 'required': False, 'default': 'remote_addr'}",
    "login_prompt": "{'description': ['Login or username prompt to expect'], 'required': False, 'default': 'login: '}",
    "password": "{'description': ['The password for login']}",
    "password_prompt": "{'description': ['Login or username prompt to expect'], 'required': False, 'default': 'Password: '}",
    "pause": "{'description': ['Seconds to pause between each command issued'], 'required': False, 'default': 1}",
    "port": "{'description': ['Remote port to use'], 'default': 23}",
    "prompts": "{'description': ['List of prompts expected before sending next command'], 'required': False, 'default': ['$']}",
    "send_newline": "{'description': ['Sends a newline character upon successful connection to start the terminal session.'], 'required': False, 'default': False, 'type': 'bool', 'version_added': '2.7'}",
    "timeout": "{'description': ['timeout for remote operations'], 'default': 120}",
    "user": "{'description': ['The user for login'], 'required': False, 'default': 'remote_user'}",
}
```

## Examples


``` yaml

- name: send configuration commands to IOS
  telnet:
    user: cisco
    password: cisco
    login_prompt: "Username: "
    prompts:
      - "[>|#]"
    command:
      - terminal length 0
      - configure terminal
      - hostname ios01

- name: run show commands
  telnet:
    user: cisco
    password: cisco
    login_prompt: "Username: "
    prompts:
      - "[>|#]"
    command:
      - terminal length 0
      - show version

```

## License

TODO

## Author Information
  - ['Ansible Core Team']
