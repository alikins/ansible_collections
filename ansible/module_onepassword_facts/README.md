# Ansible module: ansible.module_onepassword_facts


Gather items from 1Password and set them as facts

## Description

M(onepassword_facts) wraps the C(op) command line utility to fetch data about one or more 1Password items and return as Ansible facts.
A fatal error occurs if any of the items being searched for can not be found.
Recommend using with the C(no_log) option to avoid logging the values of the secrets being retrieved.

## Requirements

TODO

## Arguments

``` json
{
    "auto_login": "{'description': ['A dictionary containing authentication details. If this is set, M(onepassword_facts) will attempt to sign in to 1Password automatically.', 'Without this option, you must have already logged in via the 1Password CLI before running Ansible.', 'It is B(highly) recommened to store 1Password credentials in an Ansible Vault. Ensure that the key used to encrypt the Ansible Vault is equal to or greater in strength than the 1Password master password.'], 'suboptions': {'subdomain': {'description': ['1Password subdomain name (<subdomain>.1password.com).', 'If this is not specified, the most recent subdomain will be used.']}, 'username': {'description': ['1Password username.', 'Only required for initial sign in.']}, 'master_password': {'description': ['The master password for your subdomain.', 'This is always required when specifying C(auto_login).'], 'required': True}, 'secret_key': {'description': ['The secret key for your subdomain.', 'Only required for initial sign in.']}}, 'default': {}, 'required': False}",
    "cli_path": "{'description': ['Used to specify the exact path to the C(op) command line interface'], 'required': False, 'default': 'op'}",
    "search_terms": "{'description': ['A list of one or more search terms.', 'Each search term can either be a simple string or it can be a dictionary for more control.', 'When passing a simple string, I(field) is assumed to be C(password).', 'When passing a dictionary, the following fields are available.'], 'suboptions': {'name': {'description': ['The name of the 1Password item to search for (required).']}, 'field': {'description': ['The name of the field to search for within this item (optional, defaults to "password" (or "document" if the item has an attachment).']}, 'section': {'description': ['The name of a section within this item containing the specified field (optional, will search all sections if not specified).']}, 'vault': {'description': ['The name of the particular 1Password vault to search, useful if your 1Password user has access to multiple vaults (optional).']}}, 'required': True}",
}
```

## Examples


``` yaml

# Gather secrets from 1Password, assuming there is a 'password' field:
- name: Get a password
  onepassword_facts:
    search_terms: My 1Password item
  delegate_to: localhost
  no_log: true         # Don't want to log the secrets to the console!

# Gather secrets from 1Password, with more advanced search terms:
- name: Get a password
  onepassword_facts:
    search_terms:
      - name:    My 1Password item
        field:   Custom field name       # optional, defaults to 'password'
        section: Custom section name     # optional, defaults to 'None'
        vault:   Name of the vault       # optional, only necessary if there is more than 1 Vault available
  delegate_to: localhost
  no_log: True                           # Don't want to log the secrets to the console!

# Gather secrets combining simple and advanced search terms to retrieve two items, one of which we fetch two
# fields. In the first 'password' is fetched, as a field name is not specified (default behaviour) and in the
# second, 'Custom field name' is fetched, as that is specified explicitly.
- name: Get a password
  onepassword_facts:
    search_terms:
      - My 1Password item                # 'name' is optional when passing a simple string...
      - name: My Other 1Password item    # ...but it can also be set for consistency
      - name:    My 1Password item
        field:   Custom field name       # optional, defaults to 'password'
        section: Custom section name     # optional, defaults to 'None'
        vault:   Name of the vault       # optional, only necessary if there is more than 1 Vault available
      - name: A 1Password item with document attachment
  delegate_to: localhost
  no_log: true                           # Don't want to log the secrets to the console!

```

## License

TODO

## Author Information
  - ['Ryan Conway (@rylon)']
