# Ansible module: ansible.module_gce_eip


Create or Destroy Global or Regional External IP addresses

## Description

Create (reserve) or Destroy (release) Regional or Global IP Addresses. See U(https://cloud.google.com/compute/docs/configure-instance-ip-addresses#reserve_new_static) for more on reserving static addresses.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['Name of Address.'], 'required': True}",
    "region": "{'description': ["Region to create the address in. Set to 'global' to create a global address."], 'required': True}",
    "state": "{'description': ['The state the address should be in. C(present) or C(absent) are the only valid options.'], 'default': 'present', 'required': False, 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

# Create a Global external IP address
- gce_eip:
    service_account_email: "{{ service_account_email }}"
    credentials_file: "{{ credentials_file }}"
    project_id: "{{ project_id }}"
    name: my-global-ip
    region: global
    state: present

# Create a Regional external IP address
- gce_eip:
    service_account_email: "{{ service_account_email }}"
    credentials_file: "{{ credentials_file }}"
    project_id: "{{ project_id }}"
    name: my-global-ip
    region: us-east1
    state: present

```

## License

TODO

## Author Information
  - ['Tom Melendez (@supertom) <tom@supertom.com>']
