# Ansible module: ansible.module_omapi_host


Setup OMAPI hosts

## Description

Create, update and remove OMAPI hosts into compatible DHCPd servers.

## Requirements

TODO

## Arguments

``` json
{
    "ddns": "{'description': ['Enable dynamic DNS updates for this host.'], 'type': 'bool', 'default': False}",
    "host": "{'description': ['Sets OMAPI server host to interact with.'], 'default': 'localhost'}",
    "ip": "{'description': ['Sets the lease host IP address.']}",
    "key": "{'description': ['Sets the TSIG key content for authenticating against OMAPI server.'], 'required': True}",
    "key_name": "{'description': ['Sets the TSIG key name for authenticating against OMAPI server.'], 'required': True}",
    "macaddr": "{'description': ['Sets the lease host MAC address.'], 'required': True}",
    "name": "{'description': ['Sets the host lease hostname (mandatory if state=present).']}",
    "port": "{'description': ['Sets the OMAPI server port to interact with.'], 'default': 7911}",
    "state": "{'description': ['Create or remove OMAPI host.'], 'required': True, 'choices': ['present', 'absent']}",
    "statements": "{'description': ['Attach a list of OMAPI DHCP statements with host lease (without ending semicolon).'], 'default': []}",
}
```

## Examples


``` yaml

- name: Remove a host using OMAPI
  omapi_host:
    key_name: "defomapi"
    key: "+bFQtBCta6j2vWkjPkNFtgA=="
    host: "10.1.1.1"
    macaddr: "00:66:ab:dd:11:44"
    state: absent

- name: Add a host using OMAPI
  omapi_host:
    key_name: "defomapi"
    key: "+bFQtBCta6j2vWkjPkNFtgA=="
    host: "10.98.4.55"
    macaddr: "44:dd:ab:dd:11:44"
    name: "server01"
    ip: "192.168.88.99"
    ddns: yes
    statements:
      - 'filename "pxelinux.0"'
      - 'next-server 1.1.1.1'
    state: present

```

## License

TODO

## Author Information
  - ['Loic Blot (@nerzhul)']
