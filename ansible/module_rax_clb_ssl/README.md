# Ansible module: ansible.module_rax_clb_ssl


Manage SSL termination for a Rackspace Cloud Load Balancer

## Description

Set up, reconfigure, or remove SSL termination for an existing load balancer.

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Rackspace API key, overrides I(credentials).'], 'aliases': ['password']}",
    "auth_endpoint": "{'description': ['The URI of the authentication service.'], 'default': 'https://identity.api.rackspacecloud.com/v2.0/', 'version_added': 1.5}",
    "certificate": "{'description': ['The public SSL certificates as a string in PEM format.']}",
    "credentials": "{'description': ['File to find the Rackspace credentials in. Ignored if I(api_key) and I(username) are provided.'], 'aliases': ['creds_file']}",
    "enabled": "{'description': ['If set to "false", temporarily disable SSL termination without discarding', 'existing credentials.'], 'default': True}",
    "env": "{'description': ['Environment as configured in I(~/.pyrax.cfg), see U(https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration).'], 'version_added': 1.5}",
    "https_redirect": "{'description': ['If "true", the load balancer will redirect HTTP traffic to HTTPS.', 'Requires "secure_traffic_only" to be true. Incurs an implicit wait if SSL', 'termination is also applied or removed.']}",
    "identity_type": "{'description': ['Authentication mechanism to use, such as rackspace or keystone.'], 'default': 'rackspace', 'version_added': 1.5}",
    "intermediate_certificate": "{'description': ['One or more intermediate certificate authorities as a string in PEM', 'format, concatenated into a single string.']}",
    "loadbalancer": "{'description': ['Name or ID of the load balancer on which to manage SSL termination.'], 'required': True}",
    "private_key": "{'description': ['The private SSL key as a string in PEM format.']}",
    "region": "{'description': ['Region to create an instance in.'], 'default': 'DFW'}",
    "secure_port": "{'description': ['The port to listen for secure traffic.'], 'default': 443}",
    "secure_traffic_only": "{'description': ['If "true", the load balancer will *only* accept secure traffic.'], 'default': False}",
    "state": "{'description': ['If set to "present", SSL termination will be added to this load balancer.', 'If "absent", SSL termination will be removed instead.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "tenant_id": "{'description': ['The tenant ID used for authentication.'], 'version_added': 1.5}",
    "tenant_name": "{'description': ['The tenant name used for authentication.'], 'version_added': 1.5}",
    "username": "{'description': ['Rackspace username, overrides I(credentials).']}",
    "verify_ssl": "{'description': ['Whether or not to require SSL validation of API endpoints.'], 'version_added': 1.5}",
    "wait": "{'description': ['Wait for the balancer to be in state "running" before turning.'], 'default': False}",
    "wait_timeout": "{'description': ['How long before "wait" gives up, in seconds.'], 'default': 300}",
}
```

## Examples


``` yaml

- name: Enable SSL termination on a load balancer
  rax_clb_ssl:
    loadbalancer: the_loadbalancer
    state: present
    private_key: "{{ lookup('file', 'credentials/server.key' ) }}"
    certificate: "{{ lookup('file', 'credentials/server.crt' ) }}"
    intermediate_certificate: "{{ lookup('file', 'credentials/trust-chain.crt') }}"
    secure_traffic_only: true
    wait: true

- name: Disable SSL termination
  rax_clb_ssl:
    loadbalancer: "{{ registered_lb.balancer.id }}"
    state: absent
    wait: true

```

## License

TODO

## Author Information
  - ['Ash Wilson (@smashwilson)']
