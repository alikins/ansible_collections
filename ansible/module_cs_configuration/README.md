# Ansible module: ansible.module_cs_configuration


Manages configuration on Apache CloudStack based clouds

## Description

Manages global, zone, account, storage and cluster configurations.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Ensure the value for corresponding account.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "cluster": "{'description': ['Ensure the value for corresponding cluster.']}",
    "domain": "{'description': ['Domain the account is related to.', 'Only considered if C(account) is used.'], 'default': 'ROOT'}",
    "name": "{'description': ['Name of the configuration.'], 'required': True}",
    "storage": "{'description': ['Ensure the value for corresponding storage pool.']}",
    "value": "{'description': ['Value of the configuration.'], 'required': True}",
    "zone": "{'description': ['Ensure the value for corresponding zone.']}",
}
```

## Examples


``` yaml

# Ensure global configuration
- local_action:
    module: cs_configuration
    name: router.reboot.when.outofband.migrated
    value: false

# Ensure zone configuration
- local_action:
    module: cs_configuration
    name: router.reboot.when.outofband.migrated
    zone: ch-gva-01
    value: true

# Ensure storage configuration
- local_action:
    module: cs_configuration
    name: storage.overprovisioning.factor
    storage: storage01
    value: 2.0

# Ensure account configuration
- local_action:
    module: cs_configuration
    name: allow.public.user.templates
    value: false
    account: acme inc
    domain: customers

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
