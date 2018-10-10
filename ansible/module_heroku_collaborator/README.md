# Ansible module: ansible.module_heroku_collaborator


Add or delete app collaborators on Heroku

## Description

Manages collaborators for Heroku apps.
If set to C(present) and heroku user is already collaborator, then do nothing.
If set to C(present) and heroku user is not collaborator, then add user to app.
If set to C(absent) and heroku user is collaborator, then delete user from app.

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Heroku API key']}",
    "apps": "{'description': ['List of Heroku App names'], 'required': True}",
    "state": "{'description': ['Create or remove the heroku collaborator'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "suppress_invitation": "{'description': ['Suppress email invitation when creating collaborator'], 'type': 'bool', 'default': False}",
    "user": "{'description': ['User ID or e-mail'], 'required': True}",
}
```

## Examples


``` yaml

- heroku_collaborator:
    api_key: YOUR_API_KEY
    user: max.mustermann@example.com
    apps: heroku-example-app
    state: present

- heroku_collaborator:
    api_key: YOUR_API_KEY
    user: '{{ item.user }}'
    apps: '{{ item.apps | default(apps) }}'
    suppress_invitation: '{{ item.suppress_invitation | default(suppress_invitation) }}'
    state: '{{ item.state | default("present") }}'
  with_items:
    - { user: 'a.b@example.com' }
    - { state: 'absent', user: 'b.c@example.com', suppress_invitation: false }
    - { user: 'x.y@example.com', apps: ["heroku-example-app"] }

```

## License

TODO

## Author Information
  - ['Marcel Arns (@marns93)']
