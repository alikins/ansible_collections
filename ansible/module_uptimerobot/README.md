# Ansible module: ansible.module_uptimerobot


Pause and start Uptime Robot monitoring

## Description

This module will let you start and pause Uptime Robot Monitoring

## Requirements

TODO

## Arguments

``` json
{
    "apikey": "{'description': ['Uptime Robot API key.'], 'required': True}",
    "monitorid": "{'description': ['ID of the monitor to check.'], 'required': True}",
    "state": "{'description': ['Define whether or not the monitor should be running or paused.'], 'required': True, 'choices': ['started', 'paused']}",
}
```

## Examples


``` yaml

# Pause the monitor with an ID of 12345.
- uptimerobot:
    monitorid: 12345
    apikey: 12345-1234512345
    state: paused

# Start the monitor with an ID of 12345.
- uptimerobot:
    monitorid: 12345
    apikey: 12345-1234512345
    state: started

```

## License

TODO

## Author Information
  - ['Nate Kingsley (@nate-kingsley)']
