# Ansible module: ansible.module_webfaction_site


Add or remove a website on a Webfaction host

## Description

Add or remove a website on a Webfaction host.  Further documentation at https://github.com/quentinsf/ansible-webfaction.

## Requirements

TODO

## Arguments

``` json
{
    "host": "{'description': ['The webfaction host on which the site should be created.'], 'required': True}",
    "https": "{'description': ['Whether or not to use HTTPS'], 'type': 'bool', 'default': False}",
    "login_name": "{'description': ['The webfaction account to use'], 'required': True}",
    "login_password": "{'description': ['The webfaction password to use'], 'required': True}",
    "name": "{'description': ['The name of the website'], 'required': True}",
    "site_apps": "{'description': ['A mapping of URLs to apps'], 'default': []}",
    "state": "{'description': ['Whether the website should exist'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "subdomains": "{'description': ['A list of subdomains associated with this site.'], 'default': []}",
}
```

## Examples


``` yaml

  - name: create website
    webfaction_site:
      name: testsite1
      state: present
      host: myhost.webfaction.com
      subdomains:
        - 'testsite1.my_domain.org'
      site_apps:
        - ['testapp1', '/']
      https: no
      login_name: "{{webfaction_user}}"
      login_password: "{{webfaction_passwd}}"

```

## License

TODO

## Author Information
  - ['Quentin Stafford-Fraser (@quentinsf)']
