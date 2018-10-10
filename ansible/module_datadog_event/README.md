# Ansible module: ansible.module_datadog_event


Posts events to Datadog  service

## Description

Allows to post events to Datadog (www.datadoghq.com) service.
Uses http://docs.datadoghq.com/api/#events API.

## Requirements

TODO

## Arguments

``` json
{
    "aggregation_key": "{'description': ['An arbitrary string to use for aggregation.']}",
    "alert_type": "{'description': ['Type of alert.'], 'default': 'info', 'choices': ['error', 'warning', 'info', 'success']}",
    "api_key": "{'description': ['Your DataDog API key.'], 'required': True}",
    "app_key": "{'description': ['Your DataDog app key.'], 'required': True, 'version_added': '2.2'}",
    "date_happened": "{'description': ['POSIX timestamp of the event.', 'Default value is now.'], 'default': 'now'}",
    "host": "{'description': ['Host name to associate with the event.'], 'default': '{{ ansible_hostname }}', 'version_added': '2.4'}",
    "priority": "{'description': ['The priority of the event.'], 'default': 'normal', 'choices': ['normal', 'low']}",
    "tags": "{'description': ['Comma separated list of tags to apply to the event.']}",
    "text": "{'description': ['The body of the event.'], 'required': True}",
    "title": "{'description': ['The event title.'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True, 'version_added': '1.5.1'}",
}
```

## Examples


``` yaml

# Post an event with low priority
- datadog_event:
    title: Testing from ansible
    text: Test
    priority: low
    api_key: 9775a026f1ca7d1c6c5af9d94d9595a4
    app_key: j4JyCYfefWHhgFgiZUqRm63AXHNZQyPGBfJtAzmN
# Post an event with several tags
- datadog_event:
    title: Testing from ansible
    text: Test
    api_key: 9775a026f1ca7d1c6c5af9d94d9595a4
    app_key: j4JyCYfefWHhgFgiZUqRm63AXHNZQyPGBfJtAzmN
    tags: 'aa,bb,#host:{{ inventory_hostname }}'

```

## License

TODO

## Author Information
  - ['Artūras `arturaz` Šlajus (@arturaz)', 'Naoya Nakazawa (@n0ts)']
  - ['Artūras `arturaz` Šlajus (@arturaz)', 'Naoya Nakazawa (@n0ts)']
