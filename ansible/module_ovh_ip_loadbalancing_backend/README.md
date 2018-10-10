# Ansible module: ansible.module_ovh_ip_loadbalancing_backend


Manage OVH IP LoadBalancing backends

## Description

Manage OVH (French European hosting provider) LoadBalancing IP backends

## Requirements

TODO

## Arguments

``` json
{
    "application_key": "{'required': True, 'description': ['The applicationKey to use']}",
    "application_secret": "{'required': True, 'description': ['The application secret to use']}",
    "backend": "{'required': True, 'description': ['The IP address of the backend to update / modify / delete']}",
    "consumer_key": "{'required': True, 'description': ['The consumer key to use']}",
    "endpoint": "{'required': True, 'description': ['The endpoint to use ( for instance ovh-eu)']}",
    "name": "{'required': True, 'description': ['Name of the LoadBalancing internal name (ip-X.X.X.X)']}",
    "probe": "{'default': 'none', 'choices': ['none', 'http', 'icmp', 'oco'], 'description': ['Determines the type of probe to use for this backend']}",
    "state": "{'default': 'present', 'choices': ['present', 'absent'], 'description': ['Determines whether the backend is to be created/modified or deleted']}",
    "timeout": "{'default': 120, 'description': ['The timeout in seconds used to wait for a task to be completed.']}",
    "weight": "{'default': 8, 'description': ['Determines the weight for this backend']}",
}
```

## Examples


``` yaml

# Adds or modify the backend '212.1.1.1' to a
# loadbalancing 'ip-1.1.1.1'
- ovh_ip_loadbalancing:
    name: ip-1.1.1.1
    backend: 212.1.1.1
    state: present
    probe: none
    weight: 8
    endpoint: ovh-eu
    application_key: yourkey
    application_secret: yoursecret
    consumer_key: yourconsumerkey

# Removes a backend '212.1.1.1' from a loadbalancing 'ip-1.1.1.1'
- ovh_ip_loadbalancing:
    name: ip-1.1.1.1
    backend: 212.1.1.1
    state: absent
    endpoint: ovh-eu
    application_key: yourkey
    application_secret: yoursecret
    consumer_key: yourconsumerkey

```

## License

TODO

## Author Information
  - ['Pascal Heraud (@pascalheraud)']
