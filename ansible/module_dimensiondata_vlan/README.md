# Ansible module: ansible.module_dimensiondata_vlan


Manage a VLAN in a Cloud Control network domain

## Description

Manage VLANs in Cloud Control network domains.

## Requirements

TODO

## Arguments

``` json
{
    "allow_expand": "{'description': ["Permit expansion of the target VLAN's network if the module parameters specify a larger network than the VLAN currently posesses?", 'If C(False), the module will fail under these conditions.', "This is intended to prevent accidental expansion of a VLAN's network (since this operation is not reversible)."], 'type': 'bool', 'default': False}",
    "description": "{'description': ['A description of the VLAN.']}",
    "location": "{'description': ['The target datacenter.'], 'required': True}",
    "mcp_password": "{'description': ['The password used to authenticate to the CloudControl API.', 'If not specified, will fall back to C(MCP_PASSWORD) from environment variable or C(~/.dimensiondata).', 'Required if I(mcp_user) is specified.'], 'required': False}",
    "mcp_user": "{'description': ['The username used to authenticate to the CloudControl API.', 'If not specified, will fall back to C(MCP_USER) from environment variable or C(~/.dimensiondata).'], 'required': False}",
    "name": "{'description': ['The name of the target VLAN.', 'Required if C(state) is C(present).']}",
    "network_domain": "{'description': ['The Id or name of the target network domain.'], 'required': True}",
    "private_ipv4_base_address": "{'description': ["The base address for the VLAN's IPv4 network (e.g. 192.168.1.0)."]}",
    "private_ipv4_prefix_size": "{'description': ['The size of the IPv4 address space, e.g 24.', 'Required, if C(private_ipv4_base_address) is specified.']}",
    "region": "{'description': ['The target region.'], 'choices': ['Regions are defined in Apache libcloud project [libcloud/common/dimensiondata.py]', 'They are also listed in U(https://libcloud.readthedocs.io/en/latest/compute/drivers/dimensiondata.html)', 'Note that the default value "na" stands for "North America".', "The module prepends 'dd-' to the region choice."], 'default': 'na'}",
    "state": "{'description': ['The desired state for the target VLAN.', 'C(readonly) ensures that the state is only ever read, not modified (the module will fail if the resource does not exist).'], 'choices': ['present', 'absent', 'readonly'], 'default': 'present'}",
    "validate_certs": "{'description': ['If C(false), SSL certificates will not be validated.', 'This should only be used on private instances of the CloudControl API that use self-signed certificates.'], 'required': False, 'default': True}",
    "wait": "{'description': ['Should we wait for the task to complete before moving onto the next.'], 'required': False, 'default': False}",
    "wait_poll_interval": "{'description': ['The amount of time (in seconds) to wait between checks for task completion.', 'Only applicable if I(wait=true).'], 'required': False, 'default': 2}",
    "wait_time": "{'description': ['The maximum amount of time (in seconds) to wait for the task to complete.', 'Only applicable if I(wait=true).'], 'required': False, 'default': 600}",
}
```

## Examples


``` yaml

# Add or update VLAN
- dimensiondata_vlan:
    region: na
    location: NA5
    network_domain: test_network
    name: my_vlan1
    description: A test VLAN
    private_ipv4_base_address: 192.168.23.0
    private_ipv4_prefix_size: 24
    state: present
    wait: yes
# Read / get VLAN details
- dimensiondata_vlan:
    region: na
    location: NA5
    network_domain: test_network
    name: my_vlan1
    state: readonly
    wait: yes
# Delete a VLAN
- dimensiondata_vlan:
    region: na
    location: NA5
    network_domain: test_network
    name: my_vlan_1
    state: absent
    wait: yes

```

## License

TODO

## Author Information
  - ['Adam Friedman (@tintoy)']
