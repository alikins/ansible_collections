# Ansible module: ansible.module_ftd_file_upload


Uploads files to Cisco FTD devices over HTTP(S)

## Description

Uploads files to Cisco FTD devices including disk files, backups, and upgrades.

## Requirements

TODO

## Arguments

``` json
{
    "fileToUpload": "{'description': ['Absolute path to the file that should be uploaded.'], 'required': True}",
    "operation": "{'description': ['The name of the operation to execute.', 'Only operations that upload file can be used in this module.'], 'required': True}",
    "register_as": "{'description': ['Specifies Ansible fact name that is used to register received response from the FTD device.']}",
}
```

## Examples


``` yaml

- name: Upload disk file
  ftd_file_upload:
    operation: 'postuploaddiskfile'
    fileToUpload: /tmp/test1.txt

```

## License

TODO

## Author Information
  - ['Cisco Systems, Inc.']
