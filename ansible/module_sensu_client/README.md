# Ansible module: ansible.module_sensu_client


Manages Sensu client configuration

## Description

Manages Sensu client configuration.
For more information, refer to the Sensu documentation: U(https://sensuapp.org/docs/latest/reference/clients.html)

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'description': ['An address to help identify and reach the client. This is only informational, usually an IP address or hostname.'], 'default': 'Non-loopback IPv4 address as determined by Ruby Socket.ip_address_list (provided by Sensu)'}",
    "chef": "{'description': ['The chef definition scope, used to configure the Sensu Enterprise Chef integration (Sensu Enterprise users only).']}",
    "deregister": "{'description': ['If a deregistration event should be created upon Sensu client process stop.'], 'type': 'bool', 'default': False}",
    "deregistration": "{'description': ['The deregistration definition scope, used to configure automated Sensu client de-registration.']}",
    "ec2": "{'description': ['The ec2 definition scope, used to configure the Sensu Enterprise AWS EC2 integration (Sensu Enterprise users only).']}",
    "keepalive": "{'description': ['The keepalive definition scope, used to configure Sensu client keepalives behavior (e.g. keepalive thresholds, etc).']}",
    "keepalives": "{'description': ['If Sensu should monitor keepalives for this client.'], 'type': 'bool', 'default': True}",
    "name": "{'description': ['A unique name for the client. The name cannot contain special characters or spaces.'], 'default': 'System hostname as determined by Ruby Socket.gethostname (provided by Sensu)'}",
    "puppet": "{'description': ['The puppet definition scope, used to configure the Sensu Enterprise Puppet integration (Sensu Enterprise users only).']}",
    "redact": "{'description': ['Client definition attributes to redact (values) when logging and sending client keepalives.']}",
    "registration": "{'description': ['The registration definition scope, used to configure Sensu registration event handlers.']}",
    "safe_mode": "{'description': ['If safe mode is enabled for the client. Safe mode requires local check definitions in order to accept a check request and execute the check.'], 'type': 'bool', 'default': False}",
    "servicenow": "{'description': ['The servicenow definition scope, used to configure the Sensu Enterprise ServiceNow integration (Sensu Enterprise users only).']}",
    "socket": "{'description': ['The socket definition scope, used to configure the Sensu client socket.']}",
    "state": "{'description': ['Whether the client should be present or not'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "subscriptions": "{'description': ['An array of client subscriptions, a list of roles and/or responsibilities assigned to the system (e.g. webserver).', 'These subscriptions determine which monitoring checks are executed by the client, as check requests are sent to subscriptions.', 'The subscriptions array items must be strings.'], 'required': True}",
}
```

## Examples


``` yaml

# Minimum possible configuration
- name: Configure Sensu client
  sensu_client:
    subscriptions:
      - default

# With customization
- name: Configure Sensu client
  sensu_client:
    name: "{{ ansible_fqdn }}"
    address: "{{ ansible_default_ipv4['address'] }}"
    subscriptions:
      - default
      - webserver
    redact:
      - password
    socket:
      bind: 127.0.0.1
      port: 3030
    keepalive:
      thresholds:
        warning: 180
        critical: 300
      handlers:
        - email
      custom:
        - broadcast: irc
      occurrences: 3
  register: client
  notify:
    - Restart sensu-client

- name: Secure Sensu client configuration file
  file:
    path: "{{ client['file'] }}"
    owner: "sensu"
    group: "sensu"
    mode: "0600"

- name: Delete the Sensu client configuration
  sensu_client:
    state: "absent"

```

## License

TODO

## Author Information
  - ['David Moreau Simard (@dmsimard)']
