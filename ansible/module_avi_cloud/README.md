# Ansible module: ansible.module_avi_cloud


Module for setup of Cloud Avi RESTful Object

## Description

This module is used to configure Cloud object
more examples at U(https://github.com/avinetworks/devops)

## Requirements

TODO

## Arguments

``` json
{
    "api_context": "{'description': ['Avi API context that includes current session ID and CSRF Token.', 'This allows user to perform single login and re-use the session.'], 'version_added': '2.5'}",
    "api_version": "{'description': ['Avi API version of to use for Avi API and objects.'], 'default': '16.4.4'}",
    "apic_configuration": "{'description': ['Apicconfiguration settings for cloud.']}",
    "apic_mode": "{'description': ['Boolean flag to set apic_mode.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'type': 'bool'}",
    "avi_api_patch_op": "{'description': ['Patch operation to use when using avi_api_update_method as patch.'], 'version_added': '2.5', 'choices': ['add', 'replace', 'delete']}",
    "avi_api_update_method": "{'description': ['Default method for object update is HTTP PUT.', 'Setting to patch will override that behavior to use HTTP PATCH.'], 'version_added': '2.5', 'default': 'put', 'choices': ['put', 'patch']}",
    "avi_credentials": "{'description': ['Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details.'], 'version_added': '2.5'}",
    "aws_configuration": "{'description': ['Awsconfiguration settings for cloud.']}",
    "azure_configuration": "{'description': ['Field introduced in 17.2.1.'], 'version_added': '2.5'}",
    "cloudstack_configuration": "{'description': ['Cloudstackconfiguration settings for cloud.']}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "custom_tags": "{'description': ['Custom tags for all avi created resources in the cloud infrastructure.', 'Field introduced in 17.1.5.'], 'version_added': '2.5'}",
    "dhcp_enabled": "{'description': ['Select the ip address management scheme.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'type': 'bool'}",
    "dns_provider_ref": "{'description': ['Dns profile for the cloud.', 'It is a reference to an object of type ipamdnsproviderprofile.']}",
    "docker_configuration": "{'description': ['Dockerconfiguration settings for cloud.']}",
    "east_west_dns_provider_ref": "{'description': ['Dns profile for east-west services.', 'It is a reference to an object of type ipamdnsproviderprofile.']}",
    "east_west_ipam_provider_ref": "{'description': ['Ipam profile for east-west services.', 'Warning - please use virtual subnets in this ipam profile that do not conflict with the underlay networks or any overlay networks in the cluster.', 'For example in aws and gcp, 169.254.0.0/16 is used for storing instance metadata.', 'Hence, it should not be used in this profile.', 'It is a reference to an object of type ipamdnsproviderprofile.']}",
    "enable_vip_static_routes": "{'description': ['Use static routes for vip side network resolution during virtualservice placement.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'type': 'bool'}",
    "ipam_provider_ref": "{'description': ['Ipam profile for the cloud.', 'It is a reference to an object of type ipamdnsproviderprofile.']}",
    "license_tier": "{'description': ['Specifies the default license tier which would be used by new se groups.', 'This field by default inherits the value from system configuration.', 'Enum options - ENTERPRISE_16, ENTERPRISE_18.', 'Field introduced in 17.2.5.'], 'version_added': '2.5'}",
    "license_type": "{'description': ['If no license type is specified then default license enforcement for the cloud type is chosen.', 'The default mappings are container cloud is max ses, openstack and vmware is cores and linux it is sockets.', 'Enum options - LIC_BACKEND_SERVERS, LIC_SOCKETS, LIC_CORES, LIC_HOSTS, LIC_SE_BANDWIDTH.']}",
    "linuxserver_configuration": "{'description': ['Linuxserverconfiguration settings for cloud.']}",
    "mesos_configuration": "{'description': ['Mesosconfiguration settings for cloud.']}",
    "mtu": "{'description': ['Mtu setting for the cloud.', 'Default value when not specified in API or module is interpreted by Avi Controller as 1500.', 'Units(BYTES).']}",
    "name": "{'description': ['Name of the object.'], 'required': True}",
    "nsx_configuration": "{'description': ['Configuration parameters for nsx manager.', 'Field introduced in 17.1.1.']}",
    "obj_name_prefix": "{'description': ['Default prefix for all automatically created objects in this cloud.', 'This prefix can be overridden by the se-group template.']}",
    "openstack_configuration": "{'description': ['Openstackconfiguration settings for cloud.']}",
    "oshiftk8s_configuration": "{'description': ['Oshiftk8sconfiguration settings for cloud.']}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "prefer_static_routes": "{'description': ['Prefer static routes over interface routes during virtualservice placement.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'type': 'bool'}",
    "proxy_configuration": "{'description': ['Proxyconfiguration settings for cloud.']}",
    "rancher_configuration": "{'description': ['Rancherconfiguration settings for cloud.']}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "state_based_dns_registration": "{'description': ['Dns records for vips are added/deleted based on the operational state of the vips.', 'Field introduced in 17.1.12.', 'Default value when not specified in API or module is interpreted by Avi Controller as True.'], 'version_added': '2.5', 'type': 'bool'}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_ref": "{'description': ['It is a reference to an object of type tenant.']}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Unique object identifier of the object.']}",
    "vca_configuration": "{'description': ['Vcloudairconfiguration settings for cloud.']}",
    "vcenter_configuration": "{'description': ['Vcenterconfiguration settings for cloud.']}",
    "vtype": "{'description': ['Cloud type.', 'Enum options - CLOUD_NONE, CLOUD_VCENTER, CLOUD_OPENSTACK, CLOUD_AWS, CLOUD_VCA, CLOUD_APIC, CLOUD_MESOS, CLOUD_LINUXSERVER, CLOUD_DOCKER_UCP,', 'CLOUD_RANCHER, CLOUD_OSHIFT_K8S, CLOUD_AZURE.', 'Default value when not specified in API or module is interpreted by Avi Controller as CLOUD_NONE.'], 'required': True}",
}
```

## Examples


``` yaml

  - name: Create a VMWare cloud with write access mode
    avi_cloud:
      username: '{{ username }}'
      controller: '{{ controller }}'
      password: '{{ password }}'
      apic_mode: false
      dhcp_enabled: true
      enable_vip_static_routes: false
      license_type: LIC_CORES
      mtu: 1500
      name: VCenter Cloud
      prefer_static_routes: false
      tenant_ref: admin
      vcenter_configuration:
        datacenter_ref: /api/vimgrdcruntime/datacenter-2-10.10.20.100
        management_network: /api/vimgrnwruntime/dvportgroup-103-10.10.20.100
        password: password
        privilege: WRITE_ACCESS
        username: user
        vcenter_url: 10.10.20.100
      vtype: CLOUD_VCENTER

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
