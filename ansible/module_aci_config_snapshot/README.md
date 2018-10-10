# Ansible module: ansible.module_aci_config_snapshot


Manage Config Snapshots (config:Snapshot, config:ExportP)

## Description

Manage Config Snapshots on Cisco ACI fabrics.
Creating new Snapshots is done using the configExportP class.
Removing Snapshots is done using the configSnapshot class.

## Requirements

TODO

## Arguments

``` json
{
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "description": "{'description': ['The description for the Config Export Policy.'], 'aliases': ['descr']}",
    "export_policy": "{'description': ['The name of the Export Policy to use for Config Snapshots.'], 'aliases': ['name']}",
    "format": "{'description': ['Sets the config backup to be formatted in JSON or XML.', 'The APIC defaults to C(json) when unset.'], 'choices': ['json', 'xml']}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "include_secure": "{'description': ['Determines if secure information should be included in the backup.', 'The APIC defaults to C(yes) when unset.'], 'type': 'bool'}",
    "max_count": "{'description': ['Determines how many snapshots can exist for the Export Policy before the APIC starts to rollover.', 'Accepted values range between C(1) and C(10).', 'The APIC defaults to C(3) when unset.'], 'type': 'int'}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "snapshot": "{'description': ['The name of the snapshot to delete.']}",
    "state": "{'description': ['Use C(present) or C(absent) for adding or removing.', 'Use C(query) for listing an object or multiple objects.'], 'choices': ['absent', 'present', 'query'], 'default': 'present'}",
    "timeout": "{'description': ['The socket level timeout in seconds.'], 'type': 'int', 'default': 30}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['The username to use for authentication.'], 'default': 'admin', 'aliases': ['user']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only set to C(no) when used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Create a Snapshot
  aci_config_snapshot:
    host: apic
    username: admin
    password: SomeSecretPassword
    state: present
    export_policy: config_backup
    max_count: 10
    description: Backups taken before new configs are applied.
  delegate_to: localhost

- name: Query all Snapshots
  aci_config_snapshot:
    host: apic
    username: admin
    password: SomeSecretPassword
    state: query
  delegate_to: localhost
  register: query_result

- name: Query Snapshots associated with a particular Export Policy
  aci_config_snapshot:
    host: apic
    username: admin
    password: SomeSecretPassword
    export_policy: config_backup
    state: query
  delegate_to: localhost
  register: query_result

- name: Delete a Snapshot
  aci_config_snapshot:
    host: apic
    username: admin
    password: SomeSecretPassword
    export_policy: config_backup
    snapshot: run-2017-08-24T17-20-05
    state: absent
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Jacob McGill (@jmcgill298)']
