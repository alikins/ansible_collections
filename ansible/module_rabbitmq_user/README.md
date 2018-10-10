# Ansible module: ansible.module_rabbitmq_user


Adds or removes users to RabbitMQ

## Description

Add or remove users to RabbitMQ and assign permissions

## Requirements

TODO

## Arguments

``` json
{
    "configure_priv": "{'description': ['Regular expression to restrict configure actions on a resource for the specified vhost.', 'By default all actions are restricted.', 'This option will be ignored when permissions option is used.'], 'default': '^$'}",
    "force": "{'description': ['Deletes and recreates the user.'], 'type': 'bool', 'default': False}",
    "node": "{'description': ['erlang node name of the rabbit we wish to configure'], 'default': 'rabbit'}",
    "password": "{'description': ['Password of user to add.', 'To change the password of an existing user, you must also specify C(update_password=always).']}",
    "permissions": "{'description': ['a list of dicts, each dict contains vhost, configure_priv, write_priv, and read_priv, and represents a permission rule for that vhost.', 'This option should be preferable when you care about all permissions of the user.', 'You should use vhost, configure_priv, write_priv, and read_priv options instead if you care about permissions for just some vhosts.'], 'default': []}",
    "read_priv": "{'description': ['Regular expression to restrict configure actions on a resource for the specified vhost.', 'By default all actions are restricted.', 'This option will be ignored when permissions option is used.'], 'default': '^$'}",
    "state": "{'description': ['Specify if user is to be added or removed'], 'default': 'present', 'choices': ['present', 'absent']}",
    "tags": "{'description': ['User tags specified as comma delimited']}",
    "update_password": "{'description': ['C(on_create) will only set the password for newly created users.  C(always) will update passwords if they differ.'], 'required': False, 'default': 'on_create', 'choices': ['on_create', 'always'], 'version_added': '2.6'}",
    "user": "{'description': ['Name of user to add'], 'required': True, 'aliases': ['username', 'name']}",
    "vhost": "{'description': ['vhost to apply access privileges.', 'This option will be ignored when permissions option is used.'], 'default': '/'}",
    "write_priv": "{'description': ['Regular expression to restrict configure actions on a resource for the specified vhost.', 'By default all actions are restricted.', 'This option will be ignored when permissions option is used.'], 'default': '^$'}",
}
```

## Examples


``` yaml

# Add user to server and assign full access control on / vhost.
# The user might have permission rules for other vhost but you don't care.
- rabbitmq_user:
    user: joe
    password: changeme
    vhost: /
    configure_priv: .*
    read_priv: .*
    write_priv: .*
    state: present

# Add user to server and assign full access control on / vhost.
# The user doesn't have permission rules for other vhosts
- rabbitmq_user:
    user: joe
    password: changeme
    permissions:
      - vhost: /
        configure_priv: .*
        read_priv: .*
        write_priv: .*
    state: present

```

## License

TODO

## Author Information
  - ['"Chris Hoffman (@chrishoffman)"']
