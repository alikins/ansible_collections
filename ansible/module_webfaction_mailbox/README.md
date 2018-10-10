# Ansible module: ansible.module_webfaction_mailbox


Add or remove mailboxes on Webfaction

## Description

Add or remove mailboxes on a Webfaction account. Further documentation at https://github.com/quentinsf/ansible-webfaction.

## Requirements

TODO

## Arguments

``` json
{
    "login_name": "{'description': ['The webfaction account to use'], 'required': True}",
    "login_password": "{'description': ['The webfaction password to use'], 'required': True}",
    "mailbox_name": "{'description': ['The name of the mailbox'], 'required': True}",
    "mailbox_password": "{'description': ['The password for the mailbox'], 'required': True}",
    "state": "{'description': ['Whether the mailbox should exist'], 'choices': ['present', 'absent'], 'default': 'present'}",
}
```

## Examples


``` yaml

  - name: Create a mailbox
    webfaction_mailbox:
      mailbox_name="mybox"
      mailbox_password="myboxpw"
      state=present
      login_name={{webfaction_user}}
      login_password={{webfaction_passwd}}

```

## License

TODO

## Author Information
  - ['Quentin Stafford-Fraser (@quentinsf)']
