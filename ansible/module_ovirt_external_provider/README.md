# Ansible module: ansible.module_ovirt_external_provider


Module to manage external providers in oVirt/RHV

## Description

Module to manage external providers in oVirt/RHV

## Requirements

TODO

## Arguments

``` json
{
    "auth": "{'required': True, 'description': ['Dictionary with values needed to create HTTP/HTTPS connection to oVirt:', 'C(username)[I(required)] - The name of the user, something like I(admin@internal). Default value is set by I(OVIRT_USERNAME) environment variable.', 'C(password)[I(required)] - The password of the user. Default value is set by I(OVIRT_PASSWORD) environment variable.', 'C(url) - A string containing the API URL of the server, usually something like `I(https://server.example.com/ovirt-engine/api)`. Default value is set by I(OVIRT_URL) environment variable. Either C(url) or C(hostname) is required.', 'C(hostname) - A string containing the hostname of the server, usually something like `I(server.example.com)`. Default value is set by I(OVIRT_HOSTNAME) environment variable. Either C(url) or C(hostname) is required.', 'C(token) - Token to be used instead of login with username/password. Default value is set by I(OVIRT_TOKEN) environment variable.', 'C(insecure) - A boolean flag that indicates if the server TLS certificate and host name should be checked.', 'C(ca_file) - A PEM file containing the trusted CA certificates. The certificate presented by the server will be verified using these CA certificates. If `C(ca_file)` parameter is not set, system wide CA certificate store is used. Default value is set by I(OVIRT_CAFILE) environment variable.', 'C(kerberos) - A boolean flag indicating if Kerberos authentication should be used instead of the default basic authentication.', 'C(headers) - Dictionary of HTTP headers to be added to each API call.']}",
    "authentication_keys": "{'description': ["List of authentication keys. Each key is represented by dict like {'uuid': 'our-uuid', 'value': 'YourSecretValue=='}", 'When you will not pass these keys and there are already some of them defined in the system they will be removed.', 'Applicable for I(os_volume).'], 'default': [], 'version_added': '2.6'}",
    "authentication_url": "{'description': ['Keystone authentication URL of the openstack provider.', 'Applicable for those types: I(os_image), I(os_volume) and I(network).'], 'aliases': ['auth_url']}",
    "data_center": "{'description': ['Name of the data center where provider should be attached.', 'Applicable for those type: I(os_volume).']}",
    "description": "{'description': ['Description of the external provider.']}",
    "fetch_nested": "{'description': ['If I(True) the module will fetch additional data from the API.', 'It will fetch IDs of the VMs disks, snapshots, etc. User can configure to fetch other attributes of the nested entities by specifying C(nested_attributes).'], 'version_added': '2.3', 'type': 'bool'}",
    "name": "{'description': ['Name of the external provider to manage.']}",
    "nested_attributes": "{'description': ['Specifies list of the attributes which should be fetched from the API.', 'This parameter apply only when C(fetch_nested) is I(true).'], 'version_added': '2.3'}",
    "network_type": "{'description': ['Type of the external network provider either external (for example OVN) or neutron.', 'Applicable if C(type) is I(network).'], 'choices': ['external', 'neutron'], 'default': ['external']}",
    "password": "{'description': ['Password of the user specified in C(username) parameter.', 'Applicable for all types.']}",
    "poll_interval": "{'description': ['Number of the seconds the module waits until another poll request on entity status is sent.'], 'default': 3}",
    "read_only": "{'description': ['Specify if the network should be read only.', 'Applicable if C(type) is I(network).']}",
    "state": "{'description': ['Should the external be present or absent', 'When you are using absent for I(os_volume), you need to make sure that SD is not attached to the data center!'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "tenant_name": "{'description': ['Name of the tenant.', 'Applicable for those types: I(os_image), I(os_volume) and I(network).'], 'aliases': ['tenant']}",
    "timeout": "{'description': ['The amount of time in seconds the module should wait for the instance to get into desired state.'], 'default': 180}",
    "type": "{'description': ['Type of the external provider.'], 'choices': ['os_image', 'network', 'os_volume', 'foreman']}",
    "url": "{'description': ['URL where external provider is hosted.', 'Applicable for those types: I(os_image), I(os_volume), I(network) and I(foreman).']}",
    "username": "{'description': ['Username to be used for login to external provider.', 'Applicable for all types.']}",
    "wait": "{'description': ['I(True) if the module should wait for the entity to get into desired state.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Add image external provider:
- ovirt_external_provider:
    name: image_provider
    type: os_image
    url: http://1.2.3.4:9292
    username: admin
    password: 123456
    tenant: admin
    auth_url: http://1.2.3.4:35357/v2.0

# Add volume external provider:
- ovirt_external_provider:
    name: image_provider
    type: os_volume
    url: http://1.2.3.4:9292
    username: admin
    password: 123456
    tenant: admin
    auth_url: http://1.2.3.4:5000/v2.0
    authentication_keys:
      -
        uuid: "1234567-a1234-12a3-a234-123abc45678"
        value: "ABCD00000000111111222333445w=="

# Add foreman provider:
- ovirt_external_provider:
    name: foreman_provider
    type: foreman
    url: https://foreman.example.com
    username: admin
    password: 123456

# Add external network provider for OVN:
- ovirt_external_provider:
    name: ovn_provider
    type: network
    network_type: external
    url: http://1.2.3.4:9696

# Remove image external provider:
- ovirt_external_provider:
    state: absent
    name: image_provider
    type: os_image

```

## License

TODO

## Author Information
  - ['Ondra Machacek (@machacekondra)']
