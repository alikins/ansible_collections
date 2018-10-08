# Ansible lookup: ansible.lookup_onepassword


fetch field values from 1Password

## Description

C(onepassword) wraps the C(op) command line utility to fetch specific field values from 1Password.

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['identifier(s) (UUID, name, or subdomain; case-insensitive) of item(s) to retrieve'], 'required': True}",
    "field": "{'description': ['field to return from each matching item (case-insensitive)'], 'default': 'password'}",
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

# These examples only work when already signed in to 1Password
- name: Retrieve password for KITT when already signed in to 1Password
  debug:
    var: lookup('onepassword', 'KITT')

- name: Retrieve password for Wintermute when already signed in to 1Password
  debug:
    var: lookup('onepassword', 'Tessier-Ashpool', section='Wintermute')

- name: Retrieve username for HAL when already signed in to 1Password
  debug:
    var: lookup('onepassword', 'HAL 9000', field='username', vault='Discovery')

- name: Retrieve password for HAL when not signed in to 1Password
  debug:
    var: lookup('onepassword'
                'HAL 9000'
                subdomain='Discovery'
                master_password=vault_master_password)

- name: Retrieve password for HAL when never signed in to 1Password
  debug:
    var: lookup('onepassword'
                'HAL 9000'
                subdomain='Discovery'
                master_password=vault_master_password
                username='tweety@acme.com'
                secret_key=vault_secret_key)

```

## License

TODO

## Author Information
  - ['Scott Buchanan <sbuchanan@ri.pn>', 'Andrew Zenk <azenk@umn.edu>', 'Sam Doran<sdoran@redhat.com>']
  - ['Scott Buchanan <sbuchanan@ri.pn>', 'Andrew Zenk <azenk@umn.edu>', 'Sam Doran<sdoran@redhat.com>']
  - ['Scott Buchanan <sbuchanan@ri.pn>', 'Andrew Zenk <azenk@umn.edu>', 'Sam Doran<sdoran@redhat.com>']
