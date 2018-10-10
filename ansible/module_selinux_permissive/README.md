# Ansible module: ansible.module_selinux_permissive


Change permissive domain in SELinux policy

## Description

Add and remove a domain from the list of permissive domains.

## Requirements

TODO

## Arguments

``` json
{
    "domain": "{'description': ['The domain that will be added or removed from the list of permissive domains.'], 'required': True}",
    "no_reload": "{'description': ["Disable reloading of the SELinux policy after making change to a domain's permissive setting.", 'The default is C(no), which causes policy to be reloaded when a domain changes state.', 'Reloading the policy does not work on older versions of the C(policycoreutils-python) library, for example in EL 6."'], 'type': 'bool', 'default': False}",
    "permissive": "{'description': ['Indicate if the domain should or should not be set as permissive.'], 'required': True, 'type': 'bool'}",
    "store": "{'description': ['Name of the SELinux policy store to use.']}",
}
```

## Examples


``` yaml

- name: Change the httpd_t domain to permissive
  selinux_permissive:
    name: httpd_t
    permissive: true

```

## License

TODO

## Author Information
  - ['Michael Scherer (@mscherer) <misc@zarb.org>']
