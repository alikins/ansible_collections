# Ansible module: ansible.module_docker_image_facts


Inspect docker images

## Description

Provide one or more image names, and the module will inspect each, returning an array of inspection results.

## Requirements

TODO

## Arguments

``` json
{
    "api_version": "{'description': ['The version of the Docker API running on the Docker Host. Defaults to the latest version of the API supported by docker-py.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_API_VERSION) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'auto', 'aliases': ['docker_api_version']}",
    "cacert_path": "{'description': ['Use a CA certificate when performing server verification by providing the path to a CA certificate file.', 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(ca.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_ca_cert']}",
    "cert_path": "{'description': ["Path to the client's TLS certificate file.", 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(cert.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_client_cert']}",
    "debug": "{'description': ['Debug mode'], 'default': False, 'type': 'bool'}",
    "docker_host": "{'description': ['The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, C(tcp://192.0.2.23:2376). If TLS is used to encrypt the connection, the module will automatically replace C(tcp) in the connection URL with C(https).', 'If the value is not specified in the task, the value of environment variable C(DOCKER_HOST) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'unix://var/run/docker.sock', 'aliases': ['docker_url']}",
    "key_path": "{'description': ["Path to the client's TLS key file.", 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(key.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_client_key']}",
    "name": "{'description': ['An image name or a list of image names. Name format will be C(name[:tag]) or C(repository/name[:tag]), where C(tag) is optional. If a tag is not provided, C(latest) will be used. Instead of image names, also image IDs can be used.'], 'required': True}",
    "ssl_version": "{'description': ['Provide a valid SSL version number. Default value determined by ssl.py module.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_SSL_VERSION) will be used instead.']}",
    "timeout": "{'description': ['The maximum amount of time in seconds to wait on a response from the API.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TIMEOUT) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 60}",
    "tls": "{'description': ['Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': False, 'type': 'bool'}",
    "tls_hostname": "{'description': ['When verifying the authenticity of the Docker Host server, provide the expected name of the server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS_HOSTNAME) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'localhost'}",
    "tls_verify": "{'description': ['Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS_VERIFY) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': False, 'type': 'bool'}",
}
```

## Examples


``` yaml


- name: Inspect a single image
  docker_image_facts:
    name: pacur/centos-7

- name: Inspect multiple images
  docker_image_facts:
    name:
      - pacur/centos-7
      - sinatra

```

## License

TODO

## Author Information
  - ['Chris Houseknecht (@chouseknecht)']
