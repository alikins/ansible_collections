# Ansible module: ansible.module_nmcli


Manage Networking

## Description

Manage the network devices. Create, modify and manage various connection and device type e.g., ethernet, teams, bonds, vlans etc.
On CentOS and Fedora like systems, install dependencies as 'yum/dnf install -y python-gobject NetworkManager-glib'
On Ubuntu and Debian like systems, install dependencies as 'apt-get install -y libnm-glib-dev'

## Requirements

TODO

## Arguments

``` json
{
    "ageingtime": "{'description': ['This is only used with bridge - [ageing-time <0-1000000>] the Ethernet MAC address aging time, in seconds'], 'default': 300}",
    "arp_interval": "{'description': ['This is only used with bond - ARP interval']}",
    "arp_ip_target": "{'description': ['This is only used with bond - ARP IP target']}",
    "autoconnect": "{'description': ['Whether the connection should start on boot.', 'Whether the connection profile can be automatically activated'], 'type': 'bool', 'default': True}",
    "conn_name": "{'description': ['Where conn_name will be the name used to call the connection. when not provided a default name is generated: <type>[-<ifname>][-<num>]'], 'required': True}",
    "dhcp_client_id": "{'description': ['DHCP Client Identifier sent to the DHCP server.'], 'version_added': '2.5'}",
    "dns4": "{'description': ['A list of upto 3 dns servers, ipv4 format e.g. To add two IPv4 DNS server addresses: "192.0.2.53 198.51.100.53"']}",
    "dns4_search": "{'description': ['A list of DNS search domains.'], 'version_added': 2.5}",
    "dns6": "{'description': ['A list of upto 3 dns servers, ipv6 format e.g. To add two IPv6 DNS server addresses: "2001:4860:4860::8888 2001:4860:4860::8844"']}",
    "dns6_search": "{'description': ['A list of DNS search domains.'], 'version_added': 2.5}",
    "downdelay": "{'description': ['This is only used with bond - downdelay']}",
    "egress": "{'description': ['This is only used with VLAN - VLAN egress priority mapping']}",
    "flags": "{'description': ['This is only used with VLAN - flags']}",
    "forwarddelay": "{'description': ['This is only used with bridge - [forward-delay <2-30>] STP forwarding delay, in seconds'], 'default': 15}",
    "gw4": "{'description': ['The IPv4 gateway for this interface using this format ie: "192.0.2.1"']}",
    "gw6": "{'description': ['The IPv6 gateway for this interface using this format ie: "2001:db8::1"']}",
    "hairpin": "{'description': ["This is only used with 'bridge-slave' - 'hairpin mode' for the slave, which allows frames to be sent back out through the slave the frame was received on."], 'type': 'bool', 'default': True}",
    "hellotime": "{'description': ['This is only used with bridge - [hello-time <1-10>] STP hello time, in seconds'], 'default': 2}",
    "ifname": "{'description': ['Where IFNAME will be the what we call the interface name.', 'interface to bind the connection to. The connection will only be applicable to this interface name.', 'A special value of "*" can be used for interface-independent connections.', 'The ifname argument is mandatory for all connection types except bond, team, bridge and vlan.'], 'default': 'conn_name'}",
    "ingress": "{'description': ['This is only used with VLAN - VLAN ingress priority mapping']}",
    "ip4": "{'description': ['The IPv4 address to this interface using this format ie: "192.0.2.24/24"']}",
    "ip6": "{'description': ['The IPv6 address to this interface using this format ie: "abbe::cafe"']}",
    "mac": "{'description': ['This is only used with bridge - MAC address of the bridge (note: this requires a recent kernel feature, originally introduced in 3.15 upstream kernel)\n']}",
    "master": "{'description': ['master <master (ifname, or connection UUID or conn_name) of bridge, team, bond master connection profile.']}",
    "maxage": "{'description': ['This is only used with bridge - [max-age <6-42>] STP maximum message age, in seconds'], 'default': 20}",
    "miimon": "{'description': ['This is only used with bond - miimon'], 'default': 100}",
    "mode": "{'description': ['This is the type of device or network connection that you wish to create for a bond, team or bridge.'], 'choices': ['balance-rr', 'active-backup', 'balance-xor', 'broadcast', '802.3ad', 'balance-tlb', 'balance-alb'], 'default': 'balance-rr'}",
    "mtu": "{'description': ["The connection MTU, e.g. 9000. This can't be applied when creating the interface and is done once the interface has been created.", 'Can be used when modifying Team, VLAN, Ethernet (Future plans to implement wifi, pppoe, infiniband)'], 'default': 1500}",
    "path_cost": "{'description': ["This is only used with 'bridge-slave' - [<1-65535>] - STP port cost for destinations via this slave"], 'default': 100}",
    "primary": "{'description': ['This is only used with bond and is the primary interface name (for "active-backup" mode), this is the usually the \'ifname\'']}",
    "priority": "{'description': ["This is only used with 'bridge' - sets STP priority"], 'default': 128}",
    "slavepriority": "{'description': ["This is only used with 'bridge-slave' - [<0-63>] - STP priority of this slave"], 'default': 32}",
    "state": "{'description': ['Whether the device should exist or not, taking action if the state is different from what is stated.'], 'required': True, 'choices': ['present', 'absent']}",
    "stp": "{'description': ['This is only used with bridge and controls whether Spanning Tree Protocol (STP) is enabled for this bridge'], 'type': 'bool'}",
    "type": "{'description': ['This is the type of device or network connection that you wish to create or modify.', 'type C(generic) is added in version 2.5.'], 'choices': ['ethernet', 'team', 'team-slave', 'bond', 'bond-slave', 'bridge', 'bridge-slave', 'vlan', 'generic']}",
    "updelay": "{'description': ['This is only used with bond - updelay']}",
    "vlandev": "{'description': ['This is only used with VLAN - parent device this VLAN is on, can use ifname']}",
    "vlanid": "{'description': ['This is only used with VLAN - VLAN ID in range <0-4095>']}",
}
```

