# Ansible module: ansible.module_nsupdate


Manage DNS records

## Description

Create, update and remove DNS records using DDNS updates
DDNS works well with both bind and Microsoft DNS (see https://technet.microsoft.com/en-us/library/cc961412.aspx)

## Requirements

TODO

## Arguments

``` json
{
    "key_algorithm": "{'description': ['Specify key algorithm used by C(key_secret).'], 'choices': ['HMAC-MD5.SIG-ALG.REG.INT', 'hmac-md5', 'hmac-sha1', 'hmac-sha224', 'hmac-sha256', 'hmac-sha384', 'hmac-sha512'], 'default': 'hmac-md5'}",
    "key_name": "{'description': ['Use TSIG key name to authenticate against DNS C(server)']}",
    "key_secret": "{'description': ['Use TSIG key secret, associated with C(key_name), to authenticate against C(server)']}",
    "port": "{'description': ['Use this TCP port when connecting to C(server).'], 'default': 53, 'version_added': 2.5}",
    "record": "{'description': ['Sets the DNS record to modify. When zone is omitted this has to be absolute (ending with a dot).'], 'required': True}",
    "server": "{'description': ['Apply DNS modification on this server.'], 'required': True}",
    "state": "{'description': ['Manage DNS record.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "ttl": "{'description': ['Sets the record TTL.'], 'default': 3600}",
    "type": "{'description': ['Sets the record type.'], 'default': 'A'}",
    "value": "{'description': ['Sets the record value.']}",
    "zone": "{'description': ['DNS record will be modified on this C(zone).', 'When omitted DNS will be queried to attempt finding the correct zone.', 'Starting with Ansible 2.7 this parameter is optional.']}",
}
```

## Examples


``` yaml

- name: Add or modify ansible.example.org A to 192.168.1.1"
  nsupdate:
    key_name: "nsupdate"
    key_secret: "+bFQtBCta7j2vWkjPkAFtgA=="
    server: "10.1.1.1"
    zone: "example.org"
    record: "ansible"
    value: "192.168.1.1"

- name: Add or modify ansible.example.org A to 192.168.1.1, 192.168.1.2 and 192.168.1.3"
  nsupdate:
    key_name: "nsupdate"
    key_secret: "+bFQtBCta7j2vWkjPkAFtgA=="
    server: "10.1.1.1"
    zone: "example.org"
    record: "ansible"
    value: ["192.168.1.1", "192.168.1.2", "192.168.1.3"]

- name: Remove puppet.example.org CNAME
  nsupdate:
    key_name: "nsupdate"
    key_secret: "+bFQtBCta7j2vWkjPkAFtgA=="
    server: "10.1.1.1"
    zone: "example.org"
    record: "puppet"
    type: "CNAME"
    state: absent

```

## License

TODO

## Author Information
  - ['Loic Blot (@nerzhul)']
