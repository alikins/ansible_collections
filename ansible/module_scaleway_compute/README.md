# Ansible module: ansible.module_scaleway_compute


Scaleway compute management module

## Description

This module manages compute instances on Scaleway.

## Requirements

TODO

## Arguments

``` json
{
    "api_timeout": "{'description': ['HTTP timeout to Scaleway API in seconds.'], 'default': 30, 'aliases': ['timeout']}",
    "api_token": "{'description': ['Scaleway OAuth token.'], 'aliases': ['oauth_token']}",
    "api_url": "{'description': ['Scaleway API URL'], 'default': 'https://api.scaleway.com', 'aliases': ['base_url']}",
    "commercial_type": "{'description': ['Commercial name of the compute node'], 'required': True, 'choices': ['ARM64-2GB', 'ARM64-4GB', 'ARM64-8GB', 'ARM64-16GB', 'ARM64-32GB', 'ARM64-64GB', 'ARM64-128GB', 'C1', 'C2S', 'C2M', 'C2L', 'START1-XS', 'START1-S', 'START1-M', 'START1-L', 'X64-15GB', 'X64-30GB', 'X64-60GB', 'X64-120GB']}",
    "enable_ipv6": "{'description': ['Enable public IPv6 connectivity on the instance'], 'default': False, 'type': 'bool'}",
    "image": "{'description': ['Image identifier used to start the instance with'], 'required': True}",
    "name": "{'description': ['Name of the instance']}",
    "organization": "{'description': ['Organization identifier'], 'required': True}",
    "public_ip": "{'description': ['Manage public IP on a Scaleway server', 'Could be Scaleway IP address UUID', 'C(dynamic) Means that IP is destroyed at the same time the host is destroyed', 'C(absent) Means no public IP at all'], 'version_added': '2.8', 'default': 'absent'}",
    "region": "{'description': ['Scaleway compute zone'], 'required': True, 'choices': ['ams1', 'EMEA-NL-EVS', 'par1', 'EMEA-FR-PAR1']}",
    "state": "{'description': ['Indicate desired state of the instance.'], 'default': 'present', 'choices': ['present', 'absent', 'running', 'restarted', 'stopped']}",
    "tags": "{'description': ['List of tags to apply to the instance (5 max)'], 'required': False, 'default': []}",
    "validate_certs": "{'description': ['Validate SSL certs of the Scaleway API.'], 'default': True, 'type': 'bool'}",
    "wait": "{'description': ['Wait for the instance to reach its desired state before returning.'], 'type': 'bool', 'default': False}",
    "wait_sleep_time": "{'description': ['Time to wait before every attempt to check the state of the server'], 'required': False, 'default': 3}",
    "wait_timeout": "{'description': ['Time to wait for the server to reach the expected state'], 'required': False, 'default': 300}",
}
```

## Examples


``` yaml

- name: Create a server
  scaleway_compute:
    name: foobar
    state: present
    image: 89ee4018-f8c3-4dc4-a6b5-bca14f985ebe
    organization: 951df375-e094-4d26-97c1-ba548eeb9c42
    region: ams1
    commercial_type: VC1S
    tags:
      - test
      - www

- name: Destroy it right after
  scaleway_compute:
    name: foobar
    state: absent
    image: 89ee4018-f8c3-4dc4-a6b5-bca14f985ebe
    organization: 951df375-e094-4d26-97c1-ba548eeb9c42
    region: ams1
    commercial_type: VC1S

```

## License

TODO

## Author Information
  - ['Remy Leone (@sieben)']
