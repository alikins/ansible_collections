# Ansible module: ansible.module_bigmon_policy


Create and remove a bigmon out-of-band policy

## Description

Create and remove a bigmon out-of-band policy.

## Requirements

TODO

## Arguments

``` json
{
    "access_token": "{'description': ["Bigmon access token. If this isn't set, the environment variable C(BIGSWITCH_ACCESS_TOKEN) is used."]}",
    "action": "{'description': ['Forward matching packets to delivery interfaces, Drop is for measure rate of matching packets, but do not forward to delivery interfaces, capture packets and write to a PCAP file, or enable NetFlow generation.'], 'default': 'forward', 'choices': ['forward', 'drop', 'flow-gen']}",
    "controller": "{'description': ['The controller address.'], 'required': True}",
    "delivery_packet_count": "{'description': ['Run policy until delivery_packet_count packets are delivered.'], 'default': 0}",
    "duration": "{'description': ['Run policy for duration duration or until delivery_packet_count packets are delivered, whichever comes first.'], 'default': 0}",
    "name": "{'description': ['The name of the policy.'], 'required': True}",
    "policy_description": "{'description': ['Description of policy.']}",
    "priority": "{'description': ['A priority associated with this policy. The higher priority policy takes precedence over a lower priority.'], 'default': 100}",
    "start_time": "{'description': ['Date the policy becomes active'], 'default': 'ansible_date_time.iso8601'}",
    "state": "{'description': ['Whether the policy should be present or absent.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['If C(false), SSL certificates will not be validated. This should only be used on personally controlled devices using self-signed certificates.'], 'required': False, 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: policy to aggregate filter and deliver data center (DC) 1 traffic
  bigmon_policy:
    name: policy1
    policy_description: DC 1 traffic policy
    action: drop
    controller: '{{ inventory_hostname }}'
    state: present
    validate_certs: false

```

## License

TODO

## Author Information
  - ['Ted (@tedelhourani)']
