# Ansible module: ansible.module_meraki_config_template


Manage configuration templates in the Meraki cloud

## Description

Allows for querying, deleting, binding, and unbinding of configuration templates.

## Requirements

TODO

## Arguments

``` json
{
    "auth_key": "{'description': ['Authentication key provided by the dashboard. Required if environmental variable MERAKI_KEY is not set.']}",
    "auto_bind": "{'description': ["Optional boolean indicating whether the network's switches should automatically bind to profiles of the same model.", 'This option only affects switch networks and switch templates.', 'Auto-bind is not valid unless the switch template has at least one profile and has at most one profile per switch model.'], 'type': 'bool'}",
    "config_template": "{'description': ['Name of the configuration template within an organization to manipulate.'], 'aliases': ['name']}",
    "host": "{'description': ['Hostname for Meraki dashboard', 'Only useful for internal Meraki developers'], 'type': 'string', 'default': 'api.meraki.com'}",
    "net_id": "{'description': ['ID of the network to bind or unbind configuration template to.']}",
    "net_name": "{'description': ['Name of the network to bind or unbind configuration template to.']}",
    "org_id": "{'description': ['ID of organization associated to a configuration template.']}",
    "org_name": "{'description': ['Name of organization containing the configuration template.'], 'aliases': ['organization']}",
    "output_level": "{'description': ['Set amount of debug output during module execution'], 'choices': ['normal', 'debug'], 'default': 'normal'}",
    "state": "{'description': ['Specifies whether configuration template information should be queried, modified, or deleted.'], 'choices': ['absent', 'query', 'present'], 'default': 'query'}",
    "timeout": "{'description': ['Time to timeout for HTTP requests.'], 'type': 'int', 'default': 30}",
    "use_https": "{'description': ['If C(no), it will use HTTP. Otherwise it will use HTTPS.', 'Only useful for internal Meraki developers'], 'type': 'bool', 'default': True}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool'}",
    "validate_certs": "{'description': ['Whether to validate HTTP certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Query configuration templates
  meraki_config_template:
    auth_key: abc12345
    org_name: YourOrg
    state: query
  delegate_to: localhost

- name: Bind a template from a network
  meraki_config_template:
    auth_key: abc123
    state: present
    org_name: YourOrg
    net_name: YourNet
    config_template: DevConfigTemplate
  delegate_to: localhost

- name: Unbind a template from a network
  meraki_config_template:
    auth_key: abc123
    state: absent
    org_name: YourOrg
    net_name: YourNet
    config_template: DevConfigTemplate
  delegate_to: localhost

- name: Delete a configuration template
  meraki_config_template:
    auth_key: abc123
    state: absent
    org_name: YourOrg
    config_template: DevConfigTemplate
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Kevin Breit (@kbreit)']
