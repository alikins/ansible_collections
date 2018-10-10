# Ansible module: ansible.module_cs_router


Manages routers on Apache CloudStack based clouds

## Description

Start, restart, stop and destroy routers.
C(state=present) is not able to create routers, use M(cs_network) instead.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the router is related to.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "domain": "{'description': ['Domain the router is related to.']}",
    "name": "{'description': ['Name of the router.'], 'required': True}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'default': True, 'type': 'bool'}",
    "project": "{'description': ['Name of the project the router is related to.']}",
    "service_offering": "{'description': ['Name or id of the service offering of the router.']}",
    "state": "{'description': ['State of the router.'], 'default': 'present', 'choices': ['present', 'absent', 'started', 'stopped', 'restarted']}",
    "zone": "{'description': ['Name of the zone the router is deployed in.', 'If not set, all zones are used.'], 'version_added': '2.4'}",
}
```

## Examples


``` yaml

# Ensure the router has the desired service offering, no matter if
# the router is running or not.
- local_action:
    module: cs_router
    name: r-40-VM
    service_offering: System Offering for Software Router

# Ensure started
- local_action:
    module: cs_router
    name: r-40-VM
    state: started

# Ensure started with desired service offering.
# If the service offerings changes, router will be rebooted.
- local_action:
    module: cs_router
    name: r-40-VM
    service_offering: System Offering for Software Router
    state: started

# Ensure stopped
- local_action:
    module: cs_router
    name: r-40-VM
    state: stopped

# Remove a router
- local_action:
    module: cs_router
    name: r-40-VM
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
