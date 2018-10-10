# Ansible module: ansible.module_xattr


Manage user defined extended attributes

## Description

Manages filesystem user defined extended attributes, requires that they are enabled on the target filesystem and that the setfattr/getfattr utilities are present.

## Requirements

TODO

## Arguments

``` json
{
    "follow": "{'description': ['If C(yes), dereferences symlinks and sets/gets attributes on symlink target, otherwise acts on symlink itself.'], 'type': 'bool', 'default': True}",
    "key": "{'description': ['The name of a specific Extended attribute key to set/retrieve.']}",
    "namespace": "{'description': ['Namespace of the named name/key.'], 'default': 'user', 'version_added': '2.7'}",
    "path": "{'description': ['The full path of the file/object to get the facts of.', 'Before 2.3 this option was only usable as I(name).'], 'aliases': ['name'], 'required': True}",
    "state": "{'description': ['defines which state you want to do. C(read) retrieves the current value for a C(key) (default) C(present) sets C(name) to C(value), default if value is set C(all) dumps all data C(keys) retrieves all keys C(absent) deletes the key'], 'choices': ['absent', 'all', 'keys', 'present', 'read'], 'default': 'read'}",
    "value": "{'description': ["The value to set the named name/key to, it automatically sets the C(state) to 'set'."]}",
}
```

## Examples


``` yaml

- name: Obtain the extended attributes  of /etc/foo.conf
  xattr:
    path: /etc/foo.conf

- name: Set the key 'user.foo' to value 'bar'
  xattr:
    path: /etc/foo.conf
    key: foo
    value: bar

- name: Set the key 'trusted.glusterfs.volume-id' to value '0x817b94343f164f199e5b573b4ea1f914'
  xattr:
    path: /mnt/bricks/brick1
    namespace: trusted
    key: glusterfs.volume-id
    value: "0x817b94343f164f199e5b573b4ea1f914"

- name: Remove the key 'user.foo'
  xattr:
    path: /etc/foo.conf
    key: foo
    state: absent

- name: Remove the key 'trusted.glusterfs.volume-id'
  xattr:
    path: /mnt/bricks/brick1
    namespace: trusted
    key: glusterfs.volume-id
    state: absent

```

## License

TODO

## Author Information
  - ['Brian Coca (@bcoca)']
