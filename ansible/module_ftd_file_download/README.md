# Ansible module: ansible.module_ftd_file_download


Downloads files from Cisco FTD devices over HTTP(S)

## Description

Downloads files from Cisco FTD devices including pending changes, disk files, certificates, troubleshoot reports, and backups.

## Requirements

TODO

## Arguments

``` json
{
    "destination": "{'description': ['Absolute path of where to download the file to.', "If destination is a directory, the module uses a filename from 'Content-Disposition' header specified by the server."], 'required': True}",
    "operation": "{'description': ['The name of the operation to execute.', 'Only operations that return a file can be used in this module.'], 'required': True}",
    "path_params": "{'description': ['Key-value pairs that should be sent as path parameters in a REST API call.']}",
}
```

## Examples


``` yaml

- name: Download pending changes
  ftd_file_download:
    operation: 'getdownload'
    path_params:
      objId: 'default'
    destination: /tmp/

```

## License

TODO

## Author Information
  - ['Cisco Systems, Inc.']
