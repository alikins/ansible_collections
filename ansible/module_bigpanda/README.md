# Ansible module: ansible.module_bigpanda


Notify BigPanda about deployments

## Description

Notify BigPanda when deployments start and end (successfully or not). Returns a deployment object containing all the parameters for future module calls.

## Requirements

TODO

## Arguments

``` json
{
    "component": "{'description': ['The name of the component being deployed. Ex: billing'], 'required': True, 'aliases': ['name']}",
    "description": "{'description': ['Free text description of the deployment.'], 'required': False}",
    "env": "{'description': ["The environment name, typically 'production', 'staging', etc."], 'required': False}",
    "hosts": "{'description': ['Name of affected host name. Can be a list.'], 'required': False, 'default': "machine's hostname", 'aliases': ['host']}",
    "owner": "{'description': ['The person responsible for the deployment.'], 'required': False}",
    "state": "{'description': ['State of the deployment.'], 'required': True, 'choices': ['started', 'finished', 'failed']}",
    "token": "{'description': ['API token.'], 'required': True}",
    "url": "{'description': ['Base URL of the API server.'], 'required': False, 'default': 'https://api.bigpanda.io'}",
    "validate_certs": "{'description': ['If C(no), SSL certificates for the target url will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'required': False, 'default': True, 'type': 'bool'}",
    "version": "{'description': ['The deployment version.'], 'required': True}",
}
```

## Examples


``` yaml

- bigpanda:
    component: myapp
    version: '1.3'
    token: '{{ bigpanda_token }}'
    state: started

- bigpanda:
    component: myapp
    version: '1.3'
    token: '{{ bigpanda_token }}'
    state: finished

# If outside servers aren't reachable from your machine, use delegate_to and override hosts:
- bigpanda:
    component: myapp
    version: '1.3'
    token: '{{ bigpanda_token }}'
    hosts: '{{ ansible_hostname }}'
    state: started
  delegate_to: localhost
  register: deployment

- bigpanda:
    component: '{{ deployment.component }}'
    version: '{{ deployment.version }}'
    token: '{{ deployment.token }}'
    state: finished
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Hagai Kariti (@hkariti)']
