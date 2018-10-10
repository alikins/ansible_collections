# Ansible module: ansible.module_osx_defaults


osx_defaults allows users to read, write, and delete macOS user defaults from Ansible

## Description

osx_defaults allows users to read, write, and delete macOS user defaults from Ansible scripts. macOS applications and other programs use the defaults system to record user preferences and other information that must be maintained when the applications aren't running (such as default font for new documents, or the position of an Info panel).

## Requirements

TODO

## Arguments

``` json
{
    "array_add": "{'description': ['Add new elements to the array for a key which has an array as its value.'], 'type': 'bool', 'default': False}",
    "domain": "{'description': ['The domain is a domain name of the form com.companyname.appname.'], 'default': 'NSGlobalDomain'}",
    "host": "{'description': ['The host on which the preference should apply. The special value "currentHost" corresponds to the "-currentHost" switch of the defaults commandline tool.'], 'version_added': '2.1'}",
    "key": "{'description': ['The key of the user preference'], 'required': True}",
    "state": "{'description': ['The state of the user defaults'], 'default': 'present', 'choices': ['present', 'absent']}",
    "type": "{'description': ['The type of value to write.'], 'default': 'string', 'choices': ['array', 'bool', 'boolean', 'date', 'float', 'int', 'integer', 'string']}",
    "value": "{'description': ['The value to write. Only required when state = present.']}",
}
```

## Examples


``` yaml

- osx_defaults:
    domain: com.apple.Safari
    key: IncludeInternalDebugMenu
    type: bool
    value: true
    state: present

- osx_defaults:
    domain: NSGlobalDomain
    key: AppleMeasurementUnits
    type: string
    value: Centimeters
    state: present

- osx_defaults:
    domain: com.apple.screensaver
    host: currentHost
    key: showClock
    type: int
    value: 1

- osx_defaults:
    key: AppleMeasurementUnits
    type: string
    value: Centimeters

- osx_defaults:
    key: AppleLanguages
    type: array
    value:
      - en
      - nl

- osx_defaults:
    domain: com.geekchimp.macable
    key: ExampleKeyToRemove
    state: absent

```

## License

TODO

## Author Information
  - ['Franck Nijhof (@frenck)']
