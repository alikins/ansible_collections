# Ansible module: ansible.module_cs_zone


Manages zones on Apache CloudStack based clouds

## Description

Create, update and remove zones.

## Requirements

TODO

## Arguments

``` json
{
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "dhcp_provider": "{'description': ['DHCP provider for the Zone.']}",
    "dns1": "{'description': ['First DNS for the zone.', 'Required if C(state=present)']}",
    "dns1_ipv6": "{'description': ['First DNS for IPv6 for the zone.']}",
    "dns2": "{'description': ['Second DNS for the zone.']}",
    "dns2_ipv6": "{'description': ['Second DNS for IPv6 for the zone.']}",
    "domain": "{'description': ['Domain the zone is related to.', 'Zone is a public zone if not set.']}",
    "guest_cidr_address": "{'description': ['Guest CIDR address for the zone.']}",
    "id": "{'description': ['uuid of the existing zone.']}",
    "internal_dns1": "{'description': ['First internal DNS for the zone.', 'If not set C(dns1) will be used on C(state=present).']}",
    "internal_dns2": "{'description': ['Second internal DNS for the zone.']}",
    "name": "{'description': ['Name of the zone.'], 'required': True}",
    "network_domain": "{'description': ['Network domain for the zone.']}",
    "network_type": "{'description': ['Network type of the zone.'], 'default': 'basic', 'choices': ['basic', 'advanced']}",
    "state": "{'description': ['State of the zone.'], 'default': 'present', 'choices': ['present', 'enabled', 'disabled', 'absent']}",
}
```

## Examples


``` yaml

# Ensure a zone is present
- local_action:
    module: cs_zone
    name: ch-zrh-ix-01
    dns1: 8.8.8.8
    dns2: 8.8.4.4
    network_type: basic

# Ensure a zone is disabled
- local_action:
    module: cs_zone
    name: ch-zrh-ix-01
    state: disabled

# Ensure a zone is enabled
- local_action:
    module: cs_zone
    name: ch-zrh-ix-01
    state: enabled

# Ensure a zone is absent
- local_action:
    module: cs_zone
    name: ch-zrh-ix-01
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
