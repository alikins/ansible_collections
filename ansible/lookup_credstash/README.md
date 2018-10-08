# Ansible lookup: ansible.lookup_credstash


retrieve secrets from Credstash on AWS

## Description

Credstash is a small utility for managing secrets using AWS's KMS and DynamoDB: https://github.com/fugue/credstash

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['term or list of terms to lookup in the credit store'], 'type': 'list', 'required': True}",
    "aws_access_key_id": "{'description': ['AWS access key ID'], 'env': [{'name': 'AWS_ACCESS_KEY_ID'}]}",
    "aws_secret_access_key": "{'description': ['AWS access key'], 'env': [{'name': 'AWS_SECRET_ACCESS_KEY'}]}",
    "aws_session_token": "{'description': ['AWS session token'], 'env': [{'name': 'AWS_SESSION_TOKEN'}]}",
    "profile_name": "{'description': ['AWS profile to use for authentication'], 'env': [{'name': 'AWS_PROFILE'}]}",
    "region": "{'description': ['AWS region']}",
    "table": "{'description': ['name of the credstash table to query'], 'default': 'credential-store', 'required': True}",
    "version": "{'description': ['Credstash version']}",
}
```

## Examples


``` yaml

- name: first use credstash to store your secrets
  shell: credstash put my-github-password secure123

- name: "Test credstash lookup plugin -- get my github password"
  debug: msg="Credstash lookup! {{ lookup('credstash', 'my-github-password') }}"

- name: "Test credstash lookup plugin -- get my other password from us-west-1"
  debug: msg="Credstash lookup! {{ lookup('credstash', 'my-other-password', region='us-west-1') }}"

- name: "Test credstash lookup plugin -- get the company's github password"
  debug: msg="Credstash lookup! {{ lookup('credstash', 'company-github-password', table='company-passwords') }}"

- name: Example play using the 'context' feature
  hosts: localhost
  vars:
    context:
      app: my_app
      environment: production
  tasks:

  - name: "Test credstash lookup plugin -- get the password with a context passed as a variable"
    debug: msg="{{ lookup('credstash', 'some-password', context=context) }}"

  - name: "Test credstash lookup plugin -- get the password with a context defined here"
    debug: msg="{{ lookup('credstash', 'some-password', context=dict(app='my_app', environment='production')) }}"

```

## License

TODO

## Author Information
  - ['UNKNOWN']
