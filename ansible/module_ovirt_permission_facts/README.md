# Ansible module: ansible.module_ovirt_permission_facts


Retrieve facts about one or more oVirt/RHV permissions

## Description

Retrieve facts about one or more oVirt/RHV permissions.

## Requirements

TODO

## Arguments

``` json
{
    "auth": "{'required': True, 'description': ['Dictionary with values needed to create HTTP/HTTPS connection to oVirt:', 'C(username)[I(required)] - The name of the user, something like I(admin@internal). Default value is set by I(OVIRT_USERNAME) environment variable.', 'C(password)[I(required)] - The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.', 'C(url)- A string containing the API URL of the server, usually something like `I(https://server.example.com/ovirt-engine/api)`. Default value is set by I(OVIRT_URL) environment variable. Either C(url) or C(hostname) is required.', 'C(hostname) - A string containing the hostname of the server, usually something like `I(server.example.com)`. Default value is set by I(OVIRT_HOSTNAME) environment variable. Either C(url) or C(hostname) is required.', 'C(token) - Token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.', 'C(insecure) - A boolean flag that indicates if the server TLS certificate and host name should be checked.', 'C(ca_file) - A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `C(ca_file)` parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.', 'C(kerberos) - A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.', 'C(headers) - Dictionary of HTTP headers to be added to each API call.']}",
    "authz_name": "{'description': ['Authorization provider of the user/group. In previous versions of oVirt/RHV known as domain.'], 'required': True, 'aliases': ['domain']}",
    "fetch_nested": "{'description': ['If I(True) the module will fetch additional data from the API.', 'It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying C(nested_attributes).'], 'version_added': '2.3', 'type': 'bool'}",
    "group_name": "{'description': ['Name of the group to manage.']}",
    "namespace": "{'description': ['Namespace of the authorization provider, where user/group resides.'], 'required': False}",
    "nested_attributes": "{'description': ['Specifies list of the attributes which should be fetched from the API.', 'This parameter apply only when C(fetch_nested) is I(true).'], 'version_added': '2.3'}",
    "user_name": "{'description': ["Username of the user to manage. In most LDAPs it's I(uid) of the user, but in Active Directory you must specify I(UPN) of the user."]}",
}
```

## Examples


``` yaml

# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Gather facts about all permissions of user with username C(john):
- ovirt_permission_facts:
    user_name: john
    authz_name: example.com-authz
- debug:
    var: ovirt_permissions

```

## License

TODO

## Author Information
  - ['Ondra Machacek (@machacekondra)']
