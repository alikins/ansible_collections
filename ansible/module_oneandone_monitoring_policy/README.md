# Ansible module: ansible.module_oneandone_monitoring_policy


Configure 1&1 monitoring policy

## Description

Create, remove, update monitoring policies (and add/remove ports, processes, and servers). This module has a dependency on 1and1 >= 1.0

## Requirements

TODO

## Arguments

``` json
{
    "add_ports": "{'description': ['Ports to add to the monitoring policy.'], 'required': False}",
    "add_processes": "{'description': ['Processes to add to the monitoring policy.'], 'required': False}",
    "add_servers": "{'description': ['Servers to add to the monitoring policy.'], 'required': False}",
    "agent": "{'description': ['Set true for using agent.'], 'required': True}",
    "api_url": "{'description': ['Custom API URL. Overrides the ONEANDONE_API_URL environement variable.'], 'required': False}",
    "auth_token": "{'description': ['Authenticating API token provided by 1&1.'], 'required': True}",
    "description": "{'description': ['Monitoring policy description. maxLength=256'], 'required': False}",
    "email": "{'description': ["User's email. maxLength=128"], 'required': True}",
    "monitoring_policy": "{'description': ['The identifier (id or name) of the monitoring policy used with update state.'], 'required': True}",
    "name": "{'description': ['Monitoring policy name used with present state. Used as identifier (id or name) when used with absent state. maxLength=128'], 'required': True}",
    "ports": "{'description': ['Array of ports that will be monitoring.'], 'required': True, 'suboptions': {'protocol': {'description': ['Internet protocol.'], 'choices': ['TCP', 'UDP'], 'required': True}, 'port': {'description': ['Port number. minimum=1, maximum=65535'], 'required': True}, 'alert_if': {'description': ['Case of alert.'], 'choices': ['RESPONDING', 'NOT_RESPONDING'], 'required': True}, 'email_notification': {'description': ['Set true for sending e-mail notifications.'], 'required': True}}}",
    "processes": "{'description': ['Array of processes that will be monitoring.'], 'required': True, 'suboptions': {'process': {'description': ['Name of the process. maxLength=50'], 'required': True}, 'alert_if': {'description': ['Case of alert.'], 'choices': ['RUNNING', 'NOT_RUNNING'], 'required': True}}}",
    "remove_ports": "{'description': ['Ports to remove from the monitoring policy.'], 'required': False}",
    "remove_processes": "{'description': ['Processes to remove from the monitoring policy.'], 'required': False}",
    "remove_servers": "{'description': ['Servers to remove from the monitoring policy.'], 'required': False}",
    "state": "{'description': ["Define a monitoring policy's state to create, remove, update."], 'required': False, 'default': 'present', 'choices': ['present', 'absent', 'update']}",
    "thresholds": "{'description': ['Monitoring policy thresholds. Each of the suboptions have warning and critical, which both have alert and value suboptions. Warning is used to set limits for warning alerts, critical is used to set critical alerts. alert enables alert, and value is used to advise when the value is exceeded.'], 'required': True, 'suboptions': {'cpu': {'description': ['Consumption limits of CPU.'], 'required': True}, 'ram': {'description': ['Consumption limits of RAM.'], 'required': True}, 'disk': {'description': ['Consumption limits of hard disk.'], 'required': True}, 'internal_ping': {'description': ['Response limits of internal ping.'], 'required': True}, 'transfer': {'description': ['Consumption limits for transfer.'], 'required': True}}}",
    "update_ports": "{'description': ['Ports to be updated on the monitoring policy.'], 'required': False}",
    "update_processes": "{'description': ['Processes to be updated on the monitoring policy.'], 'required': False}",
    "wait": "{'description': ["wait for the instance to be in state 'running' before returning"], 'required': False, 'default': True, 'type': 'bool'}",
    "wait_interval": "{'description': ['Defines the number of seconds to wait when using the _wait_for methods'], 'default': 5}",
    "wait_timeout": "{'description': ['how long before wait gives up, in seconds'], 'default': 600}",
}
```

## Examples


