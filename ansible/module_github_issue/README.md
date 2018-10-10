# Ansible module: ansible.module_github_issue


View GitHub issue

## Description

View GitHub issue for a given repository.

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['Get various details about issue depending upon action specified.'], 'default': 'get_status', 'choices': [['get_status']]}",
    "issue": "{'description': ['Issue number for which information is required.'], 'required': True}",
    "organization": "{'description': ['Name of the GitHub organization in which the repository is hosted.'], 'required': True}",
    "repo": "{'description': ['Name of repository from which issue needs to be retrieved.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Check if GitHub issue is closed or not
  github_issue:
    organization: ansible
    repo: ansible
    issue: 23642
    action: get_status
  register: r

- name: Take action depending upon issue status
  debug:
    msg: Do something when issue 23642 is open
  when: r.issue_status == 'open'

```

## License

TODO

## Author Information
  - ['Abhijeet Kasurde (@Akasurde)']
