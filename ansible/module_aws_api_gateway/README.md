# Ansible module: ansible.module_aws_api_gateway


Manage AWS API Gateway APIs

## Description

Allows for the management of API Gateway APIs
Normally you should give the api_id since there is no other stable guaranteed unique identifier for the API.  If you do not give api_id then a new API will be create each time this is run.
Beware that there are very hard limits on the rate that you can call API Gateway's REST API.  You may need to patch your boto.  See https://github.com/boto/boto3/issues/876 and discuss with your AWS rep.
swagger_file and swagger_text are passed directly on to AWS transparently whilst swagger_dict is an ansible dict which is converted to JSON before the API definitions are uploaded.

## Requirements

TODO

## Arguments

``` json
{
    "api_id": "{'description': ['The ID of the API you want to manage.']}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "deploy_desc": "{'description': ['Description of the deployment - recorded and visible in the AWS console.'], 'default': 'Automatic deployment by Ansible.'}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "stage": "{'description': ['The name of the stage the API should be deployed to.']}",
    "state": "{'description': ['NOT IMPLEMENTED Create or delete API - currently we always create.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "swagger_dict": "{'description': ['Swagger definitions API ansible dictionary which will be converted to JSON and uploaded.']}",
    "swagger_file": "{'description': ['JSON or YAML file containing swagger definitions for API. Exactly one of swagger_file, swagger_text or swagger_dict must be present.']}",
    "swagger_text": "{'description': ['Swagger definitions for API in JSON or YAML as a string direct from playbook.']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Update API resources for development
- name: update API
  aws_api_gateway:
    api_id: 'abc123321cba'
    state: present
    swagger_file: my_api.yml

# update definitions and deploy API to production
- name: deploy API
  aws_api_gateway:
    api_id: 'abc123321cba'
    state: present
    swagger_file: my_api.yml
    stage: production
    deploy_desc: Make auth fix available.

```

## License

TODO

## Author Information
  - ['Michael De La Rue (@mikedlr)']
