# Ansible module: ansible.module_slurp


Slurps a file from remote nodes

## Description

This module works like M(fetch). It is used for fetching a base64- encoded blob containing the data in a remote file.
This module is also supported for Windows targets.

## Requirements

TODO

## Arguments

``` json
{
    "src": "{'description': ['The file on the remote system to fetch. This I(must) be a file, not a directory.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Find out what the remote machine's mounts are
  slurp:
    src: /proc/mounts
  register: mounts

- debug:
    msg: "{{ mounts['content'] | b64decode }}"

# From the commandline, find the pid of the remote machine's sshd
# $ ansible host -m slurp -a 'src=/var/run/sshd.pid'
# host | SUCCESS => {
#     "changed": false,
#     "content": "MjE3OQo=",
#     "encoding": "base64",
#     "source": "/var/run/sshd.pid"
# }
# $ echo MjE3OQo= | base64 -d
# 2179

```

## License

TODO

## Author Information
  - ['Ansible Core Team', 'Michael DeHaan (@mpdehaan)']
  - ['Ansible Core Team', 'Michael DeHaan (@mpdehaan)']
