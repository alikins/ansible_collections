# Ansible module: ansible.module_virt


Manages virtual machines supported by libvirt

## Description

Manages virtual machines supported by I(libvirt).

## Requirements

TODO

## Arguments

``` json
{
    "autostart": "{'description': ['start VM at host startup.'], 'type': 'bool', 'version_added': '2.3'}",
    "command": "{'description': ['In addition to state management, various non-idempotent commands are available.'], 'choices': ['create', 'define', 'destroy', 'freemem', 'get_xml', 'info', 'list_vms', 'nodeinfo', 'pause', 'shutdown', 'start', 'status', 'stop', 'undefine', 'unpause', 'virttype']}",
    "name": "{'description': ['name of the guest VM being managed. Note that VM must be previously defined with xml.', 'This option is required unless I(command) is C(list_vms).']}",
    "state": "{'description': ['Note that there may be some lag for state requests like C(shutdown) since these refer only to VM states. After starting a guest, it may not be immediately accessible.'], 'choices': ['destroyed', 'paused', 'running', 'shutdown']}",
    "uri": "{'description': ['libvirt connection uri.'], 'default': 'qemu:///system'}",
    "xml": "{'description': ['XML document used with the define command.', 'Must be raw XML content using C(lookup). XML cannot be reference to a file.']}",
}
```

## Examples


``` yaml

# a playbook task line:
- virt:
    name: alpha
    state: running

# /usr/bin/ansible invocations
# ansible host -m virt -a "name=alpha command=status"
# ansible host -m virt -a "name=alpha command=get_xml"
# ansible host -m virt -a "name=alpha command=create uri=lxc:///"

---
# a playbook example of defining and launching an LXC guest
tasks:
  - name: define vm
    virt:
        name: foo
        command: define
        xml: "{{ lookup('template', 'container-template.xml.j2') }}"
        uri: 'lxc:///'
  - name: start vm
    virt:
        name: foo
        state: running
        uri: 'lxc:///'

```

## License

TODO

## Author Information
  - ['Ansible Core Team', 'Michael DeHaan', 'Seth Vidal']
  - ['Ansible Core Team', 'Michael DeHaan', 'Seth Vidal']
  - ['Ansible Core Team', 'Michael DeHaan', 'Seth Vidal']
