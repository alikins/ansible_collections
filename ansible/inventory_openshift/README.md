# Ansible inventory: ansible.inventory_openshift


OpenShift inventory source

## Description

Fetch containers, services and routes for one or more clusters
Groups by cluster name, namespace, namespace_services, namespace_pods, namespace_routes, and labels
Uses openshift.(yml|yaml) YAML configuration file to set parameter values.

## Requirements

TODO

## Arguments

``` json
{
    "connections": "{'description': ['Optional list of cluster connection settings. If no connections are provided, the default I(~/.kube/config) and active context will be used, and objects will be returned for all namespaces the active user is authorized to access.'], 'name': {'description': ['Optional name to assign to the cluster. If not provided, a name is constructed from the server and port.']}, 'kubeconfig': {'description': ['Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the OpenShift client will attempt to load the default configuration file from I(~/.kube/config.json). Can also be specified via K8S_AUTH_KUBECONFIG environment variable.']}, 'context': {'description': ['The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable.']}, 'host': {'description': ['Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable.']}, 'api_key': {'description': ['Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable.']}, 'username': {'description': ['Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.']}, 'password': {'description': ['Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable.']}, 'cert_file': {'description': ['Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable.']}, 'key_file': {'description': ['Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_HOST environment variable.']}, 'ssl_ca_cert': {'description': ['Path to a CA certificate used to authenticate with the API. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable.']}, 'verify_ssl': {'description': ["Whether or not to verify the API server's SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable."], 'type': 'bool'}, 'namespaces': {'description': ['List of namespaces. If not specified, will fetch all containers for all namespaces user is authorized to access.']}}",
    "plugin": "{'description': ["token that ensures this is a source file for the 'openshift' plugin."], 'required': True, 'choices': ['openshift']}",
}
```

## Examples


``` yaml

# File must be named openshift.yaml or openshift.yml

# Authenticate with token, and return all pods and services for all namespaces
plugin: openshift
connections:
    host: https://192.168.64.4:8443
    token: xxxxxxxxxxxxxxxx
    ssl_verify: false

# Use default config (~/.kube/config) file and active context, and return objects for a specific namespace
plugin: openshift
connections:
    namespaces:
    - testing

# Use a custom config file, and a specific context.
plugin: openshift
connections:
  - kubeconfig: /path/to/config
    context: 'awx/192-168-64-4:8443/developer'

```

## License

TODO

## Author Information
  - ['Chris Houseknecht <@chouseknecht>']
