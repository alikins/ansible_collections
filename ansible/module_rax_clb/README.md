# Ansible module: ansible.module_rax_clb


create / delete a load balancer in Rackspace Public Cloud

## Description

creates / deletes a Rackspace Public Cloud load balancer.

## Requirements

TODO

## Arguments

``` json
{
    "algorithm": "{'description': ['algorithm for the balancer being created'], 'choices': ['RANDOM', 'LEAST_CONNECTIONS', 'ROUND_ROBIN', 'WEIGHTED_LEAST_CONNECTIONS', 'WEIGHTED_ROUND_ROBIN'], 'default': 'LEAST_CONNECTIONS'}",
    "api_key": "{'description': ['Rackspace API key, overrides I(credentials).'], 'aliases': ['password']}",
    "auth_endpoint": "{'description': ['The URI of the authentication service.'], 'default': 'https://identity.api.rackspacecloud.com/v2.0/', 'version_added': 1.5}",
    "credentials": "{'description': ['File to find the Rackspace credentials in. Ignored if I(api_key) and I(username) are provided.'], 'aliases': ['creds_file']}",
    "env": "{'description': ['Environment as configured in I(~/.pyrax.cfg), see U(https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration).'], 'version_added': 1.5}",
    "identity_type": "{'description': ['Authentication mechanism to use, such as rackspace or keystone.'], 'default': 'rackspace', 'version_added': 1.5}",
    "meta": "{'description': ['A hash of metadata to associate with the instance']}",
    "name": "{'description': ['Name to give the load balancer']}",
    "port": "{'description': ['Port for the balancer being created'], 'default': 80}",
    "protocol": "{'description': ['Protocol for the balancer being created'], 'choices': ['DNS_TCP', 'DNS_UDP', 'FTP', 'HTTP', 'HTTPS', 'IMAPS', 'IMAPv4', 'LDAP', 'LDAPS', 'MYSQL', 'POP3', 'POP3S', 'SMTP', 'TCP', 'TCP_CLIENT_FIRST', 'UDP', 'UDP_STREAM', 'SFTP'], 'default': 'HTTP'}",
    "region": "{'description': ['Region to create an instance in.'], 'default': 'DFW'}",
    "state": "{'description': ['Indicate desired state of the resource'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "tenant_id": "{'description': ['The tenant ID used for authentication.'], 'version_added': 1.5}",
    "tenant_name": "{'description': ['The tenant name used for authentication.'], 'version_added': 1.5}",
    "timeout": "{'description': ['timeout for communication between the balancer and the node'], 'default': 30}",
    "type": "{'description': ['type of interface for the balancer being created'], 'choices': ['PUBLIC', 'SERVICENET'], 'default': 'PUBLIC'}",
    "username": "{'description': ['Rackspace username, overrides I(credentials).']}",
    "verify_ssl": "{'description': ['Whether or not to require SSL validation of API endpoints.'], 'version_added': 1.5}",
    "vip_id": "{'description': ['Virtual IP ID to use when creating the load balancer for purposes of sharing an IP with another load balancer of another protocol'], 'version_added': 1.5}",
    "wait": "{'description': ["wait for the balancer to be in state 'running' before returning"], 'type': 'bool', 'default': False}",
    "wait_timeout": "{'description': ['how long before wait gives up, in seconds'], 'default': 300}",
}
```

## Examples


``` yaml

- name: Build a Load Balancer
  gather_facts: False
  hosts: local
  connection: local
  tasks:
    - name: Load Balancer create request
      local_action:
        module: rax_clb
        credentials: ~/.raxpub
        name: my-lb
        port: 8080
        protocol: HTTP
        type: SERVICENET
        timeout: 30
        region: DFW
        wait: yes
        state: present
        meta:
          app: my-cool-app
      register: my_lb

```

## License

TODO

## Author Information
  - ['Christopher H. Laco (@claco)', 'Matt Martz (@sivel)']
  - ['Christopher H. Laco (@claco)', 'Matt Martz (@sivel)']
