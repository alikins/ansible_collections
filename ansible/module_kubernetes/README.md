# Ansible module: ansible.module_kubernetes


Manage Kubernetes resources

## Description

This module can manage Kubernetes resources on an existing cluster using the Kubernetes server API. Users can specify in-line API data, or specify an existing Kubernetes YAML file.
Currently, this module (1) Only supports HTTP Basic Auth (2) Only supports 'strategic merge' for update, http://goo.gl/fCPYxT SSL certs are not working, use C(validate_certs=off) to disable.

## Requirements

TODO

## Arguments

``` json
{
    "api_endpoint": "{'description': ['The IPv4 API endpoint of the Kubernetes cluster.'], 'required': True, 'aliases': ['endpoint']}",
    "certificate_authority_data": "{'description': ["Certificate Authority data for Kubernetes server. Should be in either standard PEM format or base64 encoded PEM data. Note that certificate verification is broken until ansible supports a version of 'match_hostname' that can match the IP address against the CA data."]}",
    "file_reference": "{'description': ["Specify full path to a Kubernets YAML file to send to API I(endpoint). This option is mutually exclusive with C('inline_data')."]}",
    "inline_data": "{'description': ["The Kubernetes YAML data to send to the API I(endpoint). This option is mutually exclusive with C('file_reference')."], 'required': True}",
    "insecure": "{'description': ["Reverts the connection to using HTTP instead of HTTPS. This option should only be used when execuing the M('kubernetes') module local to the Kubernetes cluster using the insecure local port (locahost:8080 by default)."]}",
    "patch_operation": "{'description': ['Specify patch operation for Kubernetes resource update.', 'For details, see the description of PATCH operations at U(https://github.com/kubernetes/kubernetes/blob/release-1.5/docs/devel/api-conventions.md#patch-operations).'], 'default': 'Strategic Merge Patch', 'choices': ['JSON Patch', 'Merge Patch', 'Strategic Merge Patch'], 'aliases': ['patch_strategy'], 'version_added': 2.4}",
    "state": "{'description': ['The desired action to take on the Kubernetes data.'], 'required': True, 'choices': ['absent', 'present', 'replace', 'update'], 'default': 'present'}",
    "url_password": "{'description': ["The HTTP Basic Auth password for the API I(endpoint). This should be set unless using the C('insecure') option."], 'aliases': ['password']}",
    "url_username": "{'description': ["The HTTP Basic Auth username for the API I(endpoint). This should be set unless using the C('insecure') option."], 'default': 'admin', 'aliases': ['username']}",
    "validate_certs": "{'description': ['Enable/disable certificate validation. Note that this is set to C(false) until Ansible can support IP address based certificate hostname matching (exists in >= python3.5.0).'], 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

# Create a new namespace with in-line YAML.
- name: Create a kubernetes namespace
  kubernetes:
    api_endpoint: 123.45.67.89
    url_username: admin
    url_password: redacted
    inline_data:
      kind: Namespace
      apiVersion: v1
      metadata:
        name: ansible-test
        labels:
          label_env: production
          label_ver: latest
        annotations:
          a1: value1
          a2: value2
    state: present

# Create a new namespace from a YAML file.
- name: Create a kubernetes namespace
  kubernetes:
    api_endpoint: 123.45.67.89
    url_username: admin
    url_password: redacted
    file_reference: /path/to/create_namespace.yaml
    state: present

# Do the same thing, but using the insecure localhost port
- name: Create a kubernetes namespace
  kubernetes:
    api_endpoint: 123.45.67.89
    insecure: true
    file_reference: /path/to/create_namespace.yaml
    state: present


```

## License

TODO

## Author Information
  - ['Eric Johnson (@erjohnso) <erjohnso@google.com>']
