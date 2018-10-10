# Ansible module: ansible.module_alternatives


Manages alternative programs for common commands

## Description

Manages symbolic links using the 'update-alternatives' tool
Useful when multiple programs are installed but provide similar functionality (e.g. different editors).

## Requirements

TODO

## Arguments

``` json
{
    "link": "{'description': ['The path to the symbolic link that should point to the real executable.', 'This option is always required on RHEL-based distributions. On Debian-based distributions this option is required when the alternative I(name) is unknown to the system.'], 'required': False}",
    "name": "{'description': ['The generic name of the link.'], 'required': True}",
    "path": "{'description': ['The path to the real executable that the link should point to.'], 'required': True}",
    "priority": "{'description': ['The priority of the alternative'], 'required': False, 'default': 50, 'version_added': '2.2'}",
}
```

## Examples


``` yaml

- name: correct java version selected
  alternatives:
    name: java
    path: /usr/lib/jvm/java-7-openjdk-amd64/jre/bin/java

- name: alternatives link created
  alternatives:
    name: hadoop-conf
    link: /etc/hadoop/conf
    path: /etc/hadoop/conf.ansible

- name: make java 32 bit an alternative with low priority
  alternatives:
    name: java
    path: /usr/lib/jvm/java-7-openjdk-i386/jre/bin/java
    priority: -10

```

## License

TODO

## Author Information
  - ['David Wittman (@DavidWittman)', 'Gabe Mulley (@mulby)']
  - ['David Wittman (@DavidWittman)', 'Gabe Mulley (@mulby)']
