# Ansible module: ansible.module_bigip_firewall_rule


Manage AFM Firewall rules

## Description

Manages firewall rules in an AFM firewall policy. New rules will always be added to the end of the policy. Rules can be re-ordered using the C(bigip_security_policy) module. Rules can also be pre-ordered using the C(bigip_security_policy) module and then later updated using the C(bigip_firewall_rule) module.

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['Specifies the action for the firewall rule.', 'When C(accept), allows packets with the specified source, destination, and protocol to pass through the firewall. Packets that match the rule, and are accepted, traverse the system as if the firewall is not present.', 'When C(drop), drops packets with the specified source, destination, and protocol. Dropping a packet is a silent action with no notification to the source or destination systems. Dropping the packet causes the connection to be retried until the retry threshold is reached.', 'When C(reject), rejects packets with the specified source, destination, and protocol. When a packet is rejected the firewall sends a destination unreachable message to the sender.', 'When C(accept-decisively), allows packets with the specified source, destination, and protocol to pass through the firewall, and does not require any further processing by any of the further firewalls. Packets that match the rule, and are accepted, traverse the system as if the firewall is not present. If the Rule List is applied to a virtual server, management IP, or self IP firewall rule, then Accept Decisively is equivalent to Accept.', 'When creating a new rule, if this parameter is not provided, the default is C(reject).'], 'choices': ['accept', 'drop', 'reject', 'accept-decisively']}",
    "description": "{'description': ['The rule description.']}",
    "destination": "{'description': ['Specifies packet destinations to which the rule applies.', 'Leaving this field blank applies the rule to all addresses and all ports.', 'You can specify the following destination items. An IPv4 or IPv6 address, an IPv4 or IPv6 address range, geographic location, VLAN, address list, port, port range, port list or address list.', 'You can specify a mix of different types of items for the source address.'], 'suboptions': {'address': {'description': ['Specifies a specific IP address.']}, 'address_list': {'description': ['Specifies an existing address list.']}, 'address_range': {'description': ['Specifies an address range.']}, 'country': {'description': ['Specifies a country code.']}, 'port': {'description': ['Specifies a single numeric port.', 'This option is only valid when C(protocol) is C(tcp)(6) or C(udp)(17).']}, 'port_list': {'description': ['Specifes an existing port list.', 'This option is only valid when C(protocol) is C(tcp)(6) or C(udp)(17).']}, 'port_range': {'description': ['Specifies a range of ports, which is two port values separated by a hyphen. The port to the left of the hyphen should be less than the port to the right.', 'This option is only valid when C(protocol) is C(tcp)(6) or C(udp)(17).']}}}",
    "icmp_message": "{'description': ['Specifies the Internet Control Message Protocol (ICMP) or ICMPv6 message C(type) and C(code) that the rule uses.', 'This parameter is only relevant when C(protocol) is either C(icmp)(1) or C(icmpv6)(58).'], 'suboptions': {'type': {'description': ['Specifies the type of ICMP message.', 'You can specify control messages, such as Echo Reply (0) and Destination Unreachable (3), or you can specify C(any) to indicate that the system applies the rule for all ICMP messages.', 'You can also specify an arbitrary ICMP message.', 'The ICMP protocol contains definitions for the existing message type and number pairs.']}, 'code': {'description': ['Specifies the code returned in response to the specified ICMP message type.', 'You can specify codes, each set appropriate to the associated type, such as No Code (0) (associated with Echo Reply (0)) and Host Unreachable (1) (associated with Destination Unreachable (3)), or you can specify C(any) to indicate that the system applies the rule for all codes in response to that specific ICMP message.', 'You can also specify an arbitrary code.', 'The ICMP protocol contains definitions for the existing message code and number pairs.']}}}",
    "irule": "{'description': ['Specifies an iRule that is applied to the rule.', 'An iRule can be started when the firewall rule matches traffic.']}",
    "logging": "{'description': ['Specifies whether logging is enabled or disabled for the firewall rule.', 'When creating a new rule, if this parameter is not specified, the default if C(no).'], 'type': 'bool'}",
    "name": "{'description': ['Specifies the name of the rule.'], 'required': True}",
    "parent_policy": "{'description': ['The policy which contains the rule to be managed.', 'One of either C(parent_policy) or C(parent_rule_list) is required.']}",
    "parent_rule_list": "{'description': ['The rule list which contains the rule to be managed.', 'One of either C(parent_policy) or C(parent_rule_list) is required.']}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "protocol": "{'description': ['Specifies the protocol to which the rule applies.', 'Protocols may be specified by either their name or numeric value.', 'A special protocol value C(any) can be specified to match any protocol. The numeric equivalent of this protocol is C(255).']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "rule_list": "{'description': ['Specifies an existing rule list to use in the rule.', "This parameter is mutually exclusive with many of the other individual-rule specific settings. This includes C(logging), C(action), C(source), C(destination), C(irule'), C(protocol) and C(logging)."]}",
    "schedule": "{'description': ['Specifies a schedule for the firewall rule.', 'You configure schedules to define days and times when the firewall rule is made active.']}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "source": "{'description': ['Specifies packet sources to which the rule applies.', 'Leaving this field blank applies the rule to all addresses and all ports.', 'You can specify the following source items. An IPv4 or IPv6 address, an IPv4 or IPv6 address range, geographic location, VLAN, address list, port, port range, port list or address list.', 'You can specify a mix of different types of items for the source address.'], 'suboptions': {'address': {'description': ['Specifies a specific IP address.']}, 'address_list': {'description': ['Specifies an existing address list.']}, 'address_range': {'description': ['Specifies an address range.']}, 'country': {'description': ['Specifies a country code.']}, 'port': {'description': ['Specifies a single numeric port.', 'This option is only valid when C(protocol) is C(tcp)(6) or C(udp)(17).']}, 'port_list': {'description': ['Specifes an existing port list.', 'This option is only valid when C(protocol) is C(tcp)(6) or C(udp)(17).']}, 'port_range': {'description': ['Specifies a range of ports, which is two port values separated by a hyphen. The port to the left of the hyphen should be less than the port to the right.', 'This option is only valid when C(protocol) is C(tcp)(6) or C(udp)(17).']}}}",
    "state": "{'description': ['When C(state) is C(present), ensures that the rule exists.', 'When C(state) is C(absent), ensures that the rule is removed.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "status": "{'description': ['Indicates the activity state of the rule or rule list.', 'When C(disabled), specifies that the rule or rule list does not apply at all.', 'When C(enabled), specifies that the system applies the firewall rule or rule list to the given context and addresses.', 'When C(scheduled), specifies that the system applies the rule or rule list according to the specified schedule.', 'When creating a new rule, if this parameter is not provided, the default is C(enabled).'], 'choices': ['enabled', 'disabled', 'scheduled']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create a new rule in the foo firewall policy
  bigip_firewall_rule:
    name: foo
    parent_policy: policy1
    protocol: tcp
    source:
      - address: 1.2.3.4
      - address: "::1"
      - address_list: foo-list1
      - address_range: 1.1.1.1-2.2.2.2
      - vlan: vlan1
      - country: US
      - port: 22
      - port_list: port-list1
      - port_range: 80-443
    destination:
      - address: 1.2.3.4
      - address: "::1"
      - address_list: foo-list1
      - address_range: 1.1.1.1-2.2.2.2
      - country: US
      - port: 22
      - port_list: port-list1
      - port_range: 80-443
    irule: irule1
    action: accept
    logging: yes
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Create an ICMP specific rule
  bigip_firewall_rule:
    name: foo
    protocol: icmp
    icmp_message:
      type: 0
    source:
      - country: US
    action: drop
    logging: yes
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

- name: Add a new rule that is uses an existing rule list
  bigip_firewall_rule:
    name: foo
    rule_list: rule-list1
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
