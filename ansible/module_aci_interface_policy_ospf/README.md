# Ansible module: ansible.module_aci_interface_policy_ospf


Manage OSPF interface policies (ospf:IfPol)

## Description

Manage OSPF interface policies on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "controls": "{'description': ['The interface policy controls.', 'This is a list of one or more of the following controls:', 'C(advert-subnet) -- Advertise IP subnet instead of a host mask in the router LSA.', 'C(bfd) -- Bidirectional Forwarding Detection', 'C(mtu-ignore) -- Disables MTU mismatch detection on an interface.', 'C(passive) -- The interface does not participate in the OSPF protocol and will not establish adjacencies or send routing updates. However the interface is announced as part of the routing network.'], 'type': 'list', 'choices': ['advert-subnet', 'bfd', 'mtu-ignore', 'passive']}",
    "cost": "{'description': ['The OSPF cost of the interface.', 'The cost (also called metric) of an interface in OSPF is an indication of the overhead required to send packets across a certain interface. The cost of an interface is inversely proportional to the bandwidth of that interface. A higher bandwidth indicates a lower cost. There is more overhead (higher cost) and time delays involved in crossing a 56k serial line than crossing a 10M ethernet line. The formula used to calculate the cost is C(cost= 10000 0000/bandwith in bps) For example, it will cost 10 EXP8/10 EXP7 = 10 to cross a 10M Ethernet line and will cost 10 EXP8/1544000 = 64 to cross a T1 line.', 'By default, the cost of an interface is calculated based on the bandwidth; you can force the cost of an interface with the ip ospf cost value interface subconfiguration mode command.', 'Accepted values range between C(1) and C(450).', 'The APIC defaults to C(0) when unset during creation.']}",
    "dead_interval": "{'description': ['The interval between hello packets from a neighbor before the router declares the neighbor as down.', 'This value must be the same for all networking devices on a specific network.', 'Specifying a smaller dead interval (seconds) will give faster detection of a neighbor being down and improve convergence, but might cause more routing instability.', 'Accepted values range between C(1) and C(65535).', 'The APIC defaults to C(40) when unset during creation.'], 'type': 'int'}",
    "description": "{'description': ['The description for the OSPF interface.'], 'aliases': ['descr']}",
    "hello_interval": "{'description': ['The interval between hello packets that OSPF sends on the interface.', 'Note that the smaller the hello interval, the faster topological changes will be detected, but more routing traffic will ensue.', 'This value must be the same for all routers and access servers on a specific network.', 'Accepted values range between C(1) and C(65535).', 'The APIC defaults to C(10) when unset during creation.'], 'type': 'int'}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "network_type": "{'description': ['The OSPF interface policy network type.', 'OSPF supports broadcast and point-to-point.', 'The APIC defaults to C(unspecified) when unset during creation.'], 'choices': ['bcast', 'p2p']}",
    "ospf": "{'description': ['The OSPF interface policy name.', 'This name can be between 1 and 64 alphanumeric characters.', 'Note that you cannot change this name after the object has been saved.'], 'required': True, 'aliases': ['ospf_interface', 'name']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "prefix_suppression": "{'description': ['Whether prefix suppressions is enabled or disabled.', 'The APIC defaults to C(inherit) when unset during creation.'], 'type': 'bool'}",
    "priority": "{'description': ['The priority for the OSPF interface profile.', 'Accepted values ranges between C(0) and C(255).', 'The APIC defaults to C(1) when unset during creation.'], 'type': 'int'}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "retransmit_interval": "{'description': ['The interval between LSA retransmissions.', 'The retransmit interval occurs while the router is waiting for an acknowledgement from the neighbor router that it received the LSA.', 'If no acknowlegment is received at the end of the interval, then the LSA is resent.', 'Accepted values range between C(1) and C(65535).', 'The APIC defaults to C(5) when unset during creation.'], 'type': 'int'}",
    "state": "{'description': ['Use C(present) or C(absent) for adding or removing.', 'Use C(query) for listing an object or multiple objects.'], 'choices': ['absent', 'present', 'query'], 'default': 'present'}",
    "tenant": "{'description': ['The name of the Tenant the OSPF interface policy should belong to.'], 'required': True, 'aliases': ['tenant_name']}",
    "timeout": "{'description': ['The socket level timeout in seconds.'], 'type': 'int', 'default': 30}",
    "transmit_delay": "{'description': ['The delay time needed to send an LSA update packet.', 'OSPF increments the LSA age time by the transmit delay amount before transmitting the LSA update.', 'You should take into account the transmission and propagation delays for the interface when you set this value.', 'Accepted values range between C(1) and C(450).', 'The APIC defaults to C(1) when unset during creation.'], 'type': 'int'}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['The username to use for authentication.'], 'default': 'admin', 'aliases': ['user']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only set to C(no) when used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Ensure ospf interface policy exists
  aci_interface_policy_ospf:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    ospf: ospf1
    state: present
  delegate_to: localhost

- name: Ensure ospf interface policy does not exist
  aci_interface_policy_ospf:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    ospf: ospf1
    state: present
  delegate_to: localhost

- name: Query an ospf interface policy
  aci_interface_policy_ospf:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    ospf: ospf1
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all ospf interface policies in tenant production
  aci_interface_policy_ospf:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    state: query
  delegate_to: localhost
  register: query_result

```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)']
