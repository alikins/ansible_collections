# Ansible module: ansible.module_cloudscale_server


Manages servers on the cloudscale.ch IaaS service

## Description

Create, start, stop and delete servers on the cloudscale.ch IaaS service.
All operations are performed using the cloudscale.ch public API v1.
For details consult the full API documentation: U(https://www.cloudscale.ch/en/api/v1).
A valid API token is required for all operations. You can create as many tokens as you like using the cloudscale.ch control panel at U(https://control.cloudscale.ch).

## Requirements

TODO

## Arguments

``` json
{
    "anti_affinity_with": "{'description': ['UUID of another server to create an anti-affinity group with.']}",
    "api_timeout": "{'description': ['Timeout in seconds for calls to the cloudscale.ch API.'], 'default': 30, 'version_added': '2.5'}",
    "api_token": "{'description': ['cloudscale.ch API token.', 'This can also be passed in the CLOUDSCALE_API_TOKEN environment variable.']}",
    "bulk_volume_size_gb": "{'description': ['Size of the bulk storage volume in GB.', 'No bulk storage volume if not set.']}",
    "flavor": "{'description': ['Flavor of the server.']}",
    "image": "{'description': ['Image used to create the server.']}",
    "name": "{'description': ['Name of the Server.', 'Either C(name) or C(uuid) are required. These options are mutually exclusive.']}",
    "ssh_keys": "{'description': ['List of SSH public keys.', 'Use the full content of your .pub file here.']}",
    "state": "{'description': ['State of the server'], 'default': 'running', 'choices': ['running', 'stopped', 'absent']}",
    "use_ipv6": "{'description': ['Enable IPv6 on the public network interface.'], 'default': True}",
    "use_private_network": "{'description': ['Attach a private network interface to the server.'], 'default': False}",
    "use_public_network": "{'description': ['Attach a public network interface to the server.'], 'default': True}",
    "user_data": "{'description': ['Cloud-init configuration (cloud-config) data to use for the server.']}",
    "uuid": "{'description': ['UUID of the server.', 'Either C(name) or C(uuid) are required. These options are mutually exclusive.']}",
    "volume_size_gb": "{'description': ['Size of the root volume in GB.'], 'default': 10}",
}
```

## Examples


``` yaml

# Start a server (if it does not exist) and register the server details

- name: Start cloudscale.ch server
  cloudscale_server:
    name: my-shiny-cloudscale-server
    image: debian-8
    flavor: flex-4
    ssh_keys: ssh-rsa XXXXXXXXXX...XXXX ansible@cloudscale
    use_private_network: True
    bulk_volume_size_gb: 100
    api_token: xxxxxx
  register: server1

# Start another server in anti-affinity to the first one
- name: Start second cloudscale.ch server
  cloudscale_server:
    name: my-other-shiny-server
    image: ubuntu-16.04
    flavor: flex-8
    ssh_keys: ssh-rsa XXXXXXXXXXX ansible@cloudscale
    anti_affinity_with: '{{ server1.uuid }}'
    api_token: xxxxxx

# Stop the first server
- name: Stop my first server
  cloudscale_server:
    uuid: '{{ server1.uuid }}'
    state: stopped
    api_token: xxxxxx

# Delete my second server
- name: Delete my second server
  cloudscale_server:
    name: my-other-shiny-server
    state: absent
    api_token: xxxxxx

# Start a server and wait for the SSH host keys to be generated
- name: Start server and wait for SSH host keys
  cloudscale_server:
    name: my-cloudscale-server-with-ssh-key
    image: debian-8
    flavor: flex-4
    ssh_keys: ssh-rsa XXXXXXXXXXX ansible@cloudscale
    api_token: xxxxxx
  register: server
  until: server.ssh_fingerprints
  retries: 60
  delay: 2

```

## License

TODO

## Author Information
  - ['Gaudenz Steinlin (@gaudenz) <gaudenz.steinlin@cloudscale.ch>']
