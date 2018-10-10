# Ansible module: ansible.module_tower_job_template


create, update, or destroy Ansible Tower job template

## Description

Create, update, or destroy Ansible Tower job templates. See U(https://www.ansible.com/tower) for an overview.

## Requirements

TODO

## Arguments

``` json
{
    "ask_credential": "{'description': ['Prompt user for credential on launch.'], 'type': 'bool', 'default': False}",
    "ask_diff_mode": "{'description': ['Prompt user to enable diff mode (show changes) to files when supported by modules.'], 'version_added': 2.7, 'type': 'bool', 'default': False}",
    "ask_extra_vars": "{'description': ['Prompt user for (extra_vars) on launch.'], 'type': 'bool', 'default': False}",
    "ask_inventory": "{'description': ['Propmt user for inventory on launch.'], 'type': 'bool', 'default': False}",
    "ask_job_type": "{'description': ['Prompt user for job type on launch.'], 'type': 'bool', 'default': False}",
    "ask_limit": "{'description': ['Prompt user for a limit on launch.'], 'version_added': 2.7, 'type': 'bool', 'default': False}",
    "ask_skip_tags": "{'description': ['Prompt user for job tags to skip on launch.'], 'version_added': 2.7, 'type': 'bool', 'default': False}",
    "ask_tags": "{'description': ['Prompt user for job tags on launch.'], 'type': 'bool', 'default': False}",
    "ask_verbosity": "{'description': ['Prompt user to choose a verbosity level on launch.'], 'version_added': 2.7, 'type': 'bool', 'default': False}",
    "become_enabled": "{'description': ['Activate privilege escalation.'], 'type': 'bool', 'default': False}",
    "concurrent_jobs_enabled": "{'description': ['Allow simultaneous runs of the job template.'], 'version_added': 2.7, 'type': 'bool', 'default': False}",
    "credential": "{'description': ['Name of the credential to use for the job template.'], 'version_added': 2.7}",
    "description": "{'description': ['Description to use for the job template.']}",
    "extra_vars_path": "{'description': ['Path to the C(extra_vars) YAML file.']}",
    "fact_caching_enabled": "{'description': ['Enable use of fact caching for the job template.'], 'version_added': 2.7, 'type': 'bool', 'default': False}",
    "force_handlers_enabled": "{'description': ['Enable forcing playbook handlers to run even if a task fails.'], 'version_added': 2.7, 'type': 'bool', 'default': False}",
    "forks": "{'description': ['The number of parallel or simultaneous processes to use while executing the playbook.']}",
    "host_config_key": "{'description': ['Allow provisioning callbacks using this host config key.']}",
    "inventory": "{'description': ['Name of the inventory to use for the job template.']}",
    "job_tags": "{'description': ['Comma separated list of the tags to use for the job template.']}",
    "job_type": "{'description': ['The job type to use for the job template.'], 'required': True, 'choices': ['run', 'check', 'scan']}",
    "limit": "{'description': ['A host pattern to further constrain the list of hosts managed or affected by the playbook']}",
    "name": "{'description': ['Name to use for the job template.'], 'required': True}",
    "playbook": "{'description': ['Path to the playbook to use for the job template within the project provided.'], 'required': True}",
    "project": "{'description': ['Name of the project to use for the job template.'], 'required': True}",
    "skip_tags": "{'description': ['Comma separated list of the tags to skip for the job template.']}",
    "start_at_task": "{'description': ['Start the playbook at the task matching this name.'], 'version_added': 2.7}",
    "state": "{'description': ['Desired state of the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "survey_enabled": "{'description': ['Enable a survey on the job template.'], 'version_added': 2.7, 'type': 'bool', 'default': False}",
    "tower_config_file": "{'description': ['Path to the Tower config file. See notes.']}",
    "tower_host": "{'description': ['URL to your Tower instance.']}",
    "tower_password": "{'description': ['Password for your Tower instance.']}",
    "tower_username": "{'description': ['Username for your Tower instance.']}",
    "tower_verify_ssl": "{'description': ['Dis/allow insecure connections to Tower. If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
    "vault_credential": "{'description': ['Name of the vault credential to use for the job template.'], 'version_added': 2.7}",
    "verbosity": "{'description': ['Control the output level Ansible produces as the playbook runs. 0 - Normal, 1 - Verbose, 2 - More Verbose, 3 - Debug, 4 - Connection Debug.'], 'choices': [0, 1, 2, 3, 4], 'default': 0}",
}
```

## Examples


``` yaml

- name: Create tower Ping job template
  tower_job_template:
    name: "Ping"
    job_type: "run"
    inventory: "Local"
    project: "Demo"
    playbook: "ping.yml"
    credential: "Local"
    state: "present"
    tower_config_file: "~/tower_cli.cfg"

```

## License

TODO

## Author Information
  - ['Wayne Witzel III (@wwitzel3)']
