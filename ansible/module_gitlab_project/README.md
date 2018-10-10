# Ansible module: ansible.module_gitlab_project


Creates/updates/deletes Gitlab Projects

## Description

When the project does not exist in Gitlab, it will be created.
When the project does exists and state=absent, the project will be deleted.
When changes are made to the project, the project will be updated.

## Requirements

TODO

## Arguments

``` json
{
    "description": "{'description': ['An description for the project.']}",
    "group": "{'description': ['The name of the group of which this projects belongs to.', "When not provided, project will belong to user which is configured in 'login_user' or 'login_token'", "When provided with username, project will be created for this user. 'login_user' or 'login_token' needs admin rights."]}",
    "import_url": "{'description': ['Git repository which will be imported into gitlab.', 'Gitlab server needs read access to this git repository.'], 'type': 'bool', 'default': False}",
    "issues_enabled": "{'description': ['Whether you want to create issues or not.', 'Possible values are true and false.'], 'type': 'bool', 'default': True}",
    "login_password": "{'description': ['Gitlab password for login_user']}",
    "login_token": "{'description': ['Gitlab token for logging in.']}",
    "login_user": "{'description': ['Gitlab user name.']}",
    "merge_requests_enabled": "{'description': ['If merge requests can be made or not.', 'Possible values are true and false.'], 'type': 'bool', 'default': True}",
    "name": "{'description': ['The name of the project'], 'required': True}",
    "path": "{'description': ['The path of the project you want to create, this will be server_url/<group>/path', 'If not supplied, name will be used.']}",
    "public": "{'description': ['If the project is public available or not.', 'Setting this to true is same as setting visibility_level to 20.', 'Possible values are true and false.'], 'type': 'bool', 'default': False}",
    "server_url": "{'description': ['Url of Gitlab server, with protocol (http or https).'], 'required': True}",
    "snippets_enabled": "{'description': ['If creating snippets should be available or not.', 'Possible values are true and false.'], 'type': 'bool', 'default': True}",
    "state": "{'description': ['create or delete project.', 'Possible values are present and absent.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['When using https if SSL certificate needs to be verified.'], 'type': 'bool', 'default': True, 'aliases': ['verify_ssl']}",
    "visibility_level": "{'description': ['Private. visibility_level is 0. Project access must be granted explicitly for each user.', 'Internal. visibility_level is 10. The project can be cloned by any logged in user.', 'Public. visibility_level is 20. The project can be cloned without any authentication.', 'Possible values are 0, 10 and 20.'], 'default': 0}",
    "wiki_enabled": "{'description': ['If an wiki for this project should be available or not.', 'Possible values are true and false.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Delete Gitlab Project
  gitlab_project:
    server_url: http://gitlab.example.com
    validate_certs: False
    login_token: WnUzDsxjy8230-Dy_k
    name: my_first_project
    state: absent
  delegate_to: localhost

- name: Create Gitlab Project in group Ansible
  gitlab_project:
    server_url: https://gitlab.example.com
    validate_certs: True
    login_user: dj-wasabi
    login_password: MySecretPassword
    name: my_first_project
    group: ansible
    issues_enabled: False
    wiki_enabled: True
    snippets_enabled: True
    import_url: http://git.example.com/example/lab.git
    state: present
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Werner Dijkerman (@dj-wasabi)']
