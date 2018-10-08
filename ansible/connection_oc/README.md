# Ansible connection: ansible.connection_oc


Execute tasks in pods running on OpenShift

## Description

Use the oc exec command to run tasks in, or put/fetch files to, pods running on the OpenShift container platform.

## Requirements

TODO

## Arguments

``` json
{
    "oc_cert_file": "{'description': ['Path to a certificate used to authenticate with the API.'], 'default': '', 'vars': [{'name': 'ansible_oc_cert_file'}], 'env': [{'name': 'K8S_AUTH_CERT_FILE'}]}",
    "oc_container": "{'description': ['Container name. Required when a pod contains more than one container.'], 'default': '', 'vars': [{'name': 'ansible_oc_container'}], 'env': [{'name': 'K8S_AUTH_CONTAINER'}]}",
    "oc_context": "{'description': ['The name of a context found in the K8s config file.'], 'default': '', 'vars': [{'name': 'ansible_oc_context'}], 'env': [{'name': 'k8S_AUTH_CONTEXT'}]}",
    "oc_extra_args": "{'description': ['Extra arguments to pass to the oc command line.'], 'default': '', 'vars': [{'name': 'ansible_oc_extra_args'}], 'env': [{'name': 'K8S_AUTH_EXTRA_ARGS'}]}",
    "oc_host": "{'description': ['URL for accessing the API.'], 'default': '', 'vars': [{'name': 'ansible_oc_host'}, {'name': 'ansible_oc_server'}], 'env': [{'name': 'K8S_AUTH_HOST'}, {'name': 'K8S_AUTH_SERVER'}]}",
    "oc_key_file": "{'description': ['Path to a key file used to authenticate with the API.'], 'default': '', 'vars': [{'name': 'ansible_oc_key_file'}], 'env': [{'name': 'K8S_AUTH_KEY_FILE'}]}",
    "oc_kubeconfig": "{'description': ['Path to a oc config file. Defaults to I(~/.kube/conig)'], 'default': '', 'vars': [{'name': 'ansible_oc_kubeconfig'}, {'name': 'ansible_oc_config'}], 'env': [{'name': 'K8S_AUTH_KUBECONFIG'}]}",
    "oc_namespace": "{'description': ['The namespace of the pod'], 'default': '', 'vars': [{'name': 'ansible_oc_namespace'}], 'env': [{'name': 'K8S_AUTH_NAMESPACE'}]}",
    "oc_pod": "{'description': ['Pod name. Required when the host name does not match pod name.'], 'default': '', 'vars': [{'name': 'ansible_oc_pod'}], 'env': [{'name': 'K8S_AUTH_POD'}]}",
    "oc_ssl_ca_cert": "{'description': ['Path to a CA certificate used to authenticate with the API.'], 'default': '', 'vars': [{'name': 'ansible_oc_cert_file'}], 'env': [{'name': 'K8S_AUTH_SSL_CA_CERT'}]}",
    "oc_token": "{'description': ['API authentication bearer token.'], 'vars': [{'name': 'ansible_oc_token'}, {'name': 'ansible_oc_api_key'}], 'env': [{'name': 'K8S_AUTH_TOKEN'}, {'name': 'K8S_AUTH_API_KEY'}]}",
    "oc_verify_ssl": "{'description': ["Whether or not to verify the API server's SSL certificate. Defaults to I(true)."], 'default': '', 'vars': [{'name': 'ansible_oc_verify_ssl'}], 'env': [{'name': 'K8s_AUTH_VERIFY_SSL'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['xuxinkun']
