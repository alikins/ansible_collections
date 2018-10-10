# Ansible module: ansible.module_k8s


Manage Kubernetes (K8s) objects

## Description

Use the OpenShift Python client to perform CRUD operations on K8s objects.
Pass the object definition from a source file or inline. See examples for reading files and using Jinja templates.
Access to the full range of K8s APIs.
Use the M(k8s_facts) module to obtain a list of items about an object of type C(kind)
Authenticate using either a config file, certificates, password or token.
Supports check mode.

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable.']}",
    "api_version": "{'description': ['Use to specify the API version. Use to create, delete, or discover an object without providing a full resource definition. Use in conjunction with I(kind), I(name), and I(namespace) to identify a specific object. If I(resource definition) is provided, the I(apiVersion) from the I(resource_definition) will override this option.'], 'default': 'v1', 'aliases': ['api', 'version']}",
    "cert_file": "{'description': ['Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment variable.']}",
    "context": "{'description': ['The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable.']}",
    "force": "{'description': ['If set to C(True), and I(state) is C(present), an existing object will be replaced.'], 'default': False, 'type': 'bool'}",
    "host": "{'description': ['Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable.']}",
    "key_file": "{'description': ['Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_HOST environment variable.']}",
    "kind": "{'description': ['Use to specify an object model. Use to create, delete, or discover an object without providing a full resource definition. Use in conjunction with I(api_version), I(name), and I(namespace) to identify a specific object. If I(resource definition) is provided, the I(kind) from the I(resource_definition) will override this option.']}",
    "kubeconfig": "{'description': ['Path to an existing Kubernetes config file. If not provided, and no other connection options are provided, the openshift client will attempt to load the default configuration file from I(~/.kube/config.json). Can also be specified via K8S_AUTH_KUBECONFIG environment variable.']}",
    "merge_type": "{'description': ['Whether to override the default patch merge approach with a specific type. By the default, the strategic merge will typically be used.', 'For example, Custom Resource Definitions typically aren\'t updatable by the usual strategic merge. You may want to use C(merge) if you see "strategic merge patch format is not supported"', 'See U(https://kubernetes.io/docs/tasks/run-application/update-api-object-kubectl-patch/#use-a-json-merge-patch-to-update-a-deployment)', 'Requires openshift >= 0.6.2', 'If more than one merge_type is given, the merge_types will be tried in order', "If openshift >= 0.6.2, this defaults to C(['strategic-merge', 'merge']), which is ideal for using the same parameters on resource kinds that combine Custom Resources and built-in resources. For openshift < 0.6.2, the default is simply C(strategic-merge)."], 'choices': ['json', 'merge', 'strategic-merge'], 'type': 'list', 'version_added': '2.7'}",
    "name": "{'description': ['Use to specify an object name. Use to create, delete, or discover an object without providing a full resource definition. Use in conjunction with I(api_version), I(kind) and I(namespace) to identify a specific object. If I(resource definition) is provided, the I(metadata.name) value from the I(resource_definition) will override this option.']}",
    "namespace": "{'description': ['Use to specify an object namespace. Useful when creating, deleting, or discovering an object without providing a full resource definition. Use in conjunction with I(api_version), I(kind), and I(name) to identify a specfic object. If I(resource definition) is provided, the I(metadata.namespace) value from the I(resource_definition) will override this option.']}",
    "password": "{'description': ['Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment variable.']}",
    "resource_definition": "{'description': ['Provide a valid YAML definition (either as a string, list, or dict) for an object when creating or updating. NOTE: I(kind), I(api_version), I(name), and I(namespace) will be overwritten by corresponding values found in the provided I(resource_definition).'], 'aliases': ['definition', 'inline']}",
    "src": "{'description': ['Provide a path to a file containing a valid YAML definition of an object or objects to be created or updated. Mutually exclusive with I(resource_definition). NOTE: I(kind), I(api_version), I(name), and I(namespace) will be overwritten by corresponding values found in the configuration read in from the I(src) file.', "Reads from the local file system. To read from the Ansible controller's file system, use the file lookup plugin or template lookup plugin, combined with the from_yaml filter, and pass the result to I(resource_definition). See Examples below."]}",
    "ssl_ca_cert": "{'description': ['Path to a CA certificate used to authenticate with the API. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable.']}",
    "state": "{'description': ['Determines if an object should be created, patched, or deleted. When set to C(present), an object will be created, if it does not already exist. If set to C(absent), an existing object will be deleted. If set to C(present), an existing object will be patched, if its attributes differ from those specified using I(resource_definition) or I(src).'], 'default': 'present', 'choices': ['present', 'absent']}",
    "username": "{'description': ['Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment variable.']}",
    "verify_ssl": "{'description': ["Whether or not to verify the API server's SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL environment variable."], 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Create a k8s namespace
  k8s:
    name: testing
    api_version: v1
    kind: Namespace
    state: present

- name: Create a Service object from an inline definition
  k8s:
    state: present
    definition:
      apiVersion: v1
      kind: Service
      metadata:
        name: web
        namespace: testing
        labels:
          app: galaxy
          service: web
      spec:
        selector:
          app: galaxy
          service: web
        ports:
        - protocol: TCP
          targetPort: 8000
          name: port-8000-tcp
          port: 8000

- name: Create a Service object by reading the definition from a file
  k8s:
    state: present
    src: /testing/service.yml

- name: Remove an existing Service object
  k8s:
    state: absent
    api_version: v1
    kind: Service
    namespace: testing
    name: web

# Passing the object definition from a file

- name: Create a Deployment by reading the definition from a local file
  k8s:
    state: present
    src: /testing/deployment.yml

- name: Read definition file from the Ansible controller file system
  k8s:
    state: present
    definition: "{{ lookup('file', '/testing/deployment.yml') }}"

- name: Read definition file from the Ansible controller file system after Jinja templating
  k8s:
    state: present
    definition: "{{ lookup('template', '/testing/deployment.yml') }}"

```

## License

TODO

## Author Information
  - ['Chris Houseknecht (@chouseknecht)', 'Fabian von Feilitzsch (@fabianvf)']
  - ['Chris Houseknecht (@chouseknecht)', 'Fabian von Feilitzsch (@fabianvf)']
