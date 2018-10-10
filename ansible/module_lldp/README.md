# Ansible module: ansible.module_lldp


get details reported by lldp

## Description

Reads data out of lldpctl

## Requirements

TODO

## Arguments

}
```

## Examples


``` yaml

# Retrieve switch/port information
 - name: Gather information from lldp
   lldp:

 - name: Print each switch/port
   debug:
    msg: "{{ lldp[item]['chassis']['name'] }} / {{ lldp[item]['port']['ifname'] }}"
   with_items: "{{ lldp.keys() }}"

# TASK: [Print each switch/port] ***********************************************************
# ok: [10.13.0.22] => (item=eth2) => {"item": "eth2", "msg": "switch1.example.com / Gi0/24"}
# ok: [10.13.0.22] => (item=eth1) => {"item": "eth1", "msg": "switch2.example.com / Gi0/3"}
# ok: [10.13.0.22] => (item=eth0) => {"item": "eth0", "msg": "switch3.example.com / Gi0/3"}


```

## License

TODO

## Author Information
  - ['Andy Hill (@andyhky)']
