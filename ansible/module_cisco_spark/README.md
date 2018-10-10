# Ansible module: ansible.module_cisco_spark


Send a message to a Cisco Spark Room or Individual

## Description

Send a message to a Cisco Spark Room or Individual with options to control the formatting.

## Requirements

TODO

## Arguments

``` json
{
    "message": "{'description': ['The message you would like to send.'], 'required': True}",
    "message_type": "{'description': ['Specifies how you would like the message formatted.'], 'required': False, 'default': 'text', 'choices': ['text', 'markdown']}",
    "personal_token": "{'description': ['Your personal access token required to validate the Spark API.'], 'required': True, 'aliases': ['token']}",
    "recipient_id": "{'description': ['The unique identifier associated with the supplied C(recipient_type).'], 'required': True}",
    "recipient_type": "{'description': ['The request parameter you would like to send the message to.', 'Messages can be sent to either a room or individual (by ID or E-Mail).'], 'required': True, 'choices': ['roomId', 'toPersonEmail', 'toPersonId']}",
}
```

## Examples


``` yaml

# Note: The following examples assume a variable file has been imported
# that contains the appropriate information.

- name: Cisco Spark - Markdown Message to a Room
  cisco_spark:
    recipient_type: roomId
    recipient_id: "{{ room_id }}"
    message_type: markdown
    personal_token: "{{ token }}"
    message: "**Cisco Spark Ansible Module - Room Message in Markdown**"

- name: Cisco Spark - Text Message to a Room
  cisco_spark:
    recipient_type: roomId
    recipient_id: "{{ room_id }}"
    message_type: text
    personal_token: "{{ token }}"
    message: "Cisco Spark Ansible Module - Room Message in Text"

- name: Cisco Spark - Text Message by an Individuals ID
  cisco_spark:
    recipient_type: toPersonId
    recipient_id: "{{ person_id}}"
    message_type: text
    personal_token: "{{ token }}"
    message: "Cisco Spark Ansible Module - Text Message to Individual by ID"

- name: Cisco Spark - Text Message by an Individuals E-Mail Address
  cisco_spark:
    recipient_type: toPersonEmail
    recipient_id: "{{ person_email }}"
    message_type: text
    personal_token: "{{ token }}"
    message: "Cisco Spark Ansible Module - Text Message to Individual by E-Mail"


```

## License

TODO

## Author Information
  - ['Drew Rusell (@drew-russell)']
