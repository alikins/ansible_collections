# Ansible module: ansible.module_aci_config_rollback


Provides rollback and rollback preview functionality (config:ImportP)

## Description

Provides rollback and rollback preview functionality for Cisco ACI fabrics.
Config Rollbacks are done using snapshots C(aci_snapshot) with the configImportP class.

## Requirements

TODO

## Arguments

``` json
{
    "certificate_name": "{'description': ['The X.509 certificate name attached to the APIC AAA user used for signature-based authentication.', 'It defaults to the C(private_key) basename, without extension.'], 'aliases': ['cert_name']}",
    "compare_export_policy": "{'description': ['The export policy that the C(compare_snapshot) is associated to.']}",
    "compare_snapshot": "{'description': ['The name of the snapshot to compare with C(snapshot).']}",
    "description": "{'description': ['The description for the Import Policy.'], 'aliases': ['descr']}",
    "export_policy": "{'description': ['The export policy that the C(snapshot) is associated to.'], 'required': True}",
    "fail_on_decrypt": "{'description': ['Determines if the APIC should fail the rollback if unable to decrypt secured data.', 'The APIC defaults to C(yes) when unset.'], 'type': 'bool'}",
    "host": "{'description': ['IP Address or hostname of APIC resolvable by Ansible control host.'], 'required': True, 'aliases': ['hostname']}",
    "import_mode": "{'description': ['Determines how the import should be handled by the APIC.', 'The APIC defaults to C(atomic) when unset.'], 'choices': ['atomic', 'best-effort']}",
    "import_policy": "{'description': ['The name of the Import Policy to use for config rollback.']}",
    "import_type": "{'description': ['Determines how the current and snapshot configuration should be compared for replacement.', 'The APIC defaults to C(replace) when unset.'], 'choices': ['merge', 'replace']}",
    "output_level": "{'description': ['Influence the output of this ACI module.', 'C(normal) means the standard output, incl. C(current) dict', 'C(info) adds informational output, incl. C(previous), C(proposed) and C(sent) dicts', 'C(debug) adds debugging output, incl. C(filter_string), C(method), C(response), C(status) and C(url) information'], 'choices': ['debug', 'info', 'normal'], 'default': 'normal'}",
    "password": "{'description': ['The password to use for authentication.', 'This option is mutual exclusive with C(private_key). If C(private_key) is provided too, it will be used instead.'], 'required': True}",
    "port": "{'description': ['Port number to be used for REST connection.', 'The default value depends on parameter `use_ssl`.']}",
    "private_key": "{'description': ['PEM formatted file that contains your private key to be used for signature-based authentication.', 'The name of the key (without extension) is used as the certificate name in ACI, unless C(certificate_name) is specified.', 'This option is mutual exclusive with C(password). If C(password) is provided too, it will be ignored.'], 'required': True, 'aliases': ['cert_key']}",
    "snapshot": "{'description': ['The name of the snapshot to rollback to, or the base snapshot to use for comparison.', 'The C(aci_snapshot) module can be used to query the list of available snapshots.'], 'required': True}",
    "state": "{'description': ['Use C(preview) for previewing the diff between two snapshots.', 'Use C(rollback) for reverting the configuration to a previous snapshot.'], 'choices': ['preview', 'rollback'], 'default': 'rollback'}",
    "timeout": "{'description': ['The socket level timeout in seconds.'], 'type': 'int', 'default': 30}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "use_ssl": "{'description': ['If C(no), an HTTP connection will be used instead of the default HTTPS connection.'], 'type': 'bool', 'default': True}",
    "username": "{'description': ['The username to use for authentication.'], 'default': 'admin', 'aliases': ['user']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only set to C(no) when used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

---
- name: Create a Snapshot
  aci_config_snapshot:
    host: apic
    username: admin
    password: SomeSecretPassword
    export_policy: config_backup
    state: present
  delegate_to: localhost

- name: Query Existing Snapshots
  aci_config_snapshot:
    host: apic
    username: admin
    password: SomeSecretPassword
    export_policy: config_backup
    state: query
  delegate_to: localhost

- name: Compare Snapshot Files
  aci_config_rollback:
    host: apic
    username: admin
    password: SomeSecretPassword
    export_policy: config_backup
    snapshot: run-2017-08-28T06-24-01
    compare_export_policy: config_backup
    compare_snapshot: run-2017-08-27T23-43-56
    state: preview
  delegate_to: localhost

- name: Rollback Configuration
  aci_config_rollback:
    host: apic
    username: admin
    password: SomeSecretPassword
    import_policy: rollback_config
    export_policy: config_backup
    snapshot: run-2017-08-28T06-24-01
    state: rollback
  delegate_to: localhost

- name: Rollback Configuration
  aci_config_rollback:
    host: apic
    username: admin
    password: SomeSecretPassword
    import_policy: rollback_config
    export_policy: config_backup
    snapshot: run-2017-08-28T06-24-01
    description: Rollback 8-27 changes
    import_mode: atomic
    import_type: replace
    fail_on_decrypt: yes
    state: rollback
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Jacob McGill (@jmcgill298)']
