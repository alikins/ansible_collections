# Ansible module: ansible.module_purefa_facts


Collect facts from Pure Storage FlashArray

## Description

Collect facts information from a Pure Storage Flasharray running the Purity//FA operating system. By default, the module will collect basic fact information including hosts, host groups, protection groups and volume counts. Additional fact information can be collected based on the configured set of arguements.

## Requirements

TODO

## Arguments

``` json
{
    "api_token": "{'description': ['FlashArray API token for admin privileged user.'], 'required': True}",
    "fa_url": "{'description': ['FlashArray management IPv4 address or Hostname.'], 'required': True}",
    "gather_subset": "{'description': ['When supplied, this argument will define the facts to be collected. Possible values for this include all, minimum, config, performance, capacity, network, subnet, interfaces, hgroups, pgroups, hosts, volumes and snapshots.'], 'required': False, 'default': 'minimum'}",
}
```

## Examples


``` yaml

- name: collect default set of facts
  purefa_facts:
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: collect configuration and capacity facts
  purefa_facts:
    gather_subset:
      - config
      - capacity
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: collect all facts
  purefa_facts:
    gather_subset:
      - all
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

```

## License

TODO

## Author Information
  - ['Simon Dodsley (@sdodsley)']
