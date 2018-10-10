# Ansible module: ansible.module_nagios


Perform common tasks in Nagios related to downtime and notifications

## Description

The C(nagios) module has two basic functions: scheduling downtime and toggling alerts for services or hosts.
All actions require the I(host) parameter to be given explicitly. In playbooks you can use the C({{inventory_hostname}}) variable to refer to the host the playbook is currently running on.
You can specify multiple services at once by separating them with commas, .e.g., C(services=httpd,nfs,puppet).
When specifying what service to handle there is a special service value, I(host), which will handle alerts/downtime for the I(host itself), e.g., C(service=host). This keyword may not be given with other services at the same time. I(Setting alerts/downtime for a host does not affect alerts/downtime for any of the services running on it.) To schedule downtime for all services on particular host use keyword "all", e.g., C(service=all).
When using the C(nagios) module you will need to specify your Nagios server using the C(delegate_to) parameter.

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['Action to take.', 'servicegroup options were added in 2.0.', 'delete_downtime options were added in 2.2.'], 'required': True, 'choices': ['downtime', 'delete_downtime', 'enable_alerts', 'disable_alerts', 'silence', 'unsilence', 'silence_nagios', 'unsilence_nagios', 'command', 'servicegroup_service_downtime', 'servicegroup_host_downtime']}",
    "author": "{'description': ['Author to leave downtime comments as. Only usable with the C(downtime) action.'], 'default': 'Ansible'}",
    "cmdfile": "{'description': ['Path to the nagios I(command file) (FIFO pipe). Only required if auto-detection fails.'], 'default': 'auto-detected'}",
    "command": "{'description': ['The raw command to send to nagios, which should not include the submitted time header or the line-feed B(Required) option when using the C(command) action.'], 'required': True}",
    "comment": "{'version_added': '2.0', 'description': ['Comment for C(downtime) action.'], 'default': 'Scheduling downtime'}",
    "host": "{'description': ['Host to operate on in Nagios.']}",
    "minutes": "{'description': ['Minutes to schedule downtime for.', 'Only usable with the C(downtime) action.'], 'default': 30}",
    "servicegroup": "{'version_added': '2.0', 'description': ['The Servicegroup we want to set downtimes/alerts for. B(Required) option when using the C(servicegroup_service_downtime) amd C(servicegroup_host_downtime).']}",
    "services": "{'description': ['What to manage downtime/alerts for. Separate multiple services with commas. C(service) is an alias for C(services). B(Required) option when using the C(downtime), C(enable_alerts), and C(disable_alerts) actions.'], 'aliases': ['service'], 'required': True}",
}
```

## Examples


``` yaml

# set 30 minutes of apache downtime
- nagios:
    action: downtime
    minutes: 30
    service: httpd
    host: '{{ inventory_hostname }}'

# schedule an hour of HOST downtime
- nagios:
    action: downtime
    minutes: 60
    service: host
    host: '{{ inventory_hostname }}'

# schedule an hour of HOST downtime, with a comment describing the reason
- nagios:
    action: downtime
    minutes: 60
    service: host
    host: '{{ inventory_hostname }}'
    comment: Rebuilding machine

# schedule downtime for ALL services on HOST
- nagios:
    action: downtime
    minutes: 45
    service: all
    host: '{{ inventory_hostname }}'

# schedule downtime for a few services
- nagios:
    action: downtime
    services: frob,foobar,qeuz
    host: '{{ inventory_hostname }}'

# set 30 minutes downtime for all services in servicegroup foo
- nagios:
    action: servicegroup_service_downtime
    minutes: 30
    servicegroup: foo
    host: '{{ inventory_hostname }}'

# set 30 minutes downtime for all host in servicegroup foo
- nagios:
    action: servicegroup_host_downtime
    minutes: 30
    servicegroup: foo
    host: '{{ inventory_hostname }}'

# delete all downtime for a given host
- nagios:
    action: delete_downtime
    host: '{{ inventory_hostname }}'
    service: all

# delete all downtime for HOST with a particular comment
- nagios:
    action: delete_downtime
    host: '{{ inventory_hostname }}'
    service: host
    comment: Planned maintenance

# enable SMART disk alerts
- nagios:
    action: enable_alerts
    service: smart
    host: '{{ inventory_hostname }}'

# "two services at once: disable httpd and nfs alerts"
- nagios:
    action: disable_alerts
    service: httpd,nfs
    host: '{{ inventory_hostname }}'

# disable HOST alerts
- nagios:
    action: disable_alerts
    service: host
    host: '{{ inventory_hostname }}'

# silence ALL alerts
- nagios:
    action: silence
    host: '{{ inventory_hostname }}'

# unsilence all alerts
- nagios:
    action: unsilence
    host: '{{ inventory_hostname }}'

# SHUT UP NAGIOS
- nagios:
    action: silence_nagios

# ANNOY ME NAGIOS
- nagios:
    action: unsilence_nagios

# command something
- nagios:
    action: command
    command: DISABLE_FAILURE_PREDICTION

```

## License

TODO

## Author Information
  - ['Tim Bielawa (@tbielawa)']
