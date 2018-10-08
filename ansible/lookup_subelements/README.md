# Ansible lookup: ansible.lookup_subelements


traverse nested key from a list of dictionaries

## Description

Subelements walks a list of hashes (aka dictionaries) and then traverses a list with a given (nested sub-)key inside of those records.

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['tuple of list of dictionaries and dictionary key to extract'], 'required': True}",
    "skip_missing": "{'default': False, 'description': ['If set to True, the lookup plugin will skip the lists items that do not contain the given subkey. If False, the plugin will yield an error and complain about the missing subkey.']}",
}
```

## Examples


``` yaml

- name: show var structure as it is needed for example to make sense
  hosts: all
  vars:
    users:
      - name: alice
        authorized:
          - /tmp/alice/onekey.pub
          - /tmp/alice/twokey.pub
        mysql:
            password: mysql-password
            hosts:
              - "%"
              - "127.0.0.1"
              - "::1"
              - "localhost"
            privs:
              - "*.*:SELECT"
              - "DB1.*:ALL"
        groups:
          - wheel
      - name: bob
        authorized:
          - /tmp/bob/id_rsa.pub
        mysql:
            password: other-mysql-password
            hosts:
              - "db1"
            privs:
              - "*.*:SELECT"
              - "DB2.*:ALL"
  tasks:
    - name: Set authorized ssh key, extracting just that data from 'users'
      authorized_key:
        user: "{{ item.0.name }}"
        key: "{{ lookup('file', item.1) }}"
      with_subelements:
         - "{{ users }}"
         - authorized

    - name: Setup MySQL users, given the mysql hosts and privs subkey lists
      mysql_user:
        name: "{{ item.0.name }}"
        password: "{{ item.0.mysql.password }}"
        host: "{{ item.1 }}"
        priv: "{{ item.0.mysql.privs | join('/') }}"
      with_subelements:
        - "{{ users }}"
        - mysql.hosts

    - name: list groups for users that have them, don't error if groups key is missing
      debug: var=item
      loop: "{{lookup('subelements', users, 'groups', {'skip_missing': True})}}"

```

## License

TODO

## Author Information
  - ['Serge van Ginderachter <serge@vanginderachter.be>']
