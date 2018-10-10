# Ansible module: ansible.module_na_ontap_interface


NetApp ONTAP LIF configuration

## Description

Creating / deleting and modifying the LIF.

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'description': ["Specifies the LIF's IP address.", 'Required when C(state=present)']}",
    "admin_status": "{'choices': ['up', 'down'], 'description': ['Specifies the administrative status of the LIF.']}",
    "failover_policy": "{'description': ['Specifies the failover policy for the LIF.']}",
    "firewall_policy": "{'description': ['Specifies the firewall policy for the LIF.']}",
    "home_node": "{'description': ["Specifies the LIF's home node.", 'Required when C(state=present).']}",
    "home_port": "{'description': ["Specifies the LIF's home port.", 'Required when C(state=present)']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "interface_name": "{'description': ['Specifies the logical interface (LIF) name.'], 'required': True}",
    "is_auto_revert": "{'description': ['If true, data LIF will revert to its home node under certain circumstances such as startup, and load balancing migration capability is disabled automatically']}",
    "netmask": "{'description': ["Specifies the LIF's netmask.", 'Required when C(state=present).']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "protocols": "{'description': ["Specifies the list of data protocols configured on the LIF. By default, the values in this element are nfs, cifs and fcache. Other supported protocols are iscsi and fcp. A LIF can be configured to not support any data protocols by specifying 'none'. Protocol values of none, iscsi or fcp can't be combined with any other data protocol(s)."]}",
    "role": "{'description': ['Specifies the role of the LIF.', 'Required when C(state=present).']}",
    "state": "{'description': ['Whether the specified interface should exist or not.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "vserver": "{'description': ['The name of the vserver to use.'], 'required': True}",
}
```

## Examples


``` yaml

    - name: Create interface
      na_ontap_interface:
        state: present
        interface_name: data2
        home_port: e0d
        home_node: laurentn-vsim1
        role: data
        protocols: nfs
        admin_status: up
        failover_policy: local-only
        firewall_policy: mgmt
        is_auto_revert: true
        address: 10.10.10.10
        netmask: 255.255.255.0
        vserver: svm1
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"

    - name: Delete interface
      na_ontap_interface:
        state: absent
        interface_name: data2
        vserver: svm1
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"


```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
