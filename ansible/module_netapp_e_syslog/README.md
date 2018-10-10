# Ansible module: ansible.module_netapp_e_syslog


NetApp E-Series manage syslog settings

## Description

Allow the syslog settings to be configured for an individual E-Series storage-system

## Requirements

TODO

## Arguments

``` json
{
    "address": "{'description': ["The syslog server's IPv4 address or a fully qualified hostname.", 'All existing syslog configurations will be removed when I(state=absent) and I(address=None).']}",
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity Web Services Proxy or Embedded Web Services API.'], 'example': ['https://prod-1.wahoo.acme.com/devmgr/v2']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "components": "{'description': ['The e-series logging components define the specific logs to transfer to the syslog server.', "At the time of writing, 'auditLog' is the only logging component but more may become available."], 'default': ['auditLog']}",
    "log_path": "{'description': ['This argument specifies a local path for logging purposes.'], 'required': False}",
    "port": "{'description': ['This is the port the syslog server is using.'], 'default': 514}",
    "protocol": "{'description': ["This is the transmission protocol the syslog server's using to receive syslog messages."], 'choices': ['udp', 'tcp', 'tls'], 'default': 'udp'}",
    "ssid": "{'required': True, 'description': ['The ID of the array to manage. This value must be unique for each array.']}",
    "state": "{'description': ['Add or remove the syslog server configuration for E-Series storage array.', 'Existing syslog server configuration will be removed or updated when its address matches I(address).', 'Fully qualified hostname that resolve to an IPv4 address that matches I(address) will not be treated as a match.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "test": "{'description': ['This forces a test syslog message to be sent to the stated syslog server.', 'Only attempts transmission when I(state=present).'], 'type': 'bool', 'default': False}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?'], 'type': 'bool'}",
}
```

## Examples


``` yaml

    - name: Add two syslog server configurations to NetApp E-Series storage array.
      netapp_e_syslog:
        state: present
        address: "{{ item }}"
        port: 514
        protocol: tcp
        component: "auditLog"
        api_url: "10.1.1.1:8443"
        api_username: "admin"
        api_password: "myPass"
      loop:
        - "192.168.1.1"
        - "192.168.1.100"

```

## License

TODO

## Author Information
  - ['Nathan Swartz (@ndswartz)']
