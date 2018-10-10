# Ansible module: ansible.module_netapp_e_alerts


NetApp E-Series manage email notification settings

## Description

Certain E-Series systems have the capability to send email notifications on potentially critical events.
This module will allow the owner of the system to specify email recipients for these messages.

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'required': True, 'description': ['The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "api_url": "{'required': True, 'description': ['The url to the SANtricity Web Services Proxy or Embedded Web Services API.'], 'example': ['https://prod-1.wahoo.acme.com/devmgr/v2']}",
    "api_username": "{'required': True, 'description': ['The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API.']}",
    "contact": "{'description': ['Allows the owner to specify some free-form contact information to be included in the emails.', 'This is typically utilized to provide a contact phone number.'], 'required': False}",
    "log_path": "{'description': ['Path to a file on the Ansible control node to be used for debug logging'], 'required': False}",
    "recipients": "{'description': ['The email addresses that will receive the email notifications.', 'Required when I(state=enabled).'], 'required': False}",
    "sender": "{'description': ["This is the sender that the recipient will see. It doesn't necessarily need to be a valid email account.", 'Required when I(state=enabled).'], 'required': False}",
    "server": "{'description': ['A fully qualified domain name, IPv4 address, or IPv6 address of a mail server.', 'To use a fully qualified domain name, you must configure a DNS server on both controllers using M(netapp_e_mgmt_interface). - Required when I(state=enabled).'], 'required': False}",
    "ssid": "{'required': True, 'description': ['The ID of the array to manage. This value must be unique for each array.']}",
    "state": "{'description': ['Enable/disable the sending of email-based alerts.'], 'default': 'enabled', 'required': False, 'choices': ['enabled', 'disabled']}",
    "test": "{'description': ['When a change is detected in the configuration, a test email will be sent.', 'This may take a few minutes to process.', 'Only applicable if I(state=enabled).'], 'default': False, 'type': 'bool'}",
    "validate_certs": "{'required': False, 'default': True, 'description': ['Should https certificates be validated?'], 'type': 'bool'}",
}
```

## Examples


``` yaml

    - name: Enable email-based alerting
      netapp_e_alerts:
        state: enabled
        sender: noreply@example.com
        server: mail@example.com
        contact: "Phone: 1-555-555-5555"
        recipients:
            - name1@example.com
            - name2@example.com
        api_url: "10.1.1.1:8443"
        api_username: "admin"
        api_password: "myPass"

    - name: Disable alerting
      netapp_e_alerts:
        state: disabled
        api_url: "10.1.1.1:8443"
        api_username: "admin"
        api_password: "myPass"

```

## License

TODO

## Author Information
  - ['Michael Price (@lmprice)']
