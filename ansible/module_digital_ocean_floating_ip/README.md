# Ansible module: ansible.module_digital_ocean_floating_ip


Manage DigitalOcean Floating IPs

## Description

Create/delete/assign a floating IP.

## Requirements

TODO

## Arguments

``` json
{
    "droplet_id": "{'description': ['The Droplet that the Floating IP has been assigned to.']}",
    "ip": "{'description': ['Public IP address of the Floating IP. Used to remove an IP']}",
    "oauth_token": "{'description': ['DigitalOcean OAuth token.'], 'required': True}",
    "region": "{'description': ['The region that the Floating IP is reserved to.']}",
    "state": "{'description': ['Indicate desired state of the target.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

- name: "Create a Floating IP in region lon1"
  digital_ocean_floating_ip:
    state: present
    region: lon1

- name: "Create a Floating IP assigned to Droplet ID 123456"
  digital_ocean_floating_ip:
    state: present
    droplet_id: 123456

- name: "Delete a Floating IP with ip 1.2.3.4"
  digital_ocean_floating_ip:
    state: absent
    ip: "1.2.3.4"


```

## License

TODO

## Author Information
  - ['Patrick Marques (@pmarques)']
