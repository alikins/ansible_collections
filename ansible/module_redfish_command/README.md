# Ansible module: ansible.module_redfish_command


Manages Out-Of-Band controllers using Redfish APIs

## Description

Builds Redfish URIs locally and sends them to remote OOB controllers to perform an action.
Manages OOB controller ex. reboot, log management.
Manages OOB controller users ex. add, remove, update.
Manages system power ex. on, off, graceful and forced reboot.

## Requirements

TODO

## Arguments

``` json
{
    "baseuri": "{'required': True, 'description': ['Base URI of OOB controller']}",
    "bootdevice": "{'required': False, 'description': ['bootdevice when setting boot configuration']}",
    "category": "{'required': True, 'description': ['Category to execute on OOB controller']}",
    "command": "{'required': True, 'description': ['List of commands to execute on OOB controller']}",
    "password": "{'required': True, 'description': ['Password for authentication with OOB controller']}",
    "user": "{'required': True, 'description': ['User for authentication with OOB controller']}",
    "userid": "{'required': False, 'description': ['ID of user to add/delete/modify']}",
    "username": "{'required': False, 'description': ['name of user to add/delete/modify']}",
    "userpswd": "{'required': False, 'description': ['password of user to add/delete/modify']}",
    "userrole": "{'required': False, 'description': ['role of user to add/delete/modify']}",
}
```

## Examples


``` yaml

  - name: Restart system power gracefully
    redfish_command:
      category: Systems
      command: PowerGracefulRestart
      baseuri: "{{ baseuri }}"
      user: "{{ user }}"
      password: "{{ password }}"

  - name: Set one-time boot device to {{ bootdevice }}
    redfish_command:
      category: Systems
      command: SetOneTimeBoot
      bootdevice: "{{ bootdevice }}"
      baseuri: "{{ baseuri }}"
      user: "{{ user }}"
      password: "{{ password }}"

  - name: Add and enable user
    redfish_command:
      category: Accounts
      command: AddUser,EnableUser
      baseuri: "{{ baseuri }}"
      user: "{{ user }}"
      password: "{{ password }}"
      userid: "{{ userid }}"
      username: "{{ username }}"
      userpswd: "{{ userpswd }}"
      userrole: "{{ userrole }}"

  - name: Disable and delete user
    redfish_command:
      category: Accounts
      command: ["DisableUser", "DeleteUser"]
      baseuri: "{{ baseuri }}"
      user: "{{ user }}"
      password: "{{ password }}"
      userid: "{{ userid }}"

  - name: Update user password
    redfish_command:
      category: Accounts
      command: UpdateUserPassword
      baseuri: "{{ baseuri }}"
      user: "{{ user }}"
      password: "{{ password }}"
      userid: "{{ userid }}"
      userpswd: "{{ userpswd }}"

  - name: Clear Manager Logs
    redfish_command:
      category: Manager
      command: ClearLogs
      baseuri: "{{ baseuri }}"
      user: "{{ user }}"
      password: "{{ password }}"

```

## License

TODO

## Author Information
  - ['Jose Delarosa (github: jose-delarosa)']
