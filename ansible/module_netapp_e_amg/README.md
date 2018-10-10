# Ansible module: ansible.module_netapp_e_amg


NetApp E-Series create, remove, and update asynchronous mirror groups

## Description

Allows for the creation, removal and updating of Asynchronous Mirror Groups for NetApp E-series storage arrays

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity Web Services Proxy or Embedded Web Services API.'], 'example': ['https://prod-1.wahoo.acme.com/devmgr/v2']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "interfaceType": "{'description': ['The intended protocol to use if both Fibre and iSCSI are available.'], 'choices': ['iscsi', 'fibre']}",
    "manualSync": "{'description': ['Setting this to true will cause other synchronization values to be ignored'], 'type': 'bool', 'default': False}",
    "name": "{'description': ['The name of the async array you wish to target, or create.', "If C(state) is present and the name isn't found, it will attempt to create."], 'required': True}",
    "recoveryWarnThresholdMinutes": "{'description': ['Recovery point warning threshold (minutes). The user will be warned when the age of the last good failures point exceeds this value'], 'default': 20}",
    "repoUtilizationWarnThreshold": "{'description': ['Recovery point warning threshold'], 'default': 80}",
    "secondaryArrayId": "{'description': ['The ID of the secondary array to be used in mirroing process'], 'required': True}",
    "ssid": "{'required': True, 'description': ['The ID of the array to manage. This value must be unique for each array.']}",
    "state": "{'description': ['A C(state) of present will either create or update the async mirror group.', 'A C(state) of absent will remove the async mirror group.'], 'choices': ['absent', 'present'], 'required': True}",
    "syncIntervalMinutes": "{'description': ['The synchronization interval in minutes'], 'default': 10}",
    "syncWarnThresholdMinutes": "{'description': ['The threshold (in minutes) for notifying the user that periodic synchronization has taken too long to complete.'], 'default': 10}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?'], 'type': 'bool'}",
}
```

## Examples


``` yaml

    - name: AMG removal
      na_eseries_amg:
        state: absent
        ssid: "{{ ssid }}"
        secondaryArrayId: "{{amg_secondaryArrayId}}"
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"
        new_name: "{{amg_array_name}}"
        name: "{{amg_name}}"
      when: amg_create

    - name: AMG create
      netapp_e_amg:
        state: present
        ssid: "{{ ssid }}"
        secondaryArrayId: "{{amg_secondaryArrayId}}"
        api_url: "{{ netapp_api_url }}"
        api_username: "{{ netapp_api_username }}"
        api_password: "{{ netapp_api_password }}"
        new_name: "{{amg_array_name}}"
        name: "{{amg_name}}"
      when: amg_create

```

## License

TODO

## Author Information
  - ['Kevin Hulquest (@hulquest)']
