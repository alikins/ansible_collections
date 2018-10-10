# Ansible module: ansible.module_fmgr_sys_proxy


Make FortiGate API calls via the FortiMananger

## Description

The FMG proxies FOS API calls via the FMG.  Review FortiGate API documentation to ensure you are passing correct parameters for both the FortiManager and FortiGate

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ["Specify HTTP action for the request. Either 'get' or 'post'"], 'required': True}",
    "adom": "{'description': ['The administrative domain (admon) the configuration belongs to'], 'required': True}",
    "host": "{'description': ["The FortiManager's Address."], 'required': True}",
    "password": "{'description': ['The password associated with the username account.'], 'required': False}",
    "payload": "{'description': ['JSON payload of the request. The payload will be URL-encoded and becomes the "json" field in the query string for both GET and POST request.'], 'required': False}",
    "resource": "{'description': ['URL on the remote device to be accessed, string'], 'required': True}",
    "target": "{'description': ['FOS datasource, either device or group object'], 'required': True}",
    "username": "{'description': ['The username to log into the FortiManager'], 'required': True}",
}
```

## Examples


``` yaml

- name: Proxy FOS requests via FMG
  hosts: FortiManager
  connection: local
  gather_facts: False

  tasks:

    - name: Get upgrade path for FGT1
      fmgr_provision:
        host: "{{ inventory_hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        adom: "root"
        action: "get"
        resource: "/api/v2/monitor/system/firmware/upgrade-paths?vdom=root"
        target: ["/adom/root/device/FGT1"]
    - name: Upgrade firmware of FGT1
      fmgr_provision:
        host: "{{ inventory_hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        adom: "root"
        action: "post"
        payload: {source: upload, file_content: b64_encoded_string, file_name: file_name}
        resource: "/api/v2/monitor/system/firmware/upgrade?vdom=vdom"
        target: ["/adom/root/device/FGT1"]


```

## License

TODO

## Author Information
  - ['Andrew Welsh']
