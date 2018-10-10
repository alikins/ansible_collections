# Ansible module: ansible.module_tower_job_cancel


Cancel an Ansible Tower Job

## Description

Cancel Ansible Tower jobs. See U(https://www.ansible.com/tower) for an overview.

## Requirements

TODO

## Arguments

``` json
{
    "fail_if_not_running": "{'description': ['Fail loudly if the I(job_id) does not reference a running job.'], 'default': False}",
    "job_id": "{'description': ['ID of the job to cancel'], 'required': True}",
    "tower_config_file": "{'description': ['Path to the Tower config file. See notes.']}",
    "tower_host": "{'description': ['URL to your Tower instance.']}",
    "tower_password": "{'description': ['Password for your Tower instance.']}",
    "tower_username": "{'description': ['Username for your Tower instance.']}",
    "tower_verify_ssl": "{'description': ['Dis/allow insecure connections to Tower. If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Cancel job
  tower_job_cancel:
    job_id: job.id

```

## License

TODO

## Author Information
  - ['Wayne Witzel III (@wwitzel3)']
