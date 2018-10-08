# Ansible lookup: ansible.lookup_filetree


recursively match all files in a directory tree

## Description

This lookup enables you to template a complete tree of files on a target system while retaining permissions and ownership.
Supports directories, files and symlinks, including SELinux and other file properties
If you provide more than one path, it will implement a first_found logic, and will not process entries it already processed in previous paths. This enables merging different trees in order of importance, or add role_vars to specific paths to influence different instances of the same role.

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['path(s) of files to read'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create directories
  file:
    path: /web/{{ item.path }}
    state: directory
    mode: '{{ item.mode }}'
  with_filetree: web/
  when: item.state == 'directory'

- name: Template files
  template:
    src: '{{ item.src }}'
    dest: /web/{{ item.path }}
    mode: '{{ item.mode }}'
  with_filetree: web/
  when: item.state == 'file'

- name: Recreate symlinks
  file:
    src: '{{ item.src }}'
    dest: /web/{{ item.path }}
    state: link
    force: yes
    mode: '{{ item.mode }}'
  with_filetree: web/
  when: item.state == 'link'

```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers) <dag@wieers.com>']
