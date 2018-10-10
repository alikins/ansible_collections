# Ansible module: ansible.module_meraki_network


Manage networks in the Meraki cloud

## Description

Allows for creation, management, and visibility into networks within Meraki.

## Requirements

TODO

## Arguments

``` json
{
    "auth_key": "{'description': ['Authentication key provided by the dashboard. Required if environmental variable MERAKI_KEY is not set.']}",
    "disable_my_meraki": "{'description': ['- Disables the local device status pages (U[my.meraki.com](my.meraki.com), U[ap.meraki.com](ap.meraki.com), U[switch.meraki.com](switch.meraki.com), U[wired.meraki.com](wired.meraki.com))\n'], 'type': 'bool', 'version_added': '2.7'}",
    "host": "{'description': ['Hostname for Meraki dashboard', 'Only useful for internal Meraki developers'], 'type': 'string', 'default': 'api.meraki.com'}",
    "net_id": "{'description': ['ID number of a network.']}",
    "net_name": "{'description': ['Name of a network.'], 'aliases': ['name', 'network']}",
    "org_id": "{'description': ['ID of organization associated to a network.']}",
    "org_name": "{'description': ['Name of organization associated to a network.'], 'aliases': ['organization']}",
    "output_level": "{'description': ['Set amount of debug output during module execution'], 'choices': ['normal', 'debug'], 'default': 'normal'}",
    "state": "{'description': ['Create or modify an organization.'], 'choices': ['absent', 'present', 'query'], 'default': 'present'}",
    "tags": "{'description': ['Comma delimited list of tags to assign to network.']}",
    "timeout": "{'description': ['Time to timeout for HTTP requests.'], 'type': 'int', 'default': 30}",
    "timezone": "{'description': ['Timezone associated to network.', 'See U(https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) for a list of valid timezones.']}",
    "type": "{'description': ['Type of network device network manages.', 'Required when creating a network.'], 'choices': ['appliance', 'combined', 'switch', 'wireless'], 'aliases': ['net_type']}",
    "use_https": "{'description': ['If C(no), it will use HTTP. Otherwise it will use HTTPS.', 'Only useful for internal Meraki developers'], 'type': 'bool', 'default': True}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool'}",
    "validate_certs": "{'description': ['Whether to validate HTTP certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: List all networks associated to the YourOrg organization
  meraki_network:
    auth_key: abc12345
    status: query
    org_name: YourOrg
  delegate_to: localhost
- name: Query network named MyNet in the YourOrg organization
  meraki_network:
    auth_key: abc12345
    status: query
    org_name: YourOrg
    net_name: MyNet
  delegate_to: localhost
- name: Create network named MyNet in the YourOrg organization
  meraki_network:
    auth_key: abc12345
    status: present
    org_name: YourOrg
    net_name: MyNet
    type: switch
    timezone: America/Chicago
    tags: production, chicago
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Kevin Breit (@kbreit)']
