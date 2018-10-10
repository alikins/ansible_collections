# Ansible module: ansible.module_k8s_facts


Describe Kubernetes (K8s) objects

## Description

Use the OpenShift Python client to perform read operations on K8s objects.
Access to the full range of K8s APIs.
Authenticate using either a config file, certificates, password or token.
Supports check mode.

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable.']}",
    "api_version": "{'description': ['Use to specify the API version. in conjunction with I(kind), I(name), and I(namespace) to identify a specific object.'], 'default': 'v1', 'aliases': ['api', 'version']}",
    "cert_file": "{'description': ['Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable.']}",
    "context": "{'description': ['The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable.']}",
    "field_selectors": "{'description': ['List of field selectors to use to filter results']}",
    "host": "{'description': ['Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable.']}",
    "key_file": "{'description': ['Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_HOST environment variable.']}",
    "kind": "{'description': ['Use to specify an object model. Use in conjunction with I(api_version), I(name), and I(namespace) to identify a specific object.'], 'required': True}",
    "kubeconfig": "{'description': ['Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the openshift client will attempt to load the default configuration file from I(~/.kube/config.json). Can also be specified via K8S_AUTH_KUBECONFIG environment variable.']}",
    "label_selectors": "{'description': ['List of label selectors to use to filter results']}",
    "name": "{'description': ['Use to specify an object name.  Use in conjunction with I(api_version), I(kind) and I(namespace) to identify a specific object.']}",
    "namespace": "{'description': ['Use to specify an object namespace. Use in conjunction with I(api_version), I(kind), and I(name) to identify a specfic object.']}",
    "password": "{'description': ['Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable.']}",
    "ssl_ca_cert": "{'description': ['Path to a CA certificate used to authenticate with the API. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable.']}",
    "username": "{'description': ['Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.']}",
    "verify_ssl": "{'description': ["Whether or not to verify the API server's SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable."], 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Get an existing Service object
  k8s_facts:
    api_version: v1
    kind: Service
    name: web
    namespace: testing
  register: web_service

- name: Get a list of all service objects
  k8s_facts:
    api_version: v1
    kind: Service
    namespace: testing
  register: service_list

- name: Get a list of all pods from any namespace
  k8s_facts:
    kind: Pod
  register: pod_list

- name: Search for all Pods labelled app=web
  k8s_facts:
    kind: Pod
    label_selectors:
      - app = web
      - tier in (dev, test)

- name: Search for all running pods
  k8s_facts:
    kind: Pod
    field_selectors:
      - status.phase = running

```

## License

TODO

## Author Information
  - ['Will Thames (@willthames)']
