# Ansible module: ansible.module_ce_bgp


Manages BGP configuration on HUAWEI CloudEngine switches

## Description

Manages BGP configurations on HUAWEI CloudEngine switches.

## Requirements

TODO

## Arguments

``` json
{
    "as_number": "{'description': ['Local AS number. The value is a string of 1 to 11 characters.']}",
    "as_path_limit": "{'description': ['Maximum number of AS numbers in the AS_Path attribute. The default value is 255.']}",
    "bgp_rid_auto_sel": "{'description': ['The function to automatically select router IDs for all VPN BGP instances is enabled.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "check_first_as": "{'description': ['Check the first AS in the AS_Path of the update messages from EBGP peers.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "clear_interval": "{'description': ['Clear interval.']}",
    "confed_id_number": "{'description': ['Confederation ID. The value is a string of 1 to 11 characters.']}",
    "confed_nonstanded": "{'description': ['Configure the device to be compatible with devices in a nonstandard confederation.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "confed_peer_as_num": "{'description': ['Confederation AS number, in two-byte or four-byte format. The value is a string of 1 to 11 characters.']}",
    "conn_retry_time": "{'description': ['ConnectRetry interval. The value is an integer, in seconds. The default value is 32s.']}",
    "default_af_type": "{'description': ['Type of a created address family, which can be IPv4 unicast or IPv6 unicast. The default type is IPv4 unicast.'], 'choices': ['ipv4uni', 'ipv6uni']}",
    "ebgp_if_sensitive": "{'description': ['If the value is true, After the fast EBGP interface awareness function is enabled, EBGP sessions on an interface are deleted immediately when the interface goes Down. If the value is  false, After the fast EBGP interface awareness function is enabled, EBGP sessions on an interface are not deleted immediately when the interface goes Down.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "gr_peer_reset": "{'description': ['Peer disconnection through GR.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "graceful_restart": "{'description': ['Enable GR of the BGP speaker in the specified address family, peer address, or peer group.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "hold_interval": "{'description': ['Hold interval.']}",
    "hold_time": "{'description': ['Hold time, in seconds. The value of the hold time can be 0 or range from 3 to 65535.']}",
    "is_shutdown": "{'description': ['Interrupt BGP all neighbor.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "keep_all_routes": "{'description': ['If the value is true, the system stores all route update messages received from all peers (groups) after BGP connection setup. If the value is false, the system stores only BGP update messages that are received from peers and pass the configured import policy.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "keepalive_time": "{'description': ['If the value of a timer changes, the BGP peer relationship between the routers is disconnected. The value is an integer ranging from 0 to 21845. The default value is 60.']}",
    "memory_limit": "{'description': ['Support BGP RIB memory protection.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
    "min_hold_time": "{'description': ['Min hold time, in seconds. The value of the hold time can be 0 or range from 20 to 65535.']}",
    "router_id": "{'description': ['ID of a router that is in IPv4 address format.']}",
    "state": "{'description': ['Specify desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "suppress_interval": "{'description': ['Suppress interval.']}",
    "time_wait_for_rib": "{'description': ['Period of waiting for the End-Of-RIB flag. The value is an integer ranging from 3 to 3000. The default value is 600.']}",
    "vrf_name": "{'description': ['Name of a BGP instance. The name is a case-sensitive string of characters.']}",
    "vrf_rid_auto_sel": "{'description': ['If the value is true, VPN BGP instances are enabled to automatically select router IDs. If the value is false, VPN BGP instances are disabled from automatically selecting router IDs.'], 'default': 'no_use', 'choices': ['no_use', 'true', 'false']}",
}
```

## Examples


``` yaml


- name: CloudEngine BGP test
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

  - name: "Enable BGP"
    ce_bgp:
      state: present
      as_number: 100
      confed_id_number: 250
      provider: "{{ cli }}"

  - name: "Disable BGP"
    ce_bgp:
      state: absent
      as_number: 100
      confed_id_number: 250
      provider: "{{ cli }}"

  - name: "Create confederation peer AS num"
    ce_bgp:
      state: present
      confed_peer_as_num: 260
      provider: "{{ cli }}"

```

## License

TODO

## Author Information
  - ['wangdezhuang (@CloudEngine-Ansible)']
