# Ansible module: ansible.module_tower_job_launch


Launch an Ansible Job

## Description

Launch an Ansible Tower jobs. See U(https://www.ansible.com/tower) for an overview.

## Requirements

TODO

## Arguments

``` json
{
    "credential": "{'description': ['Credential to use for job, only used if prompt for credential is set.']}",
    "extra_vars": "{'description': ['Extra_vars to use for the job_template. Prepend C(@) if a file.']}",
    "inventory": "{'description': ['Inventory to use for the job, only used if prompt for inventory is set.']}",
    "job_explanation": "{'description': ['Job explanation field.']}",
    "job_template": "{'description': ['Name of the job template to use.'], 'required': True}",
    "job_type": "{'description': ['Job_type to use for the job, only used if prompt for job_type is set.'], 'choices': ['run', 'check', 'scan']}",
    "limit": "{'description': ['Limit to use for the I(job_template).']}",
    "tags": "{'description': ['Specific tags to use for from playbook.']}",
    "tower_config_file": "{'description': ['Path to the Tower config file. See notes.']}",
    "tower_host": "{'description': ['URL to your Tower instance.']}",
    "tower_password": "{'description': ['Password for your Tower instance.']}",
    "tower_username": "{'description': ['Username for your Tower instance.']}",
    "tower_verify_ssl": "{'description': ['Dis/allow insecure connections to Tower. If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
    "use_job_endpoint": "{'description': ['Disable launching jobs from job template.'], 'type': 'bool', 'default': False}",
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
