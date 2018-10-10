# Ansible module: ansible.module_aci_rest


Direct access to the Cisco APIC REST API

## Description

Enables the management of the Cisco ACI fabric through direct access to the Cisco APIC REST API.
Thanks to the idempotent nature of the APIC, this module is idempotent and reports changes.

## Requirements

TODO

## Arguments

``` json
{
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "content": "{'description': ['When used instead of C(src), sets the payload of the API request directly.', 'This may be convenient to template simple requests.', 'For anything complex use the C(template) lookup plugin (see examples) or the M(template) module with parameter C(src).']}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "method": "{'description': ['The HTTP method of the request.', 'Using C(delete) is typically used for deleting objects.', 'Using C(get) is typically used for querying objects.', 'Using C(post) is typically used for modifying objects.'], 'default': 'get', 'choices': ['delete', 'get', 'post'], 'aliases': ['action']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "path": "{'description': ['URI being used to execute API calls.', 'Must end in C(.xml) or C(.json).'], 'required': True, 'aliases': ['uri']}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "src": "{'description': ['Name of the absolute path of the filname that includes the body of the HTTP request being sent to the ACI fabric.', 'If you require a templated payload, use the C(content) parameter together with the C(template) lookup plugin, or use M(template).'], 'type': 'path', 'aliases': ['config_file']}",
    "timeout": "{'description': ['The socket level timeout in seconds.'], 'type': 'int', 'default': 30}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['The username to use for authentication.'], 'default': 'admin', 'aliases': ['user']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only set to C(no) when used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Add a tenant using certificate authentication
  aci_rest:
    host: apic
    username: admin
    private_key: pki/admin.key
    method: post
    path: /api/mo/uni.xml
    src: /home/cisco/ansible/aci/configs/aci_config.xml
  delegate_to: localhost

- name: Add a tenant from a templated payload file from templates/
  aci_rest:
    host: apic
    username: admin
    private_key: pki/admin.key
    method: post
    path: /api/mo/uni.xml
    content: "{{ lookup('template', 'aci/tenant.xml.j2') }}"
  delegate_to: localhost

- name: Add a tenant using inline YAML
  aci_rest:
    host: apic
    username: admin
    private_key: pki/admin.key
    validate_certs: no
    path: /api/mo/uni.json
    method: post
    content:
      fvTenant:
        attributes:
          name: Sales
          descr: Sales departement
  delegate_to: localhost

- name: Add a tenant using a JSON string
  aci_rest:
    host: apic
    username: admin
    private_key: pki/admin.key
    validate_certs: no
    path: /api/mo/uni.json
    method: post
    content:
      {
        "fvTenant": {
          "attributes": {
            "name": "Sales",
            "descr": "Sales departement"
          }
        }
      }
  delegate_to: localhost

- name: Add a tenant using an XML string
  aci_rest:
    host: apic
    username: admin
    private_key: pki/{{ aci_username}}.key
    validate_certs: no
    path: /api/mo/uni.xml
    method: post
    content: '<fvTenant name="Sales" descr="Sales departement"/>'
  delegate_to: localhost

- name: Get tenants using password authentication
  aci_rest:
    host: apic
    username: admin
    password: SomeSecretPassword
    method: get
    path: /api/node/class/fvTenant.json
  delegate_to: localhost
  register: query_result

- name: Configure contracts
  aci_rest:
    host: apic
    username: admin
    private_key: pki/admin.key
    method: post
    path: /api/mo/uni.xml
    src: /home/cisco/ansible/aci/configs/contract_config.xml
  delegate_to: localhost

- name: Register leaves and spines
  aci_rest:
    host: apic
    username: admin
    private_key: pki/admin.key
    validate_certs: no
    method: post
    path: /api/mo/uni/controller/nodeidentpol.xml
    content: |
      <fabricNodeIdentPol>
        <fabricNodeIdentP name="{{ item.name }}" nodeId="{{ item.nodeid }}" status="{{ item.status }}" serial="{{ item.serial }}"/>
      </fabricNodeIdentPol>
  with_items:
  - '{{ apic_leavesspines }}'
  delegate_to: localhost

- name: Wait for all controllers to become ready
  aci_rest:
    host: apic
    username: admin
    private_key: pki/admin.key
    validate_certs: no
    path: /api/node/class/topSystem.json?query-target-filter=eq(topSystem.role,"controller")
  register: apics
  until: "'totalCount' in apics and apics.totalCount|int >= groups['apic']|count"
  retries: 120
  delay: 30
  delegate_to: localhost
  run_once: yes

```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)']
