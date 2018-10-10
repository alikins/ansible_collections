# Ansible module: ansible.module_meraki_organization


Manage organizations in the Meraki cloud

## Description

Allows for creation, management, and visibility into organizations within Meraki.

## Requirements

TODO

## Arguments

``` json
{
    "auth_key": "{'description': ['Authentication key provided by the dashboard. Required if environmental variable MERAKI_KEY is not set.']}",
    "clone": "{'description': ['Organization to clone to a new organization.']}",
    "host": "{'description': ['Hostname for Meraki dashboard', 'Only useful for internal Meraki developers'], 'type': 'string', 'default': 'api.meraki.com'}",
    "org_id": "{'description': ['ID of organization.'], 'aliases': ['id']}",
    "org_name": "{'description': ['Name of organization.', 'If C(clone) is specified, C(org_name) is the name of the new organization.'], 'aliases': ['name', 'organization']}",
    "output_level": "{'description': ['Set amount of debug output during module execution'], 'choices': ['normal', 'debug'], 'default': 'normal'}",
    "state": "{'description': ['Create or modify an organization.'], 'choices': ['present', 'query'], 'default': 'present'}",
    "timeout": "{'description': ['Time to timeout for HTTP requests.'], 'type': 'int', 'default': 30}",
    "use_https": "{'description': ['If C(no), it will use HTTP. Otherwise it will use HTTPS.', 'Only useful for internal Meraki developers'], 'type': 'bool', 'default': True}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool'}",
    "validate_certs": "{'description': ['Whether to validate HTTP certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Create a new organization named YourOrg
  meraki_organization:
    auth_key: abc12345
    org_name: YourOrg
    state: present
  delegate_to: localhost

- name: Query information about all organizations associated to the user
  meraki_organization:
    auth_key: abc12345
    state: query
  delegate_to: localhost

- name: Query information about a single organization named YourOrg
  meraki_organization:
    auth_key: abc12345
    org_name: YourOrg
    state: query
  delegate_to: localhost

- name: Rename an organization to RenamedOrg
  meraki_organization:
    auth_key: abc12345
    org_id: 987654321
    org_name: RenamedOrg
    state: present
  delegate_to: localhost

- name: Clone an organization named Org to a new one called ClonedOrg
  meraki_organization:
    auth_key: abc12345
    clone: Org
    org_name: ClonedOrg
    state: present
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Kevin Breit (@kbreit)']
