# Ansible module: ansible.module_redfish_facts


Manages Out-Of-Band controllers using Redfish APIs

## Description

Builds Redfish URIs locally and sends them to remote OOB controllers to get information back.
Information retrieved is placed in a location specified by the user.

## Requirements

TODO

## Arguments

``` json
{
    "baseuri": "{'required': True, 'description': ['Base URI of OOB controller']}",
    "category": "{'required': False, 'description': ['List of categories to execute on OOB controller'], 'default': ['Systems']}",
    "command": "{'required': False, 'description': ['List of commands to execute on OOB controller']}",
    "password": "{'required': True, 'description': ['Password for authentication with OOB controller']}",
    "user": "{'required': True, 'description': ['User for authentication with OOB controller']}",
}
```

## Examples


``` yaml

  - name: Get CPU inventory
    redfish_facts:
      category: Systems
      command: GetCpuInventory
      baseuri: "{{ baseuri }}"
      user: "{{ user }}"
      password: "{{ password }}"

  - name: Get fan inventory
    redfish_facts:
      category: Chassis
      command: GetFanInventory
      baseuri: "{{ baseuri }}"
      user: "{{ user }}"
      password: "{{ password }}"

  - name: Get default inventory information
    redfish_facts:
      baseuri: "{{ baseuri }}"
      user: "{{ user }}"
      password: "{{ password }}"

  - name: Get several inventories
    redfish_facts:
      category: Systems
      command: GetNicInventory,GetPsuInventory,GetBiosAttributes
      baseuri: "{{ baseuri }}"
      user: "{{ user }}"
      password: "{{ password }}"

  - name: Get default system inventory and user information
    redfish_facts:
      category: Systems,Accounts
      baseuri: "{{ baseuri }}"
      user: "{{ user }}"
      password: "{{ password }}"

  - name: Get default system, user and firmware information
    redfish_facts:
      category: ["Systems", "Accounts", "Update"]
      baseuri: "{{ baseuri }}"
      user: "{{ user }}"
      password: "{{ password }}"

  - name: Get all information available in the Manager category
    redfish_facts:
      category: Manager
      command: all
      baseuri: "{{ baseuri }}"
      user: "{{ user }}"
      password: "{{ password }}"

  - name: Get all information available in all categories
    redfish_facts:
      category: all
      command: all
      baseuri: "{{ baseuri }}"
      user: "{{ user }}"
      password: "{{ password }}"

```

## License

TODO

## Author Information
  - ['Jose Delarosa (github: jose-delarosa)']