``` yaml


# Provisioning example. Create and destroy a monitoring policy.

- oneandone_moitoring_policy:
    auth_token: oneandone_private_api_key
    name: ansible monitoring policy
    description: Testing creation of a monitoring policy with ansible
    email: your@emailaddress.com
    agent: true
    thresholds:
     -
       cpu:
         warning:
           value: 80
           alert: false
         critical:
           value: 92
           alert: false
     -
       ram:
         warning:
           value: 80
           alert: false
         critical:
           value: 90
           alert: false
     -
       disk:
         warning:
           value: 80
           alert: false
         critical:
           value: 90
           alert: false
     -
       internal_ping:
         warning:
           value: 50
           alert: false
         critical:
           value: 100
           alert: false
     -
       transfer:
         warning:
           value: 1000
           alert: false
         critical:
           value: 2000
           alert: false
    ports:
     -
       protocol: TCP
       port: 22
       alert_if: RESPONDING
       email_notification: false
    processes:
     -
       process: test
       alert_if: NOT_RUNNING
       email_notification: false
    wait: true

- oneandone_moitoring_policy:
    auth_token: oneandone_private_api_key
    state: absent
    name: ansible monitoring policy

# Update a monitoring policy.

- oneandone_moitoring_policy:
    auth_token: oneandone_private_api_key
    monitoring_policy: ansible monitoring policy
    name: ansible monitoring policy updated
    description: Testing creation of a monitoring policy with ansible updated
    email: another@emailaddress.com
    thresholds:
     -
       cpu:
         warning:
           value: 70
           alert: false
         critical:
           value: 90
           alert: false
     -
       ram:
         warning:
           value: 70
           alert: false
         critical:
           value: 80
           alert: false
     -
       disk:
         warning:
           value: 70
           alert: false
         critical:
           value: 80
           alert: false
     -
       internal_ping:
         warning:
           value: 60
           alert: false
         critical:
           value: 90
           alert: false
     -
       transfer:
         warning:
           value: 900
           alert: false
         critical:
           value: 1900
           alert: false
    wait: true
    state: update

# Add a port to a monitoring policy.

- oneandone_moitoring_policy:
    auth_token: oneandone_private_api_key
    monitoring_policy: ansible monitoring policy updated
    add_ports:
     -
       protocol: TCP
       port: 33
       alert_if: RESPONDING
       email_notification: false
    wait: true
    state: update

# Update existing ports of a monitoring policy.

- oneandone_moitoring_policy:
    auth_token: oneandone_private_api_key
    monitoring_policy: ansible monitoring policy updated
    update_ports:
     -
       id: existing_port_id
       protocol: TCP
       port: 34
       alert_if: RESPONDING
       email_notification: false
     -
       id: existing_port_id
       protocol: TCP
       port: 23
       alert_if: RESPONDING
       email_notification: false
    wait: true
    state: update

# Remove a port from a monitoring policy.

- oneandone_moitoring_policy:
    auth_token: oneandone_private_api_key
    monitoring_policy: ansible monitoring policy updated
    remove_ports:
     - port_id
    state: update

# Add a process to a monitoring policy.

- oneandone_moitoring_policy:
    auth_token: oneandone_private_api_key
    monitoring_policy: ansible monitoring policy updated
    add_processes:
     -
       process: test_2
       alert_if: NOT_RUNNING
       email_notification: false
    wait: true
    state: update

# Update existing processes of a monitoring policy.

- oneandone_moitoring_policy:
    auth_token: oneandone_private_api_key
    monitoring_policy: ansible monitoring policy updated
    update_processes:
     -
       id: process_id
       process: test_1
       alert_if: NOT_RUNNING
       email_notification: false
     -
       id: process_id
       process: test_3
       alert_if: NOT_RUNNING
       email_notification: false
    wait: true
    state: update

# Remove a process from a monitoring policy.

- oneandone_moitoring_policy:
    auth_token: oneandone_private_api_key
    monitoring_policy: ansible monitoring policy updated
    remove_processes:
     - process_id
    wait: true
    state: update

# Add server to a monitoring policy.

- oneandone_moitoring_policy:
    auth_token: oneandone_private_api_key
    monitoring_policy: ansible monitoring policy updated
    add_servers:
     - server id or name
    wait: true
    state: update

# Remove server from a monitoring policy.

- oneandone_moitoring_policy:
    auth_token: oneandone_private_api_key
    monitoring_policy: ansible monitoring policy updated
    remove_servers:
     - server01
    wait: true
    state: update

```

## License

TODO

## Author Information
  - ['Amel Ajdinovic (@aajdinov)', 'Ethan Devenport (@edevenport)']
  - ['Amel Ajdinovic (@aajdinov)', 'Ethan Devenport (@edevenport)']
