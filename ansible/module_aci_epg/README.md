# Ansible module: ansible.module_aci_epg


Manage End Point Groups (EPG) objects (fv:AEPg)

## Description

Manage End Point Groups (EPG) on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "ap": "{'description': ['Name of an existing application network profile, that will contain the EPGs.'], 'required': True, 'aliases': ['app_profile', 'app_profile_name']}",
    "bd": "{'description': ['Name of the bridge domain being associated with the EPG.'], 'required': True, 'aliases': ['bd_name', 'bridge_domain']}",
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "description": "{'description': ['Description for the EPG.'], 'aliases': ['descr']}",
    "epg": "{'description': ['Name of the end point group.'], 'required': True, 'aliases': ['epg_name', 'name']}",
    "fwd_control": "{'description': ['The forwarding control used by the EPG.', 'The APIC defaults to C(none) when unset during creation.'], 'choices': ['none', 'proxy-arp']}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "intra_epg_isolation": "{'description': ['The Intra EPG Isolation.', 'The APIC defaults to C(unenforced) when unset during creation.'], 'choices': ['enforced', 'unenforced']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "preferred_group": "{'description': ['Whether ot not the EPG is part of the Preferred Group and can communicate without contracts.', 'This is very convenient for migration scenarios, or when ACI is used for network automation but not for policy.', 'The APIC defaults to C(no) when unset during creation.'], 'type': 'bool', 'version_added': '2.5'}",
    "priority": "{'description': ['The QoS class.', 'The APIC defaults to C(unspecified) when unset during creation.'], 'choices': ['level1', 'level2', 'level3', 'unspecified']}",
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

- name: Add a new EPG
  aci_epg:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    ap: intranet
    epg: web_epg
    description: Web Intranet EPG
    bd: prod_bd
    preferred_group: yes
    state: present
  delegate_to: localhost

- aci_epg:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    ap: ticketing
    epg: "{{ item.epg }}"
    description: Ticketing EPG
    bd: "{{ item.bd }}"
    priority: unspecified
    intra_epg_isolation: unenforced
    state: present
  delegate_to: localhost
  with_items:
    - epg: web
      bd: web_bd
    - epg: database
      bd: database_bd

- name: Remove an EPG
  aci_epg:
    host: apic
    username: admin
    password: SomeSecretPassword
    validate_certs: no
    tenant: production
    app_profile: intranet
    epg: web_epg
    state: absent
  delegate_to: localhost

- name: Query an EPG
  aci_epg:
    host: apic
    username: admin
    password: SomeSecretPassword
    tenant: production
    ap: ticketing
    epg: web_epg
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all EPGs
  aci_epg:
    host: apic
    username: admin
    password: SomeSecretPassword
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all EPGs with a Specific Name
  aci_epg:
    host: apic
    username: admin
    password: SomeSecretPassword
    validate_certs: no
    epg: web_epg
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all EPGs of an App Profile
  aci_epg:
    host: apic
    username: admin
    password: SomeSecretPassword
    validate_certs: no
    ap: ticketing
    state: query
  delegate_to: localhost
  register: query_result

```

## License

TODO

## Author Information
  - ['Swetha Chunduri (@schunduri)']
