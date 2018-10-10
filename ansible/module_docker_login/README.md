# Ansible module: ansible.module_docker_login


Log into a Docker registry

## Description

Provides functionality similar to the "docker login" command.
Authenticate with a docker registry and add the credentials to your local Docker config file. Adding the credentials to the config files allows future connections to the registry using tools such as Ansible's Docker modules, the Docker CLI and docker-py without needing to provide credentials.
Running in check mode will perform the authentication without updating the config file.

## Requirements

TODO

## Arguments

``` json
{
    "api_version": "{'description': ['The version of the Docker API running on the Docker Host. Defaults to the latest version of the API supported by docker-py.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_API_VERSION) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'auto', 'aliases': ['docker_api_version']}",
    "cacert_path": "{'description': ['Use a CA certificate when performing server verification by providing the path to a CA certificate file.', 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(ca.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_ca_cert']}",
    "cert_path": "{'description': ["Path to the client's TLS certificate file.", 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(cert.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_client_cert']}",
    "config_path": "{'description': ['Custom path to the Docker CLI configuration file.'], 'default': '~/.docker/config.json', 'aliases': ['self.config_path', 'dockercfg_path']}",
    "debug": "{'description': ['Debug mode'], 'default': False, 'type': 'bool'}",
    "docker_host": "{'description': ['The URL or Unix socket path used to connect to the Docker API. To connect to a remote host, provide the TCP connection string. For example, C(tcp://192.0.2.23:2376). If TLS is used to encrypt the connection, the module will automatically replace C(tcp) in the connection URL with C(https).', 'If the value is not specified in the task, the value of environment variable C(DOCKER_HOST) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'unix://var/run/docker.sock', 'aliases': ['docker_url']}",
    "email": "{'required': False, 'description': ['The email address for the registry account.']}",
    "key_path": "{'description': ["Path to the client's TLS key file.", 'If the value is not specified in the task and the environment variable C(DOCKER_CERT_PATH) is set, the file C(key.pem) from the directory specified in the environment variable C(DOCKER_CERT_PATH) will be used.'], 'aliases': ['tls_client_key']}",
    "password": "{'description': ['The plaintext password for the registry account'], 'required': True}",
    "reauthorize": "{'description': ['Refresh existing authentication found in the configuration file.'], 'type': 'bool', 'default': False, 'aliases': ['reauth']}",
    "registry_url": "{'required': False, 'description': ['The registry URL.'], 'default': 'https://index.docker.io/v1/', 'aliases': ['registry', 'url']}",
    "ssl_version": "{'description': ['Provide a valid SSL version number. Default value determined by ssl.py module.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_SSL_VERSION) will be used instead.']}",
    "state": "{'version_added': '2.3', 'description': ['This controls the current state of the user. C(present) will login in a user, C(absent) will log them out.', 'To logout you only need the registry server, which defaults to DockerHub.', 'Before 2.1 you could ONLY log in.', "docker does not support 'logout' with a custom config file."], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['The maximum amount of time in seconds to wait on a response from the API.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TIMEOUT) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 60}",
    "tls": "{'description': ['Secure the connection to the API by using TLS without verifying the authenticity of the Docker host server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': False, 'type': 'bool'}",
    "tls_hostname": "{'description': ['When verifying the authenticity of the Docker Host server, provide the expected name of the server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS_HOSTNAME) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': 'localhost'}",
    "tls_verify": "{'description': ['Secure the connection to the API by using TLS and verifying the authenticity of the Docker host server.', 'If the value is not specified in the task, the value of environment variable C(DOCKER_TLS_VERIFY) will be used instead. If the environment variable is not set, the default value will be used.'], 'default': False, 'type': 'bool'}",
    "username": "{'description': ['The username for the registry account'], 'required': True}",
}
```

## Examples


``` yaml


- name: Log into DockerHub
  docker_login:
    username: docker
    password: rekcod

- name: Log into private registry and force re-authorization
  docker_login:
    registry: your.private.registry.io
    username: yourself
    password: secrets3
    reauthorize: yes

- name: Log into DockerHub using a custom config file
  docker_login:
    username: docker
    password: rekcod
    config_path: /tmp/.mydockercfg

- name: Log out of DockerHub
  docker_login:
    state: absent

```

## License

TODO

## Author Information
  - ['Olaf Kilian (@olsaki) <olaf.kilian@symanex.com>', 'Chris Houseknecht (@chouseknecht)']
  - ['Olaf Kilian (@olsaki) <olaf.kilian@symanex.com>', 'Chris Houseknecht (@chouseknecht)']
