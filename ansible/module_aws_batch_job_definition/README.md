# Ansible module: ansible.module_aws_batch_job_definition


Manage AWS Batch Job Definitions

## Description

This module allows the management of AWS Batch Job Definitions. It is idempotent and supports "Check" mode.  Use module M(aws_batch_compute_environment) to manage the compute environment, M(aws_batch_job_queue) to manage job queues, M(aws_batch_job_definition) to manage job definitions.

## Requirements

TODO

## Arguments

``` json
{
    "attempts": "{'description': ['Retry strategy - The number of times to move a job to the RUNNABLE status. You may specify between 1 and 10 attempts. If attempts is greater than one, the job is retried if it fails until it has moved to RUNNABLE that many times.']}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "command": "{'description': ['The command that is passed to the container. This parameter maps to Cmd in the Create a container section of the Docker Remote API and the COMMAND parameter to docker run. For more information, see https://docs.docker.com/engine/reference/builder/#cmd.']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "environment": "{'description': ['The environment variables to pass to a container. This parameter maps to Env in the Create a container section of the Docker Remote API and the --env option to docker run. List of dictionaries.'], 'suboptions': {'name': {'description': ['The name of the key value pair. For environment variables, this is the name of the environment variable.']}, 'value': {'description': ['The value of the key value pair. For environment variables, this is the value of the environment variable.']}}}",
    "image": "{'description': ['The image used to start a container. This string is passed directly to the Docker daemon. Images in the Docker Hub registry are available by default. Other repositories are specified with `` repository-url /image <colon>tag ``. Up to 255 letters (uppercase and lowercase), numbers, hyphens, underscores, colons, periods, forward slashes, and number signs are allowed. This parameter maps to Image in the Create a container section of the Docker Remote API and the IMAGE parameter of docker run.']}",
    "job_definition_arn": "{'description': ['The arn for the job definition']}",
    "job_definition_name": "{'description': ['The name for the job definition'], 'required': True}",
    "job_role_arn": "{'description': ['The Amazon Resource Name (ARN) of the IAM role that the container can assume for AWS permissions.']}",
    "memory": "{'description': ['The hard limit (in MiB) of memory to present to the container. If your container attempts to exceed the memory specified here, the container is killed. This parameter maps to Memory in the Create a container section of the Docker Remote API and the --memory option to docker run.']}",
    "mount_points": "{'description': ['The mount points for data volumes in your container. This parameter maps to Volumes in the Create a container section of the Docker Remote API and the --volume option to docker run. List of dictionaries.'], 'suboptions': {'containerPath': {'description': ['The path on the container at which to mount the host volume.']}, 'readOnly': {'description': ['If this value is true , the container has read-only access to the volume; otherwise, the container can write to the volume. The default value is false.']}, 'sourceVolume': {'description': ['The name of the volume to mount.']}}}",
    "parameters": "{'description': ['Default parameter substitution placeholders to set in the job definition. Parameters are specified as a key-value pair mapping. Parameters in a SubmitJob request override any corresponding parameter defaults from the job definition.']}",
    "privileged": "{'description': ['When this parameter is true, the container is given elevated privileges on the host container instance (similar to the root user). This parameter maps to Privileged in the Create a container section of the Docker Remote API and the --privileged option to docker run.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "readonly_root_filesystem": "{'description': ['When this parameter is true, the container is given read-only access to its root file system. This parameter maps to ReadonlyRootfs in the Create a container section of the Docker Remote API and the --read-only option to docker run.']}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Describes the desired state.'], 'required': True, 'default': 'present', 'choices': ['present', 'absent']}",
    "type": "{'description': ['The type of job definition'], 'required': True}",
    "ulimits": "{'description': ['A list of ulimits to set in the container. This parameter maps to Ulimits in the Create a container section of the Docker Remote API and the --ulimit option to docker run. List of dictionaries.'], 'suboptions': {'hardLimit': {'description': ['The hard limit for the ulimit type.']}, 'name': {'description': ['The type of the ulimit.']}, 'softLimit': {'description': ['The soft limit for the ulimit type.']}}}",
    "user": "{'description': ['The user name to use inside the container. This parameter maps to User in the Create a container section of the Docker Remote API and the --user option to docker run.']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "vcpus": "{'description': ['The number of vCPUs reserved for the container. This parameter maps to CpuShares in the Create a container section of the Docker Remote API and the --cpu-shares option to docker run. Each vCPU is equivalent to 1,024 CPU shares.']}",
    "volumes": "{'description': ['A list of data volumes used in a job. List of dictionaries.'], 'suboptions': {'host': {'description': ['The contents of the host parameter determine whether your data volume persists on the host container instance and where it is stored. If the host parameter is empty, then the Docker daemon assigns a host path for your data volume, but the data is not guaranteed to persist after the containers associated with it stop running. This is a dictionary with one property, sourcePath - The path on the host container instance that is presented to the container. If this parameter is empty,then the Docker daemon has assigned a host path for you. If the host parameter contains a sourcePath file location, then the data volume persists at the specified location on the host container instance until you delete it manually. If the sourcePath value does not exist on the host container instance, the Docker daemon creates it. If the location does exist, the contents of the source path folder are exported.']}, 'name': {'description': ['The name of the volume. Up to 255 letters (uppercase and lowercase), numbers, hyphens, and underscores are allowed. This name is referenced in the sourceVolume parameter of container definition mountPoints.']}}}",
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
- name: My Batch Job Definition
  batch_job_definition:
    job_definition_name: My Batch Job Definition
    state: present
    type: container
    parameters:
      Param1: Val1
      Param2: Val2
    image: <Docker Image URL>
    vcpus: 1
    memory: 512
    command:
      - python
      - run_my_script.py
      - arg1
    job_role_arn: <Job Role ARN>
    attempts: 3
  register: job_definition_create_result

- name: show results
  debug: var=job_definition_create_result

```

## License

TODO

## Author Information
  - ['Jon Meran (@jonmer85)']
