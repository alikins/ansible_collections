# Ansible module: ansible.module_aci_static_binding_to_epg


Bind static paths to EPGs (fv:RsPathAtt)

## Description

Bind static paths to EPGs on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "ap": "{'description': ['Name of an existing application network profile, that will contain the EPGs.'], 'aliases': ['app_profile', 'app_profile_name']}",
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "deploy_immediacy": "{'description': ['The Deployement Immediacy of Static EPG on PC, VPC or Interface.', 'The APIC defaults to C(lazy) when unset during creation.'], 'choices': ['immediate', 'lazy']}",
    "description": "{'description': ['Description for the static path to EPG binding.'], 'aliases': ['descr'], 'version_added': '2.7'}",
    "encap_id": "{'description': ['The encapsulation ID associating the C(epg) with the interface path.', 'This acts as the secondary C(encap_id) when using micro-segmentation.', 'Accepted values are any valid encap ID for specified encap, currently ranges between C(1) and C(4096).'], 'type': 'int', 'aliases': ['vlan', 'vlan_id']}",
    "epg": "{'description': ['The name of the end point group.'], 'aliases': ['epg_name']}",
    "extpaths": "{'description': ['The C(extpaths) integer value part of the tDn.', 'C(extpaths) is only used if C(interface_type) is C(fex).', 'Usually something like C(1011).'], 'type': 'int'}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "interface": "{'description': ['The C(interface) string value part of the tDn.', 'Usually a policy group like C(test-IntPolGrp) or an interface of the following format C(1/7) depending on C(interface_type).']}",
    "interface_mode": "{'description': ['Determines how layer 2 tags will be read from and added to frames.', 'Values C(802.1p) and C(native) are identical.', 'Values C(access) and C(untagged) are identical.', 'Values C(regular), C(tagged) and C(trunk) are identical.', 'The APIC defaults to C(trunk) when unset during creation.'], 'choices': ['802.1p', 'access', 'native', 'regular', 'tagged', 'trunk', 'untagged'], 'aliases': ['interface_mode_name', 'mode']}",
    "interface_type": "{'description': ['The type of interface for the static EPG deployement.'], 'choices': ['fex', 'port_channel', 'switch_port', 'vpc'], 'default': 'switch_port'}",
    "leafs": "{'description': ['The switch ID(s) that the C(interface) belongs to.', 'When C(interface_type) is C(switch_port), C(port_channel), or C(fex), then C(leafs) is a string of the leaf ID.', 'When C(interface_type) is C(vpc), then C(leafs) is a list with both leaf IDs.', "The C(leafs) value is usually something like '101' or '101-102' depending on C(connection_type)."], 'aliases': ['leaves', 'nodes', 'paths', 'switches']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "pod_id": "{'description': ['The pod number part of the tDn.', 'C(pod_id) is usually an integer below C(10).'], 'type': 'int', 'aliases': ['pod', 'pod_number']}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "primary_encap_id": "{'description': ['Determines the primary encapsulation ID associating the C(epg) with the interface path when using micro-segmentation.', 'Accepted values are any valid encap ID for specified encap, currently ranges between C(1) and C(4096).'], 'type': 'int', 'aliases': ['primary_vlan', 'primary_vlan_id']}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "state": "{'description': ['Use C(present) or C(absent) for adding or removing.', 'Use C(query) for listing an object or multiple objects.'], 'choices': ['absent', 'present', 'query'], 'default': 'present'}",
    "tenant": "{'description': ['Name of an existing tenant.'], 'aliases': ['tenant_name']}",
    "timeout": "{'description': ['The socket level timeout in seconds.'], 'type': 'int', 'default': 30}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['The username to use for authentication.'], 'default': 'admin', 'aliases': ['user']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only set to C(no) when used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Deploy Static Path binding for given EPG
  aci_static_binding_to_epg:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: accessport-code-cert
    ap: accessport_code_app
    epg: accessport_epg1
    encap_id: 222
    deploy_immediacy: lazy
    interface_mode: untagged
    interface_type: switch_port
    pod_id: 1
    leafs: 101
    interface: '1/7'
    state: present
  delegate_to: localhost

- name: Remove Static Path binding for given EPG
  aci_static_binding_to_epg:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: accessport-code-cert
    ap: accessport_code_app
    epg: accessport_epg1
    interface_type: switch_port
    pod: 1
    leafs: 101
    interface: '1/7'
    state: absent
  delegate_to: localhost

- name: Get specific Static Path binding for given EPG
  aci_static_binding_to_epg:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: accessport-code-cert
    ap: accessport_code_app
    epg: accessport_epg1
    interface_type: switch_port
    pod: 1
    leafs: 101
    interface: '1/7'
    state: query
  delegate_to: localhost
  register: query_result

```

## License

TODO

## Author Information
  - ['Bruno Calogero (@brunocalogero)']
