# Ansible module: ansible.module_win_uri


Interacts with webservices

## Description

Interacts with FTP, HTTP and HTTPS web services.
Supports Digest, Basic and WSSE HTTP authentication mechanisms.
For non-Windows targets, use the M(uri) module instead.

## Requirements

TODO

## Arguments

``` json
{
    "body": "{'description': ['The body of the HTTP request/response to the web service.']}",
    "client_cert": "{'description': ['Specifies the client certificate (.pfx) that is used for a secure web request.', 'The WinRM connection must be authenticated with C(CredSSP) if the certificate file is not password protected.', 'Other authentication types can set I(client_cert_password) when the cert is password protected.'], 'type': 'path', 'version_added': '2.4'}",
    "client_cert_password": "{'description': ['The password for the client certificate (.pfx) file that is used for a secure web request.'], 'version_added': '2.5'}",
    "content_type": "{'description': ['Sets the "Content-Type" header.']}",
    "creates": "{'description': ['A filename, when it already exists, this step will be skipped.'], 'type': 'path', 'version_added': '2.4'}",
    "dest": "{'description': ['Output the response body to a file.'], 'type': 'path', 'version_added': '2.3'}",
    "follow_redirects": "{'description': ['Whether or not the C(win_uri) module should follow redirects.', 'C(all) will follow all redirects.', 'C(none) will not follow any redirects.', 'C(safe) will follow only "safe" redirects, where "safe" means that the client is only doing a C(GET) or C(HEAD) on the URI to which it is being redirected.'], 'choices': ['all', 'none', 'safe'], 'default': 'safe', 'version_added': '2.4'}",
    "force_basic_auth": "{'description': ['By default the authentication information is only sent when a webservice responds to an initial request with a 401 status. Since some basic auth services do not properly send a 401, logins will fail.', 'This option forces the sending of the Basic authentication header upon the initial request.'], 'type': 'bool', 'default': False, 'version_added': '2.5'}",
    "headers": "{'description': ['Extra headers to set on the request, see the examples for more details on how to set this.']}",
    "maximum_redirection": "{'description': ['Specifies how many times C(win_uri) redirects a connection to an alternate Uniform Resource Identifier (URI) before the connection fails.', 'If C(maximum_redirection) is set to 0 (zero) or C(follow_redirects) is set to C(none), or set to C(safe) when not doing C(GET) or C(HEAD) it prevents all redirection.'], 'type': 'int', 'default': 5, 'version_added': '2.4'}",
    "method": "{'description': ['The HTTP Method of the request or response.'], 'choices': ['CONNECT', 'DELETE', 'GET', 'HEAD', 'MERGE', 'OPTIONS', 'PATCH', 'POST', 'PUT', 'REFRESH', 'TRACE'], 'default': 'GET'}",
    "password": "{'description': ['Password to use for authentication.'], 'version_added': '2.4'}",
    "removes": "{'description': ['A filename, when it does not exist, this step will be skipped.'], 'type': 'path', 'version_added': '2.4'}",
    "return_content": "{'description': ['Whether or not to return the body of the response as a "content" key in the dictionary result. If the reported Content-type is "application/json", then the JSON is additionally loaded into a key called C(json) in the dictionary results.'], 'type': 'bool', 'default': False, 'version_added': '2.4'}",
    "status_code": "{'description': ['A valid, numeric, HTTP status code that signifies success of the request.', 'Can also be comma separated list of status codes.'], 'type': 'list', 'default': 200, 'version_added': '2.4'}",
    "timeout": "{'description': ['Specifies how long the request can be pending before it times out (in seconds).', 'The value 0 (zero) specifies an indefinite time-out.', 'A Domain Name System (DNS) query can take up to 15 seconds to return or time out. If your request contains a host name that requires resolution, and you set C(timeout) to a value greater than zero, but less than 15 seconds, it can take 15 seconds or more before your request times out.'], 'type': 'int', 'default': 30, 'version_added': '2.4'}",
    "url": "{'description': ['Supports FTP, HTTP or HTTPS URLs in the form of (ftp|http|https)://host.domain:port/path.'], 'required': True}",
    "user": "{'description': ['Username to use for authentication.'], 'version_added': '2.4'}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.  This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True, 'version_added': '2.4'}",
}
```

## Examples


``` yaml

- name: Perform a GET and Store Output
  win_uri:
    url: http://example.com/endpoint
  register: http_output

# Set a HOST header to hit an internal webserver:
- name: Hit a Specific Host on the Server
  win_uri:
    url: http://example.com/
    method: GET
    headers:
      host: www.somesite.com

- name: Perform a HEAD on an Endpoint
  win_uri:
    url: http://www.example.com/
    method: HEAD

- name: POST a Body to an Endpoint
  win_uri:
    url: http://www.somesite.com/
    method: POST
    body: "{ 'some': 'json' }"

```

## License

TODO

## Author Information
  - ['Corwin Brown (@blakfeld)', 'Dag Wieers (@dagwieers)']
  - ['Corwin Brown (@blakfeld)', 'Dag Wieers (@dagwieers)']