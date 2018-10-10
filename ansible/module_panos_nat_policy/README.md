# Ansible module: ansible.module_panos_nat_policy


create a policy NAT rule

## Description

Create a policy nat rule. Keep in mind that we can either end up configuring source NAT, destination NAT, or both. Instead of splitting it into two we will make a fair attempt to determine which one the user wants.

## Requirements

TODO

## Arguments

``` json
{
    "commit": "{'description': ['commit if changed'], 'type': 'bool', 'default': True}",
    "destination": "{'description': ['list of destination addresses'], 'default': ['any']}",
    "dnat_address": "{'description': ['dnat translated address']}",
    "dnat_port": "{'description': ['dnat translated port']}",
    "from_zone": "{'description': ['list of source zones'], 'required': True}",
    "ip_address": "{'description': ['IP address (or hostname) of PAN-OS device'], 'required': True}",
    "override": "{'description': ['attempt to override rule if one with the same name already exists'], 'type': 'bool', 'default': False}",
    "password": "{'description': ['password for authentication'], 'required': True}",
    "rule_name": "{'description': ['name of the SNAT rule'], 'required': True}",
    "service": "{'description': ['service'], 'default': 'any'}",
    "snat_address": "{'description': ['snat translated address']}",
    "snat_bidirectional": "{'description': ['bidirectional flag'], 'type': 'bool', 'default': False}",
    "snat_interface": "{'description': ['snat interface']}",
    "snat_interface_address": "{'description': ['snat interface address']}",
    "snat_type": "{'description': ['type of source translation']}",
    "source": "{'description': ['list of source addresses'], 'default': ['any']}",
    "to_zone": "{'description': ['destination zone'], 'required': True}",
    "username": "{'description': ['username for authentication'], 'default': 'admin'}",
}
```

## Examples


``` yaml

# Create a source and destination nat rule
  - name: create nat SSH221 rule for 10.0.1.101
    panos_nat:
      ip_address: "192.168.1.1"
      password: "admin"
      rule_name: "Web SSH"
      from_zone: ["external"]
      to_zone: "external"
      source: ["any"]
      destination: ["10.0.0.100"]
      service: "service-tcp-221"
      snat_type: "dynamic-ip-and-port"
      snat_interface: "ethernet1/2"
      dnat_address: "10.0.1.101"
      dnat_port: "22"
      commit: False

```

## License

TODO

## Author Information
  - ['Luigi Mori (@jtschichold), Ivan Bojer (@ivanbojer)']
