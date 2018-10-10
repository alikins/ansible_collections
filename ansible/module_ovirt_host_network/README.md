# Ansible module: ansible.module_ovirt_host_network


Module to manage host networks in oVirt/RHV

## Description

Module to manage host networks in oVirt/RHV.

## Requirements

TODO

## Arguments

``` json
{
    "auth": "{'required': True, 'description': ['Dictionary with values needed to create HTTP/HTTPS connection to oVirt:', 'C(username)[I(required)] - The name of the user, something like I(admin@internal). Default value is set by I(OVIRT_USERNAME) environment variable.', 'C(password)[I(required)] - The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.', 'C(url) - A string containing the API URL of the server, usually something like `I(https://server.example.com/ovirt-engine/api)`. Default value is set by I(OVIRT_URL) environment variable. Either C(url) or C(hostname) is required.', 'C(hostname) - A string containing the hostname of the server, usually something like `I(server.example.com)`. Default value is set by I(OVIRT_HOSTNAME) environment variable. Either C(url) or C(hostname) is required.', 'C(token) - Token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.', 'C(insecure) - A boolean flag that indicates if the server TLS certificate and host name should be checked.', 'C(ca_file) - A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `C(ca_file)` parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.', 'C(kerberos) - A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.', 'C(headers) - Dictionary of HTTP headers to be added to each API call.']}",
    "bond": "{'description': ['Dictionary describing network bond:', 'C(name) - Bond name.', 'C(mode) - Bonding mode.', 'C(options) - Bonding options.', 'C(interfaces) - List of interfaces to create a bond.']}",
    "check": "{'description': ['If I(true) verify connectivity between host and engine.', 'Network configuration changes will be rolled back if connectivity between engine and the host is lost after changing network configuration.'], 'type': 'bool'}",
    "fetch_nested": "{'description': ['If I(True) the module will fetch additional data from the API.', 'It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying C(nested_attributes).'], 'version_added': '2.3', 'type': 'bool'}",
    "interface": "{'description': ['Name of the network interface where logical network should be attached.']}",
    "labels": "{'description': ['List of names of the network label to be assigned to bond or interface.']}",
    "name": "{'description': ['Name of the host to manage networks for.'], 'required': True, 'aliases': ['host']}",
    "nested_attributes": "{'description': ['Specifies list of the attributes which should be fetched from the API.', 'This parameter apply only when C(fetch_nested) is I(true).'], 'version_added': '2.3'}",
    "networks": "{'description': ['List of dictionary describing networks to be attached to interface or bond:', 'C(name) - Name of the logical network to be assigned to bond or interface.', 'C(boot_protocol) - Boot protocol one of the I(none), I(static) or I(dhcp).', 'C(address) - IP address in case of I(static) boot protocol is used.', 'C(netmask) - Subnet mask in case of I(static) boot protocol is used.', 'C(gateway) - Gateway in case of I(static) boot protocol is used.', 'C(version) - IP version. Either v4 or v6. Default is v4.']}",
    "poll_interval": "{'description': ['Number of the seconds the module waits until another poll request on entity status is sent.'], 'default': 3}",
    "save": "{'description': ['If I(true) network configuration will be persistent, by default they are temporarily.'], 'type': 'bool'}",
    "state": "{'description': ['Should the host be present/absent.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['The amount of time in seconds the module should wait for the instance to get into desired state.'], 'default': 180}",
    "wait": "{'description': ['I(True) if the module should wait for the entity to get into desired state.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Create bond on eth0 and eth1 interface, and put 'myvlan' network on top of it and persist the new configuration:
- name: Bonds
  ovirt_host_network:
    name: myhost
    save: yes
    bond:
      name: bond0
      mode: 2
      interfaces:
        - eth1
        - eth2
    networks:
      - name: myvlan
        boot_protocol: static
        address: 1.2.3.4
        netmask: 255.255.255.0
        gateway: 1.2.3.4
        version: v4

# Create bond on eth1 and eth2 interface, specifiyng both mode and miimon temporarily:
- name: Bonds
  ovirt_host_network:
    name: myhost
    bond:
      name: bond0
      mode: 1
      options:
        miimon: 200
      interfaces:
        - eth1
        - eth2

# Remove bond0 bond from host interfaces temporarily:
- ovirt_host_network:
    state: absent
    name: myhost
    bond:
      name: bond0

# Assign myvlan1 and myvlan2 vlans to host eth0 interface temporarily:
- ovirt_host_network:
    name: myhost
    interface: eth0
    networks:
      - name: myvlan1
      - name: myvlan2

# Remove myvlan2 vlan from host eth0 interface temporarily:
- ovirt_host_network:
    state: absent
    name: myhost
    interface: eth0
    networks:
      - name: myvlan2

# Remove all networks/vlans from host eth0 interface temporarily:
- ovirt_host_network:
    state: absent
    name: myhost
    interface: eth0

```

## License

TODO

## Author Information
  - ['Ondra Machacek (@machacekondra)']
