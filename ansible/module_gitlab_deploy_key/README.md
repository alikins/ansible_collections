# Ansible module: ansible.module_gitlab_deploy_key


Manages GitLab project deploy keys

## Description

Adds, updates and removes project deploy keys

## Requirements

TODO

## Arguments

``` json
{
    "access_token": "{'description': ['The oauth key provided by GitLab. One of access_token or private_token is required. See https://docs.gitlab.com/ee/api/oauth2.html'], 'required': False}",
    "api_url": "{'description': ['GitLab API url, e.g. https://gitlab.example.com/api'], 'required': True}",
    "can_push": "{'description': ['Whether this key can push to the project'], 'type': 'bool', 'default': False}",
    "key": "{'description': ['Deploy key'], 'required': True}",
    "private_token": "{'description': ['Personal access token to use. One of private_token or access_token is required. See https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html'], 'required': False}",
    "project": "{'description': ['Numeric project id or name of project in the form of group/name'], 'required': True}",
    "state": "{'description': ["When C(present) the deploy key added to the project if it doesn't exist.", 'When C(absent) it will be removed from the project if it exists'], 'required': True, 'default': 'present', 'choices': ['present', 'absent']}",
    "title": "{'description': ["Deploy key's title"], 'required': True}",
}
```

## Examples


``` yaml

# Example adding a project deploy key
- gitlab_deploy_key:
    api_url: https://gitlab.example.com/api
    access_token: "{{ access_token }}"
    project: "my_group/my_project"
    title: "Jenkins CI"
    state: present
    key: "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAIEAiPWx6WM4lhHNedGfBpPJNPpZ7yKu+dnn1SJejgt4596k6YjzGGphH2TUxwKzxcKDKKezwkpfnxPkSMkuEspGRt/aZZ9w..."

# Update the above deploy key to add push access
- gitlab_deploy_key:
    api_url: https://gitlab.example.com/api
    access_token: "{{ access_token }}"
    project: "my_group/my_project"
    title: "Jenkins CI"
    state: present
    key: "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAIEAiPWx6WM4lhHNedGfBpPJNPpZ7yKu+dnn1SJejgt4596k6YjzGGphH2TUxwKzxcKDKKezwkpfnxPkSMkuEspGRt/aZZ9w..."
    can_push: yes

# Remove the previous deploy key from the project
- gitlab_deploy_key:
    api_url: https://gitlab.example.com/api
    access_token: "{{ access_token }}"
    project: "my_group/my_project"
    state: absent
    key: "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAIEAiPWx6WM4lhHNedGfBpPJNPpZ7yKu+dnn1SJejgt4596k6YjzGGphH2TUxwKzxcKDKKezwkpfnxPkSMkuEspGRt/aZZ9w..."


```

## License

TODO

## Author Information
  - ['Marcus Watkins (@marwatk)']
