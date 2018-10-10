# Ansible module: ansible.module_hall


Send notification to Hall

## Description

The C(hall) module connects to the U(https://hall.com) messaging API and allows you to deliver notication messages to rooms.

## Requirements

TODO

## Arguments

``` json
{
    "msg": "{'description': ['The message you wish to deliver as a notification'], 'required': True}",
    "picture": "{'description': ['The full URL to the image you wish to use for the Icon of the message. Defaults to U(http://cdn2.hubspot.net/hub/330046/file-769078210-png/Official_Logos/ansible_logo_black_square_small.png?t=1421076128627)\n'], 'required': False}",
    "room_token": "{'description': ['Room token provided to you by setting up the Ansible room integation on U(https://hall.com)'], 'required': True}",
    "title": "{'description': ['The title of the message'], 'required': True}",
}
```

## Examples


``` yaml

- name: Send Hall notifiation
  hall:
    room_token: <hall room integration token>
    title: Nginx
    msg: 'Created virtual host file on {{ inventory_hostname }}'
  delegate_to: loclahost

- name: Send Hall notification if EC2 servers were created.
  hall:
    room_token: <hall room integration token>
    title: Server Creation
    msg: 'Created instance {{ item.id }} of type {{ item.instance_type }}.\nInstance can be reached at {{ item.public_ip }} in the {{ item.region }} region.'
  delegate_to: loclahost
  when: ec2.instances|length > 0
  with_items: '{{ ec2.instances }}'

```

## License

TODO

## Author Information
  - ['Billy Kimble (@bkimble) <basslines@gmail.com>']
