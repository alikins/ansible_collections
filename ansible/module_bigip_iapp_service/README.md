# Ansible module: ansible.module_bigip_iapp_service


Manages TCL iApp services on a BIG-IP

## Description

Manages TCL iApp services on a BIG-IP.
If you are looking for the API that is communicated with on the BIG-IP, the one the is used is C(/mgmt/tm/sys/application/service/).

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['Description of the iApp service.', 'If this option is specified in the Ansible task, it will take precedence over any similar setting in the iApp Service payload that you provide in the C(parameters) field.'], 'version_added': 2.7}",
    "device_group": "{'description': ['The device group for the iApp service.', 'If this option is specified in the Ansible task, it will take precedence over any similar setting in the iApp Service payload that you provide in the C(parameters) field.'], 'version_added': 2.7}",
    "force": "{'description': ['Forces the updating of an iApp service even if the parameters to the service have not changed. This option is of particular importance if the iApp template that underlies the service has been updated in-place. This option is equivalent to re-configuring the iApp if that template has changed.'], 'default': False, 'type': 'bool'}",
    "metadata": "{'description': ['Metadata associated with the iApp service.', 'If this option is specified in the Ansible task, it will take precedence over any similar setting in the iApp Service payload that you provide in the C(parameters) field.'], 'version_added': 2.7}",
    "name": "{'description': ['The name of the iApp service that you want to deploy.'], 'required': True}",
    "parameters": "{'description': ['A hash of all the required template variables for the iApp template. If your parameters are stored in a file (the more common scenario) it is recommended you use either the C(file) or C(template) lookups to supply the expected parameters.', 'These parameters typically consist of the C(lists), C(tables), and C(variables) fields.']}",
    "partition": "{'description': ['Device partition to manage resources on.'], 'default': 'Common', 'version_added': 2.5}",
    "password": "{'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}",
    "provider": "{'description': ['A dict object containing connection details.'], 'default': None, 'version_added': 2.5, 'suboptions': {'password': {'description': ['The password for the user account used to connect to the BIG-IP.', 'You may omit this option by setting the environment variable C(F5_PASSWORD).'], 'required': True, 'aliases': ['pass', 'pwd']}, 'server': {'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}, 'server_port': {'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443}, 'user': {'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}, 'validate_certs': {'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool'}, 'timeout': {'description': ['Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands.  If the timeout is exceeded before the operation is completed, the module will error.'], 'default': 10}, 'ssh_keyfile': {'description': ['Specifies the SSH keyfile to use to authenticate the connection to the remote device.  This argument is only used for I(cli) transports.', 'You may omit this option by setting the environment variable C(ANSIBLE_NET_SSH_KEYFILE).']}, 'transport': {'description': ['Configures the transport connection to use when connecting to the remote device.'], 'required': True, 'choices': ['rest', 'cli'], 'default': 'cli'}}}",
    "server": "{'description': ['The BIG-IP host.', 'You may omit this option by setting the environment variable C(F5_SERVER).'], 'required': True}",
    "server_port": "{'description': ['The BIG-IP server port.', 'You may omit this option by setting the environment variable C(F5_SERVER_PORT).'], 'default': 443, 'version_added': 2.2}",
    "state": "{'description': ['When C(present), ensures that the iApp service is created and running. When C(absent), ensures that the iApp service has been removed.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "strict_updates": "{'description': ['Indicates whether the application service is tied to the template, so when the template is updated, the application service changes to reflect the updates.', 'When C(yes), disallows any updates to the resources that the iApp service has created, if they are not updated directly through the iApp.', 'When C(no), allows updates outside of the iApp.', 'If this option is specified in the Ansible task, it will take precedence over any similar setting in the iApp Service payload that you provide in the C(parameters) field.'], 'default': True, 'type': 'bool', 'version_added': 2.5}",
    "template": "{'description': ['The iApp template from which to instantiate a new service. This template must exist on your BIG-IP before you can successfully create a service.', 'When creating a new service, this parameter is required.']}",
    "traffic_group": "{'description': ['The traffic group for the iApp service. When creating a new service, if this value is not specified, the default of C(/Common/traffic-group-1) will be used.', 'If this option is specified in the Ansible task, it will take precedence over any similar setting in the iApp Service payload that you provide in the C(parameters) field.'], 'version_added': 2.5}",
    "user": "{'description': ['The username to connect to the BIG-IP with. This user must have administrative privileges on the device.', 'You may omit this option by setting the environment variable C(F5_USER).'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.', 'You may omit this option by setting the environment variable C(F5_VALIDATE_CERTS).'], 'default': True, 'type': 'bool', 'version_added': 2.0}",
}
```

## Examples


``` yaml

