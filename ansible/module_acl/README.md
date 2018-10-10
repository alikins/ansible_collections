# Ansible module: ansible.module_acl


Sets and retrieves file ACL information

## Description

Sets and retrieves file ACL information.

## Requirements

TODO

## Arguments

``` json
{
    "default": "{'description': ['if the target is a directory, setting this to yes will make it the default acl for entities created inside the directory. It causes an error if path is a file.'], 'type': 'bool', 'default': False, 'version_added': '1.5'}",
    "entity": "{'description': ['actual user or group that the ACL applies to when matching entity types user or group are selected.'], 'version_added': '1.5'}",
    "entry": "{'description': ["DEPRECATED. The acl to set or remove.  This must always be quoted in the form of '<etype>:<qualifier>:<perms>'.  The qualifier may be empty for some types, but the type and perms are always required. '-' can be used as placeholder when you do not care about permissions. This is now superseded by entity, type and permissions fields."]}",
    "etype": "{'description': ['the entity type of the ACL to apply, see setfacl documentation for more info.'], 'choices': ['group', 'mask', 'other', 'user'], 'version_added': '1.5'}",
    "follow": "{'description': ['whether to follow symlinks on the path if a symlink is encountered.'], 'type': 'bool', 'default': True}",
    "path": "{'description': ['The full path of the file or object.'], 'aliases': ['name'], 'required': True}",
    "permissions": "{'description': ['Permissions to apply/remove can be any combination of r, w and  x (read, write and execute respectively)'], 'version_added': '1.5'}",
    "recalculate_mask": "{'description': ['Select if and when to recalculate the effective right masks of the files, see setfacl documentation for more info. Incompatible with C(state=query).'], 'choices': ['default', 'mask', 'no_mask'], 'default': 'default', 'version_added': '2.7'}",
    "recursive": "{'description': ['Recursively sets the specified ACL (added in Ansible 2.0). Incompatible with C(state=query).'], 'type': 'bool', 'default': False, 'version_added': '2.0'}",
    "state": "{'description': ["defines whether the ACL should be present or not.  The C(query) state gets the current acl without changing it, for use in 'register' operations."], 'choices': ['absent', 'present', 'query'], 'default': 'query'}",
}
```

## Examples


``` yaml

- name: Grant user Joe read access to a file
  acl:
    path: /etc/foo.conf
    entity: joe
    etype: user
    permissions: r
    state: present

- name: Removes the acl for Joe on a specific file
  acl:
    path: /etc/foo.conf
    entity: joe
    etype: user
    state: absent

- name: Sets default acl for joe on foo.d
  acl:
    path: /etc/foo.d
    entity: joe
    etype: user
    permissions: rw
    default: yes
    state: present

- name: Same as previous but using entry shorthand
  acl:
    path: /etc/foo.d
    entry: "default:user:joe:rw-"
    state: present

- name: Obtain the acl for a specific file
  acl:
    path: /etc/foo.conf
  register: acl_info

```

## License

TODO

## Author Information
  - ['Brian Coca (@bcoca)', 'Jérémie Astori (@astorije)']
  - ['Brian Coca (@bcoca)', 'Jérémie Astori (@astorije)']
