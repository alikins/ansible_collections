# Ansible module: ansible.module_aci_epg_to_contract


Bind EPGs to Contracts (fv:RsCons, fv:RsProv)

## Description

Bind EPGs to Contracts on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "ap": "{'description': ['Name of an existing application network profile, that will contain the EPGs.'], 'aliases': ['app_profile', 'app_profile_name']}",
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "contract": "{'description': ['The name of the contract.'], 'aliases': ['contract_name']}",
    "contract_type": "{'description': ['Determines if the EPG should Provide or Consume the Contract.'], 'required': True, 'choices': ['consumer', 'provider']}",
    "epg": "{'description': ['The name of the end point group.'], 'aliases': ['epg_name']}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "priority": "{'description': ['QoS class.', 'The APIC defaults to C(unspecified) when unset during creation.'], 'choices': ['level1', 'level2', 'level3', 'unspecified']}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "provider_match": "{'description': ['The matching algorithm for Provided Contracts.', 'The APIC defaults to C(at_least_one) when unset during creation.'], 'choices': ['all', 'at_least_one', 'at_most_one', 'none']}",
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

- name: Add a new contract to EPG binding
  aci_epg_to_contract:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: anstest
    ap: anstest
    epg: anstest
    contract: anstest_http
    contract_type: provider
    state: present
  delegate_to: localhost

- name: Remove an existing contract to EPG binding
  aci_epg_to_contract:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: anstest
    ap: anstest
    epg: anstest
    contract: anstest_http
    contract_type: provider
    state: absent
  delegate_to: localhost

- name: Query a specific contract to EPG binding
  aci_epg_to_contract:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: anstest
    ap: anstest
    epg: anstest
    contract: anstest_http
    contract_type: provider
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all provider contract to EPG bindings
  aci_epg_to_contract:
    host: apic
    username: admin
    password: SomeSecretPassword
    contract_type: provider
    state: query
  delegate_to: localhost
  register: query_result

```

## License

TODO

## Author Information
  - ['Jacob McGill (@jmcgill298)']
