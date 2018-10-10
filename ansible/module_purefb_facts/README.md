# Ansible module: ansible.module_purefb_facts


Collect facts from Pure Storage FlashBlade

## Description

Collect facts information from a Pure Storage FlashBlade running the Purity//FB operating system. By default, the module will collect basic fact information including hosts, host groups, protection groups and volume counts. Additional fact information can be collected based on the configured set of arguements.

## Requirements

TODO

## Arguments

``` json
{
    "api_token": "{'description': ['FlashBlade API token for admin privileged user.']}",
    "fb_url": "{'description': ['FlashBlade management IP address or Hostname.']}",
    "gather_subset": "{'description': ['When supplied, this argument will define the facts to be collected. Possible values for this include all, minimum, config, performance, capacity, network, subnets, lags, filesystems and snapshots.'], 'required': False, 'default': 'minimum'}",
}
```

## Examples


``` yaml

- name: collect default set of facts
  purefb_facts:
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: collect configuration and capacity facts
  purefb_facts:
    gather_subset:
      - config
      - capacity
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: collect all facts
  purefb_facts:
    gather_subset:
      - all
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

```

## License

TODO

## Author Information
  - ['Simon Dodsley (@sdodsley)']
