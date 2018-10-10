# Ansible module: ansible.module_webfaction_domain


Add or remove domains and subdomains on Webfaction

## Description

Add or remove domains or subdomains on a Webfaction host. Further documentation at https://github.com/quentinsf/ansible-webfaction.

## Requirements

TODO

## Arguments

``` json
{
    "login_name": "{'description': ['The webfaction account to use'], 'required': True}",
    "login_password": "{'description': ['The webfaction password to use'], 'required': True}",
    "name": "{'description': ['The name of the domain'], 'required': True}",
    "state": "{'description': ['Whether the domain should exist'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "subdomains": "{'description': ['Any subdomains to create.'], 'default': []}",
}
```

## Examples


``` yaml

  - name: Create a test domain
    webfaction_domain:
      name: mydomain.com
      state: present
      subdomains:
       - www
       - blog
      login_name: "{{webfaction_user}}"
      login_password: "{{webfaction_passwd}}"

  - name: Delete test domain and any subdomains
    webfaction_domain:
      name: mydomain.com
      state: absent
      login_name: "{{webfaction_user}}"
      login_password: "{{webfaction_passwd}}"


```

## License

TODO

## Author Information
  - ['Quentin Stafford-Fraser (@quentinsf)']
