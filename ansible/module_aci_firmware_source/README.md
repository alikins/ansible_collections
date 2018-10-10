# Ansible module: ansible.module_aci_firmware_source


Manage firmware image sources (firmware:OSource)

## Description

Manage firmware image sources on Cisco ACI fabrics.

## Requirements

TODO

## Arguments

``` json
{
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "polling_interval": "{'description': ['Polling interval in minutes.'], 'type': 'int'}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "source": "{'description': ['The identifying name for the outside source of images, such as an HTTP or SCP server.'], 'required': True, 'aliases': ['name', 'source_name']}",
    "state": "{'description': ['Use C(present) or C(absent) for adding or removing.', 'Use C(query) for listing an object or multiple objects.'], 'choices': ['absent', 'present', 'query'], 'default': 'present'}",
    "timeout": "{'description': ['The socket level timeout in seconds.'], 'type': 'int', 'default': 30}",
    "url": "{'description': ['The firmware URL for the image(s) on the source.']}",
    "url_password": "{'description': ['The Firmware password or key string.']}",
    "url_protocol": "{'description': ['The Firmware download protocol.'], 'choices': ['http', 'local', 'scp', 'usbkey'], 'default': 'scp', 'aliases': ['url_proto']}",
    "url_username": "{'description': ['The username for the source.']}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['The username to use for authentication.'], 'default': 'admin', 'aliases': ['user']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only set to C(no) when used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Add firmware source
  aci_firmware_source:
    host: apic
    username: admin
    password: SomeSecretPassword
    source: aci-msft-pkg-3.1.1i.zip
    url: foo.bar.cisco.com/download/cisco/aci/aci-msft-pkg-3.1.1i.zip
    url_protocol: http
    state: present
  delegate_to: localhost

- name: Remove firmware source
  aci_firmware_source:
    host: apic
    username: admin
    password: SomeSecretPassword
    source: aci-msft-pkg-3.1.1i.zip
    state: absent
  delegate_to: localhost

- name: Query a specific firmware source
  aci_firmware_source:
    host: apic
    username: admin
    password: SomeSecretPassword
    source: aci-msft-pkg-3.1.1i.zip
    state: query
  delegate_to: localhost
  register: query_result

- name: Query all firmware sources
  aci_firmware_source:
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
  - ['Dag Wieers (@dagwieers)']
