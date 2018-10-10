# Ansible module: ansible.module_docker_secret


Manage docker secrets

## Description

Create and remove Docker secrets in a Swarm environment. Similar to `docker secret create` and `docker secret rm`.
Adds to the metadata of new secrets 'ansible_key', an encrypted hash representation of the data, which is then used
in future runs to test if a secret has changed.
If 'ansible_key is not present, then a secret will not be updated unless the C(force) option is set.
Updates to secrets are performed by removing the secret and creating it again.

## Requirements

TODO

## Arguments

``` json
{
    "api_version": "{'description': ['The version of the Docker API running on the Docker Host. Defaults to the latest version of the API supported by docker-py.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_API_VERSION) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'auto', 'aliases': ['docker_api_version']}",
    "cacert_path": "{'description': ['Use a CA certificate when performing server verification by providing the path to a CA certificate file.', 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(ca.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_ca_cert']}",
    "cert_path": "{'description': ["Path to the client's TLS certificate file.", 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(cert.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_client_cert']}",
    "data": "{'description': ['String. The value of the secret. Required when state is C(present).'], 'required': False}",
    "debug": "{'description': ['Debug mode'], 'default': False, 'type': 'bool'}",
    "docker_host": "{'description': ['The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, C(tcp://192.0.2.23:2376). If TLS is used to encrypt the connection, the module will automatically replace C(tcp) in the connection URL with C(https).', 'If the value is not specified in the task, the value of environment variable C(DOCKER_HOST) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'unix://var/run/docker.sock', 'aliases': ['docker_url']}",
    "force": "{'description': ['Use with state C(present) to always remove and recreate an existing secret.', 'If I(true), an existing secret will be replaced, even if it has not changed.'], 'default': False, 'type': 'bool'}",
    "key_path": "{'description': ["Path to the client's TLS key file.", 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(key.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_client_key']}",
    "labels": "{'description': ['A map of key:value meta data, where both the I(key) and I(value) are expected to be a string.', 'If new meta data is provided, or existing meta data is modified, the secret will be updated by removing it and creating it again.'], 'required': False}",
    "name": "{'description': ['The name of the secret.'], 'required': True}",
    "ssl_version": "{'description': ['Provide a valid SSL version number. Default value determined by ssl.py module.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_SSL_VERSION) will be used instead.']}",
    "state": "{'description': ['Set to C(present), if the secret should exist, and C(absent), if it should not.'], 'required': False, 'default': 'present', 'choices': ['absent', 'present']}",
    "timeout": "{'description': ['The maximum amount of time in seconds to wait on a response from the API.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TIMEOUT) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 60}",
    "tls": "{'description': ['Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': False, 'type': 'bool'}",
    "tls_hostname": "{'description': ['When verifying the authenticity of the Docker Host server, provide the expected name of the server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS_HOSTNAME) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'localhost'}",
    "tls_verify": "{'description': ['Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS_VERIFY) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': False, 'type': 'bool'}",
}
```

## Examples


``` yaml


- name: Create secret foo
  docker_secret:
    name: foo
    data: Hello World!
    state: present

- name: Change the secret data
  docker_secret:
    name: foo
    data: Goodnight everyone!
    labels:
      bar: baz
      one: '1'
    state: present

- name: Add a new label
  docker_secret:
    name: foo
    data: Goodnight everyone!
    labels:
      bar: baz
      one: '1'
      # Adding a new label will cause a remove/create of the secret
      two: '2'
    state: present

- name: No change
  docker_secret:
    name: foo
    data: Goodnight everyone!
    labels:
      bar: baz
      one: '1'
      # Even though 'two' is missing, there is no change to the existing secret
    state: present

- name: Update an existing label
  docker_secret:
    name: foo
    data: Goodnight everyone!
    labels:
      bar: monkey   # Changing a label will cause a remove/create of the secret
      one: '1'
    state: present

- name: Force the removal/creation of the secret
  docker_secret:
    name: foo
    data: Goodnight everyone!
    force: yes
    state: present

- name: Remove secret foo
  docker_secret:
    name: foo
    state: absent

```

## License

TODO

## Author Information
  - ['Chris Houseknecht (@chouseknecht)']
