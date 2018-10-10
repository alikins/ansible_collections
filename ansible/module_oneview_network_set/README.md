# Ansible module: ansible.module_oneview_network_set


Manage HPE OneView Network Set resources

## Description

Provides an interface to manage Network Set resources. Can create, update, or delete.

## Requirements

TODO

## Arguments

``` json
{
    "config": "{'description': ['Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section.']}",
    "data": "{'description': ['List with the Network Set properties.'], 'required': True}",
    "state": "{'description': ['Indicates the desired state for the Network Set resource. - C(present) will ensure data properties are compliant with OneView. - C(absent) will remove the resource from OneView, if it exists.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_etag": "{'description': ['When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Create a Network Set
  oneview_network_set:
    config: /etc/oneview/oneview_config.json
    state: present
    data:
      name: OneViewSDK Test Network Set
      networkUris:
        - Test Ethernet Network_1                                       # can be a name
        - /rest/ethernet-networks/e4360c9d-051d-4931-b2aa-7de846450dd8  # or a URI
  delegate_to: localhost

- name: Update the Network Set name to 'OneViewSDK Test Network Set - Renamed' and change the associated networks
  oneview_network_set:
    config: /etc/oneview/oneview_config.json
    state: present
    data:
      name: OneViewSDK Test Network Set
      newName: OneViewSDK Test Network Set - Renamed
      networkUris:
        - Test Ethernet Network_1
  delegate_to: localhost

- name: Delete the Network Set
  oneview_network_set:
    config: /etc/oneview/oneview_config.json
    state: absent
    data:
        name: OneViewSDK Test Network Set - Renamed
  delegate_to: localhost

- name: Update the Network set with two scopes
  oneview_network_set:
    config: /etc/oneview/oneview_config.json
    state: present
    data:
      name: OneViewSDK Test Network Set
      scopeUris:
        - /rest/scopes/01SC123456
        - /rest/scopes/02SC123456
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
