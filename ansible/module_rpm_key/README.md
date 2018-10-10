# Ansible module: ansible.module_rpm_key


Adds or removes a gpg key from the rpm db

## Description

Adds or removes (rpm --import) a gpg key to your rpm database.

## Requirements

TODO

## Arguments

``` json
{
    "key": "{'description': ['Key that will be modified. Can be a url, a file, or a keyid if the key already exists in the database.'], 'required': True}",
    "state": "{'description': ['If the key will be imported or removed from the rpm db.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "validate_certs": "{'description': ['If C(no) and the C(key) is a url starting with https, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

# Example action to import a key from a url
- rpm_key:
    state: present
    key: http://apt.sw.be/RPM-GPG-KEY.dag.txt

# Example action to import a key from a file
- rpm_key:
    state: present
    key: /path/to/key.gpg

# Example action to ensure a key is not present in the db
- rpm_key:
    state: absent
    key: DEADB33F

```

## License

TODO

## Author Information
  - ['Hector Acosta (@hacosta) <hector.acosta@gazzang.com>']