## Examples


``` yaml

# These examples are using the following inventory:
#
# ## Directory layout:
#
# |_/inventory/cloud-hosts
# |           /group_vars/openstack-stage.yml
# |           /host_vars/controller-01.openstack.host.com
# |           /host_vars/controller-02.openstack.host.com
# |_/playbook/library/nmcli.py
# |          /playbook-add.yml
# |          /playbook-del.yml
# ```
#
# ## inventory examples
# ### groups_vars
# ```yml
# ---
# #devops_os_define_network
# storage_gw: "192.0.2.254"
# external_gw: "198.51.100.254"
# tenant_gw: "203.0.113.254"
#
# #Team vars
# nmcli_team:
#   - conn_name: tenant
#     ip4: '{{ tenant_ip }}'
#     gw4: '{{ tenant_gw }}'
#   - conn_name: external
#     ip4: '{{ external_ip }}'
#     gw4: '{{ external_gw }}'
#   - conn_name: storage
#     ip4: '{{ storage_ip }}'
#     gw4: '{{ storage_gw }}'
# nmcli_team_slave:
#   - conn_name: em1
#     ifname: em1
#     master: tenant
#   - conn_name: em2
#     ifname: em2
#     master: tenant
#   - conn_name: p2p1
#     ifname: p2p1
#     master: storage
#   - conn_name: p2p2
#     ifname: p2p2
#     master: external
#
# #bond vars
# nmcli_bond:
#   - conn_name: tenant
#     ip4: '{{ tenant_ip }}'
#     gw4: ''
#     mode: balance-rr
#   - conn_name: external
#     ip4: '{{ external_ip }}'
#     gw4: ''
#     mode: balance-rr
#   - conn_name: storage
#     ip4: '{{ storage_ip }}'
#     gw4: '{{ storage_gw }}'
#     mode: balance-rr
# nmcli_bond_slave:
#   - conn_name: em1
#     ifname: em1
#     master: tenant
#   - conn_name: em2
#     ifname: em2
#     master: tenant
#   - conn_name: p2p1
#     ifname: p2p1
#     master: storage
#   - conn_name: p2p2
#     ifname: p2p2
#     master: external
#
# #ethernet vars
# nmcli_ethernet:
#   - conn_name: em1
#     ifname: em1
#     ip4: '{{ tenant_ip }}'
#     gw4: '{{ tenant_gw }}'
#   - conn_name: em2
#     ifname: em2
#     ip4: '{{ tenant_ip1 }}'
#     gw4: '{{ tenant_gw }}'
#   - conn_name: p2p1
#     ifname: p2p1
#     ip4: '{{ storage_ip }}'
#     gw4: '{{ storage_gw }}'
#   - conn_name: p2p2
#     ifname: p2p2
#     ip4: '{{ external_ip }}'
#     gw4: '{{ external_gw }}'
# ```
#
# ### host_vars
# ```yml
# ---
# storage_ip: "192.0.2.91/23"
# external_ip: "198.51.100.23/21"
# tenant_ip: "203.0.113.77/23"
# ```



## playbook-add.yml example

---
- hosts: openstack-stage
  remote_user: root
  tasks:

  - name: install needed network manager libs
    yum:
      name: '{{ item }}'
      state: installed
    with_items:
      - NetworkManager-glib
      - libnm-qt-devel.x86_64
      - nm-connection-editor.x86_64
      - libsemanage-python
      - policycoreutils-python

