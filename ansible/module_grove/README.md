# Ansible module: ansible.module_grove


Sends a notification to a grove.io channel

## Description

The C(grove) module sends a message for a service to a Grove.io channel.

## Requirements

TODO

## Arguments

``` json
{
    "channel_token": "{'description': ['Token of the channel to post to.'], 'required': True}",
    "icon_url": "{'description': ['Icon for the service'], 'required': False}",
    "message": "{'description': ['Message content'], 'required': True}",
    "service": "{'description': ['Name of the service (displayed as the "user" in the message)'], 'required': False, 'default': 'ansible'}",
    "url": "{'description': ['Service URL for the web client'], 'required': False}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool', 'version_added': '1.5.1'}",
}
```

## Examples


``` yaml

- grove: >
    channel_token=6Ph62VBBJOccmtTPZbubiPzdrhipZXtg
    service=my-app
    message=deployed {{ target }}

```

## License

TODO

## Author Information
  - ['Jonas Pfenniger (@zimbatm)']
