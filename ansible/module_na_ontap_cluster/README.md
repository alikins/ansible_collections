# Ansible module: ansible.module_na_ontap_cluster


NetApp ONTAP cluster - create, join, add license

## Description

Create or join or apply licenses to ONTAP clusters

## Requirements

TODO

## Arguments

``` json
{
    "cluster_ip_address": "{'description': ['IP address of cluster to be joined']}",
    "cluster_name": "{'description': ['The name of the cluster to manage.']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "license_code": "{'description': ['License code to be applied to the cluster']}",
    "license_package": "{'description': ['License package name of the license to be removed']}",
    "node_serial_number": "{'description': ['Serial number of the cluster node']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "state": "{'description': ['Whether the specified cluster should exist or not.'], 'choices': ['present'], 'default': 'present'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

    - name: Create cluster
      na_ontap_cluster:
        state: present
        cluster_name: new_cluster
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"
    - name: Add license from cluster
      na_ontap_cluster:
        state: present
        cluster_name: FPaaS-A300-01
        license_code: SGHLQDBBVAAAAAAAAAAAAAAAAAAA
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"
    - name: Join cluster
      na_ontap_cluster:
        state: present
        cluster_name: FPaaS-A300
        cluster_ip_address: 10.61.184.181
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
