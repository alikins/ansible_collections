# Ansible module: ansible.module_oneview_fc_network


Manage OneView Fibre Channel Network resources

## Description

Provides an interface to manage Fibre Channel Network resources. Can create, update, and delete.

## Requirements

TODO

## Arguments

``` json
{
    "config": "{'description': ['Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section.']}",
    "data": "{'description': ['List with the Fibre Channel Network properties.'], 'required': True}",
    "state": "{'description': ['Indicates the desired state for the Fibre Channel Network resource. C(present) will ensure data properties are compliant with OneView. C(absent) will remove the resource from OneView, if it exists.'], 'choices': ['present', 'absent']}",
    "validate_etag": "{'description': ['When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Ensure that the Fibre Channel Network is present using the default configuration
  oneview_fc_network:
    config: "{{ config_file_path }}"
    state: present
    data:
      name: 'New FC Network'

- name: Ensure that the Fibre Channel Network is present with fabricType 'DirectAttach'
  oneview_fc_network:
    config: "{{ config_file_path }}"
    state: present
    data:
      name: 'New FC Network'
      fabricType: 'DirectAttach'

- name: Ensure that the Fibre Channel Network is present and is inserted in the desired scopes
  oneview_fc_network:
    config: "{{ config_file_path }}"
    state: present
    data:
      name: 'New FC Network'
      scopeUris:
        - '/rest/scopes/00SC123456'
        - '/rest/scopes/01SC123456'

- name: Ensure that the Fibre Channel Network is absent
  oneview_fc_network:
    config: "{{ config_file_path }}"
    state: absent
    data:
      name: 'New FC Network'

```

## License

TODO

## Author Information
  - ['Felipe Bulsoni (@fgbulsoni)']
