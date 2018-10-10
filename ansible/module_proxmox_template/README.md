# Ansible module: ansible.module_proxmox_template


management of OS templates in Proxmox VE cluster

## Description

allows you to upload/delete templates in Proxmox VE cluster

## Requirements

TODO

## Arguments

``` json
{
    "api_host": "{'description': ['the host of the Proxmox VE cluster'], 'required': True}",
    "api_password": "{'description': ['the password to authenticate with', 'you can use PROXMOX_PASSWORD environment variable']}",
    "api_user": "{'description': ['the user to authenticate with'], 'required': True}",
    "content_type": "{'description': ['content type', 'required only for C(state=present)'], 'default': 'vztmpl', 'choices': ['vztmpl', 'iso']}",
    "force": "{'description': ['can be used only with C(state=present), exists template will be overwritten'], 'type': 'bool', 'default': False}",
    "node": "{'description': ['Proxmox VE node, when you will operate with template'], 'required': True}",
    "src": "{'description': ['path to uploaded file', 'required only for C(state=present)'], 'aliases': ['path']}",
    "state": "{'description': ['Indicate desired state of the template'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "storage": "{'description': ['target storage'], 'default': 'local'}",
    "template": "{'description': ['the template name', 'required only for states C(absent), C(info)']}",
    "timeout": "{'description': ['timeout for operations'], 'default': 30}",
    "validate_certs": "{'description': ['enable / disable https certificate verification'], 'default': False, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Upload new openvz template with minimal options
- proxmox_template:
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    src: ~/ubuntu-14.04-x86_64.tar.gz

# Upload new openvz template with minimal options use environment PROXMOX_PASSWORD variable(you should export it before)
- proxmox_template:
    node: uk-mc02
    api_user: root@pam
    api_host: node1
    src: ~/ubuntu-14.04-x86_64.tar.gz

# Upload new openvz template with all options and force overwrite
- proxmox_template:
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    storage: local
    content_type: vztmpl
    src: ~/ubuntu-14.04-x86_64.tar.gz
    force: yes

# Delete template with minimal options
- proxmox_template:
    node: uk-mc02
    api_user: root@pam
    api_password: 1q2w3e
    api_host: node1
    template: ubuntu-14.04-x86_64.tar.gz
    state: absent

```

## License

TODO

## Author Information
  - ['Sergei Antipov (@UnderGreen)']
