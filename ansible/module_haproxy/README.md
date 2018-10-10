# Ansible module: ansible.module_haproxy


Enable, disable, and set weights for HAProxy backend servers using socket commands

## Description

Enable, disable, drain and set weights for HAProxy backend servers using socket commands.

## Requirements

TODO

## Arguments

``` json
{
    "backend": "{'description': ['Name of the HAProxy backend pool.'], 'default': 'auto-detected'}",
    "drain": "{'description': ["Wait until the server has no active connections or until the timeout determined by wait_interval and wait_retries is reached.  Continue only after the status changes to 'MAINT'.  This overrides the shutdown_sessions option."], 'version_added': '2.4'}",
    "fail_on_not_found": "{'description': ['Fail whenever trying to enable/disable a backend host that does not exist'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "host": "{'description': ['Name of the backend host to change.'], 'required': True}",
    "shutdown_sessions": "{'description': ['When disabling a server, immediately terminate all the sessions attached to the specified server. This can be used to terminate long-running sessions after a server is put into maintenance mode. Overridden by the drain option.'], 'type': 'bool', 'default': False}",
    "socket": "{'description': ['Path to the HAProxy socket file.'], 'default': '/var/run/haproxy.sock'}",
    "state": "{'description': ['Desired state of the provided backend host.', 'Note that C(drain) state was added in version 2.4. It is supported only by HAProxy version 1.5 or later, if used on versions < 1.5, it will be ignored.'], 'required': True, 'choices': ['enabled', 'disabled', 'drain']}",
    "wait": "{'description': ["Wait until the server reports a status of 'UP' when `state=enabled`, status of 'MAINT' when `state=disabled` or status of 'DRAIN' when `state=drain`"], 'type': 'bool', 'default': False, 'version_added': '2.0'}",
    "wait_interval": "{'description': ['Number of seconds to wait between retries.'], 'default': 5, 'version_added': '2.0'}",
    "wait_retries": "{'description': ['Number of times to check for status after changing the state.'], 'default': 25, 'version_added': '2.0'}",
    "weight": "{'description': ['The value passed in argument. If the value ends with the `%` sign, then the new weight will be relative to the initially configured weight. Relative weights are only permitted between 0 and 100% and absolute weights are permitted between 0 and 256.']}",
}
```

## Examples


``` yaml

# disable server in 'www' backend pool
- haproxy:
    state: disabled
    host: '{{ inventory_hostname }}'
    backend: www

# disable server without backend pool name (apply to all available backend pool)
- haproxy:
    state: disabled
    host: '{{ inventory_hostname }}'

# disable server, provide socket file
- haproxy:
    state: disabled
    host: '{{ inventory_hostname }}'
    socket: /var/run/haproxy.sock
    backend: www

# disable server, provide socket file, wait until status reports in maintenance
- haproxy:
    state: disabled
    host: '{{ inventory_hostname }}'
    socket: /var/run/haproxy.sock
    backend: www
    wait: yes

# Place server in drain mode, providing a socket file.  Then check the server's
# status every minute to see if it changes to maintenance mode, continuing if it
# does in an hour and failing otherwise.
- haproxy:
    state: disabled
    host: '{{ inventory_hostname }}'
    socket: /var/run/haproxy.sock
    backend: www
    wait: yes
    drain: yes
    wait_interval: 1
    wait_retries: 60

# disable backend server in 'www' backend pool and drop open sessions to it
- haproxy:
    state: disabled
    host: '{{ inventory_hostname }}'
    backend: www
    socket: /var/run/haproxy.sock
    shutdown_sessions: true

# disable server without backend pool name (apply to all available backend pool) but fail when the backend host is not found
- haproxy:
    state: disabled
    host: '{{ inventory_hostname }}'
    fail_on_not_found: yes

# enable server in 'www' backend pool
- haproxy:
    state: enabled
    host: '{{ inventory_hostname }}'
    backend: www

# enable server in 'www' backend pool wait until healthy
- haproxy:
    state: enabled
    host: '{{ inventory_hostname }}'
    backend: www
    wait: yes

# enable server in 'www' backend pool wait until healthy. Retry 10 times with intervals of 5 seconds to retrieve the health
- haproxy:
    state: enabled
    host: '{{ inventory_hostname }}'
    backend: www
    wait: yes
    wait_retries: 10
    wait_interval: 5

# enable server in 'www' backend pool with change server(s) weight
- haproxy:
    state: enabled
    host: '{{ inventory_hostname }}'
    socket: /var/run/haproxy.sock
    weight: 10
    backend: www

# set the server in 'www' backend pool to drain mode
- haproxy:
    state: drain
    host: '{{ inventory_hostname }}'
    socket: /var/run/haproxy.sock
    backend: www

```

## License

TODO

## Author Information
  - ['Ravi Bhure (@ravibhure)']
