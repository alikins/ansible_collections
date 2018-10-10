# Ansible module: ansible.module_na_ontap_command


NetApp ONTAP Run any cli command

## Description

Run system-cli commands on ONTAP

## Requirements

TODO

## Arguments

``` json
{
    "command": "{'description': ['a comma separated list containing the command and arguments.']}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

    - name: run ontap cli command
      na_ontap_command:
        hostname: "{{ hostname }} "
        username: "{{ admin username }}"
        password: "{{ admin password }}"
        command: ['version']

    - name: run ontap cli command
      na_ontap_command:
        hostname: "{{ hostname }} "
        username: "{{ admin username }}"
        password: "{{ admin password }}"
        command: ['network', 'interface', 'show']

```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
