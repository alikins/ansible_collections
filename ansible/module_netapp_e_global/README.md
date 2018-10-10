# Ansible module: ansible.module_netapp_e_global


NetApp E-Series manage global settings configuration

## Description

Allow the user to configure several of the global settings associated with an E-Series storage-system

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity Web Services Proxy or Embedded Web Services API.'], 'example': ['https://prod-1.wahoo.acme.com/devmgr/v2']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "log_path": "{'description': ['A local path to a file to be used for debug logging'], 'required': False}",
    "name": "{'description': ['Set the name of the E-Series storage-system', "This label/name doesn't have to be unique.", 'May be up to 30 characters in length.'], 'aliases': ['label']}",
    "ssid": "{'required': True, 'description': ['The ID of the array to manage. This value must be unique for each array.']}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?'], 'type': 'bool'}",
}
```

## Examples


``` yaml

    - name: Set the storage-system name
      netapp_e_global:
        name: myArrayName
        api_url: "10.1.1.1:8443"
        api_username: "admin"
        api_password: "myPass"

```

## License

TODO

## Author Information
  - ['Michael Price (@lmprice)']
