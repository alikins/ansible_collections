# Ansible module: ansible.module_github_release


Interact with GitHub Releases

## Description

Fetch metadata about GitHub Releases

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['Action to perform'], 'required': True, 'choices': ['latest_release', 'create_release']}",
    "body": "{'description': ['Description of the release when creating a release'], 'version_added': 2.4}",
    "draft": "{'description': ['Sets if the release is a draft or not. (boolean)'], 'type': 'bool', 'default': False, 'version_added': 2.4}",
    "name": "{'description': ['Name of release when creating a release'], 'version_added': 2.4}",
    "password": "{'description': ['The GitHub account password for the user'], 'version_added': '2.4'}",
    "prerelease": "{'description': ['Sets if the release is a prerelease or not. (boolean)'], 'type': 'bool', 'default': False, 'version_added': 2.4}",
    "repo": "{'description': ['Repository name'], 'required': True}",
    "tag": "{'description': ['Tag name when creating a release. Required when using action is set to C(create_release).'], 'version_added': 2.4}",
    "target": "{'description': ['Target of release when creating a release'], 'version_added': 2.4}",
    "token": "{'description': ['GitHub Personal Access Token for authenticating']}",
    "user": "{'description': ['The GitHub account that owns the repository'], 'required': True}",
}
```

## Examples


``` yaml

- name: Get latest release of testuseer/testrepo
  github_release:
    token: tokenabc1234567890
    user: testuser
    repo: testrepo
    action: latest_release

- name: Get latest release of test repo using username and password. Ansible 2.4.
  github_release:
    user: testuser
    password: secret123
    repo: testrepo
    action: latest_release

- name: Create a new release
  github_release:
    token: tokenabc1234567890
    user: testuser
    repo: testrepo
    action: create_release
    tag: test
    target: master
    name: My Release
    body: Some description


```

## License

TODO

## Author Information
  - ['Adrian Moisey (@adrianmoisey)']
