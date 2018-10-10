# Ansible module: ansible.module_airbrake_deployment


Notify airbrake about app deployments

## Description

Notify airbrake about app deployments (see http://help.airbrake.io/kb/api-2/deploy-tracking)

## Requirements

TODO

## Arguments

``` json
{
    "environment": "{'description': ["The airbrake environment name, typically 'production', 'staging', etc."], 'required': True}",
    "repo": "{'description': ['URL of the project repository'], 'required': False}",
    "revision": "{'description': ['A hash, number, tag, or other identifier showing what revision was deployed'], 'required': False}",
    "token": "{'description': ['API token.'], 'required': True}",
    "url": "{'description': ['Optional URL to submit the notification to. Use to send notifications to Airbrake-compliant tools like Errbit.'], 'required': False, 'default': 'https://airbrake.io/deploys.txt', 'version_added': '1.5'}",
    "user": "{'description': ['The username of the person doing the deployment'], 'required': False}",
    "validate_certs": "{'description': ['If C(no), SSL certificates for the target url will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'required': False, 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- airbrake_deployment:
    token: AAAAAA
    environment: staging
    user: ansible
    revision: '4.2'

```

## License

TODO

## Author Information
  - ['Bruce Pennypacker (@bpennypacker)']
