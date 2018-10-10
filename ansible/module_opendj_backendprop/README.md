# Ansible module: ansible.module_opendj_backendprop


Will update the backend configuration of OpenDJ via the dsconfig set-backend-prop command

## Description

This module will update settings for OpenDJ with the command set-backend-prop.
It will check first via de get-backend-prop if configuration needs to be applied.

## Requirements

TODO

## Arguments

``` json
{
    "backend": "{'description': ['The name of the backend on which the property needs to be updated.'], 'required': True}",
    "hostname": "{'description': ['The hostname of the OpenDJ server.'], 'required': True}",
    "name": "{'description': ['The configuration setting to update.'], 'required': True}",
    "opendj_bindir": "{'description': ['The path to the bin directory of OpenDJ.'], 'required': False, 'default': '/opt/opendj/bin'}",
    "password": "{'description': ['The password for the cn=Directory Manager user.', 'Either password or passwordfile is needed.'], 'required': False}",
    "passwordfile": "{'description': ['Location to the password file which holds the password for the cn=Directory Manager user.', 'Either password or passwordfile is needed.'], 'required': False}",
    "port": "{'description': ['The Admin port on which the OpenDJ instance is available.'], 'required': True}",
    "state": "{'description': ['If configuration needs to be added/updated'], 'required': False, 'default': 'present'}",
    "username": "{'description': ['The username to connect to.'], 'required': False, 'default': 'cn=Directory Manager'}",
    "value": "{'description': ['The value for the configuration item.'], 'required': True}",
}
```

## Examples


``` yaml

  - name: "Add or update OpenDJ backend properties"
    action: opendj_backendprop
            hostname=localhost
            port=4444
            username="cn=Directory Manager"
            password=password
            backend=userRoot
            name=index-entry-limit
            value=5000

```

## License

TODO

## Author Information
  - ['Werner Dijkerman (@dj-wasabi)']
