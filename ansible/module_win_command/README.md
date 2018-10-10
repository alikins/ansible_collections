# Ansible module: ansible.module_win_command


Executes a command on a remote Windows node

## Description

The C(win_command) module takes the command name followed by a list of space-delimited arguments.
The given command will be executed on all selected nodes. It will not be processed through the shell, so variables like C($env:HOME) and operations like C("<"), C(">"), C("|"), and C(";") will not work (use the M(win_shell) module if you need these features).
For non-Windows targets, use the M(command) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "chdir": "{'description': ['Set the specified path as the current working directory before executing a command.'], 'type': 'path'}",
    "creates": "{'description': ['A path or path filter pattern; when the referenced path exists on the target host, the task will be skipped.'], 'type': 'path'}",
    "free_form": "{'description': ['The C(win_command) module takes a free form command to run.', "There is no parameter actually named 'free form'. See the examples!"], 'required': True}",
    "removes": "{'description': ['A path or path filter pattern; when the referenced path B(does not) exist on the target host, the task will be skipped.'], 'type': 'path'}",
    "stdin": "{'description': ['Set the stdin of the command directly to the specified value.'], 'version_added': '2.5'}",
}
```

## Examples


``` yaml

- name: Save the result of 'whoami' in 'whoami_out'
  win_command: whoami
  register: whoami_out

- name: Run command that only runs if folder exists and runs from a specific folder
  win_command: wbadmin -backupTarget:C:\backup\
  args:
    chdir: C:\somedir\
    creates: C:\backup\

- name: Run an executable and send data to the stdin for the executable
  win_command: powershell.exe -
  args:
    stdin: Write-Host test

```

## License

TODO

## Author Information
  - ['Matt Davis (@nitzmahone)']
