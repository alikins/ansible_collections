# Ansible module: ansible.module_data_pipeline


Create and manage AWS Datapipelines

## Description

Create and manage AWS Datapipelines. Creation is not idempotent in AWS, so the I(uniqueId) is created by hashing the options (minus objects) given to the datapipeline.
The pipeline definition must be in the format given here U(http://docs.aws.amazon.com/datapipeline/latest/APIReference/API_PutPipelineDefinition.html#API_PutPipelineDefinition_RequestSyntax).
Also operations will wait for a configurable amount of time to ensure the pipeline is in the requested state.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "description": "{'description': ['An optional description for the pipeline being created.'], 'default': ''}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "name": "{'description': ['The name of the Datapipeline to create/modify/delete.'], 'required': True}",
    "objects": "{'description': ['A list of pipeline object definitions, each of which is a dict that takes the keys C(id), C(name) and C(fields).'], 'suboptions': {'id': {'description': ['The ID of the object.']}, 'name': {'description': ['The name of the object.']}, 'fields': {'description': ['A list of dicts that take the keys C(key) and C(stringValue)/C(refValue). The value is specified as a reference to another object C(refValue) or as a string value C(stringValue) but not as both.']}}}",
    "parameters": "{'description': ['A list of parameter objects (dicts) in the pipeline definition.'], 'suboptions': {'id': {'description': ['The ID of the parameter object.']}, 'attributes': {'description': ['A list of attributes (dicts) of the parameter object. Each attribute takes the keys C(key) and C(stringValue) both of which are strings.']}}}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['The requested state of the pipeline.'], 'choices': ['present', 'absent', 'active', 'inactive'], 'default': 'present'}",
    "tags": "{'description': ['A dict of key:value pair(s) to add to the pipeline.']}",
    "timeout": "{'description': ['Time in seconds to wait for the pipeline to transition to the requested state, fail otherwise.'], 'default': 300}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "values": "{'description': ['A list of parameter values (dicts) in the pipeline definition. Each dict takes the keys C(id) and C(stringValue) both of which are strings.']}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Create pipeline
- data_pipeline:
    name: test-dp
    region: us-west-2
    objects: "{{pipelineObjects}}"
    parameters: "{{pipelineParameters}}"
    values: "{{pipelineValues}}"
    tags:
      key1: val1
      key2: val2
    state: present

# Example populating and activating a pipeline that demonstrates two ways of providing pipeline objects
- data_pipeline:
  name: test-dp
  objects:
    - "id": "DefaultSchedule"
      "name": "Every 1 day"
      "fields":
        - "key": "period"
          "stringValue": "1 days"
        - "key": "type"
          "stringValue": "Schedule"
        - "key": "startAt"
          "stringValue": "FIRST_ACTIVATION_DATE_TIME"
    - "id": "Default"
      "name": "Default"
      "fields": [ { "key": "resourceRole", "stringValue": "my_resource_role" },
                  { "key": "role", "stringValue": "DataPipelineDefaultRole" },
                  { "key": "pipelineLogUri", "stringValue": "s3://my_s3_log.txt" },
                  { "key": "scheduleType", "stringValue": "cron" },
                  { "key": "schedule", "refValue": "DefaultSchedule" },
                  { "key": "failureAndRerunMode", "stringValue": "CASCADE" } ]
  state: active

# Activate pipeline
- data_pipeline:
    name: test-dp
    region: us-west-2
    state: active

# Delete pipeline
- data_pipeline:
    name: test-dp
    region: us-west-2
    state: absent


```

## License

TODO

## Author Information
  - ['Raghu Udiyar <raghusiddarth@gmail.com> (@raags)', 'Sloane Hertel <shertel@redhat.com>']
  - ['Raghu Udiyar <raghusiddarth@gmail.com> (@raags)', 'Sloane Hertel <shertel@redhat.com>']
