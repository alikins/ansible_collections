# Ansible module: ansible.module_jenkins_job_facts


Get facts about Jenkins jobs

## Description

This module can be used to query the facts about which Jenkins jobs which already exists.

## Requirements

TODO

## Arguments

``` json
{
    "color": "{'description': ['Only fetch jobs with the given status color.']}",
    "glob": "{'description': ['A shell glob of Jenkins job names to fetch facts about.']}",
    "name": "{'description': ['Exact name of the Jenkins job to fetch facts about.']}",
    "password": "{'description': ['Password to authenticate with the Jenkins server.', 'This is a required parameter, if C(token) is not provided.']}",
    "token": "{'description': ['API token used to authenticate with the Jenkins server.', 'This is a required parameter, if C(password) is not provided.']}",
    "url": "{'description': ['URL where the Jenkins server is accessible.'], 'default': 'http://localhost:8080'}",
    "user": "{'description': ['User to authenticate with the Jenkins server.']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool', 'version_added': '2.6'}",
}
```

## Examples


``` yaml

# Get all Jenkins jobs using basic auth
- jenkins_job_facts:
    user: admin
    password: hunter2
  register: my_jenkins_job_facts

# Get all Jenkins jobs using the token
- jenkins_job_facts:
    user: admin
    token: abcdefghijklmnop
  register: my_jenkins_job_facts

# Get facts about a single job using basic auth
- jenkins_job_facts:
    name: some-job-name
    user: admin
    password: hunter2
  register: my_jenkins_job_facts

# Get facts about a single job in a folder using basic auth
- jenkins_job_facts:
    name: some-folder-name/some-job-name
    user: admin
    password: hunter2
  register: my_jenkins_job_facts

# Get facts about jobs matching a shell glob using basic auth
- jenkins_job_facts:
    glob: some-job-*
    user: admin
    password: hunter2
  register: my_jenkins_job_facts

# Get facts about all failing jobs using basic auth
- jenkins_job_facts:
    color: red
    user: admin
    password: hunter2
  register: my_jenkins_job_facts

# Get facts about passing jobs matching a shell glob using basic auth
- jenkins_job_facts:
    name: some-job-*
    color: blue
    user: admin
    password: hunter2
  register: my_jenkins_job_facts

- name: Get the facts from custom URL with token and validate_certs=False
  jenkins_job_facts:
    user: admin
    token: 126df5c60d66c66e3b75b11104a16a8a
    url: https://jenkins.example.com
    validate_certs: False
  register: my_jenkins_job_facts

```

## License

TODO

## Author Information
  - ['Chris St. Pierre (@stpierre)']
