# Ansible module: ansible.module_xenserver_facts


get facts reported on xenserver

## Description

Reads data out of XenAPI, can be used instead of multiple xe commands.

## Requirements

TODO

## Arguments

}
```

## Examples


``` yaml

- name: Gather facts from xenserver
  xenserver_facts:

- name: Print running VMs
  debug:
    msg: "{{ item }}"
  with_items: "{{ xs_vms.keys() }}"
  when: xs_vms[item]['power_state'] == "Running"

# Which will print:
#
# TASK: [Print running VMs] ***********************************************************
# skipping: [10.13.0.22] => (item=CentOS 4.7 (32-bit))
# ok: [10.13.0.22] => (item=Control domain on host: 10.0.13.22) => {
#     "item": "Control domain on host: 10.0.13.22",
#     "msg": "Control domain on host: 10.0.13.22"
# }

```

## License

TODO

## Author Information
  - ['Andy Hill (@andyhky)', 'Tim Rupp', 'Robin Lee (@cheese)']
  - ['Andy Hill (@andyhky)', 'Tim Rupp', 'Robin Lee (@cheese)']
  - ['Andy Hill (@andyhky)', 'Tim Rupp', 'Robin Lee (@cheese)']
