# Ansible module: ansible.module_ce_bgp_neighbor_af


Manages BGP neighbor Address-family configuration on HUAWEI CloudEngine switches

## Description

Manages BGP neighbor Address-family configurations on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "add_path_mode": "{'description': ['null, Null. receive, Support receiving Add-Path routes. send, Support sending Add-Path routes. both, Support receiving and sending Add-Path routes.'], 'choices': ['null', 'receive', 'send', 'both']}",
    "adv_add_path_num": "{'description': ['The number of addPath advertise route. The value is an integer ranging from 2 to 64.']}",
    "advertise_arp": "{'description': ['If the value is true, advertised ARP routes are distinguished. If the value is false, advertised ARP routes are not distinguished.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "advertise_community": "{'description': ['If the value is true, the community attribute is advertised to peers. If the value is false, the community attribute is not advertised to peers.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "advertise_ext_community": "{'description': ['If the value is true, the extended community attribute is advertised to peers. If the value is false, the extended community attribute is not advertised to peers.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "advertise_irb": "{'description': ['If the value is true, advertised IRB routes are distinguished. If the value is false, advertised IRB routes are not distinguished.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "advertise_remote_nexthop": "{'description': ['If the value is true, the remote next-hop attribute is advertised to peers. If the value is false, the remote next-hop attribute is not advertised to any peers.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "af_type": "{'description': ['Address family type of a BGP instance.'], 'required': True, 'choices': ['ipv4uni', 'ipv4multi', 'ipv4vpn', 'ipv6uni', 'ipv6vpn', 'evpn']}",
    "allow_as_loop_enable": "{'description': ['If the value is true, repetitive local AS numbers are allowed. If the value is false, repetitive local AS numbers are not allowed.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "allow_as_loop_limit": "{'description': ['Set the maximum number of repetitive local AS number. The value is an integer ranging from 1 to 10.']}",
    "default_rt_adv_enable": "{'description': ['If the value is true, the function to advertise default routes to peers is enabled. If the value is false, the function to advertise default routes to peers is disabled.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "default_rt_adv_policy": "{'description': ['Specify the name of a used policy. The value is a string. The value is a string of 1 to 40 characters.']}",
    "default_rt_match_mode": "{'description': ['null, Null. matchall, Advertise the default route if all matching conditions are met. matchany, Advertise the default route if any matching condition is met.'], 'choices': ['null', 'matchall', 'matchany']}",
    "discard_ext_community": "{'description': ['If the value is true, the extended community attribute in the peer route information is discarded. If the value is false, the extended community attribute in the peer route information is not discarded.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "export_acl_name_or_num": "{'description': ['Apply an IPv4 ACL-based filtering policy to the routes to be advertised to a specified peer. The value is a string of 1 to 32 characters.']}",
    "export_as_path_filter": "{'description': ['Apply an AS_Path-based filtering policy to the routes to be advertised to a specified peer. The value is an integer ranging from 1 to 256.']}",
    "export_as_path_name_or_num": "{'description': ['Application of a AS path list based filtering policy to the routing of a specified peer.']}",
    "export_pref_filt_name": "{'description': ['Specify the IPv4 filtering policy applied to the routes to be advertised to a specified peer. The value is a string of 1 to 169 characters.']}",
    "export_rt_policy_name": "{'description': ['Specify the filtering policy applied to the routes to be advertised to a peer. The value is a string of 1 to 40 characters.']}",
    "import_acl_name_or_num": "{'description': ['Apply an IPv4 ACL-based filtering policy to the routes received from a specified peer. The value is a string of 1 to 32 characters.']}",
    "import_as_path_filter": "{'description': ['Apply an AS_Path-based filtering policy to the routes received from a specified peer. The value is an integer ranging from 1 to 256.']}",
    "import_as_path_name_or_num": "{'description': ['A routing strategy based on the AS path list for routing received by a designated peer.']}",
    "import_pref_filt_name": "{'description': ['Specify the IPv4 filtering policy applied to the routes received from a specified peer. The value is a string of 1 to 169 characters.']}",
    "import_rt_policy_name": "{'description': ['Specify the filtering policy applied to the routes learned from a peer. The value is a string of 1 to 40 characters.']}",
    "ipprefix_orf_enable": "{'description': ['If the value is true, the address prefix-based Outbound Route Filter (ORF) capability is enabled for peers. If the value is false, the address prefix-based Outbound Route Filter (ORF) capability is disabled for peers.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "is_nonstd_ipprefix_mod": "{'description': ['If the value is true, Non-standard capability codes are used during capability negotiation. If the value is false, RFC-defined standard ORF capability codes are used during capability negotiation.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "keep_all_routes": "{'description': ['If the value is true, the system stores all route update messages received from all peers (groups) after BGP connection setup. If the value is false, the system stores only BGP update messages that are received from peers and pass the configured import policy.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "nexthop_configure": "{'description': ['null, The next hop is not changed. local, The next hop is changed to the local IP address. invariable, Prevent the device from changing the next hop of each imported IGP route when advertising it to its BGP peers.'], 'choices': ['null', 'local', 'invariable']}",
    "orf_mode": "{'description': ['ORF mode. null, Default value. receive, ORF for incoming packets. send, ORF for outgoing packets. both, ORF for incoming and outgoing packets.'], 'choices': ['null', 'receive', 'send', 'both']}",
    "orftype": "{'description': ['ORF Type. The value is an integer ranging from 0 to 65535.']}",
    "origin_as_valid": "{'description': ['If the value is true, Application results of route announcement. If the value is false, Routing application results are not notified.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "preferred_value": "{'description': ['Assign a preferred value for the routes learned from a specified peer. The value is an integer ranging from 0 to 65535.']}",
    "public_as_only": "{'description': ['If the value is true, sent BGP update messages carry only the public AS number but do not carry private AS numbers. If the value is false, sent BGP update messages can carry private AS numbers.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "public_as_only_force": "{'description': ['If the value is true, sent BGP update messages carry only the public AS number but do not carry private AS numbers. If the value is false, sent BGP update messages can carry private AS numbers.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "public_as_only_limited": "{'description': ['Limited use public as number.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "public_as_only_replace": "{'description': ['Private as replaced by public as number.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "public_as_only_skip_peer_as": "{'description': ['Public as only skip peer as.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "redirect_ip": "{'description': ['Redirect ip.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "redirect_ip_vaildation": "{'description': ['Redirect ip vaildation.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "reflect_client": "{'description': ['If the value is true, the local device functions as the route reflector and a peer functions as a client of the route reflector. If the value is false, the route reflector and client functions are not configured.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "remote_address": "{'description': ['IPv4 or IPv6 peer connection address.'], 'required': True}",
    "route_limit": "{'description': ['Configure the maximum number of routes that can be accepted from a peer. The value is an integer ranging from 1 to 4294967295.']}",
    "route_limit_idle_timeout": "{'description': ['Specify the value of the idle-timeout timer to automatically reestablish the connections after they are cut off when the number of routes exceeds the set threshold. The value is an integer ranging from 1 to 1200.']}",
    "route_limit_percent": "{'description': ['Specify the percentage of routes when a router starts to generate an alarm. The value is an integer ranging from 1 to 100.']}",
    "route_limit_type": "{'description': ['Noparameter, After the number of received routes exceeds the threshold and the timeout timer expires,no action. AlertOnly, An alarm is generated and no additional routes will be accepted if the maximum number of routes allowed have been received. IdleForever, The connection that is interrupted is not automatically re-established if the maximum number of routes allowed have been received. IdleTimeout, After the number of received routes exceeds the threshold and the timeout timer expires, the connection that is interrupted is automatically re-established.'], 'choices': ['noparameter', 'alertOnly', 'idleForever', 'idleTimeout']}",
    "rt_updt_interval": "{'description': ['Specify the minimum interval at which Update packets are sent. The value is an integer, in seconds. The value is an integer ranging from 0 to 600.']}",
    "soostring": "{'description': ['Configure the Site-of-Origin (SoO) extended community attribute. The value is a string of 3 to 21 characters.']}",
    "substitute_as_enable": "{'description': ["If the value is true, the function to replace a specified peer's AS number in the AS-Path attribute with the local AS number is enabled. If the value is false, the function to replace a specified peer's AS number in the AS-Path attribute with the local AS number is disabled."], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "update_pkt_standard_compatible": "{'description': ['If the value is true, When the vpnv4 multicast neighbor receives and updates the message, the message has no label. If the value is false, When the vpnv4 multicast neighbor receives and updates the message, the message has label.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "vpls_ad_disable": "{'description': ['If the value is true, enable vpls-ad. If the value is false, disable vpls-ad.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "vpls_enable": "{'description': ['If the value is true, vpls enable. If the value is false, vpls disable.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "vrf_name": "{'description': ['Name of a BGP instance. The name is a case-sensitive string of characters. The BGP instance can be used only after the corresponding VPN instance is created.'], 'required': True}",
}
```

## Examples


``` yaml


- name: CloudEngine BGP neighbor address family test
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

  - name: "Config BGP peer Address_Family"
    ce_bgp_neighbor_af:
      state: present
      vrf_name: js
      af_type: ipv4uni
      remote_address: 192.168.10.10
      nexthop_configure: local
      provider: "{{ cli }}"

  - name: "Undo BGP peer Address_Family"
    ce_bgp_neighbor_af:
      state: absent
      vrf_name: js
      af_type: ipv4uni
      remote_address: 192.168.10.10
      nexthop_configure: local
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['wangdezhuang (@CloudEngine-Ansible)']
