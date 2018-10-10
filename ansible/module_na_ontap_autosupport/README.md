# Ansible module: ansible.module_na_ontap_autosupport


NetApp ONTAP manage Autosupport

## Description

Enable/Disable Autosupport

## Requirements

TODO

## Arguments

``` json
{
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "mail_hosts": "{'description': ['List of mail server(s) used to deliver AutoSupport messages via SMTP.', 'Both host names and IP addresses may be used as valid input.']}",
    "node_name": "{'description': ['The name fo the filer that owns the AutoSupport Configuration.'], 'required': True}",
    "noteto": "{'description': ['Specifies up to five recipients of full AutoSupport e-mail messages.']}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "post_url": "{'description': ['The URL used to deliver AutoSupport messages via HTTP POST']}",
    "state": "{'description': ['Specifies whether the AutoSupport daemon is present or absent.', 'When this setting is absent, delivery of all AutoSupport messages is turned off.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "support": "{'description': ['Specifies whether AutoSupport notification to technical support is enabled.'], 'type': 'bool'}",
    "transport": "{'description': ['The name of the transport protocol used to deliver AutoSupport messages'], 'choices': ['http', 'https', 'smtp']}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

   - name: Enable autosupport
     na_ontap_autosupport:
       hostname: "{{ hostname }}"
       username: "{{ username }}"
       password: "{{ password }}"
       state: present
       node_name: test
       transport: https
       noteto: abc@def.com,def@ghi.com
       mail_hosts: 1.2.3.4,5.6.7.8
       support: False
       post_url: url/1.0/post

   - name: Disable autosupport
     na_ontap_autosupport:
       hostname: "{{ hostname }}"
       username: "{{ username }}"
       password: "{{ password }}"
       state: absent
       node_name: test


```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
