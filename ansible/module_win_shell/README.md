# Ansible module: ansible.module_win_shell


Execute shell commands on target hosts

## Description

The C(win_shell) module takes the command name followed by a list of space-delimited arguments. It is similar to the M(win_command) module, but runs the command via a shell (defaults to PowerShell) on the target host.
For non-Windows targets, use the M(shell) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "chdir": "{'description': ['Set the specified path as the current working directory before executing a command'], 'type': 'path'}",
    "creates": "{'description': ['A path or path filter pattern; when the referenced path exists on the target host, the task will be skipped.'], 'type': 'path'}",
    "executable": "{'description': ['Change the shell used to execute the command (eg, C(cmd)).', 'The target shell must accept a C(/c) parameter followed by the raw command line to be executed.'], 'type': 'path'}",
    "free_form": "{'description': ['The C(win_shell) module takes a free form command to run.', "There is no parameter actually named 'free form'. See the examples!"], 'required': True}",
    "removes": "{'description': ['A path or path filter pattern; when the referenced path B(does not) exist on the target host, the task will be skipped.'], 'type': 'path'}",
    "stdin": "{'description': ['Set the stdin of the command directly to the specified value.'], 'version_added': '2.5'}",
}
```

## Examples


``` yaml

# Execute a command in the remote shell; stdout goes to the specified
# file on the remote.
- win_shell: C:\somescript.ps1 >> C:\somelog.txt

# Change the working directory to somedir/ before executing the command.
- win_shell: C:\somescript.ps1 >> C:\somelog.txt chdir=C:\somedir

# You can also use the 'args' form to provide the options. This command
# will change the working directory to somedir/ and will only run when
# somedir/somelog.txt doesn't exist.
- win_shell: C:\somescript.ps1 >> C:\somelog.txt
  args:
    chdir: C:\somedir
    creates: C:\somelog.txt

# Run a command under a non-Powershell interpreter (cmd in this case)
- win_shell: echo %HOMEDIR%
  args:
    executable: cmd
  register: homedir_out

- name: run multi-lined shell commands
  win_shell: |
    $value = Test-Path -Path C:\temp
    if ($value) {
        Remove-Item -Path C:\temp -Force
    }
    New-Item -Path C:\temp -ItemType Directory

- name: retrieve the input based on stdin
  win_shell: '$string = [Console]::In.ReadToEnd(); Write-Output $string.Trim()'
  args:
    stdin: Input message

```

## License

TODO

## Author Information
  - ['Matt Davis (@nitzmahone)']
