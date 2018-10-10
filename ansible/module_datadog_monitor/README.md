# Ansible module: ansible.module_datadog_monitor


Manages Datadog monitors

## Description

Manages monitors within Datadog
Options like described on http://docs.datadoghq.com/api/

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Your DataDog API key.'], 'required': True}",
    "app_key": "{'description': ['Your DataDog app key.'], 'required': True}",
    "escalation_message": "{'description': ["A message to include with a re-notification. Supports the '@username' notification we allow elsewhere. Not applicable if renotify_interval is None"]}",
    "evaluation_delay": "{'description': ['Time to delay evaluation (in seconds). It is effective for sparse values.'], 'version_added': '2.7'}",
    "id": "{'description': ['The id of the alert. If set, will be used instead of the name to locate the alert.'], 'version_added': '2.3'}",
    "locked": "{'description': ['A boolean indicating whether changes to this monitor should be restricted to the creator or admins.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "message": "{'description': ["A message to include with notifications for this monitor. Email notifications can be sent to specific users by using the same '@username' notation as events. Monitor message template variables can be accessed by using double square brackets, i.e '[[' and ']]'."]}",
    "name": "{'description': ['The name of the alert.'], 'required': True}",
    "new_host_delay": "{'description': ['A positive integer representing the number of seconds to wait before evaluating the monitor for new hosts. This gives the host time to fully initialize.'], 'version_added': '2.4'}",
    "no_data_timeframe": "{'description': ['The number of minutes before a monitor will notify when data stops reporting. Must be at least 2x the monitor timeframe for metric alerts or 2 minutes for service checks.'], 'default': '2x timeframe for metric, 2 minutes for service'}",
    "notify_audit": "{'description': ['A boolean indicating whether tagged users will be notified on changes to this monitor.'], 'type': 'bool', 'default': False}",
    "notify_no_data": "{'description': ['A boolean indicating whether this monitor will notify when data stops reporting..'], 'type': 'bool', 'default': False}",
    "query": "{'description': ['The monitor query to notify on with syntax varying depending on what type of monitor you are creating.']}",
    "renotify_interval": "{'description': ["The number of minutes after the last notification before a monitor will re-notify on the current status. It will only re-notify if it's not resolved."]}",
    "require_full_window": "{'description': ["A boolean indicating whether this monitor needs a full window of data before it's evaluated. We highly recommend you set this to False for sparse metrics, otherwise some evaluations will be skipped."], 'version_added': '2.3'}",
    "silenced": "{'description': ['Dictionary of scopes to timestamps or None. Each scope will be muted until the given POSIX timestamp or forever if the value is None. '], 'default': ''}",
    "state": "{'description': ['The designated state of the monitor.'], 'required': True, 'choices': ['present', 'absent', 'mute', 'unmute']}",
    "tags": "{'description': ['A list of tags to associate with your monitor when creating or updating. This can help you categorize and filter monitors.'], 'version_added': '2.2'}",
    "thresholds": "{'description': ['A dictionary of thresholds by status. This option is only available for service checks and metric alerts. Because each of them can have multiple thresholds, we don\'t define them directly in the query."]'], 'default': {'ok': 1, 'critical': 1, 'warning': 1}}",
    "timeout_h": "{'description': ['The number of hours of the monitor not reporting data before it will automatically resolve from a triggered state.']}",
    "type": "{'description': ['The type of the monitor.', "The 'event alert'is available starting at Ansible 2.1"], 'choices': ['metric alert', 'service check', 'event alert']}",
}
```

## Examples


``` yaml

# Create a metric monitor
- datadog_monitor:
    type: "metric alert"
    name: "Test monitor"
    state: "present"
    query: "datadog.agent.up.over('host:host1').last(2).count_by_status()"
    message: "Host [[host.name]] with IP [[host.ip]] is failing to report to datadog."
    api_key: "9775a026f1ca7d1c6c5af9d94d9595a4"
    app_key: "87ce4a24b5553d2e482ea8a8500e71b8ad4554ff"

# Deletes a monitor
- datadog_monitor:
    name: "Test monitor"
    state: "absent"
    api_key: "9775a026f1ca7d1c6c5af9d94d9595a4"
    app_key: "87ce4a24b5553d2e482ea8a8500e71b8ad4554ff"

# Mutes a monitor
- datadog_monitor:
    name: "Test monitor"
    state: "mute"
    silenced: '{"*":None}'
    api_key: "9775a026f1ca7d1c6c5af9d94d9595a4"
    app_key: "87ce4a24b5553d2e482ea8a8500e71b8ad4554ff"

# Unmutes a monitor
- datadog_monitor:
    name: "Test monitor"
    state: "unmute"
    api_key: "9775a026f1ca7d1c6c5af9d94d9595a4"
    app_key: "87ce4a24b5553d2e482ea8a8500e71b8ad4554ff"

```

## License

TODO

## Author Information
  - ['Sebastian Kornehl (@skornehl)']
