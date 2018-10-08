# Ansible lookup: ansible.lookup_k8s


Query the K8s API

## Description

Uses the OpenShift Python client to fetch a specific object by name, all matching objects within a namespace, or all matching objects for all namespaces, as well as information about the cluster.
Provides access the full range of K8s APIs.
Enables authentication via config file, certificates, password or token.

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable.']}",
    "api_version": "{'description': ['Use to specify the API version. If I(resource definition) is provided, the I(apiVersion) from the I(resource_definition) will override this option.'], 'default': 'v1'}",
    "cert_file": "{'description': ['Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable.']}",
    "cluster_info": "{'description': ['Use to specify the type of cluster information you are attempting to retrieve. Will take priority over all the other options.']}",
    "context": "{'description': ['The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable.']}",
    "field_selector": "{'description': ['Specific fields on which to query. Ignored when I(resource_name) is provided.']}",
    "host": "{'description': ['Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable.']}",
    "key_file": "{'description': ['Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_HOST environment variable.']}",
    "kind": "{'description': ['Use to specify an object model. If I(resource definition) is provided, the I(kind) from a I(resource_definition) will override this option.'], 'required': True}",
    "kubeconfig": "{'description': ['Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the openshift client will attempt to load the default configuration file from I(~/.kube/config.json). Can also be specified via K8S_AUTH_KUBECONFIG environment variable.']}",
    "label_selector": "{'description': ['Additional labels to include in the query. Ignored when I(resource_name) is provided.']}",
    "namespace": "{'description': ['Limit the objects returned to a specific namespace. If I(resource definition) is provided, the I(metadata.namespace) value from the I(resource_definition) will override this option.']}",
    "password": "{'description': ['Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable.']}",
    "resource_definition": "{'description': ['Provide a YAML configuration for an object. NOTE: I(kind), I(api_version), I(resource_name), and I(namespace) will be overwritten by corresponding values found in the provided I(resource_definition).']}",
    "resource_name": "{'description': ['Fetch a specific object by name. If I(resource definition) is provided, the I(metadata.name) value from the I(resource_definition) will override this option.']}",
    "src": "{'description': ['Provide a path to a file containing a valid YAML definition of an object dated. Mutually exclusive with I(resource_definition). NOTE: I(kind), I(api_version), I(resource_name), and I(namespace) will be overwritten by corresponding values found in the configuration read in from the I(src) file.', "Reads from the local file system. To read from the Ansible controller's file system, use the file lookup plugin or template lookup plugin, combined with the from_yaml filter, and pass the result to I(resource_definition). See Examples below."]}",
    "ssl_ca_cert": "{'description': ['Path to a CA certificate used to authenticate with the API. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable.']}",
    "username": "{'description': ['Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.']}",
    "verify_ssl": "{'description': ["Whether or not to verify the API server's SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable."], 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Fetch a list of namespaces
  set_fact:
    projects: "{{ lookup('k8s', api_version='v1', kind='Namespace') }}"

- name: Fetch all deployments
  set_fact:
    deployments: "{{ lookup('k8s', kind='Deployment', namespace='testing') }}"

- name: Fetch all deployments in a namespace
  set_fact:
    deployments: "{{ lookup('k8s', kind='Deployment', namespace='testing') }}"

- name: Fetch a specific deployment by name
  set_fact:
    deployments: "{{ lookup('k8s', kind='Deployment', namespace='testing', resource_name='elastic') }}"

- name: Fetch with label selector
  set_fact:
    service: "{{ lookup('k8s', kind='Service', label_selector='app=galaxy') }}"

# Use parameters from a YAML config

- name: Load config from the Ansible controller filesystem
  set_fact:
    config: "{{ lookup('file', 'service.yml') | from_yaml }}"

- name: Using the config (loaded from a file in prior task), fetch the latest version of the object
  set_fact:
    service: "{{ lookup('k8s', resource_definition=config) }}"

- name: Use a config from the local filesystem
  set_fact:
    service: "{{ lookup('k8s', src='service.yml') }}"

```

## License

TODO

## Author Information
  - ['UNKNOWN']
