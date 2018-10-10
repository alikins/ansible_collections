# Ansible module: ansible.module_netscaler_nitro_request


Issue Nitro API requests to a Netscaler instance

## Description

Issue Nitro API requests to a Netscaler instance.
This is intended to be a short hand for using the uri Ansible module to issue the raw HTTP requests directly.
It provides consistent return values and has no other dependencies apart from the base Ansible runtime environment.
This module is intended to run either on the Ansible control node or a bastion (jumpserver) with access to the actual Netscaler instance

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['The action to perform when the I(operation) value is set to C(action).', 'Some common values for this parameter are C(enable), C(disable), C(rename).']}",
    "args": "{'description': ['A dictionary which defines the key arguments by which we will select the Nitro object to operate on.', "It is required for the following I(operation) values: C(get_by_args), C('delete_by_args')."]}",
    "attributes": "{'description': ['The attributes of the Nitro object we are operating on.', 'It is required for the following I(operation) values: C(add), C(update), C(action).']}",
    "expected_nitro_errorcode": "{'description': ['A list of numeric values that signify that the operation was successful.'], 'default': [0], 'required': True}",
    "filter": "{'description': ['A dictionary which defines the filter with which to refine the Nitro objects returned by the C(get_filtered) I(operation).']}",
    "instance_id": "{'description': ['The id of the target Netscaler instance when issuing a Nitro request through a MAS proxy.']}",
    "instance_ip": "{'description': ['The IP address of the target Netscaler instance when issuing a Nitro request through a MAS proxy.']}",
    "instance_name": "{'description': ['The name of the target Netscaler instance when issuing a Nitro request through a MAS proxy.']}",
    "name": "{'description': ['The name of the resource we are operating on.', 'It is required for the following I(operation) values: C(update), C(get), C(delete).']}",
    "nitro_auth_token": "{'description': ['The authentication token provided by the C(mas_login) operation. It is required when issuing Nitro API calls through a MAS proxy.']}",
    "nitro_pass": "{'description': ['The password with which to authenticate to the Netscaler node.'], 'required': True}",
    "nitro_protocol": "{'choices': ['http', 'https'], 'default': 'http', 'description': ['Which protocol to use when accessing the Nitro API objects.']}",
    "nitro_user": "{'description': ['The username with which to authenticate to the Netscaler node.'], 'required': True}",
    "nsip": "{'description': ['The IP address of the Netscaler or MAS instance where the Nitro API calls will be made.', 'The port can be specified with the colon C(:). E.g. C(192.168.1.1:555).']}",
    "operation": "{'description': ['Define the Nitro operation that we want to perform.'], 'choices': ['add', 'update', 'get', 'get_by_args', 'get_filtered', 'get_all', 'delete', 'delete_by_args', 'count', 'mas_login', 'save_config', 'action']}",
    "resource": "{'description': ['The type of resource we are operating on.', 'It is required for all I(operation) values except C(mas_login) and C(save_config).']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'default': 'yes'}",
}
```

## Examples


``` yaml

- name: Add a server
  delegate_to: localhost
  netscaler_nitro_request:
    nsip: "{{ nsip }}"
    nitro_user: "{{ nitro_user }}"
    nitro_pass: "{{ nitro_pass }}"
    operation: add
    resource: server
    name: test-server-1
    attributes:
      name: test-server-1
      ipaddress: 192.168.1.1

- name: Update server
  delegate_to: localhost
  netscaler_nitro_request:
    nsip: "{{ nsip }}"
    nitro_user: "{{ nitro_user }}"
    nitro_pass: "{{ nitro_pass }}"
    operation: update
    resource: server
    name: test-server-1
    attributes:
      name: test-server-1
      ipaddress: 192.168.1.2

- name: Get server
  delegate_to: localhost
  register: result
  netscaler_nitro_request:
    nsip: "{{ nsip }}"
    nitro_user: "{{ nitro_user }}"
    nitro_pass: "{{ nitro_pass }}"
    operation: get
    resource: server
    name: test-server-1

- name: Delete server
  delegate_to: localhost
  register: result
  netscaler_nitro_request:
    nsip: "{{ nsip }}"
    nitro_user: "{{ nitro_user }}"
    nitro_pass: "{{ nitro_pass }}"
    operation: delete
    resource: server
    name: test-server-1

- name: Rename server
  delegate_to: localhost
  netscaler_nitro_request:
    nsip: "{{ nsip }}"
    nitro_user: "{{ nitro_user }}"
    nitro_pass: "{{ nitro_pass }}"
    operation: action
    action: rename
    resource: server
    attributes:
      name: test-server-1
      newname: test-server-2

- name: Get server by args
  delegate_to: localhost
  register: result
  netscaler_nitro_request:
    nsip: "{{ nsip }}"
    nitro_user: "{{ nitro_user }}"
    nitro_pass: "{{ nitro_pass }}"
    operation: get_by_args
    resource: server
    args:
      name: test-server-1

- name: Get server by filter
  delegate_to: localhost
  register: result
  netscaler_nitro_request:
    nsip: "{{ nsip }}"
    nitro_user: "{{ nitro_user }}"
    nitro_pass: "{{ nitro_pass }}"
    operation: get_filtered
    resource: server
    filter:
      ipaddress: 192.168.1.2

# Doing a NITRO request through MAS.
# Requires to have an authentication token from the mas_login and used as the nitro_auth_token parameter
# Also nsip is the MAS address and the target Netscaler IP must be defined with instance_ip
# The rest of the task arguments remain the same as when issuing the NITRO request directly to a Netscaler instance.

- name: Do mas login
  delegate_to: localhost
  register: login_result
  netscaler_nitro_request:
    nsip: "{{ mas_ip }}"
    nitro_user: "{{ nitro_user }}"
    nitro_pass: "{{ nitro_pass }}"
    operation: mas_login

- name: Add resource through MAS proxy
  delegate_to: localhost
  netscaler_nitro_request:
    nsip: "{{ mas_ip }}"
    nitro_auth_token: "{{ login_result.nitro_auth_token }}"
    instance_ip: "{{ nsip }}"
    operation: add
    resource: server
    name: test-server-1
    attributes:
      name: test-server-1
      ipaddress: 192.168.1.7

```

## License

TODO

## Author Information
  - ['George Nikolopoulos (@giorgos-nikolopoulos)']
