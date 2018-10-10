# Ansible module: ansible.module_ec2_tag


create and remove tags on ec2 resources

## Description

Creates, removes and lists tags for any EC2 resource.  The resource is referenced by its resource id (e.g. an instance being i-XXXXXXX). It is designed to be used with complex args (tags), see the examples.

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "purge_tags": "{'description': ['Whether unspecified tags should be removed from the resource.', 'Note that when combined with C(state: absent), specified tags with non-matching values are not purged.'], 'type': 'bool', 'default': False, 'version_added': '2.7'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "resource": "{'description': ['The EC2 resource id.'], 'required': True}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Whether the tags should be present or absent on the resource. Use list to interrogate the tags of an instance.'], 'default': 'present', 'choices': ['present', 'absent', 'list']}",
    "tags": "{'description': ['a hash/dictionary of tags to add to the resource; \'{"key":"value"}\' and \'{"key":"value","key":"value"}\''], 'required': True}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

- name: Ensure tags are present on a resource
  ec2_tag:
    region: eu-west-1
    resource: vol-XXXXXX
    state: present
    tags:
      Name: ubervol
      env: prod

- name: Ensure all volumes are tagged
  ec2_tag:
    region:  eu-west-1
    resource: '{{ item.id }}'
    state: present
    tags:
      Name: dbserver
      Env: production
  with_items: '{{ ec2_vol.volumes }}'

- name: Retrieve all tags on an instance
  ec2_tag:
    region: eu-west-1
    resource: i-xxxxxxxxxxxxxxxxx
    state: list
  register: ec2_tags

- name: Remove all tags except for Name from an instance
  ec2_tag:
    region: eu-west-1
    resource: i-xxxxxxxxxxxxxxxxx
    tags:
        Name: ''
    state: absent
    purge_tags: true

```

## License

TODO

## Author Information
  - ['Lester Wade (@lwade)', 'Paul Arthur (@flowerysong)']
  - ['Lester Wade (@lwade)', 'Paul Arthur (@flowerysong)']
