# Ansible module: ansible.module_fmgr_provisioning


Provision devices via FortiMananger

## Description

Add model devices on the FortiManager using jsonrpc API and have them pre-configured, so when central management is configured, the configuration is pushed down to the registering devices

## Requirements

TODO

## Arguments

``` json
{
    "adom": "{'description': ['The administrative domain (admon) the configuration belongs to'], 'required': True}",
    "description": "{'description': ['Description of the device to be provisioned.'], 'required': False}",
    "group": "{'description': ['The name of the device group the provisioned device can belong to.'], 'required': False}",
    "host": "{'description': ["The FortiManager's Address."], 'required': True}",
    "minor_release": "{'description': ['The minor release number such as 6.X.1, as X being the minor release.'], 'required': False}",
    "name": "{'description': ['The name of the device to be provisioned.'], 'required': True}",
    "os_type": "{'description': ["The Fortinet OS type to be pushed to the device, such as 'FOS' for FortiOS."], 'required': True}",
    "os_version": "{'description': ['The Fortinet OS version to be used for the device, such as 5.0 or 6.0.'], 'required': True}",
    "password": "{'description': ['The password associated with the username account.'], 'required': False}",
    "patch_release": "{'description': ['The patch release number such as 6.0.X, as X being the patch release.'], 'required': False}",
    "platform": "{'description': ['The platform of the device, such as model number or VM.'], 'required': True}",
    "policy_package": "{'description': ['The name of the policy package to be assigned to the device.'], 'required': True}",
    "serial": "{'description': ['The serial number of the device that will be provisioned.'], 'required': True}",
    "username": "{'description': ['The username to log into the FortiManager'], 'required': True}",
    "vdom": "{'description': ['The virtual domain (vdom) the configuration belongs to']}",
}
```

## Examples


``` yaml

- name: Create Model Device
  hosts: FortiManager
  connection: local
  gather_facts: False

  tasks:

    - name: Create FGT1 Model Device
      fmgr_provision:
        host: "{{ inventory_hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        adom: "root"
        vdom: "root"
        policy_package: "default"
        name: "FGT1"
        group: "Ansible"
        serial: "FGVM000000117994"
        platform: "FortiGate-VM64"
        description: "Provisioned by Ansible"
        os_version: '6.0'
        minor_release: 0
        patch_release: 0
        os_type: 'fos'


    - name: Create FGT2 Model Device
      fmgr_provision:
        host: "{{ inventory_hostname }}"
        username: "{{ username }}"
        password: "{{ password }}"
        adom: "root"
        vdom: "root"
        policy_package: "test_pp"
        name: "FGT2"
        group: "Ansible"
        serial: "FGVM000000117992"
        platform: "FortiGate-VM64"
        description: "Provisioned by Ansible"
        os_version: '5.0'
        minor_release: 6
        patch_release: 0
        os_type: 'fos'


```

## License

TODO

## Author Information
  - ['Andrew Welsh']
