# Ansible module: ansible.module_tower_job_list


List Ansible Tower jobs

## Description

List Ansible Tower jobs. See U(https://www.ansible.com/tower) for an overview.

## Requirements

TODO

## Arguments

``` json
{
    "all_pages": "{'description': ['Fetch all the pages and return a single result.'], 'type': 'bool', 'default': False}",
    "page": "{'description': ['Page number of the results to fetch.']}",
    "query": "{'description': ['Query used to further filter the list of jobs. C({"foo":"bar"}) will be passed at C(?foo=bar)']}",
    "status": "{'description': ['Only list jobs with this status.'], 'choices': ['pending', 'waiting', 'running', 'error', 'failed', 'canceled', 'successful']}",
    "tower_config_file": "{'description': ['Path to the Tower config file. See notes.']}",
    "tower_host": "{'description': ['URL to your Tower instance.']}",
    "tower_password": "{'description': ['Password for your Tower instance.']}",
    "tower_username": "{'description': ['Username for your Tower instance.']}",
    "tower_verify_ssl": "{'description': ['Dis/allow insecure connections to Tower. If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: List running jobs for the testing.yml playbook
  tower_job_list:
    status: running
    query: {"playbook": "testing.yml"}
    register: testing_jobs
    tower_config_file: "~/tower_cli.cfg"

```

## License

TODO

## Author Information
  - ['Wayne Witzel III (@wwitzel3)']
