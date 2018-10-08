# Ansible lookup: ansible.lookup_passwordstore


manage passwords with passwordstore.org's pass utility

## Description

Enables Ansible to retrieve, create or update passwords from the passwordstore.org pass utility. It also retrieves YAML style keys stored as multilines in the passwordfile.

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['query key'], 'required': True}",
    "backup": "{'description': ['Used with C(overwrite=yes). Backup the previous password in a subkey.'], 'type': 'bool', 'default': False, 'version_added': 2.7}",
    "create": "{'description': ['Create the password if it does not already exist.'], 'type': 'bool', 'default': False}",
    "directory": "{'description': ['The directory of the password store.'], 'env': [{'name': 'PASSWORD_STORE_DIR'}]}",
    "length": "{'description': ['The length of the generated password'], 'type': 'integer', 'default': 16}",
    "overwrite": "{'description': ['Overwrite the password if it does already exist.'], 'type': 'bool', 'default': False}",
    "passwordstore": "{'description': ['location of the password store'], 'default': '~/.password-store'}",
    "returnall": "{'description': ['Return all the content of the password, not only the first line.'], 'type': 'bool', 'default': False}",
    "subkey": "{'description': ['Return a specific subkey of the password.'], 'default': 'password'}",
    "userpass": "{'description': ['Specify a password to save, instead of a generated one.']}",
}
```

## Examples


``` yaml

# Debug is used for examples, BAD IDEA to show passwords on screen
- name: Basic lookup. Fails if example/test doesn't exist
  debug:
    msg: "{{ lookup('passwordstore', 'example/test')}}"

- name: Create pass with random 16 character password. If password exists just give the password
  debug:
    var: mypassword
  vars:
    mypassword: "{{ lookup('passwordstore', 'example/test create=true')}}"

- name: Different size password
  debug:
    msg: "{{ lookup('passwordstore', 'example/test create=true length=42')}}"

- name: Create password and overwrite the password if it exists. As a bonus, this module includes the old password inside the pass file
  debug:
    msg: "{{ lookup('passwordstore', 'example/test create=true overwrite=true')}}"

- name: Return the value for user in the KV pair user, username
  debug:
    msg: "{{ lookup('passwordstore', 'example/test subkey=user')}}"

- name: Return the entire password file content
  set_fact:
    passfilecontent: "{{ lookup('passwordstore', 'example/test returnall=true')}}"

```

## License

TODO

## Author Information
  - ['Patrick Deelman <patrick@patrickdeelman.nl>']
