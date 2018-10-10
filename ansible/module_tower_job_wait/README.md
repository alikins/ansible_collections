# Ansible module: ansible.module_tower_job_wait


Wait for Ansible Tower job to finish

## Description

Wait for Ansible Tower job to finish and report success or failure. See U(https://www.ansible.com/tower) for an overview.

## Requirements

TODO

## Arguments

``` json
{
    "job_id": "{'description': ['ID of the job to monitor.'], 'required': True}",
    "max_interval": "{'description': ['Maximum interval in seconds, to request an update from Tower.'], 'default': 30}",
    "min_interval": "{'description': ['Minimum interval in seconds, to request an update from Tower.'], 'default': 1}",
    "timeout": "{'description': ['Maximum time in seconds to wait for a job to finish.']}",
    "tower_config_file": "{'description': ['Path to the Tower config file. See notes.']}",
    "tower_host": "{'description': ['URL to your Tower instance.']}",
    "tower_password": "{'description': ['Password for your Tower instance.']}",
    "tower_username": "{'description': ['Username for your Tower instance.']}",
    "tower_verify_ssl": "{'description': ['Dis/allow insecure connections to Tower. If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Launch a job
  tower_job_launch:
    job_template: "My Job Template"
    register: job

- name: Wait for job max 120s
  tower_job_wait:
    job_id: job.id
    timeout: 120

```

## License

TODO

## Author Information
  - ['Wayne Witzel III (@wwitzel3)']
