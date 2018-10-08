# Ansible connection: ansible.connection_kubectl


Execute tasks in pods running on Kubernetes

## Description

Use the kubectl exec command to run tasks in, or put/fetch files to, pods running on the Kubernetes container platform.

## Requirements

TODO

## Arguments

``` json
{
    "kubectl_cert_file": "{'description': ['Path to a certificate used to authenticate with the API.'], 'default': '', 'vars': [{'name': 'ansible_kubectl_cert_file'}], 'env': [{'name': 'K8S_AUTH_CERT_FILE'}]}",
    "kubectl_container": "{'description': ['Container name. Required when a pod contains more than one container.'], 'default': '', 'vars': [{'name': 'ansible_kubectl_container'}], 'env': [{'name': 'K8S_AUTH_CONTAINER'}]}",
    "kubectl_context": "{'description': ['The name of a context found in the K8s config file.'], 'default': '', 'vars': [{'name': 'ansible_kubectl_context'}], 'env': [{'name': 'k8S_AUTH_CONTEXT'}]}",
    "kubectl_extra_args": "{'description': ['Extra arguments to pass to the kubectl command line.'], 'default': '', 'vars': [{'name': 'ansible_kubectl_extra_args'}], 'env': [{'name': 'K8S_AUTH_EXTRA_ARGS'}]}",
    "kubectl_host": "{'description': ['URL for accessing the API.'], 'default': '', 'vars': [{'name': 'ansible_kubectl_host'}, {'name': 'ansible_kubectl_server'}], 'env': [{'name': 'K8S_AUTH_HOST'}, {'name': 'K8S_AUTH_SERVER'}]}",
    "kubectl_key_file": "{'description': ['Path to a key file used to authenticate with the API.'], 'default': '', 'vars': [{'name': 'ansible_kubectl_key_file'}], 'env': [{'name': 'K8S_AUTH_KEY_FILE'}]}",
    "kubectl_kubeconfig": "{'description': ['Path to a kubectl config file. Defaults to I(~/.kube/conig)'], 'default': '', 'vars': [{'name': 'ansible_kubectl_kubeconfig'}, {'name': 'ansible_kubectl_config'}], 'env': [{'name': 'K8S_AUTH_KUBECONFIG'}]}",
    "kubectl_namespace": "{'description': ['The namespace of the pod'], 'default': '', 'vars': [{'name': 'ansible_kubectl_namespace'}], 'env': [{'name': 'K8S_AUTH_NAMESPACE'}]}",
    "kubectl_password": "{'description': ['Provide a password for authenticating with the API.'], 'default': '', 'vars': [{'name': 'ansible_kubectl_password'}], 'env': [{'name': 'K8S_AUTH_PASSWORD'}]}",
    "kubectl_pod": "{'description': ['Pod name. Required when the host name does not match pod name.'], 'default': '', 'vars': [{'name': 'ansible_kubectl_pod'}], 'env': [{'name': 'K8S_AUTH_POD'}]}",
    "kubectl_ssl_ca_cert": "{'description': ['Path to a CA certificate used to authenticate with the API.'], 'default': '', 'vars': [{'name': 'ansible_kubectl_cert_file'}], 'env': [{'name': 'K8S_AUTH_SSL_CA_CERT'}]}",
    "kubectl_token": "{'description': ['API authentication bearer token.'], 'vars': [{'name': 'ansible_kubectl_token'}, {'name': 'ansible_kubectl_api_key'}], 'env': [{'name': 'K8S_AUTH_TOKEN'}, {'name': 'K8S_AUTH_API_KEY'}]}",
    "kubectl_username": "{'description': ['Provide a username for authenticating with the API.'], 'default': '', 'vars': [{'name': 'ansible_kubectl_username'}], 'env': [{'name': 'K8S_AUTH_USERNAME'}]}",
    "kubectl_verify_ssl": "{'description': ["Whether or not to verify the API server's SSL certificate. Defaults to I(true)."], 'default': '', 'vars': [{'name': 'ansible_kubectl_verify_ssl'}], 'env': [{'name': 'K8s_AUTH_VERIFY_SSL'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['xuxinkun']
