# Ansible module: ansible.module_aci_tenant_ep_retention_policy


Manage End Point (EP) retention protocol policies (fv:EpRetPol)

## Description

Manage End Point (EP) retention protocol policies on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "bounce_age": "{'description': ['Bounce entry aging interval in seconds.', 'Accepted values range between C(150) and C(65535); 0 is used for infinite.', 'The APIC defaults to C(630) when unset during creation.'], 'type': 'int'}",
    "bounce_trigger": "{'description': ['Determines if the bounce entries are installed by RARP Flood or COOP Protocol.', 'The APIC defaults to C(coop) when unset during creation.'], 'choices': ['coop', 'flood']}",
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "description": "{'description': ['Description for the End point rentention policy.'], 'aliases': ['descr']}",
    "epr_policy": "{'description': ['The name of the end point retention policy.'], 'aliases': ['epr_name', 'name']}",
    "hold_interval": "{'description': ['Hold interval in seconds.', 'Accepted values range between C(5) and C(65535).', 'The APIC defaults to C(300) when unset during creation.'], 'type': 'int'}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "local_ep_interval": "{'description': ['Local end point aging interval in seconds.', 'Accepted values range between C(120) and C(65535); 0 is used for infinite.', 'The APIC defaults to C(900) when unset during creation.'], 'type': 'int'}",
    "move_frequency": "{'description': ['Move frequency per second.', 'Accepted values range between C(0) and C(65535); 0 is used for none.', 'The APIC defaults to C(256) when unset during creation.'], 'type': 'int'}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "remote_ep_interval": "{'description': ['Remote end point aging interval in seconds.', 'Accepted values range between C(120) and C(65535); 0 is used for infinite.', 'The APIC defaults to C(300) when unset during creation.'], 'type': 'int'}",
    "state": "{'description': ['Use C(present) or C(absent) for adding or removing.', 'Use C(query) for listing an object or multiple objects.'], 'choices': ['absent', 'present', 'query'], 'default': 'present'}",
    "tenant": "{'description': ['The name of an existing tenant.'], 'aliases': ['tenant_name']}",
    "timeout": "{'description': ['The socket level timeout in seconds.'], 'type': 'int', 'default': 30}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['The username to use for authentication.'], 'default': 'admin', 'aliases': ['user']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only set to C(no) when used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Add a new EPR policy
  aci_epr_policy:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    epr_policy: EPRPol1
    bounce_age: 630
    hold_interval: 300
    local_ep_interval: 900
    remote_ep_interval: 300
    move_frequency: 256
    description: test
    state: present
  delegate_to: localhost

- name: Remove an EPR policy
  aci_epr_policy:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    epr_policy: EPRPol1
    state: absent
  delegate_to: localhost

- name: Query an EPR policy
  aci_epr_policy:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    epr_policy: EPRPol1
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all EPR policies
  aci_epr_policy:
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
  - ['Swetha Chunduri (@schunduri)']
