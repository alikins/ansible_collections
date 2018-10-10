# Ansible module: ansible.module_ovirt_nic


Module to manage network interfaces of Virtual Machines in oVirt/RHV

## Description

Module to manage network interfaces of Virtual Machines in oVirt/RHV.

## Requirements

TODO

## Arguments

``` json
{
    "auth": "{'required': True, 'description': ['Dictionary with values needed to create HTTP/HTTPS connection to oVirt:', 'C(username)[I(required)] - The name of the user, something like I(admin@internal). Default value is set by I(OVIRT_USERNAME) environment variable.', 'C(password)[I(required)] - The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.', 'C(url) - A string containing the API URL of the server, usually something like `I(https://server.example.com/ovirt-engine/api)`. Default value is set by I(OVIRT_URL) environment variable. Either C(url) or C(hostname) is required.', 'C(hostname) - A string containing the hostname of the server, usually something like `I(server.example.com)`. Default value is set by I(OVIRT_HOSTNAME) environment variable. Either C(url) or C(hostname) is required.', 'C(token) - Token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.', 'C(insecure) - A boolean flag that indicates if the server TLS certificate and host name should be checked.', 'C(ca_file) - A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `C(ca_file)` parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.', 'C(kerberos) - A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.', 'C(headers) - Dictionary of HTTP headers to be added to each API call.']}",
    "fetch_nested": "{'description': ['If I(True) the module will fetch additional data from the API.', 'It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying C(nested_attributes).'], 'version_added': '2.3', 'type': 'bool'}",
    "id": "{'description': ['ID of the nic to manage.'], 'version_added': '2.8'}",
    "interface": "{'description': ['Type of the network interface. For example e1000, pci_passthrough, rtl8139, rtl8139_virtio, spapr_vlan or virtio.', "It's required parameter when creating the new NIC."]}",
    "mac_address": "{'description': ["Custom MAC address of the network interface, by default it's obtained from MAC pool."]}",
    "name": "{'description': ['Name of the network interface to manage.'], 'required': True}",
    "nested_attributes": "{'description': ['Specifies list of the attributes which should be fetched from the API.', 'This parameter apply only when C(fetch_nested) is I(true).'], 'version_added': '2.3'}",
    "network": "{'description': ['Logical network to which the VM network interface should use, by default Empty network is used if network is not specified.']}",
    "poll_interval": "{'description': ['Number of the seconds the module waits until another poll request on entity status is sent.'], 'default': 3}",
    "profile": "{'description': ['Virtual network interface profile to be attached to VM network interface.']}",
    "state": "{'description': ['Should the Virtual Machine NIC be present/absent/plugged/unplugged.'], 'choices': ['absent', 'plugged', 'present', 'unplugged'], 'default': 'present'}",
    "template": "{'description': ['Name of the template to manage.', 'You must provide either C(vm) parameter or C(template) parameter.'], 'version_added': '2.4'}",
    "timeout": "{'description': ['The amount of time in seconds the module should wait for the instance to get into desired state.'], 'default': 180}",
    "vm": "{'description': ['Name of the Virtual Machine to manage.', 'You must provide either C(vm) parameter or C(template) parameter.']}",
    "wait": "{'description': ['I(True) if the module should wait for the entity to get into desired state.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

- name: Add NIC to VM
  ovirt_nic:
    state: present
    vm: myvm
    name: mynic
    interface: e1000
    mac_address: 00:1a:4a:16:01:56
    profile: ovirtmgmt
    network: ovirtmgmt

- name: Plug NIC to VM
  ovirt_nic:
    state: plugged
    vm: myvm
    name: mynic

- name: Unplug NIC from VM
  ovirt_nic:
    state: unplugged
    vm: myvm
    name: mynic

- name: Add NIC to template
  ovirt_nic:
    auth: "{{ ovirt_auth }}"
    state: present
    template: my_template
    name: nic1
    interface: virtio
    profile: ovirtmgmt
    network: ovirtmgmt

- name: Remove NIC from VM
  ovirt_nic:
    state: absent
    vm: myvm
    name: mynic

# Change NIC Name
- ovirt_nic:
    id: 00000000-0000-0000-0000-000000000000
    name: "new_nic_name"
    vm: myvm

```

## License

TODO

## Author Information
  - ['Ondra Machacek (@machacekondra)']
