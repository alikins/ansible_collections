# Ansible module: ansible.module_ufw


Manage firewall with UFW

## Description

Manage firewall with UFW.

## Requirements

TODO

## Arguments

``` json
{
    "comment": "{'description': ['Add a comment to the rule. Requires UFW version >=0.35.'], 'version_added': '2.4'}",
    "delete": "{'description': ['Delete rule.'], 'type': 'bool'}",
    "direction": "{'description': ['Select direction for a rule or default policy command.'], 'choices': ['in', 'incoming', 'out', 'outgoing', 'routed']}",
    "from_ip": "{'description': ['Source IP address.'], 'aliases': ['from', 'src'], 'default': 'any'}",
    "from_port": "{'description': ['Source port.']}",
    "insert": "{'description': ['Insert the corresponding rule as rule number NUM']}",
    "interface": "{'description': ['Specify interface for rule.'], 'aliases': ['if']}",
    "log": "{'description': ['Log new connections matched to this rule'], 'type': 'bool'}",
    "logging": "{'description': ['Toggles logging. Logged packets use the LOG_KERN syslog facility.'], 'choices': [True, False, 'low', 'medium', 'high', 'full']}",
    "name": "{'description': ['Use profile located in C(/etc/ufw/applications.d).'], 'aliases': ['app']}",
    "policy": "{'description': ['Change the default policy for incoming or outgoing traffic.'], 'aliases': ['default'], 'choices': ['allow', 'deny', 'reject']}",
    "proto": "{'description': ['TCP/IP protocol.'], 'choices': ['any', 'tcp', 'udp', 'ipv6', 'esp', 'ah']}",
    "route": "{'description': ['Apply the rule to routed/forwarded packets.'], 'type': 'bool'}",
    "rule": "{'description': ['Add firewall rule'], 'choices': ['allow', 'deny', 'limit', 'reject']}",
    "state": "{'description': ['C(enabled) reloads firewall and enables firewall on boot.', 'C(disabled) unloads firewall and disables firewall on boot.', 'C(reloaded) reloads firewall.', 'C(reset) disables and resets firewall to installation defaults.'], 'choices': ['disabled', 'enabled', 'reloaded', 'reset']}",
    "to_ip": "{'description': ['Destination IP address.'], 'aliases': ['dest', 'to'], 'default': 'any'}",
    "to_port": "{'description': ['Destination port.'], 'aliases': ['port']}",
}
```

## Examples


``` yaml

- name: Allow everything and enable UFW
  ufw:
    state: enabled
    policy: allow

- name: Set logging
  ufw:
    logging: on

# Sometimes it is desirable to let the sender know when traffic is
# being denied, rather than simply ignoring it. In these cases, use
# reject instead of deny. In addition, log rejected connections:
- ufw:
    rule: reject
    port: auth
    log: yes

# ufw supports connection rate limiting, which is useful for protecting
# against brute-force login attacks. ufw will deny connections if an IP
# address has attempted to initiate 6 or more connections in the last
# 30 seconds. See  http://www.debian-administration.org/articles/187
# for details. Typical usage is:
- ufw:
    rule: limit
    port: ssh
    proto: tcp

# Allow OpenSSH. (Note that as ufw manages its own state, simply removing
# a rule=allow task can leave those ports exposed. Either use delete=yes
# or a separate state=reset task)
- ufw:
    rule: allow
    name: OpenSSH

- name: Delete OpenSSH rule
  ufw:
    rule: allow
    name: OpenSSH
    delete: yes

- name: Deny all access to port 53
  ufw:
    rule: deny
    port: 53

- name: Allow port range 60000-61000
  ufw:
    rule: allow
    port: 60000:61000

- name: Allow all access to tcp port 80
  ufw:
    rule: allow
    port: 80
    proto: tcp

- name: Allow all access from RFC1918 networks to this host
  ufw:
    rule: allow
    src: '{{ item }}'
  with_items:
    - 10.0.0.0/8
    - 172.16.0.0/12
    - 192.168.0.0/16

- name: Deny access to udp port 514 from host 1.2.3.4 and include a comment
  ufw:
    rule: deny
    proto: udp
    src: 1.2.3.4
    port: 514
    comment: Block syslog

- name: Allow incoming access to eth0 from 1.2.3.5 port 5469 to 1.2.3.4 port 5469
  ufw:
    rule: allow
    interface: eth0
    direction: in
    proto: udp
    src: 1.2.3.5
    from_port: 5469
    dest: 1.2.3.4
    to_port: 5469

# Note that IPv6 must be enabled in /etc/default/ufw for IPv6 firewalling to work.
- name: Deny all traffic from the IPv6 2001:db8::/32 to tcp port 25 on this host
  ufw:
    rule: deny
    proto: tcp
    src: 2001:db8::/32
    port: 25

# Can be used to further restrict a global FORWARD policy set to allow
- name: Deny forwarded/routed traffic from subnet 1.2.3.0/24 to subnet 4.5.6.0/24
  ufw:
    rule: deny
    route: yes
    src: 1.2.3.0/24
    dest: 4.5.6.0/24

```

## License

TODO

## Author Information
  - ['Aleksey Ovcharenko (@ovcharenko)', 'Jarno Keskikangas (@pyykkis)', 'Ahti Kitsik (@ahtik)']
  - ['Aleksey Ovcharenko (@ovcharenko)', 'Jarno Keskikangas (@pyykkis)', 'Ahti Kitsik (@ahtik)']
  - ['Aleksey Ovcharenko (@ovcharenko)', 'Jarno Keskikangas (@pyykkis)', 'Ahti Kitsik (@ahtik)']
