# Ansible module: ansible.module_pulp_repo


Add or remove Pulp repos from a remote host

## Description

Add or remove Pulp repos from a remote host.

## Requirements

TODO

## Arguments

``` json
{
    "add_export_distributor": "{'description': ['Whether or not to add the export distributor to new C(rpm) repositories.'], 'type': 'bool', 'default': False}",
    "client_cert": "{'description': ['PEM formatted certificate chain file to be used for SSL client authentication. This file can also include the key as well, and if the key is included, C(client_key) is not required.']}",
    "client_key": "{'description': ['PEM formatted file that contains your private key to be used for SSL client authentication. If C(client_cert) contains both the certificate and key, this option is not required.']}",
    "feed": "{'description': ['Upstream feed URL to receive updates from.']}",
    "force": "{'description': ['If C(yes) do not get a cached copy.'], 'aliases': ['thirsty'], 'type': 'bool', 'default': False}",
    "force_basic_auth": "{'description': ['httplib2, the library used by the M(uri) module only sends authentication information when a webservice responds to an initial request with a 401 status. Since some basic auth services do not properly send a 401, logins will fail. This option forces the sending of the Basic authentication header upon initial request.'], 'default': False, 'type': 'bool'}",
    "http_agent": "{'description': ['Header to identify as, generally appears in web server logs.'], 'default': 'ansible-httpget'}",
    "importer_ssl_ca_cert": "{'description': ['CA certificate string used to validate the feed source SSL certificate. This can be the file content or the path to the file.']}",
    "importer_ssl_client_cert": "{'description': ['Certificate used as the client certificate when synchronizing the repository. This is used to communicate authentication information to the feed source. The value to this option must be the full path to the certificate. The specified file may be the certificate itself or a single file containing both the certificate and private key. This can be the file content or the path to the file.']}",
    "importer_ssl_client_key": "{'description': ['Private key to the certificate specified in I(importer_ssl_client_cert), assuming it is not included in the certificate file itself. This can be the file content or the path to the file.']}",
    "name": "{'description': ['Name of the repo to add or remove. This correlates to repo-id in Pulp.'], 'required': True}",
    "proxy_host": "{'description': ['Proxy url setting for the pulp repository importer. This is in the format scheme://host.']}",
    "proxy_port": "{'description': ['Proxy port setting for the pulp repository importer.']}",
    "publish_distributor": "{'description': ['Distributor to use when state is C(publish). The default is to publish all distributors.']}",
    "pulp_host": "{'description': ['URL of the pulp server to connect to.'], 'default': 'http://127.0.0.1'}",
    "relative_url": "{'description': ['Relative URL for the local repository.'], 'required': True}",
    "repo_type": "{'description': ['Repo plugin type to use (i.e. C(rpm), C(docker)).'], 'default': 'rpm'}",
    "serve_http": "{'description': ['Make the repo available over HTTP.'], 'type': 'bool', 'default': False}",
    "serve_https": "{'description': ['Make the repo available over HTTPS.'], 'type': 'bool', 'default': True}",
    "state": "{'description': ["The repo state. A state of C(sync) will queue a sync of the repo. This is asynchronous but not delayed like a scheduled sync. A state of C(publish) will use the repository's distributor to publish the content."], 'default': 'present', 'choices': ['present', 'absent', 'sync', 'publish']}",
    "url": "{'description': ['HTTP, HTTPS, or FTP URL in the form (http|https|ftp)://[user[:pass]]@host.domain[:port]/path']}",
    "url_password": "{'description': ['The password for use in HTTP basic authentication to the pulp API. If the I(url_username) parameter is not specified, the I(url_password) parameter will not be used.']}",
    "url_username": "{'description': ['The username for use in HTTP basic authentication to the pulp API.']}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "wait_for_completion": "{'description': ['Wait for asynchronous tasks to complete before returning.'], 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

- name: Create a new repo with name 'my_repo'
  pulp_repo:
    name: my_repo
    relative_url: my/repo
    state: present

- name: Create a repo with a feed and a relative URL
  pulp_repo:
    name: my_centos_updates
    repo_type: rpm
    feed: http://mirror.centos.org/centos/6/updates/x86_64/
    relative_url: centos/6/updates
    url_username: admin
    url_password: admin
    force_basic_auth: yes
    state: present

- name: Remove a repo from the pulp server
  pulp_repo:
    name: my_old_repo
    repo_type: rpm
    state: absent

```

## License

TODO

## Author Information
  - ['Joe Adams (@sysadmind)']
