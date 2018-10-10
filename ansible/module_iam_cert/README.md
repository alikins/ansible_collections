# Ansible module: ansible.module_iam_cert


Manage server certificates for use on ELBs and CloudFront

## Description

Allows for the management of server certificates

## Requirements

TODO

## Arguments

``` json
{
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "cert": "{'description': ['The path to, or content of the certificate body in PEM encoded format. As of 2.4 content is accepted. If the parameter is not a file, it is assumed to be content.']}",
    "cert_chain": "{'description': ['The path to, or content of the CA certificate chain in PEM encoded format. As of 2.4 content is accepted. If the parameter is not a file, it is assumed to be content.']}",
    "dup_ok": "{'description': ['By default the module will not upload a certificate that is already uploaded into AWS. If set to True, it will upload the certificate as long as the name is unique.'], 'default': False}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "key": "{'description': ['The path to, or content of the private key in PEM encoded format. As of 2.4 content is accepted. If the parameter is not a file, it is assumed to be content.']}",
    "name": "{'description': ['Name of certificate to add, update or remove.'], 'required': True}",
    "new_name": "{'description': ['When state is present, this will update the name of the cert.', 'The cert, key and cert_chain parameters will be ignored if this is defined.']}",
    "new_path": "{'description': ['When state is present, this will update the path of the cert.', 'The cert, key and cert_chain parameters will be ignored if this is defined.']}",
    "path": "{'description': ['When creating or updating, specify the desired path of the certificate.'], 'default': '/'}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['Whether to create(or update) or delete certificate.', 'If new_path or new_name is defined, specifying present will attempt to make an update these.'], 'required': True, 'choices': ['present', 'absent']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Basic server certificate upload from local file
- iam_cert:
    name: very_ssl
    state: present
    cert: "{{ lookup('file', 'path/to/cert') }}"
    key: "{{ lookup('file', 'path/to/key') }}"
    cert_chain: "{{ lookup('file', 'path/to/certchain') }}"

# Basic server certificate upload
- iam_cert:
    name: very_ssl
    state: present
    cert: path/to/cert
    key: path/to/key
    cert_chain: path/to/certchain

# Server certificate upload using key string
- iam_cert:
    name: very_ssl
    state: present
    path: "/a/cert/path/"
    cert: body_of_somecert
    key: vault_body_of_privcertkey
    cert_chain: body_of_myverytrustedchain

# Basic rename of existing certificate
- iam_cert:
    name: very_ssl
    new_name: new_very_ssl
    state: present


```

## License

TODO

## Author Information
  - ['Jonathan I. Davila']
