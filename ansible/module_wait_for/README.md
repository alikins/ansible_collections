# Ansible module: ansible.module_wait_for


Waits for a condition before continuing

## Description

You can wait for a set amount of time C(timeout), this is the default if nothing is specified or just C(timeout) is specified. This does not produce an error.
Waiting for a port to become available is useful for when services are not immediately available after their init scripts return which is true of certain Java application servers. It is also useful when starting guests with the M(virt) module and needing to pause until they are ready.
This module can also be used to wait for a regex match a string to be present in a file.
In 1.6 and later, this module can also be used to wait for a file to be available or absent on the filesystem.
In 1.8 and later, this module can also be used to wait for active connections to be closed before continuing, useful if a node is being rotated out of a load balancer pool.
For Windows targets, use the M(win_wait_for) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "active_connection_states": "{'description': ['The list of TCP connection states which are counted as active connections.'], 'default': ['ESTABLISHED', 'FIN_WAIT1', 'FIN_WAIT2', 'SYN_RECV', 'SYN_SENT', 'TIME_WAIT'], 'version_added': '2.3'}",
    "connect_timeout": "{'description': ['Maximum number of seconds to wait for a connection to happen before closing and retrying.'], 'default': 5}",
    "delay": "{'description': ['Number of seconds to wait before starting to poll.'], 'default': 0}",
    "exclude_hosts": "{'version_added': '1.8', 'description': ['List of hosts or IPs to ignore when looking for active TCP connections for C(drained) state.']}",
    "host": "{'description': ['A resolvable hostname or IP address to wait for.'], 'default': '127.0.0.1'}",
    "msg": "{'version_added': '2.4', 'description': ['This overrides the normal error message from a failure to meet the required conditions.']}",
    "path": "{'version_added': '1.4', 'description': ['Path to a file on the filesystem that must exist before continuing.']}",
    "port": "{'description': ['Port number to poll.']}",
    "search_regex": "{'version_added': '1.4', 'description': ['Can be used to match a string in either a file or a socket connection.', 'Defaults to a multiline regex.']}",
    "sleep": "{'version_added': '2.3', 'default': 1, 'description': ['Number of seconds to sleep between checks, before 2.3 this was hardcoded to 1 second.']}",
    "state": "{'description': ['Either C(present), C(started), or C(stopped), C(absent), or C(drained).', 'When checking a port C(started) will ensure the port is open, C(stopped) will check that it is closed, C(drained) will check for active connections.', 'When checking for a file or a search string C(present) or C(started) will ensure that the file or string is present before continuing, C(absent) will check that file is absent or removed.'], 'choices': ['absent', 'drained', 'present', 'started', 'stopped'], 'default': 'started'}",
    "timeout": "{'description': ['Maximum number of seconds to wait for, when used with another condition it will force an error.', 'When used without other conditions it is equivalent of just sleeping.'], 'default': 300}",
}
```

## Examples


``` yaml

- name: sleep for 300 seconds and continue with play
  wait_for: timeout=300
  delegate_to: localhost

- name: Wait for port 8000 to become open on the host, don't start checking for 10 seconds
  wait_for:
    port: 8000
    delay: 10

- name: Waits for port 8000 of any IP to close active connections, don't start checking for 10 seconds
  wait_for:
    host: 0.0.0.0
    port: 8000
    delay: 10
    state: drained

- name: Wait for port 8000 of any IP to close active connections, ignoring connections for specified hosts
  wait_for:
    host: 0.0.0.0
    port: 8000
    state: drained
    exclude_hosts: 10.2.1.2,10.2.1.3

- name: Wait until the file /tmp/foo is present before continuing
  wait_for:
    path: /tmp/foo

- name: Wait until the string "completed" is in the file /tmp/foo before continuing
  wait_for:
    path: /tmp/foo
    search_regex: completed

- name: Wait until the lock file is removed
  wait_for:
    path: /var/lock/file.lock
    state: absent

- name: Wait until the process is finished and pid was destroyed
  wait_for:
    path: /proc/3466/status
    state: absent

- name: Output customized message when failed
  wait_for:
    path: /tmp/foo
    state: present
    msg: Timeout to find file /tmp/foo

# Don't assume the inventory_hostname is resolvable and delay 10 seconds at start
- name: Wait 300 seconds for port 22 to become open and contain "OpenSSH"
  wait_for:
    port: 22
    host: '{{ (ansible_ssh_host|default(ansible_host))|default(inventory_hostname) }}'
    search_regex: OpenSSH
    delay: 10
  connection: local

# Same as above but you normally have ansible_connection set in inventory, which overrides 'connection'
- name: Wait 300 seconds for port 22 to become open and contain "OpenSSH"
  wait_for:
    port: 22
    host: '{{ (ansible_ssh_host|default(ansible_host))|default(inventory_hostname) }}'
    search_regex: OpenSSH
    delay: 10
  vars:
    ansible_connection: local

```

## License

TODO

## Author Information
  - ['Jeroen Hoekx (@jhoekx)', 'John Jarvis (@jarv)', 'Andrii Radyk (@AnderEnder)']
  - ['Jeroen Hoekx (@jhoekx)', 'John Jarvis (@jarv)', 'Andrii Radyk (@AnderEnder)']
  - ['Jeroen Hoekx (@jhoekx)', 'John Jarvis (@jarv)', 'Andrii Radyk (@AnderEnder)']
