# Ansible module: ansible.module_gitlab_hooks


Manages GitLab project hooks

## Description

Adds, updates and removes project hooks

## Requirements

TODO

## Arguments

``` json
{
    "access_token": "{'description': ['The oauth key provided by GitLab. One of access_token or private_token is required. See https://docs.gitlab.com/ee/api/oauth2.html'], 'required': False}",
    "api_url": "{'description': ['GitLab API url, e.g. https://gitlab.example.com/api'], 'required': True}",
    "enable_ssl_verification": "{'description': ['Whether GitLab will do SSL verification when triggering the hook'], 'type': 'bool', 'default': False}",
    "hook_url": "{'description': ['The url that you want GitLab to post to, this is used as the primary key for updates and deletion.'], 'required': True}",
    "issues_events": "{'description': ['Trigger hook on issues events'], 'type': 'bool', 'default': False}",
    "job_events": "{'description': ['Trigger hook on job events'], 'type': 'bool', 'default': False}",
    "merge_requests_events": "{'description': ['Trigger hook on merge requests events'], 'type': 'bool', 'default': False}",
    "note_events": "{'description': ['Trigger hook on note events'], 'type': 'bool', 'default': False}",
    "pipeline_events": "{'description': ['Trigger hook on pipeline events'], 'type': 'bool', 'default': False}",
    "private_token": "{'description': ['Personal access token to use. One of private_token or access_token is required. See https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html'], 'required': False}",
    "project": "{'description': ['Numeric project id or name of project in the form of group/name'], 'required': True}",
    "push_events": "{'description': ['Trigger hook on push events'], 'type': 'bool', 'default': True}",
    "state": "{'description': ["When C(present) the hook will be updated to match the input or created if it doesn't exist. When C(absent) it will be deleted if it exists."], 'required': True, 'default': 'present', 'choices': ['present', 'absent']}",
    "tag_push_events": "{'description': ['Trigger hook on tag push events'], 'type': 'bool', 'default': False}",
    "token": "{'description': ['Secret token to validate hook messages at the receiver.', 'If this is present it will always result in a change as it cannot be retrieved from GitLab.', 'Will show up in the X-Gitlab-Token HTTP request header'], 'required': False}",
    "wiki_page_events": "{'description': ['Trigger hook on wiki events'], 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

# Example creating a new project hook
- gitlab_hooks:
    api_url: https://gitlab.example.com/api
    access_token: "{{ access_token }}"
    project: "my_group/my_project"
    hook_url: "https://my-ci-server.example.com/gitlab-hook"
    state: present
    push_events: yes
    enable_ssl_verification: no
    token: "my-super-secret-token-that-my-ci-server-will-check"

# Update the above hook to add tag pushes
- gitlab_hooks:
    api_url: https://gitlab.example.com/api
    access_token: "{{ access_token }}"
    project: "my_group/my_project"
    hook_url: "https://my-ci-server.example.com/gitlab-hook"
    state: present
    push_events: yes
    tag_push_events: yes
    enable_ssl_verification: no
    token: "my-super-secret-token-that-my-ci-server-will-check"

# Delete the previous hook
- gitlab_hooks:
    api_url: https://gitlab.example.com/api
    access_token: "{{ access_token }}"
    project: "my_group/my_project"
    hook_url: "https://my-ci-server.example.com/gitlab-hook"
    state: absent

# Delete a hook by numeric project id
- gitlab_hooks:
    api_url: https://gitlab.example.com/api
    access_token: "{{ access_token }}"
    project: 10
    hook_url: "https://my-ci-server.example.com/gitlab-hook"
    state: absent

```

## License

TODO

## Author Information
  - ['Marcus Watkins (@marwatk)']
