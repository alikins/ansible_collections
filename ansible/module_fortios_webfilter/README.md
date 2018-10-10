# Ansible module: ansible.module_fortios_webfilter


Configure webfilter capabilities of FortiGate and FortiOS

## Description

This module is able to configure a FortiGate or FortiOS by allowing the user to configure webfilter feature. For now it is able to handle url and content filtering capabilities. The module uses FortiGate REST API internally to configure the device.

## Requirements

TODO

## Arguments

``` json
{
    "host": "{'description': ['FortiOS or FortiGate ip adress.'], 'required': True}",
    "password": "{'description': ['FortiOS or FortiGate password.'], 'default': ''}",
    "username": "{'description': ['FortiOS or FortiGate username.'], 'required': True}",
    "vdom": "{'description': ['Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.'], 'default': 'root'}",
    "webfilter_content": "{'description': ['Container for a group of content-filtering entries that the FortiGate must act upon'], 'suboptions': {'id': {'description': ['Id of content-filter list.'], 'required': True}, 'name': {'description': ['Name of content-filter list.']}, 'comment': {'description': ['Optional comments.']}, 'entries': {'description': ['Content filter entries.'], 'default': [], 'suboptions': {'name': {'description': ['Banned word.'], 'required': True}, 'pattern-type': {'description': ['Banned word pattern type. It can be a wildcard pattern or Perl regular expression.'], 'required': True, 'choices': ['wildcard', 'regexp']}, 'status': {'description': ['Enable/disable banned word.'], 'required': True, 'choices': ['enable', 'disable']}, 'lang': {'description': ['Language of banned word.'], 'required': True, 'choices': ['western', 'simch', 'trach', 'japanese', 'korean', 'french', 'thai', 'spanish', 'cyrillic']}, 'score': {'description': ['Score, to be applied every time the word appears on a web page.'], 'required': True}, 'action': {'description': ['Block or exempt word when a match is found.'], 'required': True, 'choices': ['block', 'exempt']}}}, 'state': {'description': ['Configures the intended state of this object on the FortiGate. When this value is set to I(present), the object is configured on the device and when this value is set to I(absent) the object is removed from the device.'], 'required': True, 'choices': ['absent', 'present']}}}",
    "webfilter_url": "{'description': ['Container for a group of url entries that the FortiGate must act upon'], 'suboptions': {'id': {'description': ['Id of URL filter list.'], 'required': True}, 'name': {'description': ['Name of URL filter list.'], 'required': True}, 'comment': {'description': ['Optional comments.']}, 'one-arm-ips-urlfilter': {'description': ['Enable/disable DNS resolver for one-arm IPS URL filter operation.'], 'choices': ['enable', 'disable'], 'default': 'disable'}, 'ip-addr-block': {'description': ['Enable/disable blocking URLs when the hostname appears as an IP address.'], 'choices': ['enable', 'disable'], 'default': 'disable'}, 'entries': {'description': ['URL filter entries.'], 'default': [], 'suboptions': {'id': {'description': ['Id of URL.'], 'required': True}, 'url': {'description': ['URL to be filtered.'], 'required': True}, 'type': {'description': ['Filter type (simple, regex, or wildcard).'], 'required': True, 'choices': ['simple', 'regex', 'wildcard']}, 'action': {'description': ['Action to take for URL filter matches.'], 'required': True, 'choices': ['exempt', 'block', 'allow', 'monitor']}, 'status': {'description': ['Enable/disable this URL filter.'], 'required': True, 'choices': ['enable', 'disable']}, 'exempt': {'description': ['If action is set to exempt, select the security profile operations that exempt URLs skip. Separate multiple options with a space.'], 'required': True, 'choices': ['av', 'web-content', 'activex-java-cookie', 'dlp', 'fortiguard', 'range-block', 'pass', 'all']}, 'web-proxy-profile': {'description': ['Web proxy profile.'], 'required': True}, 'referrer-host': {'description': ['Referrer host name.'], 'required': True}}}, 'state': {'description': ['Configures the intended state of this object on the FortiGate. When this value is set to I(present), the object is configured on the device and when this value is set to I(absent) the object is removed from the device.'], 'required': True, 'choices': ['absent', 'present']}}}",
}
```

## Examples


``` yaml

- hosts: localhost
  vars:
   host: "192.168.122.40"
   username: "admin"
   password: ""
   vdom: "root"
  tasks:
  - name: Configure url to be filtered by fortigate
    fortios_webfilter:
      host:  "{{  host }}"
      username: "{{  username}}"
      password: "{{ password }}"
      vdom:  "{{  vdom }}"
      webfilter_url:
        state: "present"
        id: "1"
        name: "default"
        comment: "mycomment"
        one-arm-ips-url-filter: "disable"
        ip-addr-block: "disable"
        entries:
          - id: "1"
            url: "www.test1.com"
            type: "simple"
            action: "exempt"
            status: "enable"
            exempt: "pass"
            web-proxy-profile: ""
            referrrer-host: ""
          - id: "2"
            url: "www.test2.com"
            type: "simple"
            action: "exempt"
            status: "enable"
            exempt: "pass"
            web-proxy-profile: ""
            referrrer-host: ""


- hosts: localhost
  vars:
   host: "192.168.122.40"
   username: "admin"
   password: ""
   vdom: "root"
  tasks:
  - name: Configure web content filtering in fortigate
    fortios_webfilter:
      host:  "{{  host }}"
      username: "{{  username}}"
      password: "{{ password }}"
      vdom:  "{{  vdom }}"
      webfilter_content:
        id: "1"
        name: "default"
        comment: ""
        entries:
          - name: "1"
            pattern-type: "www.test45.com"
            status: "enable"
            lang: "western"
            score: 40
            action: "block"
          - name: "2"
            pattern-type: "www.test46.com"
            status: "enable"
            lang: "western"
            score: 42
            action: "block"
        state: "present"

```

## License

TODO

## Author Information
  - ['Miguel Angel Munoz (@mamunozgonzalez)', 'Nicolas Thomas (@thomnico)']
  - ['Miguel Angel Munoz (@mamunozgonzalez)', 'Nicolas Thomas (@thomnico)']
