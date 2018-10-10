# Ansible module: ansible.module_win_wait_for


Waits for a condition before continuing

## Description

You can wait for a set amount of time C(timeout), this is the default if nothing is specified.
Waiting for a port to become available is useful for when services are not immediately available after their init scripts return which is true of certain Java application servers.
You can wait for a file to exist or not exist on the filesystem.
This module can also be used to wait for a regex match string to be present in a file.
You can wait for active connections to be closed before continuing on a local port.

## Requirements

TODO

## Arguments

``` json
{
    "connect_timeout": "{'description': ['The maximum number of seconds to wait for a connection to happen before closing and retrying.'], 'type': 'int', 'default': 5}",
    "delay": "{'description': ['The number of seconds to wait before starting to poll.'], 'type': 'int'}",
    "exclude_hosts": "{'description': ['The list of hosts or IPs to ignore when looking for active TCP connections when C(state=drained).'], 'type': 'list'}",
    "host": "{'description': ['A resolvable hostname or IP address to wait for.', "If C(state=drained) then it will only check for connections on the IP specified, you can use '0.0.0.0' to use all host IPs."], 'default': '127.0.0.1'}",
    "path": "{'description': ['The path to a file on the filesystem to check.', 'If C(state) is present or started then it will wait until the file exists.', 'If C(state) is absent then it will wait until the file does not exist.'], 'type': 'path'}",
    "port": "{'description': ['The port number to poll on C(host).'], 'type': 'int'}",
    "search_regex": "{'description': ['Can be used to match a string in a file.', 'If C(state) is present or started then it will wait until the regex matches.', 'If C(state) is absent then it will wait until the regex does not match.', 'Defaults to a multiline regex.']}",
    "sleep": "{'description': ['Number of seconds to sleep between checks.'], 'type': 'int', 'default': 1}",
    "state": "{'description': ['When checking a port, C(started) will ensure the port is open, C(stopped) will check that is it closed and C(drained) will check for active connections.', 'When checking for a file or a search string C(present) or C(started) will ensure that the file or string is present, C(absent) will check that the file or search string is absent or removed.'], 'default': 'started', 'choices': ['absent', 'drained', 'present', 'started', 'stopped']}",
    "timeout": "{'description': ['The maximum number of seconds to wait for.'], 'type': 'int', 'default': 300}",
}
```

## Examples


``` yaml

- name: wait 300 seconds for port 8000 to become open on the host, don't start checking for 10 seconds
  win_wait_for:
    port: 8000
    delay: 10

- name: wait 150 seconds for port 8000 of any IP to close active connections
  win_wait_for:
    host: 0.0.0.0
    port: 8000
    state: drained
    timeout: 150

- name: wait for port 8000 of any IP to close active connection, ignoring certain hosts
  win_wait_for:
    host: 0.0.0.0
    port: 8000
    state: drained
    exclude_hosts: ['10.2.1.2', '10.2.1.3']

- name: wait for file C:\temp\log.txt to exist before continuing
  win_wait_for:
    path: C:\temp\log.txt

- name: wait until process complete is in the file before continuing
  win_wait_for:
    path: C:\temp\log.txt
    search_regex: process complete

- name: wait until file if removed
  win_wait_for:
    path: C:\temp\log.txt
    state: absent

- name: wait until port 1234 is offline but try every 10 seconds
  win_wait_for:
    port: 1234
    state: absent
    sleep: 10

```

## License

TODO

## Author Information
  - ['Jordan Borean (@jborean93)']
