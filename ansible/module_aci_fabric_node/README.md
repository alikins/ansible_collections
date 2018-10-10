# Ansible module: ansible.module_aci_fabric_node


Manage Fabric Node Members (fabric:NodeIdentP)

## Description

Manage Fabric Node Members on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "description": "{'description': ['Description for the new Fabric Node Member.'], 'aliases': ['descr']}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "node_id": "{'description': ['Node ID Number for the new Fabric Node Member.'], 'type': 'int'}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "pod_id": "{'description': ['The pod id of the new Fabric Node Member.'], 'type': 'int'}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "role": "{'description': ['Role for the new Fabric Node Member.'], 'aliases': ['role_name'], 'choices': ['leaf', 'spine', 'unspecified']}",
    "serial": "{'description': ['Serial Number for the new Fabric Node Member.'], 'aliases': ['serial_number']}",
    "state": "{'description': ['Use C(present) or C(absent) for adding or removing.', 'Use C(query) for listing an object or multiple objects.'], 'choices': ['absent', 'present', 'query'], 'default': 'present'}",
    "switch": "{'description': ['Switch Name for the new Fabric Node Member.'], 'aliases': ['name', 'switch_name']}",
    "timeout": "{'description': ['The socket level timeout in seconds.'], 'type': 'int', 'default': 30}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['The username to use for authentication.'], 'default': 'admin', 'aliases': ['user']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only set to C(no) when used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Add fabric node
  aci_fabric_node:
    host: apic
    username: admin
    password: SomeSecretPassword
    serial: FDO2031124L
    node_id: 1011
    switch: fab4-sw1011
    state: present
  delegate_to: localhost

- name: Remove fabric node
  aci_fabric_node:
    host: apic
    username: admin
    password: SomeSecretPassword
    serial: FDO2031124L
    node_id: 1011
    state: absent
  delegate_to: localhost

- name: Query fabric nodes
  aci_fabric_node:
    host: apic
    username: admin
    password: SomeSecretPassword
    state: query
  delegate_to: localhost
  register: query_result

```

## License

TODO

## Author Information
  - ['Bruno Calogero (@brunocalogero)']
