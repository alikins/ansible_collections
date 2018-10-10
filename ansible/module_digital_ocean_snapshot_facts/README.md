# Ansible module: ansible.module_digital_ocean_snapshot_facts


Gather facts about DigitalOcean Snapshot

## Description

This module can be used to gather facts about snapshot facts based upon provided values such as droplet, volume and snapshot id.

## Requirements

TODO

## Arguments

``` json
{
    "oauth_token": "{'description': ['DigitalOcean OAuth token.', 'There are several other environment variables which can be used to provide this value.', "i.e., - 'DO_API_TOKEN', 'DO_API_KEY', 'DO_OAUTH_TOKEN' and 'OAUTH_TOKEN'"], 'required': False, 'aliases': ['api_token']}",
    "snapshot_id": "{'description': ['To retrieve information about a snapshot, please specify this as a snapshot id.', 'If set to actual snapshot id, then facts are gathered related to that particular snapshot only.', 'This is required parameter, if C(snapshot_type) is set to C(by_id).'], 'required': False}",
    "snapshot_type": "{'description': ['Specifies the type of snapshot facts to be retrived.', 'If set to C(droplet), then facts are gathered related to snapshots based on Droplets only.', 'If set to C(volume), then facts are gathered related to snapshots based on volumes only.', 'If set to C(by_id), then facts are gathered related to snapshots based on snapshot id only.', 'If not set to any of the above, then facts are gathered related to all snapshots.'], 'default': 'all', 'choices': ['all', 'droplet', 'volume', 'by_id'], 'required': False}",
    "timeout": "{'description': ["The timeout in seconds used for polling DigitalOcean's API."], 'default': 30}",
    "validate_certs": "{'description': ['If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Gather facts about all snapshots
  digital_ocean_snapshot_facts:
    snapshot_type: all
    oauth_token: "{{ oauth_token }}"

- name: Gather facts about droplet snapshots
  digital_ocean_snapshot_facts:
    snapshot_type: droplet
    oauth_token: "{{ oauth_token }}"

- name: Gather facts about volume snapshots
  digital_ocean_snapshot_facts:
    snapshot_type: volume
    oauth_token: "{{ oauth_token }}"

- name: Gather facts about snapshot by snapshot id
  digital_ocean_snapshot_facts:
    snapshot_type: by_id
    snapshot_id: 123123123
    oauth_token: "{{ oauth_token }}"

- name: Get facts about snapshot named big-data-snapshot1
  digital_ocean_snapshot_facts:
  register: resp_out
- set_fact:
    snapshot_id: "{{ item.id }}"
  with_items: "{{ resp_out.data|json_query(name) }}"
  vars:
    name: "[?name=='big-data-snapshot1']"
- debug: var=snapshot_id


```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
