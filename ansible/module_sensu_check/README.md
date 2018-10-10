# Ansible module: ansible.module_sensu_check


Manage Sensu checks

## Description

Manage the checks that should be run on a machine by I(Sensu).
Most options do not have a default and will not be added to the check definition unless specified.
All defaults except I(path), I(state), I(backup) and I(metric) are not managed by this module,
they are simply specified for your convenience.

## Requirements

TODO

## Arguments

``` json
{
    "aggregate": "{'description': ['Classifies the check as an aggregate check,', 'making it available via the aggregate API'], 'type': 'bool', 'default': False}",
    "backup": "{'description': ['Create a backup file (if yes), including the timestamp information so', 'you can get the original file back if you somehow clobbered it incorrectly.'], 'type': 'bool', 'default': False}",
    "command": "{'description': ['Path to the sensu check to run (not required when I(state=absent))'], 'required': True}",
    "custom": "{'version_added': '2.1', 'description': ['A hash/dictionary of custom parameters for mixing to the configuration.', "You can't rewrite others module parameters using this"], 'default': {}}",
    "dependencies": "{'description': ['Other checks this check depends on, if dependencies fail,', 'handling of this check will be disabled'], 'default': []}",
    "handle": "{'description': ['Whether the check should be handled or not'], 'type': 'bool', 'default': True}",
    "handlers": "{'description': ['List of handlers to notify when the check fails'], 'default': []}",
    "high_flap_threshold": "{'description': ['The high threshold for flap detection']}",
    "interval": "{'description': ['Check interval in seconds']}",
    "low_flap_threshold": "{'description': ['The low threshold for flap detection']}",
    "metric": "{'description': ['Whether the check is a metric'], 'type': 'bool', 'default': False}",
    "name": "{'description': ['The name of the check', 'This is the key that is used to determine whether a check exists'], 'required': True}",
    "occurrences": "{'description': ['Number of event occurrences before the handler should take action'], 'default': 1}",
    "path": "{'description': ['Path to the json file of the check to be added/removed.', 'Will be created if it does not exist (unless I(state=absent)).', 'The parent folders need to exist when I(state=present), otherwise an error will be thrown'], 'default': '/etc/sensu/conf.d/checks.json'}",
    "publish": "{'description': ['Whether the check should be scheduled at all.', 'You can still issue it via the sensu api'], 'type': 'bool', 'default': True}",
    "refresh": "{'description': ['Number of seconds handlers should wait before taking second action']}",
    "source": "{'version_added': '2.1', 'description': ['The check source, used to create a JIT Sensu client for an external resource (e.g. a network switch).']}",
    "standalone": "{'description': ['Whether the check should be scheduled by the sensu client or server', 'This option obviates the need for specifying the I(subscribers) option'], 'type': 'bool', 'default': False}",
    "state": "{'description': ['Whether the check should be present or not'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "subdue_begin": "{'description': ['When to disable handling of check failures']}",
    "subdue_end": "{'description': ['When to enable handling of check failures']}",
    "subscribers": "{'description': ['List of subscribers/channels this check should run for', 'See sensu_subscribers to subscribe a machine to a channel'], 'default': []}",
    "timeout": "{'description': ['Timeout for the check'], 'default': 10}",
    "ttl": "{'description': ['Time to live in seconds until the check is considered stale'], 'version_added': 2.4}",
}
```

## Examples


``` yaml

# Fetch metrics about the CPU load every 60 seconds,
# the sensu server has a handler called 'relay' which forwards stats to graphite
- name: get cpu metrics
  sensu_check:
    name: cpu_load
    command: /etc/sensu/plugins/system/cpu-mpstat-metrics.rb
    metric: yes
    handlers: relay
    subscribers: common
    interval: 60

# Check whether nginx is running
- name: check nginx process
  sensu_check:
    name: nginx_running
    command: /etc/sensu/plugins/processes/check-procs.rb -f /var/run/nginx.pid
    handlers: default
    subscribers: nginx
    interval: 60

# Stop monitoring the disk capacity.
# Note that the check will still show up in the sensu dashboard,
# to remove it completely you need to issue a DELETE request to the sensu api.
- name: check disk
  sensu_check:
    name: check_disk_capacity
    state: absent

```

## License

TODO

## Author Information
  - ['Anders Ingemann (@andsens)']
