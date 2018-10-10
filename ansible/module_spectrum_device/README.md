# Ansible module: ansible.module_spectrum_device


Creates/deletes devices in CA Spectrum

## Description

This module allows you to create and delete devices in CA Spectrum U(https://www.ca.com/us/products/ca-spectrum.html).
Tested on CA Spectrum 9.4.2, 10.1.1 and 10.2.1

## Requirements

TODO

## Arguments

``` json
{
    "agentport": "{'required': False, 'description': ['UDP port used for SNMP discovery.'], 'default': 161}",
    "community": "{'description': ['SNMP community used for device discovery.', 'Required when C(state=present).']}",
    "device": "{'aliases': ['host', 'name'], 'required': True, 'description': ['IP address of the device.', 'If a hostname is given, it will be resolved to the IP address.']}",
    "landscape": "{'required': True, 'description': ['Landscape handle of the SpectroServer to which add or remove the device.']}",
    "state": "{'required': False, 'description': ['On C(present) creates the device when it does not exist.', 'On C(absent) removes the device when it exists.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "url": "{'aliases': ['oneclick_url'], 'required': True, 'description': ['HTTP, HTTPS URL of the Oneclick server in the form (http|https)://host.domain[:port]']}",
    "url_password": "{'aliases': ['oneclick_password'], 'required': True, 'description': ['Oneclick user password.']}",
    "url_username": "{'aliases': ['oneclick_user'], 'required': True, 'description': ['Oneclick user name.']}",
    "use_proxy": "{'required': False, 'description': ['if C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'default': True, 'type': 'bool'}",
    "validate_certs": "{'required': False, 'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Add device to CA Spectrum
  local_action:
    module: spectrum_device
    device: '{{ ansible_host }}'
    community: secret
    landscape: '0x100000'
    oneclick_url: http://oneclick.example.com:8080
    oneclick_user: username
    oneclick_password: password
    state: present


- name: Remove device from CA Spectrum
  local_action:
    module: spectrum_device
    device: '{{ ansible_host }}'
    landscape: '{{ landscape_handle }}'
    oneclick_url: http://oneclick.example.com:8080
    oneclick_user: username
    oneclick_password: password
    use_proxy: no
    state: absent

```

## License

TODO

## Author Information
  - ['Renato Orgito (@orgito)']
