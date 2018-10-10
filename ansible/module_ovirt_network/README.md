# Ansible module: ansible.module_ovirt_network


Module to manage logical networks in oVirt/RHV

## Description

Module to manage logical networks in oVirt/RHV

## Requirements

TODO

## Arguments

``` json
{
    "auth": "{'required': True, 'description': ['Dictionary with values needed to create HTTP/HTTPS connection to oVirt:', 'C(username)[I(required)] - The name of the user, something like I(admin@internal). Default value is set by I(OVIRT_USERNAME) environment variable.', 'C(password)[I(required)] - The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.', 'C(url) - A string containing the API URL of the server, usually something like `I(https://server.example.com/ovirt-engine/api)`. Default value is set by I(OVIRT_URL) environment variable. Either C(url) or C(hostname) is required.', 'C(hostname) - A string containing the hostname of the server, usually something like `I(server.example.com)`. Default value is set by I(OVIRT_HOSTNAME) environment variable. Either C(url) or C(hostname) is required.', 'C(token) - Token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.', 'C(insecure) - A boolean flag that indicates if the server TLS certificate and host name should be checked.', 'C(ca_file) - A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `C(ca_file)` parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.', 'C(kerberos) - A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.', 'C(headers) - Dictionary of HTTP headers to be added to each API call.']}",
    "clusters": "{'description': ['List of dictionaries describing how the network is managed in specific cluster.', 'C(name) - Cluster name.', 'C(assigned) - I(true) if the network should be assigned to cluster. Default is I(true).', 'C(required) - I(true) if the network must remain operational for all hosts associated with this network.', 'C(display) - I(true) if the network should marked as display network.', 'C(migration) - I(true) if the network should marked as migration network.', 'C(gluster) - I(true) if the network should marked as gluster network.']}",
    "comment": "{'description': ['Comment of the network.']}",
    "data_center": "{'description': ['Datacenter name where network reside.']}",
    "description": "{'description': ['Description of the network.']}",
    "external_provider": "{'description': ['Name of external network provider.'], 'version_added': 2.8}",
    "fetch_nested": "{'description': ['If I(True) the module will fetch additional data from the API.', 'It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying C(nested_attributes).'], 'version_added': '2.3', 'type': 'bool'}",
    "id": "{'description': ['ID of the network to manage.'], 'version_added': '2.8'}",
    "label": "{'description': ['Name of the label to assign to the network.'], 'version_added': '2.5'}",
    "mtu": "{'description': ['Maximum transmission unit (MTU) of the network.']}",
    "name": "{'description': ['Name of the network to manage.'], 'required': True}",
    "nested_attributes": "{'description': ['Specifies list of the attributes which should be fetched from the API.', 'This parameter apply only when C(fetch_nested) is I(true).'], 'version_added': '2.3'}",
    "poll_interval": "{'description': ['Number of the seconds the module waits until another poll request on entity status is sent.'], 'default': 3}",
    "state": "{'description': ['Should the network be present or absent'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['The amount of time in seconds the module should wait for the instance to get into desired state.'], 'default': 180}",
    "vlan_tag": "{'description': ['Specify VLAN tag.']}",
    "vm_network": "{'description': ['If I(True) network will be marked as network for VM.', 'VM network carries traffic relevant to the virtual machine.'], 'type': 'bool'}",
    "wait": "{'description': ['I(True) if the module should wait for the entity to get into desired state.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Create network
- ovirt_network:
    data_center: mydatacenter
    name: mynetwork
    vlan_tag: 1
    vm_network: true

# Remove network
- ovirt_network:
    state: absent
    name: mynetwork

# Change Network Name
- ovirt_network:
    id: 00000000-0000-0000-0000-000000000000
    name: "new_network_name"
    data_center: mydatacenter

# Add network from external provider
- ovirt_networks:
    data_center: mydatacenter
    name: mynetwork
    external_provider: ovirt-provider-ovn

```

## License

TODO

## Author Information
  - ['Ondra Machacek (@machacekondra)']
