# Ansible module: ansible.module_packet_sshkey


Create/delete an SSH key in Packet host

## Description

Create/delete an SSH key in Packet host.
API is documented at U(https://www.packet.net/help/api/#page:ssh-keys,header:ssh-keys-ssh-keys-post).

## Requirements

TODO

## Arguments

``` json
{
    "auth_token": "{'description': ['Packet api token. You can also supply it in env var C(PACKET_API_TOKEN).']}",
    "fingerprint": "{'description': ['Fingerprint of the key which you want to remove.']}",
    "id": "{'description': ['UUID of the key which you want to remove.']}",
    "key": "{'description': ['Public Key string ({type} {base64 encoded key} {description}).']}",
    "key_file": "{'description': ['File with the public key.']}",
    "label": "{'description': ['Label for the key. If you keep it empty, it will be read from key string.']}",
    "state": "{'description': ['Indicate desired state of the target.'], 'default': 'present', 'choices': ['present', 'absent']}",
}
```

## Examples


``` yaml

# All the examples assume that you have your Packet API token in env var PACKET_API_TOKEN.
# You can also pass the api token in module param auth_token.

- name: create sshkey from string
  hosts: localhost
  tasks:
    packet_sshkey:
      key: "{{ lookup('file', 'my_packet_sshkey.pub') }}"

- name: create sshkey from file
  hosts: localhost
  tasks:
    packet_sshkey:
      label: key from file
      key_file: ~/ff.pub

- name: remove sshkey by id
  hosts: localhost
  tasks:
    packet_sshkey:
      state: absent
      id: eef49903-7a09-4ca1-af67-4087c29ab5b6

```

## License

TODO

## Author Information
  - ['Tomas Karasek (@t0mk) <tom.to.the.k@gmail.com>']
