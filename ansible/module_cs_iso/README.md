# Ansible module: ansible.module_cs_iso


Manages ISO images on Apache CloudStack based clouds

## Description

Register and remove ISO images.

## Requirements

TODO

## Arguments

``` json
{
    "account": "{'description': ['Account the ISO is related to.']}",
    "api_http_method": "{'description': ['HTTP method used to query the API endpoint.', 'If not given, the C(CLOUDSTACK_METHOD) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is C(get) if not specified.'], 'choices': ['get', 'post']}",
    "api_key": "{'description': ['API key of the CloudStack API.', 'If not given, the C(CLOUDSTACK_KEY) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_region": "{'description': ['Name of the ini section in the C(cloustack.ini) file.', 'If not given, the C(CLOUDSTACK_REGION) env variable is considered.'], 'default': 'cloudstack'}",
    "api_secret": "{'description': ['Secret key of the CloudStack API.', 'If not set, the C(CLOUDSTACK_SECRET) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "api_timeout": "{'description': ['HTTP timeout in seconds.', 'If not given, the C(CLOUDSTACK_TIMEOUT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.', 'Fallback value is 10 seconds if not specified.']}",
    "api_url": "{'description': ['URL of the CloudStack API e.g. https://cloud.example.com/client/api.', 'If not given, the C(CLOUDSTACK_ENDPOINT) env variable is considered.', 'As the last option, the value is taken from the ini config file, also see the notes.']}",
    "bootable": "{'description': ['Register the ISO to be bootable. Only used if C(state) is present.']}",
    "checksum": "{'description': ['The MD5 checksum value of this ISO. If set, we search by checksum instead of name.']}",
    "cross_zones": "{'description': ['Whether the ISO should be synced or removed across zones.', 'Mutually exclusive with C(zone).'], 'type': 'bool', 'default': False, 'version_added': '2.4'}",
    "display_text": "{'description': ['Display text of the ISO.', 'If not specified, C(name) will be used.'], 'version_added': '2.4'}",
    "domain": "{'description': ['Domain the ISO is related to.']}",
    "is_dynamically_scalable": "{'description': ['Register the ISO having XS/VMWare tools installed inorder to support dynamic scaling of VM cpu/memory. Only used if C(state) is present.']}",
    "is_featured": "{'description': ['Register the ISO to be featured. Only used if C(state) is present.']}",
    "is_public": "{'description': ['Register the ISO to be publicly available to all users. Only used if C(state) is present.']}",
    "is_ready": "{'description': ['This flag is used for searching existing ISOs. If set to C(yes), it will only list ISO ready for deployment e.g. successfully downloaded and installed. Recommended to set it to C(no).'], 'type': 'bool', 'default': False}",
    "iso_filter": "{'description': ['Name of the filter used to search for the ISO.'], 'default': 'self', 'choices': ['featured', 'self', 'selfexecutable', 'sharedexecutable', 'executable', 'community']}",
    "name": "{'description': ['Name of the ISO.'], 'required': True}",
    "os_type": "{'description': ['Name of the OS that best represents the OS of this ISO. If the iso is bootable this parameter needs to be passed. Required if C(state) is present.']}",
    "poll_async": "{'description': ['Poll async jobs until job has finished.'], 'type': 'bool', 'default': True, 'version_added': '2.3'}",
    "project": "{'description': ['Name of the project the ISO to be registered in.']}",
    "state": "{'description': ['State of the ISO.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tags": "{'description': ['List of tags. Tags are a list of dictionaries having keys C(key) and C(value).', 'To delete all tags, set a empty list e.g. C(tags: []).'], 'aliases': ['tag'], 'version_added': '2.4'}",
    "url": "{'description': ['URL where the ISO can be downloaded from. Required if C(state) is present.']}",
    "zone": "{'description': ['Name of the zone you wish the ISO to be registered or deleted from.', 'If not specified, first zone found will be used.']}",
}
```

## Examples


``` yaml

# Register an ISO if ISO name does not already exist.
- local_action:
    module: cs_iso
    name: Debian 7 64-bit
    url: http://mirror.switch.ch/ftp/mirror/debian-cd/current/amd64/iso-cd/debian-7.7.0-amd64-netinst.iso
    os_type: Debian GNU/Linux 7(64-bit)

# Register an ISO with given name if ISO md5 checksum does not already exist.
- local_action:
    module: cs_iso
    name: Debian 7 64-bit
    url: http://mirror.switch.ch/ftp/mirror/debian-cd/current/amd64/iso-cd/debian-7.7.0-amd64-netinst.iso
    os_type: Debian GNU/Linux 7(64-bit)
    checksum: 0b31bccccb048d20b551f70830bb7ad0

# Remove an ISO by name
- local_action:
    module: cs_iso
    name: Debian 7 64-bit
    state: absent

# Remove an ISO by checksum
- local_action:
    module: cs_iso
    name: Debian 7 64-bit
    checksum: 0b31bccccb048d20b551f70830bb7ad0
    state: absent

```

## License

TODO

## Author Information
  - ['René Moser (@resmo)']
