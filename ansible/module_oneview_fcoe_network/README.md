# Ansible module: ansible.module_oneview_fcoe_network


Manage OneView FCoE Network resources

## Description

Provides an interface to manage FCoE Network resources. Can create, update, or delete.

## Requirements

TODO

## Arguments

``` json
{
    "config": "{'description': ['Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section.']}",
    "data": "{'description': ['List with FCoE Network properties.'], 'required': True}",
    "state": "{'description': ['Indicates the desired state for the FCoE Network resource. C(present) will ensure data properties are compliant with OneView. C(absent) will remove the resource from OneView, if it exists.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_etag": "{'description': ['When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Ensure that FCoE Network is present using the default configuration
  oneview_fcoe_network:
    config: '/etc/oneview/oneview_config.json'
    state: present
    data:
      name: Test FCoE Network
      vlanId: 201
  delegate_to: localhost

- name: Update the FCOE network scopes
  oneview_fcoe_network:
    config: '/etc/oneview/oneview_config.json'
    state: present
    data:
      name: New FCoE Network
      scopeUris:
        - '/rest/scopes/00SC123456'
        - '/rest/scopes/01SC123456'
  delegate_to: localhost

- name: Ensure that FCoE Network is absent
  oneview_fcoe_network:
    config: '/etc/oneview/oneview_config.json'
    state: absent
    data:
      name: New FCoE Network
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Felipe Bulsoni (@fgbulsoni)']
