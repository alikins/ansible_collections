# Ansible module: ansible.module_bigip_timer_policy


Manage timer policies on a BIG-IP

## Description

Manage timer policies on a BIG-IP.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['Specifies descriptive text that identifies the timer policy.']}",
    "name": "{'description': ['Specifies the name of the timer policy.'], 'required': True}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common'}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "rules": "{'description': ['Rules that you want assigned to the timer policy'], 'suboptions': {'name': {'description': ['The name of the rule.'], 'required': True}, 'protocol': {'description': ['Specifies the IP protocol entry for which the timer policy rule is being configured. This could be a layer-4 protocol (such as C(tcp), C(udp) or C(sctp).', 'Only flows matching the configured protocol will make use of this rule.', 'When C(all-other) is specified, if there are no specific ip-protocol rules that match the flow, the flow matches all the other ip-protocol rules.', 'When specifying rules, if this parameter is not specified, the default of C(all-other) will be used.'], 'choices': ['all-other', 'ah', 'bna', 'esp', 'etherip', 'gre', 'icmp', 'ipencap', 'ipv6', 'ipv6-auth', 'ipv6-crypt', 'ipv6-icmp', 'isp-ip', 'mux', 'ospf', 'sctp', 'tcp', 'udp', 'udplite']}, 'destination_ports': {'description': ['The list of destination ports to match the rule on.', 'Specify a port range by specifying start and end ports separated by a dash (-).', 'This field is only available if you have selected the C(sctp), C(tcp), or C(udp) protocol.']}, 'idle_timeout': {'description': ['Specifies an idle timeout, in seconds, for protocol and port pairs that match the timer policy rule.', 'When C(infinite), specifies that the protocol and port pairs that match the timer policy rule have no idle timeout.', 'When specifying rules, if this parameter is not specified, the default of C(unspecified) will be used.']}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present), ensures that the resource exists.', 'When C(absent), ensures the resource is removed.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create a timer policy
  bigip_timer_policy:
    name: timer1
    description: My timer policy
    rules:
      - name: rule1
        protocol: tcp
        idle_timeout: indefinite
        destination_ports:
          - 443
          - 80
      - name: rule2
        protocol: 200
      - name: rule3
        protocol: sctp
        idle_timeout: 200
        destination_ports:
          - 21
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

- name: Remove a timer policy and all its associated rules
  bigip_timer_policy:
    name: timer1
    description: My timer policy
    password: secret
    server: lb.mydomain.com
    state: absent
    user: admin
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
