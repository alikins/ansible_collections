#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['stableinterface'],
                    'supported_by': 'core'}

DOCUMENTATION = r'''
---
module: win_reboot
short_description: Reboot a windows machine
description:
- Reboot a Windows machine, wait for it to go down, come back up, and respond to commands.
version_added: '2.1'
options:
  pre_reboot_delay:
    description:
    - Seconds for shutdown to wait before requesting reboot.
    type: int
    default: 2
    aliases: [ pre_reboot_delay_sec ]
  post_reboot_delay:
    description:
    - Seconds to wait after the reboot was successful and the connection was re-established.
    - This is useful if you want wait for something to settle despite your connection already working.
    type: int
    default: 0
    version_added: '2.4'
    aliases: [ post_reboot_delay_sec ]
  shutdown_timeout:
    description:
    - Maximum seconds to wait for shutdown to occur.
    - Increase this timeout for very slow hardware, large update applications, etc.
    - This option has been removed since Ansible 2.5 as the win_reboot behavior has changed.
    type: int
    default: 600
    aliases: [ shutdown_timeout_sec ]
  reboot_timeout:
    description:
    - Maximum seconds to wait for machine to re-appear on the network and respond to a test command.
    - This timeout is evaluated separately for both network appearance and test command success (so maximum clock time is actually twice this value).
    type: int
    default: 600
    aliases: [ reboot_timeout_sec ]
  connect_timeout:
    description:
    - Maximum seconds to wait for a single successful TCP connection to the WinRM endpoint before trying again.
    type: int
    default: 5
    aliases: [ connect_timeout_sec ]
  test_command:
    description:
    - Command to expect success for to determine the machine is ready for management.
    type: str
    default: whoami
  msg:
    description:
    - Message to display to users.
    type: str
    default: Reboot initiated by Ansible
notes:
- If a shutdown was already scheduled on the system, C(win_reboot) will abort the scheduled shutdown and enforce its own shutdown.
- Beware that when C(win_reboot) returns, the Windows system may not have settled yet and some base services could be in limbo.
  This can result in unexpected behavior. Check the examples for ways to mitigate this.
- For non-Windows targets, use the M(reboot) module instead.
author:
- Matt Davis (@nitzmahone)
'''

EXAMPLES = r'''
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
'''

RETURN = r'''
rebooted:
  description: true if the machine was rebooted
  returned: always
  type: boolean
  sample: true
elapsed:
  description: The number of seconds that elapsed waiting for the system to be rebooted.
  returned: always
  type: float
  sample: 23.2
'''
