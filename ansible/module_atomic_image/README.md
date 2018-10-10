# Ansible module: ansible.module_atomic_image


Manage the container images on the atomic host platform

## Description

Manage the container images on the atomic host platform.
Allows to execute the commands specified by the RUN label in the container image when present.

## Requirements

TODO

## Arguments

``` json
{
    "backend": "{'description': ['Define the backend where the image is pulled.'], 'choices': ['docker', 'ostree'], 'version_added': '2.4'}",
    "name": "{'description': ['Name of the container image.'], 'required': True}",
    "started": "{'description': ['Start or Stop the container.'], 'type': 'bool', 'default': True}",
    "state": "{'description': ['The state of the container image.', 'The state C(latest) will ensure container image is upgraded to the latest version and forcefully restart container, if running.'], 'choices': ['absent', 'latest', 'present'], 'default': 'latest'}",
}
```

## Examples


``` yaml

- name: Execute the run command on rsyslog container image (atomic run rhel7/rsyslog)
  atomic_image:
    name: rhel7/rsyslog
    state: latest

- name: Pull busybox to the OSTree backend
  atomic_image:
    name: busybox
    state: latest
    backend: ostree

```

## License

TODO

## Author Information
  - ['Saravanan KR (@krsacme)']
