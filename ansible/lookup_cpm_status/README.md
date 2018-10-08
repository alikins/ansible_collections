# Ansible lookup: ansible.lookup_cpm_status


Get status and parameters from WTI OOB and PDU devices

## Description

Get various status and parameters from WTI OOB and PDU devices.

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['This is the Action to send the module.'], 'required': True, 'choices': ['temperature', 'firmware', 'status', 'alarms']}",
    "cpm_password": "{'description': ['This is the Basic Authentication Password of the WTI device to send the module.'], 'required': True}",
    "cpm_url": "{'description': ['This is the URL of the WTI device to send the module.'], 'required': True}",
    "cpm_username": "{'description': ['This is the Basic Authentication Username of the WTI device to send the module.'], 'required': True}",
    "use_https": "{'description': ['Designates to use an https connection or http connection.'], 'required': False, 'type': 'bool', 'default': True}",
    "use_proxy": "{'description': ['Flag to control if the lookup will observe HTTP proxy environment variables when present.'], 'type': 'boolean', 'default': True}",
    "validate_certs": "{'description': ['If false, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'required': False, 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

# Get temperature
  - name: run Get Device Temperature
  - debug:
        var: lookup('cpm_status',
                'temperature',
                validate_certs=true,
                use_https=true,
                cpm_url='rest.wti.com',
                cpm_username='rest',
                cpm_password='restfulpassword')

# Get firmware version
  - name: Get the firmware version of a given WTI device
  - debug:
        var: lookup('cpm_status',
                'firmware',
                validate_certs=false,
                use_https=true,
                cpm_url="192.168.0.158",
                cpm_username="super",
                cpm_password="super")

# Get status output
  - name: Get the status output from a given WTI device
  - debug:
        var: lookup('cpm_status',
                'status',
                validate_certs=true,
                use_https=true,
                cpm_url="rest.wti.com",
                cpm_username="rest",
                cpm_password="restfulpassword")

# Get Alarm output
  - name: Get the alarms status of a given WTI device
  - debug:
        var: lookup('cpm_status',
                'alarms',
                validate_certs=false,
                use_https=false,
                cpm_url="192.168.0.158",
                cpm_username="super",
                cpm_password="super")

```

## License

TODO

## Author Information
  - ['Western Telematic Inc. (@wtinetworkgear)']
