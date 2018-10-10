# Ansible module: ansible.module_newrelic_deployment


Notify newrelic about app deployments

## Description

Notify newrelic about app deployments (see https://docs.newrelic.com/docs/apm/new-relic-apm/maintenance/deployment-notifications#api)

## Requirements

TODO

## Arguments

``` json
{
    "app_name": "{'description': ['(one of app_name or application_id are required) The value of app_name in the newrelic.yml file used by the application'], 'required': False}",
    "application_id": "{'description': ['(one of app_name or application_id are required) The application id, found in the URL when viewing the application in RPM'], 'required': False}",
    "appname": "{'description': ['Name of the application'], 'required': False}",
    "changelog": "{'description': ['A list of changes for this deployment'], 'required': False}",
    "description": "{'description': ['Text annotation for the deployment - notes for you'], 'required': False}",
    "environment": "{'description': ['The environment for this deployment'], 'required': False}",
    "revision": "{'description': ['A revision number (e.g., git commit SHA)'], 'required': False}",
    "token": "{'description': ['API token, to place in the x-api-key header.'], 'required': True}",
    "user": "{'description': ['The name of the user/process that triggered this deployment'], 'required': False}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'required': False, 'default': True, 'type': 'bool', 'version_added': '1.5.1'}",
}
```

## Examples


``` yaml

- newrelic_deployment:
    token: AAAAAA
    app_name: myapp
    user: ansible deployment
    revision: '1.0'

```

## License

TODO

## Author Information
  - ['Matt Coddington (@mcodd)']
