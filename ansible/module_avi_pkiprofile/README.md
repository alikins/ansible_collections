# Ansible module: ansible.module_avi_pkiprofile


Module for setup of PKIProfile Avi RESTful Object

## Description

This module is used to configure PKIProfile object
more examples at U(https://github.com/avinetworks/devops)

## Requirements

TODO

## Arguments

``` json
{
    "api_context": "{'description': ['Avi API context that includes current session ID and CSRF Token.', 'This allows user to perform single login and re-use the session.'], 'version_added': '2.5'}",
    "api_version": "{'description': ['Avi API version of to use for Avi API and objects.'], 'default': '16.4.4'}",
    "avi_api_patch_op": "{'description': ['Patch operation to use when using avi_api_update_method as patch.'], 'version_added': '2.5', 'choices': ['add', 'replace', 'delete']}",
    "avi_api_update_method": "{'description': ['Default method for object update is HTTP PUT.', 'Setting to patch will override that behavior to use HTTP PATCH.'], 'version_added': '2.5', 'default': 'put', 'choices': ['put', 'patch']}",
    "avi_credentials": "{'description': ['Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details.'], 'version_added': '2.5'}",
    "ca_certs": "{'description': ['List of certificate authorities (root and intermediate) trusted that is used for certificate validation.']}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "created_by": "{'description': ['Creator name.']}",
    "crl_check": "{'description': ['When enabled, avi will verify via crl checks that certificates in the trust chain have not been revoked.', 'Default value when not specified in API or module is interpreted by Avi Controller as True.'], 'type': 'bool'}",
    "crls": "{'description': ['Certificate revocation lists.']}",
    "ignore_peer_chain": "{'description': ['When enabled, avi will not trust intermediate and root certs presented by a client.', "Instead, only the chain certs configured in the certificate authority section will be used to verify trust of the client's cert.", 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'type': 'bool'}",
    "is_federated": "{'description': ["This field describes the object's replication scope.", 'If the field is set to false, then the object is visible within the controller-cluster and its associated service-engines.', 'If the field is set to true, then the object is replicated across the federation.', 'Field introduced in 17.1.3.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'version_added': '2.4', 'type': 'bool'}",
    "name": "{'description': ['Name of the pki profile.'], 'required': True}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Unique object identifier of the object.']}",
    "validate_only_leaf_crl": "{'description': ['When enabled, avi will only validate the revocation status of the leaf certificate using crl.', 'To enable validation for the entire chain, disable this option and provide all the relevant crls.', 'Default value when not specified in API or module is interpreted by Avi Controller as True.'], 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: Example to create PKIProfile object
  avi_pkiprofile:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_pkiprofile

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
