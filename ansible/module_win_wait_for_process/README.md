# Ansible module: ansible.module_win_wait_for_process


Waits for a process to exist or not exist before continuing

## Description

Waiting for a process to start or stop.
This is useful when Windows services behave poorly and do not enumerate external dependencies in their manifest.

## Requirements

TODO

## Arguments

``` json
{
    "owner": "{'description': ['The owner of the process.', 'Requires PowerShell version 4.0 or newer.'], 'type': 'str'}",
    "pid": "{'description': ['The PID of the process.'], 'type': 'int'}",
    "post_wait_delay": "{'description': ['Seconds to wait after checking for processes.'], 'type': 'int', 'default': 0}",
    "pre_wait_delay": "{'description': ['Seconds to wait before checking processes.'], 'type': 'int', 'default': 0}",
    "process_min_count": "{'description': ['Minimum number of process matching the supplied pattern to satisfy C(present) condition.', 'Only applies to C(present).'], 'type': 'int', 'default': 1}",
    "process_name_exact": "{'description': ['The name of the process(es) for which to wait.'], 'type': 'str'}",
    "process_name_pattern": "{'description': ['RegEx pattern matching desired process(es).'], 'type': 'str'}",
    "sleep": "{'description': ['Number of seconds to sleep between checks.', 'Only applies when waiting for a process to start.  Waiting for a process to start does not have a native non-polling mechanism. Waiting for a stop uses native PowerShell and does not require polling.'], 'type': 'int', 'default': 1}",
    "state": "{'description': ['When checking for a running process C(present) will block execution until the process exists, or until the timeout has been reached. C(absent) will block execution untile the processs no longer exists, or until the timeout has been reached.', 'When waiting for C(present), the module will return changed only if the process was not present on the initial check but became present on subsequent checks.', 'If, while waiting for C(absent), new processes matching the supplied pattern are started, these new processes will not be included in the action.'], 'type': 'str', 'default': 'present', 'choices': ['absent', 'present']}",
    "timeout": "{'description': ['The maximum number of seconds to wait for a for a process to start or stop before erroring out.'], 'type': 'int', 'default': 300}",
}
```

## Examples


``` yaml

- name: Wait 300 seconds for all Oracle VirtualBox processes to stop. (VBoxHeadless, VirtualBox, VBoxSVC)
  win_wait_for_process:
    process_name: 'v(irtual)?box(headless|svc)?'
    state: absent
    timeout: 500

- name: Wait 300 seconds for 3 instances of cmd to start, waiting 5 seconds between each check
  win_wait_for_process:
    process_name_exact: cmd
    state: present
    timeout: 500
    sleep: 5
    process_min_count: 3

```

## License

TODO

## Author Information
  - ['Charles Crossan (@crossan007)']
