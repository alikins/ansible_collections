# Ansible module: ansible.module_netapp_e_iscsi_target


NetApp E-Series manage iSCSI target configuration

## Description

Configure the settings of an E-Series iSCSI target

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity Web Services Proxy or Embedded Web Services API.'], 'example': ['https://prod-1.wahoo.acme.com/devmgr/v2']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "chap_secret": "{'description': ['Enable Challenge-Handshake Authentication Protocol (CHAP), utilizing this value as the password.', 'When this value is specified, we will always trigger an update (changed=True). We have no way of verifying whether or not the password has changed.', 'The chap secret may only use ascii characters with values between 32 and 126 decimal.', 'The chap secret must be no less than 12 characters, but no more than 16 characters in length.'], 'aliases': ['chap', 'password']}",
    "log_path": "{'description': ['A local path (on the Ansible controller), to a file to be used for debug logging.'], 'required': False}",
    "name": "{'description': ['The name/alias to assign to the iSCSI target.', 'This alias is often used by the initiator software in order to make an iSCSI target easier to identify.'], 'aliases': ['alias']}",
    "ping": "{'description': ['Enable ICMP ping responses from the configured iSCSI ports.'], 'type': 'bool', 'default': True}",
    "ssid": "{'required': True, 'description': ['The ID of the array to manage. This value must be unique for each array.']}",
    "unnamed_discovery": "{'description': ['When an initiator initiates a discovery session to an initiator port, it is considered an unnamed discovery session if the iSCSI target iqn is not specified in the request.', 'This option may be disabled to increase security if desired.'], 'type': 'bool', 'default': True}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?'], 'type': 'bool'}",
}
```

## Examples


``` yaml

    - name: Enable ping responses and unnamed discovery sessions for all iSCSI ports
      netapp_e_iscsi_target:
        api_url: "https://localhost:8443/devmgr/v2"
        api_username: admin
        api_password: myPassword
        ssid: "1"
        validate_certs: no
        name: myTarget
        ping: yes
        unnamed_discovery: yes

    - name: Set the target alias and the CHAP secret
      netapp_e_iscsi_target:
        ssid: "{{ ssid }}"
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"
        name: myTarget
        chap: password1234

```

## License

TODO

## Author Information
  - ['Michael Price (@lmprice)']
