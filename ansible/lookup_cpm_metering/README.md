# Ansible lookup: ansible.lookup_cpm_metering


Get Power and Current data from WTI OOB/Combo and PDU devices

## Description

Get Power and Current data from WTI OOB/Combo and PDU devices

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['This is the Action to send the module.'], 'required': True, 'choices': ['getpower', 'getcurrent']}",
    "cpm_password": "{'description': ['This is the Password of the WTI device to send the module.']}",
    "cpm_url": "{'description': ['This is the URL of the WTI device  to send the module.'], 'required': True}",
    "cpm_username": "{'description': ['This is the Username of the WTI device to send the module.']}",
    "enddate": "{'description': ['End date of the range to look for power data'], 'required': False}",
    "startdate": "{'description': ['Start date of the range to look for power data'], 'required': False}",
    "use_https": "{'description': ['Designates to use an https connection or http connection.'], 'required': False, 'default': True, 'choices': [True, False]}",
    "use_proxy": "{'description': ['Flag to control if the lookup will observe HTTP proxy environment variables when present.'], 'type': 'boolean', 'default': True}",
    "validate_certs": "{'description': ['If false, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'required': False, 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

# Get Power data
  - name: Get Power data for a given WTI device
  - debug:
        var: lookup('cpm_metering',
                'getpower',
                validate_certs=true,
                use_https=true,
                cpm_url='rest.wti.com',
                cpm_username='restpower',
                cpm_password='restfulpowerpass12')

# Get Current data
  - name: Get Current data for a given WTI device
  - debug:
        var: lookup('cpm_metering',
                'getcurrent',
                validate_certs=true,
                use_https=true,
                cpm_url='rest.wti.com',
                cpm_username='restpower',
                cpm_password='restfulpowerpass12')

# Get Power data for a date range
  - name: Get Power data for a given WTI device given a certain date range
  - debug:
        var: lookup('cpm_metering',
                'getpower',
                validate_certs=true,
                use_https=true,
                cpm_url='rest.wti.com',
                cpm_username='restpower',
                cpm_password='restfulpowerpass12',
                startdate='08-12-2018'
                enddate='08-14-2018')

```

## License

TODO

## Author Information
  - ['Western Telematic Inc. (@wtinetworkgear)']
