# Ansible lookup: ansible.lookup_onepassword_raw


fetch an entire item from 1Password

## Description

C(onepassword_raw) wraps C(op) command line utility to fetch an entire item from 1Password

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['identifier(s) (UUID, name, or domain; case-insensitive) of item(s) to retrieve'], 'required': True}",
    "master_password": "{'description': ['The password used to unlock the specified vault.'], 'default': 'None', 'version_added': '2.7', 'aliases': ['vault_password']}",
    "secret_key": "{'description': ['The secret key used when performing an initial sign in.'], 'version_added': '2.7'}",
    "section": "{'description': ['Item section containing the field to retrieve (case-insensitive). If absent will return first match from any section.'], 'default': 'None'}",
    "subdomain": "{'description': ['The 1Password subdomain to authenticate against.'], 'default': 'None', 'version_added': '2.7'}",
    "username": "{'description': ['The username used to sign in.'], 'version_added': '2.7'}",
    "vault": "{'description': ['Vault containing the item to retrieve (case-insensitive). If absent will search all vaults'], 'default': 'None'}",
}
```

## Examples


``` yaml

- name: Retrieve all data about Wintermute
  debug:
    var: lookup('onepassword_raw', 'Wintermute')

- name: Retrieve all data about Wintermute when not signed in to 1Password
  debug:
    var: lookup('onepassword_raw', 'Wintermute', subdomain='Turing', vault_password='DmbslfLvasjdl')

```

## License

TODO

## Author Information
  - ['Scott Buchanan <sbuchanan@ri.pn>', 'Andrew Zenk <azenk@umn.edu>', 'Sam Doran <sdoran@redhat.com>']
  - ['Scott Buchanan <sbuchanan@ri.pn>', 'Andrew Zenk <azenk@umn.edu>', 'Sam Doran <sdoran@redhat.com>']
  - ['Scott Buchanan <sbuchanan@ri.pn>', 'Andrew Zenk <azenk@umn.edu>', 'Sam Doran <sdoran@redhat.com>']
