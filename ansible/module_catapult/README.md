# Ansible module: ansible.module_catapult


Send a sms / mms using the catapult bandwidth api

## Description

Allows notifications to be sent using sms / mms via the catapult bandwidth api.

## Requirements

TODO

## Arguments

``` json
{
    "api_secret": "{'description': ['Api Secret from Api account page.'], 'required': True}",
    "api_token": "{'description': ['Api Token from Api account page.'], 'required': True}",
    "dest": "{'description': ['The phone number or numbers the message should be sent to (must be in E.164 format, like C(+19195551212)).'], 'required': True}",
    "media": "{'description': ['For MMS messages, a media url to the location of the media to be sent with the message.']}",
    "msg": "{'description': ['The contents of the text message (must be 2048 characters or less).'], 'required': True}",
    "src": "{'description': ['One of your catapult telephone numbers the message should come from (must be in E.164 format, like C(+19195551212)).'], 'required': True}",
    "user_id": "{'description': ['User Id from Api account page.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Send a mms to multiple users
  catapult:
    src: "+15035555555"
    dest:
      - "+12525089000"
      - "+12018994225"
    media: "http://example.com/foobar.jpg"
    msg: "Task is complete"
    user_id: "{{ user_id }}"
    api_token: "{{ api_token }}"
    api_secret: "{{ api_secret }}"

- name: Send a sms to a single user
  catapult:
    src: "+15035555555"
    dest: "+12018994225"
    msg: "Consider yourself notified"
    user_id: "{{ user_id }}"
    api_token: "{{ api_token }}"
    api_secret: "{{ api_secret }}"


```

## License

TODO

## Author Information
  - ['Jonathan Mainguy (@Jmainguy)']
