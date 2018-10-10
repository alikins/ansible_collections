# Ansible module: ansible.module_meraki_admin


Manage administrators in the Meraki cloud

## Description

Allows for creation, management, and visibility into administrators within Meraki.

## Requirements

TODO

## Arguments

``` json
{
    "auth_key": "{'description': ['Authentication key provided by the dashboard. Required if environmental variable MERAKI_KEY is not set.']}",
    "email": "{'description': ['Email address for the dashboard administrator.', 'Email cannot be updated.', 'Required when creating or editing an administrator.']}",
    "host": "{'description': ['Hostname for Meraki dashboard', 'Only useful for internal Meraki developers'], 'type': 'string', 'default': 'api.meraki.com'}",
    "name": "{'description': ['Name of the dashboard administrator.', 'Required when creating a new administrator.']}",
    "networks": "{'description': ['List of networks the administrator has privileges on.', 'When creating a new administrator, C(org_name), C(network), or C(tags) must be specified.']}",
    "org_id": "{'description': ['ID of organization.']}",
    "org_name": "{'description': ['Name of organization.', 'Used when C(name) should refer to another object.', 'When creating a new administrator, C(org_name), C(network), or C(tags) must be specified.'], 'aliases': ['organization']}",
    "orgAccess": "{'description': ['Privileges assigned to the administrator in the organization.'], 'choices': ['full', 'none', 'read-only']}",
    "output_level": "{'description': ['Set amount of debug output during module execution'], 'choices': ['normal', 'debug'], 'default': 'normal'}",
    "state": "{'description': ['Create or modify an organization'], 'choices': ['absent', 'present', 'query'], 'required': True}",
    "tags": "{'description': ['Tags the administrator has privileges on.', 'When creating a new administrator, C(org_name), C(network), or C(tags) must be specified.', 'If C(none) is specified, C(network) or C(tags) must be specified.']}",
    "timeout": "{'description': ['Time to timeout for HTTP requests.'], 'type': 'int', 'default': 30}",
    "use_https": "{'description': ['If C(no), it will use HTTP. Otherwise it will use HTTPS.', 'Only useful for internal Meraki developers'], 'type': 'bool', 'default': True}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool'}",
    "validate_certs": "{'description': ['Whether to validate HTTP certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Query information about all administrators associated to the organization
  meraki_admin:
    auth_key: abc12345
    org_name: YourOrg
    state: query
  delegate_to: localhost

- name: Query information about a single administrator by name
  meraki_admin:
    auth_key: abc12345
    org_id: 12345
    state: query
    name: Jane Doe

- name: Query information about a single administrator by email
  meraki_admin:
    auth_key: abc12345
    org_name: YourOrg
    state: query
    email: jane@doe.com

- name: Create new administrator with organization access
  meraki_admin:
    auth_key: abc12345
    org_name: YourOrg
    state: present
    name: Jane Doe
    orgAccess: read-only
    email: jane@doe.com

- name: Create new administrator with organization access
  meraki_admin:
    auth_key: abc12345
    org_name: YourOrg
    state: present
    name: Jane Doe
    orgAccess: read-only
    email: jane@doe.com

- name: Create a new administrator with organization access
  meraki_admin:
    auth_key: abc12345
    org_name: YourOrg
    state: present
    name: Jane Doe
    orgAccess: read-only
    email: jane@doe.com

- name: Revoke access to an organization for an administrator
  meraki_admin:
    auth_key: abc12345
    org_name: YourOrg
    state: absent
    email: jane@doe.com

```

## License

TODO

## Author Information
  - ['Kevin Breit (@kbreit)']
