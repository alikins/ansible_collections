# Ansible module: ansible.module_rax_dns_record


Manage DNS records on Rackspace Cloud DNS

## Description

Manage DNS records on Rackspace Cloud DNS

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Rackspace API key, overrides I(credentials).'], 'aliases': ['password']}",
    "auth_endpoint": "{'description': ['The URI of the authentication service.'], 'default': 'https://identity.api.rackspacecloud.com/v2.0/', 'version_added': 1.5}",
    "comment": "{'description': ['Brief description of the domain. Maximum length of 160 characters']}",
    "credentials": "{'description': ['File to find the Rackspace credentials in. Ignored if I(api_key) and I(username) are provided.'], 'aliases': ['creds_file']}",
    "data": "{'description': ['IP address for A/AAAA record, FQDN for CNAME/MX/NS, or text data for SRV/TXT'], 'required': True}",
    "domain": "{'description': ['Domain name to create the record in. This is an invalid option when type=PTR']}",
    "env": "{'description': ['Environment as configured in I(~/.pyrax.cfg), see U(https://github.com/rackspace/pyrax/blob/master/docs/getting_started.md#pyrax-configuration).'], 'version_added': 1.5}",
    "identity_type": "{'description': ['Authentication mechanism to use, such as rackspace or keystone.'], 'default': 'rackspace', 'version_added': 1.5}",
    "loadbalancer": "{'description': ['Load Balancer ID to create a PTR record for. Only used with type=PTR'], 'version_added': 1.7}",
    "name": "{'description': ['FQDN record name to create'], 'required': True}",
    "overwrite": "{'description': ["Add new records if data doesn't match, instead of updating existing record with matching name. If there are already multiple records with matching name and overwrite=true, this module will fail."], 'default': True, 'version_added': 2.1}",
    "priority": "{'description': ['Required for MX and SRV records, but forbidden for other record types. If specified, must be an integer from 0 to 65535.']}",
    "region": "{'description': ['Region to create an instance in.'], 'default': 'DFW'}",
    "server": "{'description': ['Server ID to create a PTR record for. Only used with type=PTR'], 'version_added': 1.7}",
    "state": "{'description': ['Indicate desired state of the resource'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "tenant_id": "{'description': ['The tenant ID used for authentication.'], 'version_added': 1.5}",
    "tenant_name": "{'description': ['The tenant name used for authentication.'], 'version_added': 1.5}",
    "ttl": "{'description': ['Time to live of record in seconds'], 'default': 3600}",
    "type": "{'description': ['DNS record type'], 'choices': ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'SRV', 'TXT', 'PTR'], 'required': True}",
    "username": "{'description': ['Rackspace username, overrides I(credentials).']}",
    "verify_ssl": "{'description': ['Whether or not to require SSL validation of API endpoints.'], 'version_added': 1.5}",
}
```

## Examples


``` yaml

- name: Create DNS Records
  hosts: all
  gather_facts: False
  tasks:
    - name: Create A record
      local_action:
        module: rax_dns_record
        credentials: ~/.raxpub
        domain: example.org
        name: www.example.org
        data: "{{ rax_accessipv4 }}"
        type: A
      register: a_record

    - name: Create PTR record
      local_action:
        module: rax_dns_record
        credentials: ~/.raxpub
        server: "{{ rax_id }}"
        name: "{{ inventory_hostname }}"
        region: DFW
      register: ptr_record

```

## License

TODO

## Author Information
  - ['Matt Martz (@sivel)']
