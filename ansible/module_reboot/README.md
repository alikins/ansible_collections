# Ansible module: ansible.module_reboot


Reboot a machine

## Description

Reboot a machine, wait for it to go down, come back up, and respond to commands.

## Requirements

TODO

## Arguments

``` json
{
    "connect_timeout": "{'description': ['Maximum seconds to wait for a successful connection to the managed hosts before trying again.', 'If unspecified, the default setting for the underlying connection plugin is used.'], 'type': 'int'}",
    "msg": "{'description': ['Message to display to users before reboot.'], 'default': 'Reboot initiated by Ansible', 'type': 'str'}",
    "post_reboot_delay": "{'description': ['Seconds to wait after the reboot was successful and the connection was re-established.', 'This is useful if you want wait for something to settle despite your connection already working.'], 'default': 0, 'type': 'int'}",
    "pre_reboot_delay": "{'description': ['Seconds for shutdown to wait before requesting reboot.', 'On Linux, macOS and OpenBSD, this is converted to minutes and rounded down. If less than 60, it will be set to 0.', 'On Solaris and FreeBSD, this will be seconds.'], 'default': 0, 'type': 'int'}",
    "reboot_timeout": "{'description': ['Maximum seconds to wait for machine to reboot and respond to a test command.', 'This timeout is evaluated separately for both network connection and test command success so the maximum execution time for the module is twice this amount.'], 'default': 600, 'type': 'int'}",
    "test_command": "{'description': ['Command to run on the rebooted host and expect success from to determine the machine is ready for further tasks.'], 'default': 'whoami', 'type': 'str'}",
}
```

## Examples


``` yaml

- name: Unconditionally reboot the machine with all defaults
  reboot:

- name: Reboot a slow machine that might have lots of updates to apply
  reboot:
    reboot_timeout: 3600

```

## License

TODO

## Author Information
  - ['Matt Davis (@nitzmahone)', 'Sam Doran (@samdoran)']
  - ['Matt Davis (@nitzmahone)', 'Sam Doran (@samdoran)']
