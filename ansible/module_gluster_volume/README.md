# Ansible module: ansible.module_gluster_volume


Manage GlusterFS volumes

## Description

Create, remove, start, stop and tune GlusterFS volumes

## Requirements

TODO

## Arguments

``` json
{
    "arbiters": "{'description': ['Arbiter count for volume.'], 'version_added': '2.3'}",
    "bricks": "{'description': ['Brick paths on servers. Multiple brick paths can be separated by commas.'], 'aliases': ['brick']}",
    "cluster": "{'description': ['List of hosts to use for probing and brick setup.']}",
    "directory": "{'description': ['Directory for limit-usage.']}",
    "disperses": "{'description': ['Disperse count for volume.'], 'version_added': '2.2'}",
    "force": "{'description': ['If brick is being created in the root partition, module will fail. Set force to true to override this behaviour.'], 'type': 'bool'}",
    "host": "{'description': ['Override local hostname (for peer probing purposes).']}",
    "name": "{'description': ['The volume name.'], 'required': True, 'aliases': ['volume']}",
    "options": "{'description': ['A dictionary/hash with options/settings for the volume.']}",
    "quota": "{'description': ['Quota value for limit-usage (be sure to use 10.0MB instead of 10MB, see quota list).']}",
    "rebalance": "{'description': ['Controls whether the cluster is rebalanced after changes.'], 'type': 'bool', 'default': False}",
    "redundancies": "{'description': ['Redundancy count for volume.'], 'version_added': '2.2'}",
    "replicas": "{'description': ['Replica count for volume.']}",
    "start_on_create": "{'description': ['Controls whether the volume is started after creation or not.'], 'type': 'bool', 'default': True}",
    "state": "{'description': ['Use present/absent ensure if a volume exists or not. Use started/stopped to control its availability.'], 'required': True, 'choices': ['absent', 'present', 'started', 'stopped']}",
    "stripes": "{'description': ['Stripe count for volume.']}",
    "transport": "{'description': ['Transport type for volume.'], 'default': 'tcp', 'choices': ['tcp', 'rdma', 'tcp,rdma']}",
}
```

## Examples


``` yaml

- name: create gluster volume
  gluster_volume:
    state: present
    name: test1
    bricks: /bricks/brick1/g1
    rebalance: yes
    cluster:
      - 192.0.2.10
      - 192.0.2.11
  run_once: true

- name: tune
  gluster_volume:
    state: present
    name: test1
    options:
      performance.cache-size: 256MB

- name: Set multiple options on GlusterFS volume
  gluster_volume:
    state: present
    name: test1
    options:
      { performance.cache-size: 128MB,
        write-behind: 'off',
        quick-read: 'on'
      }

- name: start gluster volume
  gluster_volume:
    state: started
    name: test1

- name: limit usage
  gluster_volume:
    state: present
    name: test1
    directory: /foo
    quota: 20.0MB

- name: stop gluster volume
  gluster_volume:
    state: stopped
    name: test1

- name: remove gluster volume
  gluster_volume:
    state: absent
    name: test1

- name: create gluster volume with multiple bricks
  gluster_volume:
    state: present
    name: test2
    bricks: /bricks/brick1/g2,/bricks/brick2/g2
    cluster:
      - 192.0.2.10
      - 192.0.2.11
  run_once: true

```

## License

TODO

## Author Information
  - ['Taneli Leppä (@rosmo)']
