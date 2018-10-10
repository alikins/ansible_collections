# Ansible module: ansible.module_honeybadger_deployment


Notify Honeybadger.io about app deployments

## Description

Notify Honeybadger.io about app deployments (see http://docs.honeybadger.io/article/188-deployment-tracking)

## Requirements

TODO

## Arguments

``` json
{
    "environment": "{'description': ["The environment name, typically 'production', 'staging', etc."], 'required': True}",
    "repo": "{'description': ['URL of the project repository']}",
    "revision": "{'description': ['A hash, number, tag, or other identifier showing what revision was deployed']}",
    "token": "{'description': ['API token.'], 'required': True}",
    "url": "{'description': ['Optional URL to submit the notification to.'], 'default': 'https://api.honeybadger.io/v1/deploys'}",
    "user": "{'description': ['The username of the person doing the deployment']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates for the target url will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- honeybadger_deployment:
    token: AAAAAA
    environment: staging
    user: ansible
    revision: b6826b8
    repo: 'git@github.com:user/repo.git'

```

## License

TODO

## Author Information
  - ['Benjamin Curtis (@stympy)']
