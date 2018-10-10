# Ansible module: ansible.module_aws_batch_job_queue


Manage AWS Batch Job Queues

## Description

This module allows the management of AWS Batch Job Queues. It is idempotent and supports "Check" mode.  Use module M(aws_batch_compute_environment) to manage the compute environment, M(aws_batch_job_queue) to manage job queues, M(aws_batch_job_definition) to manage job definitions.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "compute_environment_order": "{'description': ['The set of compute environments mapped to a job queue and their order relative to each other. The job scheduler uses this parameter to determine which compute environment should execute a given job. Compute environments must be in the VALID state before you can associate them with a job queue. You can associate up to 3 compute environments with a job queue.'], 'required': True}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "job_queue_name": "{'description': ['The name for the job queue'], 'required': True}",
    "job_queue_state": "{'description': ['The state of the job queue. If the job queue state is ENABLED , it is able to accept jobs.'], 'default': 'ENABLED', 'choices': ['ENABLED', 'DISABLED']}",
    "priority": "{'description': ['The priority of the job queue. Job queues with a higher priority (or a lower integer value for the priority parameter) are evaluated first when associated with same compute environment. Priority is determined in ascending order, for example, a job queue with a priority value of 1 is given scheduling preference over a job queue with a priority value of 10.'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Describes the desired state.'], 'required': True, 'default': 'present', 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

---
- hosts: localhost
  gather_facts: no
  vars:
    state: present
  tasks:
  - name: My Batch Job Queue
    batch_job_queue:
      job_queue_name: jobQueueName
      state: present
      region: us-east-1
      job_queue_state: ENABLED
      priority: 1
      compute_environment_order:
        - order: 1
          compute_environment: my_compute_env1
        - order: 2
          compute_environment: my_compute_env2

  - name: show results
    debug: var=batch_job_queue_action

```

## License

TODO

## Author Information
  - ['Jon Meran (@jonmer85)']
