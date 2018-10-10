# Ansible module: ansible.module_oneview_logical_interconnect_group


Manage OneView Logical Interconnect Group resources

## Description

Provides an interface to manage Logical Interconnect Group resources. Can create, update, or delete.

## Requirements

TODO

## Arguments

``` json
{
    "config": "{'description': ['Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section.']}",
    "data": "{'description': ['List with the Logical Interconnect Group properties.'], 'required': True}",
    "state": "{'description': ['Indicates the desired state for the Logical Interconnect Group resource. C(absent) will remove the resource from OneView, if it exists. C(present) will ensure data properties are compliant with OneView.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "validate_etag": "{'description': ['When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Ensure that the Logical Interconnect Group is present
  oneview_logical_interconnect_group:
    config: /etc/oneview/oneview_config.json
    state: present
    data:
      name: Test Logical Interconnect Group
      uplinkSets: []
      enclosureType: C7000
      interconnectMapTemplate:
        interconnectMapEntryTemplates:
          - logicalDownlinkUri: ~
            logicalLocation:
                locationEntries:
                    - relativeValue: 1
                      type: Bay
                    - relativeValue: 1
                      type: Enclosure
            permittedInterconnectTypeName: HP VC Flex-10/10D Module
            # Alternatively you can inform permittedInterconnectTypeUri
  delegate_to: localhost

- name: Ensure that the Logical Interconnect Group has the specified scopes
  oneview_logical_interconnect_group:
    config: /etc/oneview/oneview_config.json
    state: present
    data:
      name: Test Logical Interconnect Group
      scopeUris:
        - /rest/scopes/00SC123456
        - /rest/scopes/01SC123456
  delegate_to: localhost

- name: Ensure that the Logical Interconnect Group is present with name 'Test'
  oneview_logical_interconnect_group:
    config: /etc/oneview/oneview_config.json
    state: present
    data:
      name: New Logical Interconnect Group
      newName: Test
  delegate_to: localhost

- name: Ensure that the Logical Interconnect Group is absent
  oneview_logical_interconnect_group:
    config: /etc/oneview/oneview_config.json
    state: absent
    data:
      name: New Logical Interconnect Group
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
