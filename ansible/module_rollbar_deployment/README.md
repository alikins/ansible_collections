# Ansible module: ansible.module_rollbar_deployment


Notify Rollbar about app deployments

## Description

Notify Rollbar about app deployments (see https://rollbar.com/docs/deploys_other/)

## Requirements

TODO

## Arguments

``` json
{
    "comment": "{'description': ['Deploy comment (e.g. what is being deployed).'], 'required': False}",
    "environment": "{'description': ["Name of the environment being deployed, e.g. 'production'."], 'required': True}",
    "revision": "{'description': ['Revision number/sha being deployed.'], 'required': True}",
    "rollbar_user": "{'description': ['Rollbar username of the user who deployed.'], 'required': False}",
    "token": "{'description': ['Your project access token.'], 'required': True}",
    "url": "{'description': ['Optional URL to submit the notification to.'], 'required': False, 'default': 'https://api.rollbar.com/api/1/deploy/'}",
    "user": "{'description': ['User who deployed.'], 'required': False}",
    "validate_certs": "{'description': ['If C(no), SSL certificates for the target url will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'required': False, 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- rollbar_deployment:
    token: AAAAAA
    environment: staging
    user: ansible
    revision: '4.2'
    rollbar_user: admin
    comment: Test Deploy

```

## License

TODO

## Author Information
  - ['Max Riveiro (@kavu)']