- name: Create HTTP iApp service from iApp template
  bigip_iapp_service:
    name: foo-service
    template: f5.http
    parameters: "{{ lookup('file', 'f5.http.parameters.json') }}"
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

- name: Upgrade foo-service to v1.2.0rc4 of the f5.http template
  bigip_iapp_service:
    name: foo-service
    template: f5.http.v1.2.0rc4
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

- name: Configure a service using parameters in YAML
  bigip_iapp_service:
    name: tests
    template: web_frontends
    password: admin
    server: "{{ inventory_hostname }}"
    server_port: "{{ bigip_port }}"
    validate_certs: "{{ validate_certs }}"
    state: present
    user: admin
    parameters:
      variables:
        - name: var__vs_address
          value: 1.1.1.1
        - name: pm__apache_servers_for_http
          value: 2.2.2.1:80
        - name: pm__apache_servers_for_https
          value: 2.2.2.2:80
  delegate_to: localhost

- name: Re-configure a service whose underlying iApp was updated in place
  bigip_iapp_service:
    name: tests
    template: web_frontends
    password: admin
    force: yes
    server: "{{ inventory_hostname }}"
    server_port: "{{ bigip_port }}"
    validate_certs: "{{ validate_certs }}"
    state: present
    user: admin
    parameters:
      variables:
        - name: var__vs_address
          value: 1.1.1.1
        - name: pm__apache_servers_for_http
          value: 2.2.2.1:80
        - name: pm__apache_servers_for_https
          value: 2.2.2.2:80
  delegate_to: localhost

- name: Try to remove the iApp template before the associated Service is removed
  bigip_iapp_template:
    name: web_frontends
    state: absent
  register: result
  failed_when:
    - result is not success
    - "'referenced by one or more applications' not in result.msg"

- name: Configure a service using more complicated parameters
  bigip_iapp_service:
    name: tests
    template: web_frontends
    password: admin
    server: "{{ inventory_hostname }}"
    server_port: "{{ bigip_port }}"
    validate_certs: "{{ validate_certs }}"
    state: present
    user: admin
    parameters:
      variables:
        - name: var__vs_address
          value: 1.1.1.1
        - name: pm__apache_servers_for_http
          value: 2.2.2.1:80
        - name: pm__apache_servers_for_https
          value: 2.2.2.2:80
      lists:
        - name: irules__irules
          value:
            - foo
            - bar
      tables:
        - name: basic__snatpool_members
        - name: net__snatpool_members
        - name: optimizations__hosts
        - name: pool__hosts
          columnNames:
            - name
          rows:
            - row:
                - internal.company.bar
        - name: pool__members
          columnNames:
            - addr
            - port
            - connection_limit
          rows:
            - row:
                - "none"
                - 80
                - 0
        - name: server_pools__servers
  delegate_to: localhost

- name: Override metadata that may or may not exist in parameters
  bigip_iapp_service:
    name: foo-service
    template: f5.http
    parameters: "{{ lookup('file', 'f5.http.parameters.json') }}"
    metadata:
      - persist: yes
        name: data 1
      - persist: yes
        name: data 2
    password: secret
    server: lb.mydomain.com
    state: present
    user: admin
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Tim Rupp (@caphrim007)']
