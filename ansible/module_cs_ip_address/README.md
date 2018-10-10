# Ansible module: ansible.module_cs_ip_address


Manages public IP address associations on Apache CloudStack based clouds

## Description

Acquires and associates a public IP to an account or project.
Due to API limitations this is not an idempotent call, so be sure to only conditionally call this when C(state=present).
Tagging the IP address can also make the call idempotent.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the IP address is related to.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "domain": "{'description': ['Domain the IP address is related to.']}",
    "ip_address": "{'description': ['Public IP address.', 'Required if C(state=absent) and C(tags) is not set']}",
    "network": "{'description': ['Network the IP address is related to.']}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'type': 'bool', 'default': True}",
    "project": "{'description': ['Name of the project the IP address is related to.']}",
    "state": "{'description': ['State of the IP address.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tags": "{'description': ['List of tags. Tags are a list of dictionaries having keys C(key) and C(value).', 'Tags can be used as an unique identifier for the IP Addresses.', 'In this case, at least one of them must be unique to ensure idempontency.'], 'aliases': ['tag'], 'version_added': '2.6'}",
    "vpc": "{'description': ['VPC the IP address is related to.'], 'version_added': '2.2'}",
    "zone": "{'description': ['Name of the zone in which the IP address is in.', 'If not set, default zone is used.']}",
}
```

## Examples


``` yaml

- name: Associate an IP address conditonally
  local_action:
    module: cs_ip_address
    network: My Network
  register: ip_address
  when: instance.public_ip is undefined

- name: Disassociate an IP address
  local_action:
    module: cs_ip_address
    ip_address: 1.2.3.4
    state: absent

- name: Associate an IP address with tags
  local_action:
    module: cs_ip_address
    network: My Network
    tags:
      - key: myCustomID
      - value: 5510c31a-416e-11e8-9013-02000a6b00bf
  register: ip_address

- name: Disassociate an IP address with tags
  local_action:
    module: cs_ip_address
    state: absent
    tags:
      - key: myCustomID
      - value: 5510c31a-416e-11e8-9013-02000a6b00bf

```

## License

TODO

## Author Information
  - ['Darren Worrall (@dazworrall)', 'René Moser (@resmo)']
  - ['Darren Worrall (@dazworrall)', 'René Moser (@resmo)']
