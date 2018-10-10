# Ansible module: ansible.module_redfish_config


Manages Out-Of-Band controllers using Redfish APIs

## Description

Builds Redfish URIs locally and sends them to remote OOB controllers to set or update a configuration attribute.
Manages BIOS configuration settings.
Manages OOB controller configuration settings.

## Requirements

TODO

## Arguments

``` json
{
    "baseuri": "{'required': True, 'description': ['Base URI of OOB controller']}",
    "bios_attr_name": "{'required': False, 'description': ['name of BIOS attribute to update'], 'default': 'null'}",
    "bios_attr_value": "{'required': False, 'description': ['value of BIOS attribute to update'], 'default': 'null'}",
    "category": "{'required': True, 'description': ['Category to execute on OOB controller']}",
    "command": "{'required': True, 'description': ['List of commands to execute on OOB controller']}",
    "mgr_attr_name": "{'required': False, 'description': ['name of Manager attribute to update'], 'default': 'null'}",
    "mgr_attr_value": "{'required': False, 'description': ['value of Manager attribute to update'], 'default': 'null'}",
    "password": "{'required': True, 'description': ['Password for authentication with OOB controller']}",
    "user": "{'required': True, 'description': ['User for authentication with OOB controller']}",
}
```

## Examples


``` yaml

  - name: Set BootMode to UEFI
    redfish_config:
      category: Systems
      command: SetBiosAttributes
      bios_attr_name: BootMode
      bios_attr_value: Uefi
      baseuri: "{{ baseuri }}"
      user: "{{ user }}"
      password: "{{ password }}"

  - name: Set BootMode to Legacy BIOS
    redfish_config:
      category: Systems
      command: SetBiosAttributes
      bios_attr_name: BootMode
      bios_attr_value: Bios
      baseuri: "{{ baseuri }}"
      user: "{{ user }}"
      password: "{{ password }}"

  - name: Enable PXE Boot for NIC1
    redfish_config:
      category: Systems
      command: SetBiosAttributes
      bios_attr_name: PxeDev1EnDis
      bios_attr_value: Enabled
      baseuri: "{{ baseuri }}"
      user: "{{ user }}"
      password: "{{ password }}"

  - name: Set BIOS default settings
    redfish_config:
      category: Systems
      command: SetBiosDefaultSettings
      baseuri: "{{ baseuri }}"
      user: "{{ user }}"
      password: "{{ password }}"

  - name: Enable NTP in the OOB Controller
    redfish_config:
      category: Manager
      command: SetManagerAttributes
      mgr_attr_name: NTPConfigGroup.1.NTPEnable
      mgr_attr_value: Enabled
      baseuri: "{{ baseuri }}"
      user: "{{ user}}"
      password: "{{ password }}"

  - name: Set NTP server 1 to {{ ntpserver1 }} in the OOB Controller
    redfish_config:
      category: Manager
      command: SetManagerAttributes
      mgr_attr_name: NTPConfigGroup.1.NTP1
      mgr_attr_value: "{{ ntpserver1 }}"
      baseuri: "{{ baseuri }}"
      user: "{{ user}}"
      password: "{{ password }}"

  - name: Set Timezone to {{ timezone }} in the OOB Controller
    redfish_config:
      category: Manager
      command: SetManagerAttributes
      mgr_attr_name: Time.1.Timezone
      mgr_attr_value: "{{ timezone }}"
      baseuri: "{{ baseuri }}"
      user: "{{ user}}"
      password: "{{ password }}"

```

## License

TODO

## Author Information
  - ['Jose Delarosa (github: jose-delarosa)']
