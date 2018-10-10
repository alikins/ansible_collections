# Ansible module: ansible.module_oneview_ethernet_network


Manage OneView Ethernet Network resources

## Description

Provides an interface to manage Ethernet Network resources. Can create, update, or delete.

## Requirements

TODO

## Arguments

``` json
{
    "config": "{'description': ['Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section.']}",
    "data": "{'description': ['List with Ethernet Network properties.'], 'required': True}",
    "state": "{'description': ['Indicates the desired state for the Ethernet Network resource. - C(present) will ensure data properties are compliant with OneView. - C(absent) will remove the resource from OneView, if it exists. - C(default_bandwidth_reset) will reset the network connection template to the default.'], 'default': 'present', 'choices': ['present', 'absent', 'default_bandwidth_reset']}",
    "validate_etag": "{'description': ['When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Ensure that the Ethernet Network is present using the default configuration
  oneview_ethernet_network:
    config: '/etc/oneview/oneview_config.json'
    state: present
    data:
      name: 'Test Ethernet Network'
      vlanId: '201'
  delegate_to: localhost

- name: Update the Ethernet Network changing bandwidth and purpose
  oneview_ethernet_network:
    config: '/etc/oneview/oneview_config.json'
    state: present
    data:
      name: 'Test Ethernet Network'
      purpose: Management
      bandwidth:
          maximumBandwidth: 3000
          typicalBandwidth: 2000
  delegate_to: localhost

- name: Ensure that the Ethernet Network is present with name 'Renamed Ethernet Network'
  oneview_ethernet_network:
    config: '/etc/oneview/oneview_config.json'
    state: present
    data:
      name: 'Test Ethernet Network'
      newName: 'Renamed Ethernet Network'
  delegate_to: localhost

- name: Ensure that the Ethernet Network is absent
  oneview_ethernet_network:
    config: '/etc/oneview/oneview_config.json'
    state: absent
    data:
      name: 'New Ethernet Network'
  delegate_to: localhost

- name: Create Ethernet networks in bulk
  oneview_ethernet_network:
    config: '/etc/oneview/oneview_config.json'
    state: present
    data:
      vlanIdRange: '1-10,15,17'
      purpose: General
      namePrefix: TestNetwork
      smartLink: false
      privateNetwork: false
      bandwidth:
        maximumBandwidth: 10000
        typicalBandwidth: 2000
  delegate_to: localhost

- name: Reset to the default network connection template
  oneview_ethernet_network:
    config: '/etc/oneview/oneview_config.json'
    state: default_bandwidth_reset
    data:
      name: 'Test Ethernet Network'
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
