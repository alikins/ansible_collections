# Ansible module: ansible.module_sensu_handler


Manages Sensu handler configuration

## Description

Manages Sensu handler configuration
For more information, refer to the Sensu documentation: U(https://sensuapp.org/docs/latest/reference/handlers.html)

## Requirements

TODO

## Arguments

``` json
{
    "command": "{'description': ['The handler command to be executed.', 'The event data is passed to the process via STDIN.', 'NOTE: the command attribute is only required for Pipe handlers (i.e. handlers configured with "type": "pipe").']}",
    "filter": "{'description': ['The Sensu event filter (name) to use when filtering events for the handler.']}",
    "filters": "{'description': ['An array of Sensu event filters (names) to use when filtering events for the handler.', 'Each array item must be a string.']}",
    "handle_flapping": "{'description': ['If events in the flapping state should be handled.'], 'type': 'bool', 'default': False}",
    "handle_silenced": "{'description': ['If events matching one or more silence entries should be handled.'], 'type': 'bool', 'default': False}",
    "handlers": "{'description': ['An array of Sensu event handlers (names) to use for events using the handler set.', 'Each array item must be a string.', 'NOTE: the handlers attribute is only required for handler sets (i.e. handlers configured with "type": "set").']}",
    "mutator": "{'description': ['The Sensu event mutator (name) to use to mutate event data for the handler.']}",
    "name": "{'description': ['A unique name for the handler. The name cannot contain special characters or spaces.'], 'required': True}",
    "pipe": "{'description': ['The pipe definition scope, used to configure the Sensu transport pipe.', 'NOTE: the pipe attribute is only required for Transport handlers (i.e. handlers configured with "type": "transport").']}",
    "severities": "{'description': ['An array of check result severities the handler will handle.', 'NOTE: event resolution bypasses this filtering.'], 'choices': ['warning', 'critical', 'unknown']}",
    "socket": "{'description': ['The socket definition scope, used to configure the TCP/UDP handler socket.', 'NOTE: the socket attribute is only required for TCP/UDP handlers (i.e. handlers configured with "type": "tcp" or "type": "udp").']}",
    "state": "{'description': ['Whether the handler should be present or not'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['The handler execution duration timeout in seconds (hard stop).', 'Only used by pipe and tcp handler types.'], 'default': 10}",
    "type": "{'description': ['The handler type'], 'choices': ['pipe', 'tcp', 'udp', 'transport', 'set'], 'required': True}",
}
```

## Examples


``` yaml

# Configure a handler that sends event data as STDIN (pipe)
- name: Configure IRC Sensu handler
  sensu_handler:
    name: "irc_handler"
    type: "pipe"
    command: "/usr/local/bin/notify-irc.sh"
    severities:
      - "ok"
      - "critical"
      - "warning"
      - "unknown"
    timeout: 15
  notify:
    - Restart sensu-client
    - Restart sensu-server

# Delete a handler
- name: Delete IRC Sensu handler
  sensu_handler:
    name: "irc_handler"
    state: "absent"

# Example of a TCP handler
- name: Configure TCP Sensu handler
  sensu_handler:
    name: "tcp_handler"
    type: "tcp"
    timeout: 30
    socket:
      host: "10.0.1.99"
      port: 4444
  register: handler
  notify:
    - Restart sensu-client
    - Restart sensu-server

- name: Secure Sensu handler configuration file
  file:
    path: "{{ handler['file'] }}"
    owner: "sensu"
    group: "sensu"
    mode: "0600"

```

## License

TODO

## Author Information
  - ['David Moreau Simard (@dmsimard)']
