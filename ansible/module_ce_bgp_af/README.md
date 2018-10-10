# Ansible module: ansible.module_ce_bgp_af


Manages BGP Address-family configuration on HUAWEI CloudEngine switches

## Description

Manages BGP Address-family configurations on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "active_route_advertise": "{'description': ['If the value is true, BGP is enabled to advertise only optimal routes in the RM to peers. If the value is false, BGP is not enabled to advertise only optimal routes in the RM to peers.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "add_path_sel_num": "{'description': ['Number of Add-Path routes. The value is an integer ranging from 2 to 64.']}",
    "af_type": "{'description': ['Address family type of a BGP instance.'], 'required': True, 'choices': ['ipv4uni', 'ipv4multi', 'ipv4vpn', 'ipv6uni', 'ipv6vpn', 'evpn']}",
    "allow_invalid_as": "{'description': ['Allow routes with BGP origin AS validation result Invalid to be selected. If the value is true, invalid routes can participate in route selection. If the value is false, invalid routes cannot participate in route selection.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "always_compare_med": "{'description': ['If the value is true, the MEDs of routes learned from peers in different autonomous systems are compared when BGP selects an optimal route. If the value is false, the MEDs of routes learned from peers in different autonomous systems are not compared when BGP selects an optimal route.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "as_path_neglect": "{'description': ['If the value is true, the AS path attribute is ignored when BGP selects an optimal route. If the value is false, the AS path attribute is not ignored when BGP selects an optimal route. An AS path with a smaller length has a higher priority.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "auto_frr_enable": "{'description': ['If the value is true, BGP auto FRR is enabled. If the value is false, BGP auto FRR is disabled.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "default_local_pref": "{'description': ['Set the Local-Preference attribute. The value is an integer. The value is an integer ranging from 0 to 4294967295.']}",
    "default_med": "{'description': ['Specify the Multi-Exit-Discriminator (MED) of BGP routes. The value is an integer ranging from 0 to 4294967295.']}",
    "default_rt_import_enable": "{'description': ['If the value is true, importing default routes to the BGP routing table is allowed. If the value is false, importing default routes to the BGP routing table is not allowed.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "determin_med": "{'description': ['If the value is true, BGP deterministic-MED is enabled. If the value is false, BGP deterministic-MED is disabled.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "ebgp_ecmp_nexthop_changed": "{'description': ['If the value is true, the next hop of an advertised route is changed to the advertiser itself in EBGP load-balancing scenarios. If the value is false, the next hop of an advertised route is not changed to the advertiser itself in EBGP load-balancing scenarios.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "ebgp_if_sensitive": "{'description': ['If the value is true, after the fast EBGP interface awareness function is enabled, EBGP sessions on an interface are deleted immediately when the interface goes Down. If the value is false, after the fast EBGP interface awareness function is enabled, EBGP sessions on an interface are not deleted immediately when the interface goes Down.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "ecmp_nexthop_changed": "{'description': ['If the value is true, the next hop of an advertised route is changed to the advertiser itself in BGP load-balancing scenarios. If the value is false, the next hop of an advertised route is not changed to the advertiser itself in BGP load-balancing scenarios.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "ibgp_ecmp_nexthop_changed": "{'description': ['If the value is true, the next hop of an advertised route is changed to the advertiser itself in IBGP load-balancing scenarios. If the value is false, the next hop of an advertised route is not changed to the advertiser itself in IBGP load-balancing scenarios.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "igp_metric_ignore": "{'description': ['If the value is true, the metrics of next-hop IGP routes are not compared when BGP selects an optimal route. If the value is false, the metrics of next-hop IGP routes are not compared when BGP selects an optimal route. A route with a smaller metric has a higher priority.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "import_process_id": "{'description': ['Process ID of an imported routing protocol. The value is an integer ranging from 0 to 4294967295.']}",
    "import_protocol": "{'description': ['Routing protocol from which routes can be imported.'], 'choices': ['direct', 'ospf', 'isis', 'static', 'rip', 'ospfv3', 'ripng']}",
    "ingress_lsp_policy_name": "{'description': ['Ingress lsp policy name.']}",
    "load_balancing_as_path_ignore": "{'description': ['Load balancing as path ignore.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "lowest_priority": "{'description': ['If the value is true, enable reduce priority to advertise route. If the value is false, disable reduce priority to advertise route.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "mask_len": "{'description': ['Specify the mask length of an IP address. The value is an integer ranging from 0 to 128.']}",
    "max_load_ebgp_num": "{'description': ['Specify the maximum number of equal-cost EBGP routes. The value is an integer ranging from 1 to 65535.']}",
    "max_load_ibgp_num": "{'description': ['Specify the maximum number of equal-cost IBGP routes. The value is an integer ranging from 1 to 65535.']}",
    "maximum_load_balance": "{'description': ['Specify the maximum number of equal-cost routes in the BGP routing table. The value is an integer ranging from 1 to 65535.']}",
    "med_none_as_maximum": "{'description': ["If the value is true, when BGP selects an optimal route, the system uses 4294967295 as the MED value of a route if the route's attribute does not carry a MED value. If the value is false, the system uses 0 as the MED value of a route if the route's attribute does not carry a MED value."], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "network_address": "{'description': ['Specify the IP address advertised by BGP. The value is a string of 0 to 255 characters.']}",
    "next_hop_sel_depend_type": "{'description': ['Next hop select depend type.'], 'choices': ['default', 'dependTunnel', 'dependIp'], 'default': 'default'}",
    "nexthop_third_party": "{'description': ['If the value is true, the third-party next hop function is enabled. If the value is false, the third-party next hop function is disabled.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "nhp_relay_route_policy_name": "{'description': ['Specify the name of a route-policy for route iteration. The value is a string of 1 to 40 characters.']}",
    "originator_prior": "{'description': ['Originator prior.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "policy_ext_comm_enable": "{'description': ['If the value is true, modifying extended community attributes is allowed. If the value is false, modifying extended community attributes is not allowed.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "policy_vpn_target": "{'description': ['If the value is true, VPN-Target filtering function is performed for received VPN routes. If the value is false, VPN-Target filtering function is not performed for received VPN routes.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "preference_external": "{'description': ['Set the protocol priority of EBGP routes. The value is an integer ranging from 1 to 255.']}",
    "preference_internal": "{'description': ['Set the protocol priority of IBGP routes. The value is an integer ranging from 1 to 255.']}",
    "preference_local": "{'description': ['Set the protocol priority of a local BGP route. The value is an integer ranging from 1 to 255.']}",
    "prefrence_policy_name": "{'description': ['Set a routing policy to filter routes so that a configured priority is applied to the routes that match the specified policy. The value is a string of 1 to 40 characters.']}",
    "reflect_between_client": "{'description': ['If the value is true, route reflection is enabled between clients. If the value is false, route reflection is disabled between clients.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "reflect_chg_path": "{'description': ['If the value is true, the route reflector is enabled to modify route path attributes based on an export policy. If the value is false, the route reflector is disabled from modifying route path attributes based on an export policy.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "reflector_cluster_id": "{'description': ['Set a cluster ID. Configuring multiple RRs in a cluster can enhance the stability of the network. The value is an integer ranging from 1 to 4294967295.']}",
    "reflector_cluster_ipv4": "{'description': ['Set a cluster ipv4 address. The value is expressed in the format of an IPv4 address.']}",
    "relay_delay_enable": "{'description': ['If the value is true, relay delay enable. If the value is false, relay delay disable.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "rib_only_enable": "{'description': ['If the value is true, BGP routes cannot be advertised to the IP routing table. If the value is false, Routes preferred by BGP are advertised to the IP routing table.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "rib_only_policy_name": "{'description': ['Specify the name of a routing policy. The value is a string of 1 to 40 characters.']}",
    "route_sel_delay": "{'description': ['Route selection delay. The value is an integer ranging from 0 to 3600.']}",
    "router_id": "{'description': ['ID of a router that is in IPv4 address format. The value is a string of 0 to 255 characters. The value is in dotted decimal notation.']}",
    "router_id_neglect": "{'description': ['If the value is true, the router ID attribute is ignored when BGP selects the optimal route. If the value is false, the router ID attribute is not ignored when BGP selects the optimal route.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "rr_filter_number": "{'description': ['Set the number of the extended community filter supported by an RR group. The value is a string of 1 to 51 characters.']}",
    "state": "{'description': ['Specify desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "summary_automatic": "{'description': ['If the value is true, automatic aggregation is enabled for locally imported routes. If the value is false, automatic aggregation is disabled for locally imported routes.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "supernet_label_adv": "{'description': ['If the value is true, the function to advertise supernetwork label is enabled. If the value is false, the function to advertise supernetwork label is disabled.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "supernet_uni_adv": "{'description': ['If the value is true, the function to advertise supernetwork unicast routes is enabled. If the value is false, the function to advertise supernetwork unicast routes is disabled.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
    "vrf_name": "{'description': ['Name of a BGP instance. The name is a case-sensitive string of characters. The BGP instance can be used only after the corresponding VPN instance is created. The value is a string of 1 to 31 case-sensitive characters.'], 'required': True}",
    "vrf_rid_auto_sel": "{'description': ['If the value is true, VPN BGP instances are enabled to automatically select router IDs. If the value is false, VPN BGP instances are disabled from automatically selecting router IDs.'], 'choices': ['no_use', 'true', 'false'], 'default': 'no_use'}",
}
```

## Examples


``` yaml


- name: CloudEngine BGP address family test
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

  - name: "Config BGP Address_Family"
    ce_bgp_af:
      state: present
      vrf_name: js
      af_type: ipv4uni
      provider: "{{ cli }}"

  - name: "Undo BGP Address_Family"
    ce_bgp_af:
      state: absent
      vrf_name: js
      af_type: ipv4uni
      provider: "{{ cli }}"

  - name: "Config import route"
    ce_bgp_af:
      state: present
      vrf_name: js
      af_type: ipv4uni
      import_protocol: ospf
      import_process_id: 123
      provider: "{{ cli }}"

  - name: "Undo import route"
    ce_bgp_af:
      state: absent
      vrf_name: js
      af_type: ipv4uni
      import_protocol: ospf
      import_process_id: 123
      provider: "{{ cli }}"

  - name: "Config network route"
    ce_bgp_af:
      state: present
      vrf_name: js
      af_type: ipv4uni
      network_address: 1.1.1.1
      mask_len: 24
      provider: "{{ cli }}"

  - name: "Undo network route"
    ce_bgp_af:
      state: absent
      vrf_name: js
      af_type: ipv4uni
      network_address: 1.1.1.1
      mask_len: 24
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['wangdezhuang (@CloudEngine-Ansible)']
