# Ansible lookup: ansible.lookup_first_found


return first file found from list

## Description

this lookup checks a list of files and paths and returns the full path to the first combination found.
As all lookups, when fed relative paths it will try use the current task's location first and go up the chain to the containing role/play/include/etc's location.
The list of files has precedence over the paths searched. i.e, A task in a  role has a 'file1' in the play's relative path, this will be used, 'file2' in role's relative path will not.

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['list of file names'], 'required': True}",
    "paths": "{'description': ['list of paths in which to look for the files']}",
}
```

## Examples


``` yaml

- name: show first existing file
  debug: msg={{lookup('first_found', findme)}}
  vars:
    findme:
      - "/path/to/foo.txt"
      - "bar.txt"  # will be looked in files/ dir relative to role and/or play
      - "/path/to/biz.txt"

- name: |
        copy first existing file found to /some/file,
        looking in relative directories from where the task is defined and
        including any play objects that contain it
  copy: src={{lookup('first_found', findme)}} dest=/some/file
  vars:
    findme:
      - foo
      - "{{inventory_hostname}}"
      - bar

- name: same copy but specific paths
  copy: src={{lookup('first_found', params)}} dest=/some/file
  vars:
    params:
      files:
        - foo
        - "{{inventory_hostname}}"
        - bar
      paths:
        - /tmp/production
        - /tmp/staging

- name: INTERFACES | Create Ansible header for /etc/network/interfaces
  template:
    src: "{{ lookup('first_found', findme)}}"
    dest: "/etc/foo.conf"
  vars:
    findme:
      - "{{ ansible_virtualization_type }}_foo.conf"
      - "default_foo.conf"

- name: read vars from first file found, use 'vars/' relative subdir
  include_vars: "{{lookup('first_found', params)}}"
  vars:
    params:
      files:
        - '{{ansible_os_distribution}}.yml'
        - '{{ansible_os_family}}.yml'
        - default.yml
      paths:
        - 'vars'

```

## License

TODO

## Author Information
  - ['Seth Vidal <skvidal@fedoraproject.org>']
