# Ansible module: ansible.module_na_elementsw_network_interfaces


NetApp Element Software Configure Node Network Interfaces

## Description

Configure Element SW Node Network Interfaces for Bond 1G and 10G IP address.

## Requirements

TODO

## Arguments

``` json
{
    "bond_mode_10g": "{'description': ['Bond mode for 10GbE configuration.'], 'choices': ['ActivePassive', 'ALB', 'LACP'], 'default': 'ActivePassive'}",
    "bond_mode_1g": "{'description': ['Bond mode for 1GbE configuration.'], 'choices': ['ActivePassive', 'ALB', 'LACP'], 'default': 'ActivePassive'}",
    "dns_nameservers": "{'description': ['List of addresses for domain name servers.']}",
    "dns_search_domains": "{'description': ['List of DNS search domains.']}",
    "gateway_address_10g": "{'description': ['Router network address to send packets out of the local network.'], 'required': True}",
    "gateway_address_1g": "{'description': ['Router network address to send packets out of the local network.'], 'required': True}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the SolidFire cluster.']}",
    "ip_address_10g": "{'description': ['IP address for the 10G network.'], 'required': True}",
    "ip_address_1g": "{'description': ['IP address for the 1G network.'], 'required': True}",
    "lacp_10g": "{'description': ['Link Aggregation Control Protocol useful only if LACP is selected as the Bond Mode.', 'Slow - Packets are transmitted at 30 second intervals.', 'Fast - Packets are transmitted in 1 second intervals.'], 'choices': ['Fast', 'Slow'], 'default': 'Slow'}",
    "lacp_1g": "{'description': ['Link Aggregation Control Protocol useful only if LACP is selected as the Bond Mode.', 'Slow - Packets are transmitted at 30 second intervals.', 'Fast - Packets are transmitted in 1 second intervals.'], 'choices': ['Fast', 'Slow'], 'default': 'Slow'}",
    "method": "{'description': ['Type of Method used to configure the interface.', 'method depends on other settings such as the use of a static IP address, which will change the method to static.', 'loopback - Used to define the IPv4 loopback interface.', 'manual - Used to define interfaces for which no configuration is done by default.', 'dhcp - May be used to obtain an IP address via DHCP.', 'static - Used to define Ethernet interfaces with statically allocated IPv4 addresses.'], 'choices': ['loopback', 'manual', 'dhcp', 'static'], 'required': True}",
    "mtu_10g": "{'description': ['Maximum Transmission Unit for 10GbE, Largest packet size that a network protocol can transmit.', 'Must be greater than or equal to 1500 bytes.'], 'default': '1500'}",
    "mtu_1g": "{'description': ['Maximum Transmission Unit for 1GbE, Largest packet size that a network protocol can transmit.', 'Must be greater than or equal to 1500 bytes.'], 'default': '1500'}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "subnet_10g": "{'description': ['10GbE Subnet Mask.'], 'required': True}",
    "subnet_1g": "{'description': ['1GbE Subnet Mask.'], 'required': True}",
    "username": "{'required': True, 'description': ['Please ensure that the user has the adequate permissions. For more information, please read the official documentation U(https://mysupport.netapp.com/documentation/docweb/index.html?productID=62636&language=en-US).'], 'aliases': ['user']}",
    "virtual_network_tag": "{'description': ['This is the primary network tag. All nodes in a cluster have the same VLAN tag.']}",
}
```

## Examples


``` yaml


  - name: Set Node network interfaces configuration for Bond 1G and 10G properties
    tags:
    - elementsw_network_interfaces
    na_elementsw_network_interfaces:
      hostname: "{{ elementsw_hostname }}"
      username: "{{ elementsw_username }}"
      password: "{{ elementsw_password }}"
      method: static
      ip_address_1g: 10.226.109.68
      ip_address_10g: 10.226.201.72
      subnet_1g: 255.255.255.0
      subnet_10g: 255.255.255.0
      gateway_address_1g: 10.193.139.1
      gateway_address_10g: 10.193.140.1
      mtu_1g: 1500
      mtu_10g: 9000
      bond_mode_1g: ActivePassive
      bond_mode_10g: LACP
      lacp_10g: Fast

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
