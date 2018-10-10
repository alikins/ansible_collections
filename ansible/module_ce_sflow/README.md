# Ansible module: ansible.module_ce_sflow


Manages sFlow configuration on HUAWEI CloudEngine switches

## Description

Configure Sampled Flow (sFlow) to monitor traffic on an interface in real time, detect abnormal traffic, and locate the source of attack traffic, ensuring stable running of the network.

## Requirements

TODO

## Arguments

``` json
{
    "agent_ip": "{'description': ['Specifies the IPv4/IPv6 address of an sFlow agent.']}",
    "collector_datagram_size": "{'description': ['Specifies the maximum length of sFlow packets sent from an sFlow agent to an sFlow collector. The value is an integer, in bytes. It ranges from 1024 to 8100. The default value is 1400.']}",
    "collector_description": "{'description': ['Specifies the description of an sFlow collector. The value is a string of 1 to 255 case-sensitive characters without spaces.']}",
    "collector_id": "{'description': ['Specifies the ID of an sFlow collector. This ID is used when you specify the collector in subsequent sFlow configuration.'], 'choices': ['1', '2']}",
    "collector_ip": "{'description': ['Specifies the IPv4/IPv6 address of the sFlow collector.']}",
    "collector_ip_vpn": "{'description': ['Specifies the name of a VPN instance. The value is a string of 1 to 31 case-sensitive characters, spaces not supported. When double quotation marks are used around the string, spaces are allowed in the string. The value C(_public_) is reserved and cannot be used as the VPN instance name.']}",
    "collector_meth": "{'description': ['Configures the device to send sFlow packets through service interfaces, enhancing the sFlow packet forwarding capability. The enhanced parameter is optional. No matter whether you configure the enhanced mode, the switch determines to send sFlow packets through service cards or management port based on the routing information on the collector. When the value is meth, the device forwards sFlow packets at the control plane. When the value is enhanced, the device forwards sFlow packets at the forwarding plane to enhance the sFlow packet forwarding capacity.'], 'choices': ['meth', 'enhanced']}",
    "collector_udp_port": "{'description': ['Specifies the UDP destination port number of sFlow packets. The value is an integer that ranges from 1 to 65535. The default value is 6343.']}",
    "counter_collector": "{'description': ['Indicates the ID list of the counter collector.']}",
    "counter_interval": "{'description': ['Indicates the counter sampling interval. The value is an integer that ranges from 10 to 4294967295, in seconds. The default value is 20.']}",
    "export_route": "{'description': ['Configures the sFlow packets sent by the switch not to carry routing information.'], 'choices': ['enable', 'disable']}",
    "forward_enp_slot": "{'description': ["Enable the Embedded Network Processor (ENP) chip function. The switch uses the ENP chip to perform sFlow sampling, and the maximum sFlow sampling interval is 65535. If you set the sampling interval to be larger than 65535, the switch automatically restores it to 65535. The value is an integer or 'all'."]}",
    "rate_limit": "{'description': ['Specifies the rate of sFlow packets sent from a card to the control plane. The value is an integer that ranges from 100 to 1500, in pps.']}",
    "rate_limit_slot": "{'description': ['Specifies the slot where the rate of output sFlow packets is limited. If this parameter is not specified, the rate of sFlow packets sent from all cards to the control plane is limited. The value is an integer or a string of characters.']}",
    "sample_collector": "{'description': ['Indicates the ID list of the collector.']}",
    "sample_direction": "{'description': ['Enables flow sampling in the inbound or outbound direction.'], 'choices': ['inbound', 'outbound', 'both']}",
    "sample_length": "{'description': ['Specifies the maximum length of sampled packets. The value is an integer and ranges from 18 to 512, in bytes. The default value is 128.']}",
    "sample_rate": "{'description': ['Specifies the flow sampling rate in the format 1/rate. The value is an integer and ranges from 1 to 4294967295. The default value is 8192.']}",
    "sflow_interface": "{'description': ['Full name of interface for Flow Sampling or Counter. It must be a physical interface, Eth-Trunk, or Layer 2 subinterface.']}",
    "source_ip": "{'description': ['Specifies the source IPv4/IPv6 address of sFlow packets.']}",
    "state": "{'description': ['Determines whether the config should be present or not on the device.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

---

- name: sflow module test
  hosts: ce128
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
  - name: Configuring sFlow Agent
    ce_sflow:
      agent_ip: 6.6.6.6
      provider: '{{ cli }}'

  - name: Configuring sFlow Collector
    ce_sflow:
      collector_id: 1
      collector_ip: 7.7.7.7
      collector_ip_vpn: vpn1
      collector_description: Collector1
      provider: '{{ cli }}'

  - name: Configure flow sampling.
    ce_sflow:
      sflow_interface: 10GE2/0/2
      sample_collector: 1
      sample_direction: inbound
      provider: '{{ cli }}'

  - name: Configure counter sampling.
    ce_sflow:
      sflow_interface: 10GE2/0/2
      counter_collector: 1
      counter_interval: 1000
      provider: '{{ cli }}'

```

## License

TODO

## Author Information
  - ['QijunPan (@CloudEngine-Ansible)']
