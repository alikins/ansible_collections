# Ansible module: ansible.module_atomic_container


Manage the containers on the atomic host platform

## Description

Manage the containers on the atomic host platform
Allows to manage the lifecycle of a container on the atomic host platform

## Requirements

TODO

## Arguments

``` json
{
    "backend": "{'description': ['Define the backend to use for the container'], 'required': True, 'choices': ['docker', 'ostree']}",
    "image": "{'description': ['The image to use to install the container'], 'required': True}",
    "mode": "{'description': ['Define if it is an user or a system container'], 'required': True, 'choices': ['user', 'system']}",
    "name": "{'description': ['Name of the container'], 'required': True}",
    "rootfs": "{'description': ['Define the rootfs of the image']}",
    "state": "{'description': ['State of the container'], 'required': True, 'choices': ['latest', 'present', 'absent', 'rollback'], 'default': 'latest'}",
    "values": "{'description': ["Values for the installation of the container.  This option is permitted only with mode 'user' or 'system'. The values specified here will be used at installation time as --set arguments for atomic install."]}",
}
```

## Examples


``` yaml


# Install the etcd system container
- atomic_container:
    name: etcd
    image: rhel/etcd
    backend: ostree
    state: latest
    mode: system
    values:
        - ETCD_NAME=etcd.server

# Uninstall the etcd system container
- atomic_container:
    name: etcd
    image: rhel/etcd
    backend: ostree
    state: absent
    mode: system

```

## License

TODO

## Author Information
  - ['Giuseppe Scrivano (@giuseppe)']
