# Ansible httpapi: ansible.httpapi_ftd


HttpApi Plugin for Cisco ASA Firepower device

## Description

This HttpApi plugin provides methods to connect to Cisco ASA firepower devices over a HTTP(S)-based api.

## Requirements

TODO

## Arguments

``` json
{
    "spec_path": "{'type': 'str', 'description': ['Specifies the api spec path of the FTD device'], 'default': '/apispec/ngfw.json', 'vars': [{'name': 'ansible_httpapi_ftd_spec_path'}]}",
    "token_path": "{'type': 'str', 'description': ['Specifies the api token path of the FTD device'], 'default': '/api/fdm/v2/fdm/token', 'vars': [{'name': 'ansible_httpapi_ftd_token_path'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['Ansible Networking Team']
