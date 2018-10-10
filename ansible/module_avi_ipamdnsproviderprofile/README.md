# Ansible module: ansible.module_avi_ipamdnsproviderprofile


Module for setup of IpamDnsProviderProfile Avi RESTful Object

## Description

This module is used to configure IpamDnsProviderProfile object
more examples at U(https://github.com/avinetworks/devops)

## Requirements

TODO

## Arguments

``` json
{
    "allocate_ip_in_vrf": "{'description': ['If this flag is set, only allocate ip from networks in the virtual service vrf.', 'Applicable for avi vantage ipam only.', 'Field introduced in 17.2.4.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'version_added': '2.5', 'type': 'bool'}",
    "api_context": "{'description': ['Avi API context that includes current session ID and CSRF Token.', 'This allows user to perform single login and re-use the session.'], 'version_added': '2.5'}",
    "api_version": "{'description': ['Avi API version of to use for Avi API and objects.'], 'default': '16.4.4'}",
    "avi_api_patch_op": "{'description': ['Patch operation to use when using avi_api_update_method as patch.'], 'version_added': '2.5', 'choices': ['add', 'replace', 'delete']}",
    "avi_api_update_method": "{'description': ['Default method for object update is HTTP PUT.', 'Setting to patch will override that behavior to use HTTP PATCH.'], 'version_added': '2.5', 'default': 'put', 'choices': ['put', 'patch']}",
    "avi_credentials": "{'description': ['Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details.'], 'version_added': '2.5'}",
    "aws_profile": "{'description': ['Provider details if type is aws.']}",
    "azure_profile": "{'description': ['Provider details if type is microsoft azure.', 'Field introduced in 17.2.1.'], 'version_added': '2.5'}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "custom_profile": "{'description': ['Provider details if type is custom.', 'Field introduced in 17.1.1.']}",
    "gcp_profile": "{'description': ['Provider details if type is google cloud.']}",
    "infoblox_profile": "{'description': ['Provider details if type is infoblox.']}",
    "internal_profile": "{'description': ['Provider details if type is avi.']}",
    "name": "{'description': ['Name for the ipam/dns provider profile.'], 'required': True}",
    "openstack_profile": "{'description': ['Provider details if type is openstack.']}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "proxy_configuration": "{'description': ['Field introduced in 17.1.1.']}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "type": "{'description': ['Provider type for the ipam/dns provider profile.', 'Enum options - IPAMDNS_TYPE_INFOBLOX, IPAMDNS_TYPE_AWS, IPAMDNS_TYPE_OPENSTACK, IPAMDNS_TYPE_GCP, IPAMDNS_TYPE_INFOBLOX_DNS, IPAMDNS_TYPE_CUSTOM,', 'IPAMDNS_TYPE_CUSTOM_DNS, IPAMDNS_TYPE_AZURE, IPAMDNS_TYPE_INTERNAL, IPAMDNS_TYPE_INTERNAL_DNS, IPAMDNS_TYPE_AWS_DNS, IPAMDNS_TYPE_AZURE_DNS.'], 'required': True}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Uuid of the ipam/dns provider profile.']}",
}
```

## Examples


``` yaml

  - name: Create IPAM DNS provider setting
    avi_ipamdnsproviderprofile:
      controller: '{{ controller }}'
      username: '{{ username }}'
      password: '{{ password }}'
      internal_profile:
        dns_service_domain:
        - domain_name: ashish.local
          num_dns_ip: 1
          pass_through: true
          record_ttl: 100
        - domain_name: guru.local
          num_dns_ip: 1
          pass_through: true
          record_ttl: 200
        ttl: 300
      name: Ashish-DNS
      tenant_ref: Demo
      type: IPAMDNS_TYPE_INTERNAL

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
