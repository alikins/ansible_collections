# Ansible lookup: ansible.lookup_hashi_vault


retrieve secrets from HashiCorp's vault

## Description

retrieve secrets from HashiCorp's vault

## Requirements

TODO

## Arguments

``` json
{
    "auth_method": "{'description': ['authentication method used']}",
    "cacert": "{'description': ['path to certificate to use for authentication']}",
    "mount_point": "{'description': ['vault mount point, only required if you have a custom mount point'], 'default': 'ldap'}",
    "password": "{'description': ['authentication password']}",
    "role_id": "{'description': ['Role id for a vault AppRole auth'], 'env': [{'name': 'VAULT_ROLE_ID'}]}",
    "secret": "{'description': ['query you are making'], 'required': True}",
    "secret_id": "{'description': ['Secret id for a vault AppRole auth'], 'env': [{'name': 'VAULT_SECRET_ID'}]}",
    "token": "{'description': ['vault token'], 'env': [{'name': 'VAULT_TOKEN'}]}",
    "url": "{'description': ['url to vault service'], 'env': [{'name': 'VAULT_ADDR'}], 'default': 'http://127.0.0.1:8200'}",
    "username": "{'description': ['authentication user name']}",
    "validate_certs": "{'description': ['controls verification and validation of SSL certificates, mostly you only want to turn off with self signed ones.'], 'type': 'boolean', 'default': True}",
}
```

## Examples


``` yaml

- debug:
    msg: "{{ lookup('hashi_vault', 'secret=secret/hello:value token=c975b780-d1be-8016-866b-01d0f9b688a5 url=http://myvault:8200')}}"

- name: Return all secrets from a path
  debug:
    msg: "{{ lookup('hashi_vault', 'secret=secret/hello token=c975b780-d1be-8016-866b-01d0f9b688a5 url=http://myvault:8200')}}"

- name: Vault that requires authentication via LDAP
  debug:
      msg: "{{ lookup('hashi_vault', 'secret=secret/hello:value auth_method=ldap mount_point=ldap username=myuser password=mypas url=http://myvault:8200')}}"

- name: Using an ssl vault
  debug:
      msg: "{{ lookup('hashi_vault', 'secret=secret/hola:value token=c975b780-d1be-8016-866b-01d0f9b688a5 url=https://myvault:8200 validate_certs=False')}}"

- name: using certificate auth
  debug:
      msg: "{{ lookup('hashi_vault', 'secret=secret/hi:value token=xxxx-xxx-xxx url=https://myvault:8200 validate_certs=True cacert=/cacert/path/ca.pem')}}"

- name: authenticate with a Vault app role
  debug:
      msg: "{{ lookup('hashi_vault', 'secret=secret/hello:value auth_method=approle role_id=myroleid secret_id=mysecretid url=http://myvault:8200')}}"

```

## License

TODO

## Author Information
  - ['Jonathan Davila <jdavila(at)ansible.com>']
