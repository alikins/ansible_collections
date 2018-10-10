# Ansible module: ansible.module_known_hosts


Add or remove a host from the ``known_hosts`` file

## Description

The C(known_hosts) module lets you add or remove a host keys from the C(known_hosts) file.
Starting at Ansible 2.2, multiple entries per host are allowed, but only one for each key type supported by ssh. This is useful if you're going to want to use the M(git) module over ssh, for example.
If you have a very large number of host keys to manage, you will find the M(template) module more useful.

## Requirements

TODO

## Arguments

``` json
{
    "hash_host": "{'description': ['Hash the hostname in the known_hosts file'], 'type': 'bool', 'default': False, 'version_added': '2.3'}",
    "key": "{'description': ['The SSH public host key, as a string (required if state=present, optional when state=absent, in which case all keys for the host are removed). The key must be in the right format for ssh (see sshd(8), section "SSH_KNOWN_HOSTS FILE FORMAT").\nSpecifically, the key should not match the format that is found in an SSH pubkey file, but should rather have the hostname prepended to a line that includes the pubkey, the same way that it would appear in the known_hosts file. The value prepended to the line must also match the value of the name parameter.']}",
    "name": "{'aliases': ['host'], 'description': ['The host to add or remove (must match a host specified in key). It will be converted to lowercase so that ssh-keygen can find it.'], 'required': True}",
    "path": "{'description': ['The known_hosts file to edit'], 'default': '(homedir)+/.ssh/known_hosts'}",
    "state": "{'description': ['I(present) to add the host key, I(absent) to remove it.'], 'choices': ['present', 'absent'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: tell the host about our servers it might want to ssh to
  known_hosts:
    path: /etc/ssh/ssh_known_hosts
    name: foo.com.invalid
    key: "{{ lookup('file', 'pubkeys/foo.com.invalid') }}"

```

## License

TODO

## Author Information
  - ['Matthew Vernon (@mcv21)']
