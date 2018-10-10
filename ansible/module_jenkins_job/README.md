# Ansible module: ansible.module_jenkins_job


Manage jenkins jobs

## Description

Manage Jenkins jobs by using Jenkins REST API.

## Requirements

TODO

## Arguments

``` json
{
    "config": "{'description': ['config in XML format.', 'Required if job does not yet exist.', 'Mutually exclusive with C(enabled).', 'Considered if C(state=present).'], 'required': False}",
    "enabled": "{'description': ['Whether the job should be enabled or disabled.', 'Mutually exclusive with C(config).', 'Considered if C(state=present).'], 'type': 'bool', 'required': False}",
    "name": "{'description': ['Name of the Jenkins job.'], 'required': True}",
    "password": "{'description': ['Password to authenticate with the Jenkins server.'], 'required': False}",
    "state": "{'description': ['Attribute that specifies if the job has to be created or deleted.'], 'required': False, 'default': 'present', 'choices': ['present', 'absent']}",
    "token": "{'description': ['API token used to authenticate alternatively to password.'], 'required': False}",
    "url": "{'description': ['URL where the Jenkins server is accessible.'], 'required': False, 'default': 'http://localhost:8080'}",
    "user": "{'description': ['User to authenticate with the Jenkins server.'], 'required': False}",
}
```

## Examples


``` yaml

# Create a jenkins job using basic authentication
- jenkins_job:
    config: "{{ lookup('file', 'templates/test.xml') }}"
    name: test
    password: admin
    url: http://localhost:8080
    user: admin

# Create a jenkins job using the token
- jenkins_job:
    config: "{{ lookup('template', 'templates/test.xml.j2') }}"
    name: test
    token: asdfasfasfasdfasdfadfasfasdfasdfc
    url: http://localhost:8080
    user: admin

# Delete a jenkins job using basic authentication
- jenkins_job:
    name: test
    password: admin
    state: absent
    url: http://localhost:8080
    user: admin

# Delete a jenkins job using the token
- jenkins_job:
    name: test
    token: asdfasfasfasdfasdfadfasfasdfasdfc
    state: absent
    url: http://localhost:8080
    user: admin

# Disable a jenkins job using basic authentication
- jenkins_job:
    name: test
    password: admin
    enabled: False
    url: http://localhost:8080
    user: admin

# Disable a jenkins job using the token
- jenkins_job:
    name: test
    token: asdfasfasfasdfasdfadfasfasdfasdfc
    enabled: False
    url: http://localhost:8080
    user: admin

```

## License

TODO

## Author Information
  - ['Sergio Millan Rodriguez (@sermilrod)']
