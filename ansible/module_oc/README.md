# Ansible module: ansible.module_oc


Manage OpenShift Resources

## Description

This module allows management of resources in an OpenShift cluster. The inventory host can be any host with network connectivity to the OpenShift cluster; the default port being 8443/TCP.
This module relies on a token to authenticate to OpenShift. This can either be a user or a service account.

## Requirements

TODO

## Arguments

``` json
{
    "host": "{'description': ['Hostname or address of the OpenShift API endpoint. By default, this is expected to be the current inventory host.'], 'required': False, 'default': '127.0.0.1'}",
    "inline": "{'description': ['The inline definition of the resource. This is mutually exclusive with name, namespace and kind.'], 'required': False, 'aliases': ['def', 'definition']}",
    "kind": "{'description': ['The kind of the resource upon which to take action.'], 'required': True}",
    "name": "{'description': ['The name of the resource on which to take action.'], 'required': False}",
    "namespace": "{'description': ['The namespace of the resource upon which to take action.'], 'required': False}",
    "port": "{'description': ['The port number of the API endpoint.'], 'required': False, 'default': 8443}",
    "state": "{'choices': ['present', 'absent'], 'description': ["If the state is present, and the resource doesn't exist, it shall be created using the inline definition. If the state is present and the resource exists, the definition will be updated, again using an inline definition. If the state is absent, the resource will be deleted if it exists."], 'required': True}",
    "token": "{'description': ['The token with which to authenticate against the OpenShift cluster.'], 'required': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates for the target url will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Create project
  oc:
    state: present
    inline:
      kind: ProjectRequest
      metadata:
        name: ansibletestproject
      displayName: Ansible Test Project
      description: This project was created using Ansible
    token: << redacted >>

- name: Delete a service
  oc:
    state: absent
    name: myservice
    namespace: mynamespace
    kind: Service
    token: << redacted >>

- name: Add project role Admin to a user
  oc:
    state: present
    inline:
      kind: RoleBinding
      metadata:
        name: admin
        namespace: mynamespace
      roleRef:
        name: admin
      userNames:
        - "myuser"
      token: << redacted >>

- name: Obtain an object definition
  oc:
   state: present
   name: myroute
   namespace: mynamespace
   kind: Route
   token: << redacted >>

```

## License

TODO

## Author Information
  - ['Kenneth D. Evensen (@kevensen)']
