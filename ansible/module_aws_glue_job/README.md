# Ansible module: ansible.module_aws_glue_job


Manage an AWS Glue job

## Description

Manage an AWS Glue job. See U(https://aws.amazon.com/glue/) for details.

## Requirements

TODO

## Arguments

``` json
{
    "allocated_capacity": "{'description': ['The number of AWS Glue data processing units (DPUs) to allocate to this Job. From 2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory.'], 'required': False}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "command_name": "{'description': ["The name of the job command. This must be 'glueetl'."], 'required': False, 'default': 'glueetl'}",
    "command_script_location": "{'description': ['The S3 path to a script that executes a job.'], 'required': True}",
    "connections": "{'description': ['A list of Glue connections used for this job.'], 'required': False}",
    "default_arguments": "{'description': ['A dict of default arguments for this job.  You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes.'], 'required': False}",
    "description": "{'description': ['Description of the job being defined.'], 'required': False}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "max_concurrent_runs": "{'description': ['The maximum number of concurrent runs allowed for the job. The default is 1. An error is returned when this threshold is reached. The maximum value you can specify is controlled by a service limit.'], 'required': False}",
    "max_retries": "{'description': ['The maximum number of times to retry this job if it fails.'], 'required': False}",
    "name": "{'description': ['The name you assign to this job definition. It must be unique in your account.'], 'required': True}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "role": "{'description': ['The name or ARN of the IAM role associated with this job.'], 'required': True}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Create or delete the AWS Glue job.'], 'required': True, 'choices': ['present', 'absent']}",
    "timeout": "{'description': ['The job timeout in minutes.'], 'required': False}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Create an AWS Glue job
- aws_glue_job:
    command_script_location: s3bucket/script.py
    name: my-glue-job
    role: my-iam-role
    state: present

# Delete an AWS Glue job
- aws_glue_job:
    name: my-glue-job
    state: absent


```

## License

TODO

## Author Information
  - ['Rob White (@wimnat)']
