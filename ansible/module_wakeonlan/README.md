# Ansible module: ansible.module_wakeonlan


Send a magic Wake-on-LAN (WoL) broadcast packet

## Description

The C(wakeonlan) module sends magic Wake-on-LAN (WoL) broadcast packets.

## Requirements

TODO

## Arguments

``` json
{
    "broadcast": "{'description': ['Network broadcast address to use for broadcasting magic Wake-on-LAN packet.'], 'default': '255.255.255.255'}",
    "mac": "{'description': ['MAC address to send Wake-on-LAN broadcast packet for.'], 'required': True}",
    "port": "{'description': ['UDP port to use for magic Wake-on-LAN packet.'], 'default': 7}",
}
```

## Examples


``` yaml

- name: Send a magic Wake-on-LAN packet to 00:00:5E:00:53:66
  wakeonlan:
    mac: '00:00:5E:00:53:66'
    broadcast: 192.0.2.23
  delegate_to: localhost

- wakeonlan:
    mac: 00:00:5E:00:53:66
    port: 9
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)']
