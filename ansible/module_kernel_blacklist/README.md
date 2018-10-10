# Ansible module: ansible.module_kernel_blacklist


Blacklist kernel modules

## Description

Add or remove kernel modules from blacklist.

## Requirements

TODO

## Arguments

``` json
{
    "blacklist_file": "{'description': ['If specified, use this blacklist file instead of C(/etc/modprobe.d/blacklist-ansible.conf).']}",
    "name": "{'description': ['Name of kernel module to black- or whitelist.'], 'required': True}",
    "state": "{'description': ['Whether the module should be present in the blacklist or absent.'], 'choices': ['absent', 'present'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: Blacklist the nouveau driver module
  kernel_blacklist:
    name: nouveau
    state: present

```

## License

TODO

## Author Information
  - ['Matthias Vogelgesang (@matze)']
