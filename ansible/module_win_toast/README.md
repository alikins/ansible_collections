# Ansible module: ansible.module_win_toast


Sends Toast windows notification to logged in users on Windows 10 or later hosts

## Description

Sends alerts which appear in the Action Center area of the windows desktop.

## Requirements

TODO

## Arguments

``` json
{
    "expire": "{'description': ['How long in seconds before the notification expires.'], 'type': 'int', 'default': 45}",
    "group": "{'description': ['Which notification group to add the notification to.'], 'default': 'Powershell'}",
    "msg": "{'description': ['The message to appear inside the notification.', 'May include \\n to format the message to appear within the Action Center.'], 'default': 'Hello, World!'}",
    "popup": "{'description': ['If C(no), the notification will not pop up and will only appear in the Action Center.'], 'type': 'bool', 'default': True}",
    "tag": "{'description': ['The tag to add to the notification.'], 'default': 'Ansible'}",
    "title": "{'description': ['The notification title, which appears in the pop up..'], 'default': 'Notification HH:mm'}",
}
```

## Examples


``` yaml

- name: Warn logged in users of impending upgrade (note use of async to stop the module from waiting until notification expires).
  win_toast:
    expire: 60
    title: System Upgrade Notification
    msg: Automated upgrade about to start.  Please save your work and log off before {{ deployment_start_time }}
  async: 60
  poll: 0

```

## License

TODO

## Author Information
  - ['Jon Hawkesworth (@jhawkesworth)']
