# Ansible module: ansible.module_win_get_url


Downloads file from HTTP, HTTPS, or FTP to node

## Description

Downloads files from HTTP, HTTPS, or FTP to the remote server. The remote server I(must) have direct access to the remote resource.
For non-Windows targets, use the M(get_url) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "dest": "{'description': ['The location to save the file at the URL.', 'Be sure to include a filename and extension as appropriate.'], 'required': True, 'type': 'path'}",
    "force": "{'description': ['If C(yes), will always download the file. If C(no), will only download the file if it does not exist or the remote file has been modified more recently than the local file.', 'This works by sending an http HEAD request to retrieve last modified time of the requested resource, so for this to work, the remote web server must support HEAD requests.'], 'type': 'bool', 'default': True, 'version_added': '2.0'}",
    "force_basic_auth": "{'description': ['If C(yes), will add a Basic authentication header on the initial request.', "If C(no), will use Microsoft's WebClient to handle authentication."], 'type': 'bool', 'default': False, 'version_added': '2.5'}",
    "headers": "{'description': ['Add custom HTTP headers to a request (as a dictionary).'], 'type': 'dict', 'version_added': '2.4'}",
    "proxy_password": "{'description': ['Proxy authentication password.'], 'type': 'str', 'version_added': '2.0'}",
    "proxy_url": "{'description': ['The full URL of the proxy server to download through.'], 'type': 'str', 'version_added': '2.0'}",
    "proxy_username": "{'description': ['Proxy authentication username.'], 'type': 'str', 'version_added': '2.0'}",
    "timeout": "{'description': ['Timeout in seconds for URL request.'], 'type': 'int', 'default': 10, 'version_added': '2.4'}",
    "url": "{'description': ['The full URL of a file to download.'], 'required': True, 'type': 'str'}",
    "url_password": "{'description': ['Basic authentication password.'], 'type': 'str', 'aliases': ['password']}",
    "url_username": "{'description': ['Basic authentication username.'], 'type': 'str', 'aliases': ['username']}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True, 'version_added': '2.4'}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.', 'If C(skip_certificate_validation) was set, it overrides this option.'], 'type': 'bool', 'default': True, 'version_added': '2.4'}",
}
```

## Examples


``` yaml

- name: Download earthrise.jpg to specified path
  win_get_url:
    url: http://www.example.com/earthrise.jpg
    dest: C:\Users\RandomUser\earthrise.jpg

- name: Download earthrise.jpg to specified path only if modified
  win_get_url:
    url: http://www.example.com/earthrise.jpg
    dest: C:\Users\RandomUser\earthrise.jpg
    force: no

- name: Download earthrise.jpg to specified path through a proxy server.
  win_get_url:
    url: http://www.example.com/earthrise.jpg
    dest: C:\Users\RandomUser\earthrise.jpg
    proxy_url: http://10.0.0.1:8080
    proxy_username: username
    proxy_password: password

- name: Download file from FTP with authentication
  win_get_url:
    url: ftp://server/file.txt
    dest: '%TEMP%\ftp-file.txt'
    url_username: ftp-user
    url_password: ftp-password

```

## License

TODO

## Author Information
  - ['Paul Durivage (@angstwad)', 'Takeshi Kuramochi (@tksarah)']
  - ['Paul Durivage (@angstwad)', 'Takeshi Kuramochi (@tksarah)']
