# Ansible module: ansible.module_win_psexec


Runs commands (remotely) as another (privileged) user

## Description

Run commands (remotely) through the PsExec service
Run commands as another (domain) user (with elevated privileges)

## Requirements

TODO

## Arguments

``` json
{
    "chdir": "{'description': ['Run the command from this (remote) directory.'], 'type': 'path'}",
    "command": "{'description': ['The command line to run through PsExec (limited to 260 characters).'], 'required': True}",
    "elevated": "{'description': ['Run the command with elevated privileges.'], 'type': 'bool', 'default': False}",
    "executable": "{'description': ['The location of the PsExec utility (in case it is not located in your PATH).'], 'type': 'path', 'default': 'psexec.exe'}",
    "hostnames": "{'description': ['The hostnames to run the command.', 'If not provided, the command is run locally.'], 'type': 'list'}",
    "interactive": "{'description': ['Run the program so that it interacts with the desktop on the remote system.'], 'type': 'bool', 'default': False}",
    "limited": "{'description': ['Run the command as limited user (strips the Administrators group and allows only privileges assigned to the Users group).'], 'type': 'bool', 'default': False}",
    "nobanner": "{'description': ['Do not display the startup banner and copyright message.', 'This only works for specific versions of the PsExec binary.'], 'type': 'bool', 'default': False, 'version_added': '2.4'}",
    "noprofile": "{'description': ["Run the command without loading the account's profile."], 'type': 'bool', 'default': False}",
    "password": "{'description': ['The password for the (remote) user to run the command as.', 'This is mandatory in order authenticate yourself.']}",
    "priority": "{'description': ['Used to run the command at a different priority.'], 'choices': ['background', 'low', 'belownormal', 'abovenormal', 'high', 'realtime']}",
    "session": "{'description': ['Specifies the session ID to use.', 'This parameter works in conjunction with I(interactive).', 'It has no effect when I(interactive) is set to C(no).'], 'type': 'int', 'version_added': '2.7'}",
    "system": "{'description': ['Run the remote command in the System account.'], 'type': 'bool', 'default': False}",
    "timeout": "{'description': ['The connection timeout in seconds'], 'type': 'int'}",
    "username": "{'description': ['The (remote) user to run the command as.', 'If not provided, the current user is used.']}",
    "wait": "{'description': ['Wait for the application to terminate.', 'Only use for non-interactive applications.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Test the PsExec connection to the local system (target node) with your user
  win_psexec:
    command: whoami.exe

- name: Run regedit.exe locally (on target node) as SYSTEM and interactively
  win_psexec:
    command: regedit.exe
    interactive: yes
    system: yes

- name: Run the setup.exe installer on multiple servers using the Domain Administrator
  win_psexec:
    command: E:\setup.exe /i /IACCEPTEULA
    hostnames:
    - remote_server1
    - remote_server2
    username: DOMAIN\Administrator
    password: some_password
    priority: high

- name: Run PsExec from custom location C:\Program Files\sysinternals\
  win_psexec:
    command: netsh advfirewall set allprofiles state off
    executable: C:\Program Files\sysinternals\psexec.exe
    hostnames: [ remote_server ]
    password: some_password
    priority: low

```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)']
