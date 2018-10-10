# Ansible module: ansible.module_oneview_san_manager


Manage OneView SAN Manager resources

## Description

Provides an interface to manage SAN Manager resources. Can create, update, or delete.

## Requirements

TODO

## Arguments

``` json
{
    "config": "{'description': ['Path to a .json configuration file containing the OneView client configuration. The configuration file is optional and when used should be present in the host running the ansible commands. If the file path is not provided, the configuration will be loaded from environment variables. For links to example configuration files or how to use the environment variables verify the notes section.']}",
    "data": "{'description': ['List with SAN Manager properties.'], 'required': True}",
    "state": "{'description': ['Indicates the desired state for the Uplink Set resource. - C(present) ensures data properties are compliant with OneView. - C(absent) removes the resource from OneView, if it exists. - C(connection_information_set) updates the connection information for the SAN Manager. This operation is non-idempotent.'], 'default': 'present', 'choices': ['present', 'absent', 'connection_information_set']}",
    "validate_etag": "{'description': ['When the ETag Validation is enabled, the request will be conditionally processed only if the current ETag for the resource matches the ETag provided in the data.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Creates a Device Manager for the Brocade SAN provider with the given hostname and credentials
  oneview_san_manager:
    config: /etc/oneview/oneview_config.json
    state: present
    data:
      providerDisplayName: Brocade Network Advisor
      connectionInfo:
        - name: Host
          value: 172.18.15.1
        - name: Port
          value: 5989
        - name: Username
          value: username
        - name: Password
          value: password
        - name: UseSsl
          value: true
  delegate_to: localhost

- name: Ensure a Device Manager for the Cisco SAN Provider is present
  oneview_san_manager:
    config: /etc/oneview/oneview_config.json
    state: present
    data:
      name: 172.18.20.1
      providerDisplayName: Cisco
      connectionInfo:
        - name: Host
          value: 172.18.20.1
        - name: SnmpPort
          value: 161
        - name: SnmpUserName
          value: admin
        - name: SnmpAuthLevel
          value: authnopriv
        - name: SnmpAuthProtocol
          value: sha
        - name: SnmpAuthString
          value: password
  delegate_to: localhost

- name: Sets the SAN Manager connection information
  oneview_san_manager:
    config: /etc/oneview/oneview_config.json
    state: connection_information_set
    data:
      connectionInfo:
        - name: Host
          value: '172.18.15.1'
        - name: Port
          value: '5989'
        - name: Username
          value: 'username'
        - name: Password
          value: 'password'
        - name: UseSsl
          value: true
  delegate_to: localhost

- name: Refreshes the SAN Manager
  oneview_san_manager:
    config: /etc/oneview/oneview_config.json
    state: present
    data:
      name: 172.18.15.1
      refreshState: RefreshPending
  delegate_to: localhost

- name: Delete the SAN Manager recently created
  oneview_san_manager:
    config: /etc/oneview/oneview_config.json
    state: absent
    data:
      name: '172.18.15.1'
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
  - ['Felipe Bulsoni (@fgbulsoni)', 'Thiago Miotto (@tmiotto)', 'Adriane Cardozo (@adriane-cardozo)']
