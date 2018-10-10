# Ansible module: ansible.module_k8s_scale


Set a new size for a Deployment, ReplicaSet, Replication Controller, or Job

## Description

Similar to the kubectl scale command. Use to set the number of replicas for a Deployment, ReplicatSet, or Replication Controller, or the parallelism attribute of a Job. Supports check mode.

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable.']}",
    "api_version": "{'description': ['Use to specify the API version. Use to create, delete, or discover an object without providing a full resource definition. Use in conjunction with I(kind), I(name), and I(namespace) to identify a specific object. If I(resource definition) is provided, the I(apiVersion) from the I(resource_definition) will override this option.'], 'default': 'v1', 'aliases': ['api', 'version']}",
    "cert_file": "{'description': ['Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable.']}",
    "context": "{'description': ['The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable.']}",
    "current_replicas": "{'description': ['For Deployment, ReplicaSet, Replication Controller, only scale, if the number of existing replicas matches. In the case of a Job, update parallelism only if the current parallelism value matches.'], 'type': 'int'}",
    "host": "{'description': ['Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable.']}",
    "key_file": "{'description': ['Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_HOST environment variable.']}",
    "kind": "{'description': ['Use to specify an object model. Use to create, delete, or discover an object without providing a full resource definition. Use in conjunction with I(api_version), I(name), and I(namespace) to identify a specific object. If I(resource definition) is provided, the I(kind) from the I(resource_definition) will override this option.']}",
    "kubeconfig": "{'description': ['Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the openshift client will attempt to load the default configuration file from I(~/.kube/config.json). Can also be specified via K8S_AUTH_KUBECONFIG environment variable.']}",
    "name": "{'description': ['Use to specify an object name. Use to create, delete, or discover an object without providing a full resource definition. Use in conjunction with I(api_version), I(kind) and I(namespace) to identify a specific object. If I(resource definition) is provided, the I(metadata.name) value from the I(resource_definition) will override this option.']}",
    "namespace": "{'description': ['Use to specify an object namespace. Useful when creating, deleting, or discovering an object without providing a full resource definition. Use in conjunction with I(api_version), I(kind), and I(name) to identify a specfic object. If I(resource definition) is provided, the I(metadata.namespace) value from the I(resource_definition) will override this option.']}",
    "password": "{'description': ['Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable.']}",
    "replicas": "{'description': ['The desired number of replicas.']}",
    "resource_definition": "{'description': ['Provide a valid YAML definition (either as a string, list, or dict) for an object when creating or updating. NOTE: I(kind), I(api_version), I(name), and I(namespace) will be overwritten by corresponding values found in the provided I(resource_definition).'], 'aliases': ['definition', 'inline']}",
    "resource_version": "{'description': ['Only attempt to scale, if the current object version matches.'], 'type': 'str'}",
    "src": "{'description': ['Provide a path to a file containing a valid YAML definition of an object or objects to be created or updated. Mutually exclusive with I(resource_definition). NOTE: I(kind), I(api_version), I(name), and I(namespace) will be overwritten by corresponding values found in the configuration read in from the I(src) file.', "Reads from the local file system. To read from the Ansible controller's file system, use the file lookup plugin or template lookup plugin, combined with the from_yaml filter, and pass the result to I(resource_definition). See Examples below."]}",
    "ssl_ca_cert": "{'description': ['Path to a CA certificate used to authenticate with the API. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable.']}",
    "username": "{'description': ['Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.']}",
    "verify_ssl": "{'description': ["Whether or not to verify the API server's SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable."], 'type': 'bool'}",
    "wait": "{'description': ['For Deployment, ReplicaSet, Replication Controller, wait for the status value of I(ready_replicas) to change to the number of I(replicas). In the case of a Job, this option is ignored.'], 'type': 'bool', 'default': True}",
    "wait_timeout": "{'description': ['When C(wait) is I(True), the number of seconds to wait for the I(ready_replicas) status to equal  I(replicas). If the status is not reached within the allotted time, an error will result. In the case of a Job, this option is ignored.'], 'type': 'int', 'default': 20}",
}
```

## Examples


``` yaml

- name: Scale deployment up, and extend timeout
  k8s_scale:
    api_version: v1
    kind: Deployment
    name: elastic
    namespace: myproject
    replicas: 3
    wait_timeout: 60

- name: Scale deployment down when current replicas match
  k8s_scale:
    api_version: v1
    kind: Deployment
    name: elastic
    namespace: myproject
    current_replicas: 3
    replicas: 2

- name: Increase job parallelism
  k8s_scale:
    api_version: batch/v1
    kind: job
    name: pi-with-timeout
    namespace: testing
    replicas: 2

# Match object using local file or inline definition

- name: Scale deployment based on a file from the local filesystem
  k8s_scale:
    src: /myproject/elastic_deployment.yml
    replicas: 3
    wait: no

- name: Scale deployment based on a template output
  k8s_scale:
    resource_definition: "{{ lookup('template', '/myproject/elastic_deployment.yml') | from_yaml }}"
    replicas: 3
    wait: no

- name: Scale deployment based on a file from the Ansible controller filesystem
  k8s_scale:
    resource_definition: "{{ lookup('file', '/myproject/elastic_deployment.yml') | from_yaml }}"
    replicas: 3
    wait: no

```

## License

TODO

## Author Information
  - ['Chris Houseknecht (@chouseknecht)', 'Fabian von Feilitzsch (@fabianvf)']
  - ['Chris Houseknecht (@chouseknecht)', 'Fabian von Feilitzsch (@fabianvf)']
