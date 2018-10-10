# Ansible module: ansible.module_ovirt_vnic_profile


Module to manage vNIC profile of network in oVirt/RHV

## Description

Module to manage vNIC profile of network in oVirt/RHV

## Requirements

TODO

## Arguments

``` json
{
    "auth": "{'required': True, 'description': ['Dictionary with values needed to create HTTP/HTTPS connection to oVirt:', 'C(username)[I(required)] - The name of the user, something like I(admin@internal). Default value is set by I(OVIRT_USERNAME) environment variable.', 'C(password)[I(required)] - The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.', 'C(url) - A string containing the API URL of the server, usually something like `I(https://server.example.com/ovirt-engine/api)`. Default value is set by I(OVIRT_URL) environment variable. Either C(url) or C(hostname) is required.', 'C(hostname) - A string containing the hostname of the server, usually something like `I(server.example.com)`. Default value is set by I(OVIRT_HOSTNAME) environment variable. Either C(url) or C(hostname) is required.', 'C(token) - Token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.', 'C(insecure) - A boolean flag that indicates if the server TLS certificate and host name should be checked.', 'C(ca_file) - A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `C(ca_file)` parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.', 'C(kerberos) - A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.', 'C(headers) - Dictionary of HTTP headers to be added to each API call.']}",
    "custom_properties": "{'description': ['Custom properties applied to the vNIC profile.', 'Custom properties is a list of dictionary which can have following values:', 'C(name) - Name of the custom property. For example: I(hugepages), I(vhost), I(sap_agent), etc.', 'C(regexp) - Regular expression to set for custom property.', 'C(value) - Value to set for custom property.']}",
    "data_center": "{'description': ['Datacenter name where network reside.'], 'required': True}",
    "description": "{'description': ['A human-readable description in plain text.']}",
    "fetch_nested": "{'description': ['If I(True) the module will fetch additional data from the API.', 'It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying C(nested_attributes).'], 'version_added': '2.3', 'type': 'bool'}",
    "migratable": "{'description': ['Marks whether pass_through NIC is migratable or not.'], 'type': 'bool'}",
    "name": "{'description': ['A human-readable name in plain text.'], 'required': True}",
    "nested_attributes": "{'description': ['Specifies list of the attributes which should be fetched from the API.', 'This parameter apply only when C(fetch_nested) is I(true).'], 'version_added': '2.3'}",
    "network": "{'description': ['Name of network to which is vNIC attached.'], 'required': True}",
    "network_filter": "{'description': ["The network filter enables to filter packets send to/from the VM's nic according to defined rules."]}",
    "pass_through": "{'description': ['Enables passthrough to an SR-IOV-enabled host NIC.'], 'choices': ['disabled', 'enabled']}",
    "poll_interval": "{'description': ['Number of the seconds the module waits until another poll request on entity status is sent.'], 'default': 3}",
    "port_mirroring": "{'description': ['Enables port mirroring.'], 'type': 'bool'}",
    "qos": "{'description': ['Quality of Service attributes regulate inbound and outbound network traffic of the NIC.']}",
    "state": "{'description': ['Should the vNIC be absent/present.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "timeout": "{'description': ['The amount of time in seconds the module should wait for the instance to get into desired state.'], 'default': 180}",
    "wait": "{'description': ['I(True) if the module should wait for the entity to get into desired state.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:
- name: Add vNIC
  ovirt_vnics_profile:
    name: myvnic
    network: mynetwork
    state: present
    data_center: datacenter

- name: Editing vNICs network_filter, custom_properties, qos
  ovirt_vnics_profile:
    name: myvnic
    network: mynetwork
    data_center: datacenter
    qos: myqos
    custom_properties:
      - name: SecurityGroups
        value: 9bd9bde9-39da-44a8-9541-aa39e1a81c9d
    network_filter: allow-dhcp

- name: Editing vNICs network_filter, custom_properties, qos
  ovirt_vnics_profile:
    name: myvnic
    network: mynetwork
    data_center: datacenter
    qos: myqos
    custom_properties:
      - name: SecurityGroups
        value: 9bd9bde9-39da-44a8-9541-aa39e1a81c9d
    network_filter: allow-dhcp

- name: Dont use migratable
  ovirt_vnics_profile:
    name: myvnic
    network: mynetwork
    data_center: datacenter
    migratable: False
    pass_through: enabled

- name: Remove vNIC
  ovirt_vnics_profile:
    name: myvnic
    network: mynetwork
    state: absent
    data_center: datacenter

```

## License

TODO

## Author Information
  - ['Ondra Machacek (@machacekondra)', 'Martin Necas (@mnecas)']
  - ['Ondra Machacek (@machacekondra)', 'Martin Necas (@mnecas)']
