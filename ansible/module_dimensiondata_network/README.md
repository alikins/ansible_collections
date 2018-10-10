# Ansible module: ansible.module_dimensiondata_network


Create, update, and delete MCP 1.0 & 2.0 networks

## Description

Create, update, and delete MCP 1.0 & 2.0 networks

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['Additional description of the network domain.'], 'required': False}",
    "location": "{'description': ['The target datacenter.'], 'required': True}",
    "mcp_password": "{'description': ['The password used to authenticate to the CloudControl API.', 'If not specified, will fall back to C(MCP_PASSWORD) from environment variable or C(~/.dimensiondata).', 'Required if I(mcp_user) is specified.'], 'required': False}",
    "mcp_user": "{'description': ['The username used to authenticate to the CloudControl API.', 'If not specified, will fall back to C(MCP_USER) from environment variable or C(~/.dimensiondata).'], 'required': False}",
    "name": "{'description': ['The name of the network domain to create.'], 'required': True}",
    "region": "{'description': ['The target region.'], 'choices': ['Regions are defined in Apache libcloud project [libcloud/common/dimensiondata.py]', 'They are also listed in U(https://libcloud.readthedocs.io/en/latest/compute/drivers/dimensiondata.html)', 'Note that the default value "na" stands for "North America".', "The module prepends 'dd-' to the region choice."], 'default': 'na'}",
    "service_plan": "{'description': ['The service plan, either "ESSENTIALS" or "ADVANCED".', 'MCP 2.0 Only.'], 'choices': ['ESSENTIALS', 'ADVANCED'], 'default': 'ESSENTIALS'}",
    "state": "{'description': ['Should the resource be present or absent.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "validate_certs": "{'description': ['If C(false), SSL certificates will not be validated.', 'This should only be used on private instances of the CloudControl API that use self-signed certificates.'], 'required': False, 'default': True}",
    "wait": "{'description': ['Should we wait for the task to complete before moving onto the next.'], 'required': False, 'default': False}",
    "wait_poll_interval": "{'description': ['The amount of time (in seconds) to wait between checks for task completion.', 'Only applicable if I(wait=true).'], 'required': False, 'default': 2}",
    "wait_time": "{'description': ['The maximum amount of time (in seconds) to wait for the task to complete.', 'Only applicable if I(wait=true).'], 'required': False, 'default': 600}",
}
```

## Examples


``` yaml

# Create an MCP 1.0 network
- dimensiondata_network:
    region: na
    location: NA5
    name: mynet
# Create an MCP 2.0 network
- dimensiondata_network:
    region: na
    mcp_user: my_user
    mcp_password: my_password
    location: NA9
    name: mynet
    service_plan: ADVANCED
# Delete a network
- dimensiondata_network:
    region: na
    location: NA1
    name: mynet
    state: absent

```

## License

TODO

## Author Information
  - ['Aimon Bustardo (@aimonb)']
