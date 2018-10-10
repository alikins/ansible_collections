# Ansible module: ansible.module_na_ontap_dns


NetApp ONTAP Create, delete, modify DNS servers

## Description

Create, delete, modify DNS servers.

## Requirements

TODO

## Arguments

``` json
{
    "domains": "{'description': ["List of DNS domains such as 'sales.bar.com'. The first domain is the one that the Vserver belongs to."]}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "nameservers": "{'description': ["List of IPv4 addresses of name servers such as '123.123.123.123'."]}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "state": "{'description': ['Whether the DNS servers should be enabled for the given vserver.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "vserver": "{'description': ['The name of the vserver to use.'], 'required': True}",
}
```

## Examples


``` yaml

    - name: create DNS
      na_ontap_dns:
        state: present
        hostname: "{{hostname}}"
        username: "{{username}}"
        password: "{{password}}"
        vserver:  "{{vservername}}"
        domains: sales.bar.com
        nameservers: 10.193.0.250,10.192.0.250

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
