# Ansible module: ansible.module_webfaction_app


Add or remove applications on a Webfaction host

## Description

Add or remove applications on a Webfaction host. Further documentation at U(https://github.com/quentinsf/ansible-webfaction).

## Requirements

TODO

## Arguments

``` json
{
    "autostart": "{'description': ['Whether the app should restart with an C(autostart.cgi) script'], 'type': 'bool', 'default': False}",
    "extra_info": "{'description': ['Any extra parameters required by the app'], 'default': ''}",
    "login_name": "{'description': ['The webfaction account to use'], 'required': True}",
    "login_password": "{'description': ['The webfaction password to use'], 'required': True}",
    "machine": "{'description': ['The machine name to use (optional for accounts with only one machine)']}",
    "name": "{'description': ['The name of the application'], 'required': True}",
    "port_open": "{'description': ['IF the port should be opened'], 'type': 'bool', 'default': False}",
    "state": "{'description': ['Whether the application should exist'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "type": "{'description': ['The type of application to create. See the Webfaction docs at U(https://docs.webfaction.com/xmlrpc-api/apps.html) for a list.'], 'required': True}",
}
```

## Examples


``` yaml

  - name: Create a test app
    webfaction_app:
      name: "my_wsgi_app1"
      state: present
      type: mod_wsgi35-python27
      login_name: "{{webfaction_user}}"
      login_password: "{{webfaction_passwd}}"
      machine: "{{webfaction_machine}}"

```

## License

TODO

## Author Information
  - ['Quentin Stafford-Fraser (@quentinsf)']
