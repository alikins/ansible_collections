# Ansible module: ansible.module_win_reboot


Reboot a windows machine

## Description

Reboot a Windows machine, wait for it to go down, come back up, and respond to commands.

## Requirements

TODO

## Arguments

``` json
{
    "connect_timeout": "{'description': ['Maximum seconds to wait for a single successful TCP connection to the WinRM endpoint before trying again.'], 'type': 'int', 'default': 5, 'aliases': ['connect_timeout_sec']}",
    "msg": "{'description': ['Message to display to users.'], 'type': 'str', 'default': 'Reboot initiated by Ansible'}",
    "post_reboot_delay": "{'description': ['Seconds to wait after the reboot was successful and the connection was re-established.', 'This is useful if you want wait for something to settle despite your connection already working.'], 'type': 'int', 'default': 0, 'version_added': '2.4', 'aliases': ['post_reboot_delay_sec']}",
    "pre_reboot_delay": "{'description': ['Seconds for shutdown to wait before requesting reboot.'], 'type': 'int', 'default': 2, 'aliases': ['pre_reboot_delay_sec']}",
    "reboot_timeout": "{'description': ['Maximum seconds to wait for machine to re-appear on the network and respond to a test command.', 'This timeout is evaluated separately for both network appearance and test command success (so maximum clock time is actually twice this value).'], 'type': 'int', 'default': 600, 'aliases': ['reboot_timeout_sec']}",
    "shutdown_timeout": "{'description': ['Maximum seconds to wait for shutdown to occur.', 'Increase this timeout for very slow hardware, large update applications, etc.', 'This option has been removed since Ansible 2.5 as the win_reboot behavior has changed.'], 'type': 'int', 'default': 600, 'aliases': ['shutdown_timeout_sec']}",
    "test_command": "{'description': ['Command to expect success for to determine the machine is ready for management.'], 'type': 'str', 'default': 'whoami'}",
}
```

## Examples


``` yaml

- name: Reboot the machine with all defaults
  win_reboot:

- name: Reboot a slow machine that might have lots of updates to apply
  win_reboot:
    reboot_timeout: 3600

# Install a Windows feature and reboot if necessary
- name: Install IIS Web-Server
  win_feature:
    name: Web-Server
  register: iis_install

- name: Reboot when Web-Server feature requires it
  win_reboot:
  when: iis_install.reboot_required

# One way to ensure the system is reliable, is to add a delay before running the next task
- name: Reboot a machine that takes time to settle after being booted
  win_reboot:
    post_reboot_delay: 120

# Alternatively, you can set WinRM to a delayed startup
- name: Ensure WinRM starts when the system has settled and is ready to work reliably
  win_service:
    name: WinRM
    start_mode: delayed

# Or you can make win_reboot validate exactly what you need to work before running the next task
- name: Validate that the netlogon service has started, before running the next task
  win_reboot:
    test_command: 'exit (Get-Service -Name Netlogon).Status -ne "Running"'

```

## License

TODO

## Author Information
  - ['Matt Davis (@nitzmahone)']
