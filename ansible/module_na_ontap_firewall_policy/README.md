# Ansible module: ansible.module_na_ontap_firewall_policy


NetApp ONTAP Manage a firewall policy

## Description

Manage a firewall policy for an Ontap Cluster

## Requirements

TODO

## Arguments

``` json
{
    "allow_list": "{'description': ['A list of IPs and masks to use']}",
    "enable": "{'description': ['enabled firewall'], 'choices': ['enable', 'disable'], 'default': 'enable'}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "logging": "{'description': ['enable logging'], 'choices': ['enable', 'disable'], 'default': 'disable'}",
    "node": "{'description': ['The node to run the firewall configuration on'], 'required': True}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "policy": "{'description': ['A policy name for the firewall policy'], 'required': True}",
    "service": "{'description': ['The service to apply the policy to'], 'choices': ['http', 'https', 'ntp', 'rsh', 'snmp', 'ssh', 'telnet'], 'required': True}",
    "state": "{'description': ['Whether to set up a fire policy or not'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "vserver": "{'description': ['The Vserver to apply the policy to.'], 'required': True}",
}
```

## Examples


``` yaml

    - name: create firewall Policy
      na_ontap_firewall_policy:
        state: present
        allow_list: [1.2.3.4/24,1.3.3.4/24]
        policy: pizza
        service: http
        vserver: ci_dev
        hostname: "{{ netapp hostname }}"
        username: "{{ netapp username }}"
        password: "{{ netapp password }}"
        node: laurentn-vsim1

    - name: Modify firewall Policy
      na_ontap_firewall_policy:
        state: present
        allow_list: [1.2.3.4/24,1.3.3.4/24]
        policy: pizza
        service: http
        vserver: ci_dev
        hostname: "{{ netapp hostname }}"
        username: "{{ netapp username }}"
        password: "{{ netapp password }}"
        node: laurentn-vsim1

    - name: Destory firewall Policy
      na_ontap_firewall_policy:
        state: absent
        policy: pizza
        service: http
        vserver: ci_dev
        hostname: "{{ netapp hostname }}"
        username: "{{ netapp username }}"
        password: "{{ netapp password }}"
        node: laurentn-vsim1

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
