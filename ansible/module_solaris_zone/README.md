# Ansible module: ansible.module_solaris_zone


Manage Solaris zones

## Description

Create, start, stop and delete Solaris zones. This module doesn't currently allow changing of options for a zone that's already been created.

## Requirements

TODO

## Arguments

``` json
{
    "attach_options": "{'description': ['Extra options to the zoneadm attach command. For example, this can be used to specify whether a minimum or full update of packages is required and if any packages need to be deleted. For valid values, see zoneadm(1M)'], 'default': 'empty string'}",
    "config": "{'description': ['The zonecfg configuration commands for this zone. See zonecfg(1M) for the valid options and syntax. Typically this is a list of options separated by semi-colons or new lines, e.g. "set auto-boot=true;add net;set physical=bge0;set address=10.1.1.1;end"'], 'default': 'empty string'}",
    "create_options": "{'description': ['Extra options to the zonecfg(1M) create command.'], 'default': 'empty string'}",
    "install_options": "{'description': ['Extra options to the zoneadm(1M) install command. To automate Solaris 11 zone creation, use this to specify the profile XML file, e.g. install_options="-c sc_profile.xml"'], 'default': 'empty string'}",
    "name": "{'description': ['Zone name.'], 'required': True}",
    "path": "{'description': ['The path where the zone will be created. This is required when the zone is created, but not used otherwise.']}",
    "root_password": "{'description': ["The password hash for the root account. If not specified, the zone's root account will not have a password."]}",
    "sparse": "{'description': ['Whether to create a sparse (C(true)) or whole root (C(false)) zone.'], 'type': 'bool', 'default': False}",
    "state": "{'description': ['C(present), configure and install the zone.', 'C(installed), synonym for C(present).', 'C(running), if the zone already exists, boot it, otherwise, configure and install the zone first, then boot it.', 'C(started), synonym for C(running).', 'C(stopped), shutdown a zone.', 'C(absent), destroy the zone.', "C(configured), configure the ready so that it's to be attached.", 'C(attached), attach a zone, but do not boot it.', 'C(detached), shutdown and detach a zone'], 'choices': ['absent', 'attached', 'configured', 'detached', 'installed', 'present', 'running', 'started', 'stopped'], 'default': 'present', 'required': True}",
    "timeout": "{'description': ['Timeout, in seconds, for zone to boot.'], 'default': 600}",
}
```

## Examples


``` yaml

- name: Create and install a zone, but don't boot it
  solaris_zone:
    name: zone1
    state: present
    path: /zones/zone1
    sparse: True
    root_password: Be9oX7OSwWoU.
    config: 'set autoboot=true; add net; set physical=bge0; set address=10.1.1.1; end'

- name: Create and install a zone and boot it
  solaris_zone:
    name: zone1
    state: running
    path: /zones/zone1
    root_password: Be9oX7OSwWoU.
    config: 'set autoboot=true; add net; set physical=bge0; set address=10.1.1.1; end'

- name: Boot an already installed zone
  solaris_zone:
    name: zone1
    state: running

- name: Stop a zone
  solaris_zone:
    name: zone1
    state: stopped

- name: Destroy a zone
  solaris_zone:
    name: zone1
    state: absent

- name: Detach a zone
  solaris_zone:
    name: zone1
    state: detached

- name: Configure a zone, ready to be attached
  solaris_zone:
    name: zone1
    state: configured
    path: /zones/zone1
    root_password: Be9oX7OSwWoU.
    config: 'set autoboot=true; add net; set physical=bge0; set address=10.1.1.1; end'

- name: Attach zone1
  solaris_zone:
    name: zone1
    state: attached
    attach_options: -u

```

## License

TODO

## Author Information
  - ['Paul Markham (@pmarkham)']
