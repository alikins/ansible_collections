# Ansible module: ansible.module_ce_ospf_vrf


Manages configuration of an OSPF VPN instance on HUAWEI CloudEngine switches

## Description

Manages configuration of an OSPF VPN instance on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "bandwidth": "{'description': ['Specifies the reference bandwidth used to assign ospf cost. Valid values are an integer, in Mbps, 1 - 2147483648, the default value is 100.']}",
    "description": "{'description': ['Specifies the description information of ospf process.']}",
    "lsaaholdinterval": "{'description': ['Specifies the hold interval of arrive LSA when use the intelligent timer. Valid value is an integer, in millisecond, from 0 to 10000, the default value is 500.']}",
    "lsaainterval": "{'description': ['Specifies the interval of arrive LSA when use the general timer. Valid value is an integer, in millisecond, from 0 to 10000.']}",
    "lsaalflag": "{'description': ['Specifies the mode of timer to calculate interval of arrive LSA. If set the parameter but not specifies value, the default will be used. If true use general timer. If false use intelligent timer.'], 'type': 'bool', 'default': False}",
    "lsaamaxinterval": "{'description': ['Specifies the max interval of arrive LSA when use the intelligent timer. Valid value is an integer, in millisecond, from 0 to 10000, the default value is 1000.']}",
    "lsaastartinterval": "{'description': ['Specifies the start interval of arrive LSA when use the intelligent timer. Valid value is an integer, in millisecond, from 0 to 10000, the default value is 500.']}",
    "lsaoholdinterval": "{'description': ['Specifies the hold interval of originate LSA . Valid value is an integer, in millisecond, from 0 to 5000, the default value is 1000.']}",
    "lsaointerval": "{'description': ['Specifies the interval of originate LSA . Valid value is an integer, in second, from 0 to 10, the default value is 5.']}",
    "lsaointervalflag": "{'description': ['Specifies whether cancel the interval of LSA originate or not. If set the parameter but noe specifies value, the default will be used. true:cancel the interval of LSA originate, the interval is 0. false:do not cancel the interval of LSA originate.'], 'type': 'bool', 'default': False}",
    "lsaomaxinterval": "{'description': ['Specifies the max interval of originate LSA . Valid value is an integer, in millisecond, from 1 to 10000, the default value is 5000.']}",
    "lsaostartinterval": "{'description': ['Specifies the start interval of originate LSA . Valid value is an integer, in millisecond, from 0 to 1000, the default value is 500.']}",
    "ospf": "{'description': ['The ID of the ospf process. Valid values are an integer, 1 - 4294967295, the default value is 1.'], 'required': True}",
    "route_id": "{'description': ['Specifies the ospf private route id,. Valid values are a string, formatted as an IP address (i.e. "10.1.1.1") the length is 0 - 20.']}",
    "spfholdinterval": "{'description': ['Specifies the hold interval to calculate SPF when use intelligent timer. Valid value is an integer, in millisecond, from 1 to 5000, the default value is 200.']}",
    "spfinterval": "{'description': ['Specifies the interval to calculate SPF when use second level  timer. Valid value is an integer, in second, from 1 to 10.']}",
    "spfintervalmi": "{'description': ['Specifies the interval to calculate SPF when use millisecond level  timer. Valid value is an integer, in millisecond, from 1 to 10000.']}",
    "spfintervaltype": "{'description': ['Specifies the mode of timer which used to calculate SPF. If set the parameter but noe specifies value, the default will be used. If is intelligent-timer, then use intelligent timer. If is timer, then use second level timer. If is millisecond, then use millisecond level timer.'], 'choices': ['intelligent-timer', 'timer', 'millisecond'], 'default': 'intelligent-timer'}",
    "spfmaxinterval": "{'description': ['Specifies the max interval to calculate SPF when use intelligent timer. Valid value is an integer, in millisecond, from 1 to 20000, the default value is 5000.']}",
    "spfstartinterval": "{'description': ['Specifies the start interval to calculate SPF when use intelligent timer. Valid value is an integer, in millisecond, from 1 to 1000, the default value is 50.']}",
    "state": "{'description': ['Specify desired state of the resource.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "vrf": "{'description': ['Specifies the vpn instance which use ospf,length is 1 - 31. Valid values are a string.'], 'default': '_public_'}",
}
```

## Examples


``` yaml

- name: ospf vrf module test
  hosts: cloudengine
  connection: local
  gather_facts: no
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:

  - name: Configure ospf route id
    ce_ospf_vrf:
      ospf: 2
      route_id: 2.2.2.2
      lsaointervalflag: False
      lsaointerval: 2
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['Yang yang (@CloudEngine Ansible)']
