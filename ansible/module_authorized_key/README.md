# Ansible module: ansible.module_authorized_key


Adds or removes an SSH authorized key

## Description

Adds or removes SSH authorized keys for particular user accounts

## Requirements

TODO

## Arguments

``` json
{
    "comment": "{'description': ['Change the comment on the public key. Rewriting the comment is useful in cases such as fetching it from GitHub or GitLab.', 'If no comment is specified, the existing comment will be kept.'], 'version_added': '2.4'}",
    "exclusive": "{'description': ['Whether to remove all other non-specified keys from the authorized_keys file. Multiple keys can be specified in a single C(key) string value by separating them by newlines.', 'This option is not loop aware, so if you use C(with_) , it will be exclusive per iteration of the loop, if you want multiple keys in the file you need to pass them all to C(key) in a single batch as mentioned above.'], 'type': 'bool', 'default': False, 'version_added': '1.9'}",
    "follow": "{'description': ['Follow path symlink instead of replacing it'], 'type': 'bool', 'default': False, 'version_added': '2.7'}",
    "key": "{'description': ['The SSH public key(s), as a string or (since 1.9) url (https://github.com/username.keys)'], 'required': True}",
    "key_options": "{'description': ['A string of ssh key options to be prepended to the key in the authorized_keys file'], 'version_added': '1.4'}",
    "manage_dir": "{'description': ['Whether this module should manage the directory of the authorized key file.  If set, the module will create the directory, as well as set the owner and permissions of an existing directory. Be sure to set C(manage_dir=no) if you are using an alternate directory for authorized_keys, as set with C(path), since you could lock yourself out of SSH access. See the example below.'], 'type': 'bool', 'default': True}",
    "path": "{'description': ['Alternate path to the authorized_keys file'], 'default': '(homedir)+/.ssh/authorized_keys'}",
    "state": "{'description': ['Whether the given key (with the given key_options) should or should not be in the file'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "user": "{'description': ['The username on the remote host whose authorized_keys file will be modified'], 'required': True}",
    "validate_certs": "{'description': ['This only applies if using a https url as the source of the keys. If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates as it avoids verifying the source site.', 'Prior to 2.1 the code worked as if this was set to C(yes).'], 'type': 'bool', 'default': True, 'version_added': '2.1'}",
}
```

## Examples


``` yaml

- name: Set authorized key taken from file
  authorized_key:
    user: charlie
    state: present
    key: "{{ lookup('file', '/home/charlie/.ssh/id_rsa.pub') }}"

- name: Set authorized keys taken from url
  authorized_key:
    user: charlie
    state: present
    key: https://github.com/charlie.keys

- name: Set authorized key in alternate location
  authorized_key:
    user: charlie
    state: present
    key: "{{ lookup('file', '/home/charlie/.ssh/id_rsa.pub') }}"
    path: /etc/ssh/authorized_keys/charlie
    manage_dir: False

- name: Set up multiple authorized keys
  authorized_key:
    user: deploy
    state: present
    key: '{{ item }}'
  with_file:
    - public_keys/doe-jane
    - public_keys/doe-john

- name: Set authorized key defining key options
  authorized_key:
    user: charlie
    state: present
    key: "{{ lookup('file', '/home/charlie/.ssh/id_rsa.pub') }}"
    key_options: 'no-port-forwarding,from="10.0.1.1"'

- name: Set authorized key without validating the TLS/SSL certificates
  authorized_key:
    user: charlie
    state: present
    key: https://github.com/user.keys
    validate_certs: False

- name: Set authorized key, removing all the authorized keys already set
  authorized_key:
    user: root
    key: '{{ item }}'
    state: present
    exclusive: True
  with_file:
    - public_keys/doe-jane

- name: Set authorized key for user ubuntu copying it from current user
  authorized_key:
    user: ubuntu
    state: present
    key: "{{ lookup('file', lookup('env','HOME') + '/.ssh/id_rsa.pub') }}"

```

## License

TODO

## Author Information
  - ['Ansible Core Team']
