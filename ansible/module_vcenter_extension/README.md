# Ansible module: ansible.module_vcenter_extension


Register/deregister vCenter Extensions

## Description

This module can be used to register/deregister vCenter Extensions.

## Requirements

TODO

## Arguments

``` json
{
    "client_type": "{'description': ['Required for C(state=present). Type of client the extension is (win32, .net, linux, etc.).'], 'default': 'vsphere-client-serenity'}",
    "company": "{'description': ['Required for C(state=present). The name of the company that makes the extension.']}",
    "description": "{'description': ['Required for C(state=present). A short description of the extension.']}",
    "email": "{'description': ['Required for C(state=present). Administrator email to use for extension.']}",
    "extension_key": "{'description': ['The extension key of the extension to install or uninstall.'], 'required': True}",
    "hostname": "{'description': ['The hostname or IP address of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_HOST) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str'}",
    "name": "{'description': ['Required for C(state=present). The name of the extension you are installing.']}",
    "password": "{'description': ['The password of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PASSWORD) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['pass', 'pwd']}",
    "port": "{'description': ['The port number of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_PORT) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'int', 'default': 443, 'version_added': 2.5}",
    "server_type": "{'description': ['Required for C(state=present). Type of server being used to install the extension (SOAP, REST, HTTP, etc.).'], 'default': 'vsphere-client-serenity'}",
    "ssl_thumbprint": "{'description': ['Required for C(state=present). SSL thumbprint of the extension hosting server.']}",
    "state": "{'description': ['Add or remove vCenter Extension.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "url": "{'description': ['Required for C(state=present). Link to server hosting extension zip file to install.']}",
    "username": "{'description': ['The username of the vSphere vCenter or ESXi server.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_USER) will be used instead.', 'Environment variable supported added in version 2.6.'], 'type': 'str', 'aliases': ['admin', 'user']}",
    "validate_certs": "{'description': ['Allows connection when SSL certificates are not valid. Set to C(false) when certificates are not trusted.', 'If the value is not specified in the task, the value of environment variable C(VMWARE_VALIDATE_CERTS) will be used instead.', 'Environment variable supported added in version 2.6.', 'If set to C(yes), please make sure Python >= 2.7.9 is installed on the given machine.'], 'type': 'bool', 'default': True}",
    "version": "{'description': ['The version of the extension you are installing or uninstalling.'], 'required': True}",
    "visible": "{'description': ['Show the extension in solution manager inside vCenter.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

    - name: Register vCenter Extension
      vcenter_extension:
         hostname: "{{ groups['vcsa'][0] }}"
         username: "{{ vcenter_username }}"
         password: "{{ site_password }}"
         extension_key: "{{ extension_key }}"
         version: "1.0"
         company: "Acme"
         name: "Acme Extension"
         description: "acme management"
         email: "user@example.com"
         url: "https://10.0.0.1/ACME-vSphere-web-plugin-1.0.zip"
         ssl_thumbprint: "{{ ssl_thumbprint }}"
         state: present
      delegate_to: localhost
      register: register_extension

    - name: Deregister vCenter Extension
      vcenter_extension:
         hostname: "{{ groups['vcsa'][0] }}"
         username: "{{ vcenter_username }}"
         password: "{{ site_password }}"
         extension_key: "{{ extension_key }}"
         version: "1.0"
         state: absent
      delegate_to: localhost
      register: deregister_extension

```

## License

TODO

## Author Information
  - ['Michael Tipton (@castawayegr)']