##### Working with all cloud nodes - Teaming
  - name: try nmcli add team - conn_name only & ip4 gw4
    nmcli:
      type: team
      conn_name: '{{ item.conn_name }}'
      ip4: '{{ item.ip4 }}'
      gw4: '{{ item.gw4 }}'
      state: present
    with_items:
      - '{{ nmcli_team }}'

  - name: try nmcli add teams-slave
    nmcli:
      type: team-slave
      conn_name: '{{ item.conn_name }}'
      ifname: '{{ item.ifname }}'
      master: '{{ item.master }}'
      state: present
    with_items:
      - '{{ nmcli_team_slave }}'

###### Working with all cloud nodes - Bonding
  - name: try nmcli add bond - conn_name only & ip4 gw4 mode
    nmcli:
      type: bond
      conn_name: '{{ item.conn_name }}'
      ip4: '{{ item.ip4 }}'
      gw4: '{{ item.gw4 }}'
      mode: '{{ item.mode }}'
      state: present
    with_items:
      - '{{ nmcli_bond }}'

  - name: try nmcli add bond-slave
    nmcli:
      type: bond-slave
      conn_name: '{{ item.conn_name }}'
      ifname: '{{ item.ifname }}'
      master: '{{ item.master }}'
      state: present
    with_items:
      - '{{ nmcli_bond_slave }}'

##### Working with all cloud nodes - Ethernet
  - name: nmcli add Ethernet - conn_name only & ip4 gw4
    nmcli:
      type: ethernet
      conn_name: '{{ item.conn_name }}'
      ip4: '{{ item.ip4 }}'
      gw4: '{{ item.gw4 }}'
      state: present
    with_items:
      - '{{ nmcli_ethernet }}'

## playbook-del.yml example
- hosts: openstack-stage
  remote_user: root
  tasks:

  - name: try nmcli del team - multiple
    nmcli:
      conn_name: '{{ item.conn_name }}'
      state: absent
    with_items:
      - conn_name: em1
      - conn_name: em2
      - conn_name: p1p1
      - conn_name: p1p2
      - conn_name: p2p1
      - conn_name: p2p2
      - conn_name: tenant
      - conn_name: storage
      - conn_name: external
      - conn_name: team-em1
      - conn_name: team-em2
      - conn_name: team-p1p1
      - conn_name: team-p1p2
      - conn_name: team-p2p1
      - conn_name: team-p2p2

# To add an Ethernet connection with static IP configuration, issue a command as follows
  - nmcli:
    conn_name: my-eth1
    ifname: eth1
    type: ethernet
    ip4: 192.0.2.100/24
    gw4: 192.0.2.1
    state: present

# To add an Team connection with static IP configuration, issue a command as follows
  - nmcli:
      conn_name: my-team1
      ifname: my-team1
      type: team
      ip4: 192.0.2.100/24
      gw4: 192.0.2.1
      state: present
      autoconnect: yes

# Optionally, at the same time specify IPv6 addresses for the device as follows:
  - nmcli:
      conn_name: my-eth1
      ifname: eth1
      type: ethernet
      ip4: 192.0.2.100/24
      gw4: 192.0.2.1
      ip6: '2001:db8::cafe'
      gw6: '2001:db8::1'
      state: present

# To add two IPv4 DNS server addresses:
  - nmcli:
      conn_name: my-eth1
      type: ethernet
      dns4:
        - 192.0.2.53
        - 198.51.100.53
      state: present

# To make a profile usable for all compatible Ethernet interfaces, issue a command as follows
  - nmcli:
      ctype: ethernet
      name: my-eth1
      ifname: '*'
      state: present

# To change the property of a setting e.g. MTU, issue a command as follows:
  - nmcli:
      conn_name: my-eth1
      mtu: 9000
      type: ethernet
      state: present

# nmcli exits with status 0 if it succeeds and exits with a status greater
# than zero when there is a failure. The following list of status codes may be
# returned:
#
#     - 0 Success - indicates the operation succeeded
#     - 1 Unknown or unspecified error
#     - 2 Invalid user input, wrong nmcli invocation
#     - 3 Timeout expired (see --wait option)
#     - 4 Connection activation failed
#     - 5 Connection deactivation failed
#     - 6 Disconnecting device failed
#     - 7 Connection deletion failed
#     - 8 NetworkManager is not running
#     - 9 nmcli and NetworkManager versions mismatch
#     - 10 Connection, device, or access point does not exist.

```

## License

TODO

## Author Information
  - ['Chris Long (@alcamie101)']
