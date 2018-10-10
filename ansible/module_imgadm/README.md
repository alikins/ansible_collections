# Ansible module: ansible.module_imgadm


Manage SmartOS images

## Description

Manage SmartOS virtual machine images through imgadm(1M)

## Requirements

TODO

## Arguments

``` json
{
    "force": "{'required': False, 'type': 'bool', 'description': ['Force a given operation (where supported by imgadm(1M)).']}",
    "pool": "{'required': False, 'default': 'zones', 'description': ['zpool to import to or delete images from.']}",
    "source": "{'required': False, 'description': ['URI for the image source.']}",
    "state": "{'required': True, 'choices': ['present', 'absent', 'deleted', 'imported', 'updated', 'vacuumed'], 'description': ['State the object operated on should be in. C(imported) is an alias for for C(present) and C(deleted) for C(absent). When set to C(vacuumed) and C(uuid) to C(*), it will remove all unused images.']}",
    "type": "{'required': False, 'choices': ['imgapi', 'docker', 'dsapi'], 'default': 'imgapi', 'description': ['Type for image sources.']}",
    "uuid": "{'required': False, 'description': ['Image UUID. Can either be a full UUID or C(*) for all images.']}",
}
```

## Examples


``` yaml

- name: Import an image
  imgadm:
    uuid: '70e3ae72-96b6-11e6-9056-9737fd4d0764'
    state: imported

- name: Delete an image
  imgadm:
    uuid: '70e3ae72-96b6-11e6-9056-9737fd4d0764'
    state: deleted

- name: Update all images
  imgadm:
    uuid: '*'
    state: updated

- name: Update a single image
  imgadm:
    uuid: '70e3ae72-96b6-11e6-9056-9737fd4d0764'
    state: updated

- name: Add a source
  imgadm:
    source: 'https://datasets.project-fifo.net'
    state: present

- name: Add a Docker source
  imgadm:
    source: 'https://docker.io'
    type: docker
    state: present

- name: Remove a source
  imgadm:
    source: 'https://docker.io'
    state: absent

```

## License

TODO

## Author Information
  - ['Jasper Lievisse Adriaanse (@jasperla)']
