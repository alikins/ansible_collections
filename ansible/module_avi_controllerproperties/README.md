# Ansible module: ansible.module_avi_controllerproperties


Module for setup of ControllerProperties Avi RESTful Object

## Description

This module is used to configure ControllerProperties object
more examples at U(https://github.com/avinetworks/devops)

## Requirements

TODO

## Arguments

``` json
{
    "allow_ip_forwarding": "{'description': ['Field introduced in 17.1.1.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'type': 'bool'}",
    "allow_unauthenticated_apis": "{'description': ['Allow unauthenticated access for special apis.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'type': 'bool'}",
    "allow_unauthenticated_nodes": "{'description': ['Boolean flag to set allow_unauthenticated_nodes.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'type': 'bool'}",
    "api_context": "{'description': ['Avi API context that includes current session ID and CSRF Token.', 'This allows user to perform single login and re-use the session.'], 'version_added': '2.5'}",
    "api_idle_timeout": "{'description': ['Allowed values are 0-1440.', 'Default value when not specified in API or module is interpreted by Avi Controller as 15.', 'Units(MIN).']}",
    "api_version": "{'description': ['Avi API version of to use for Avi API and objects.'], 'default': '16.4.4'}",
    "appviewx_compat_mode": "{'description': ['Export configuration in appviewx compatibility mode.', 'Field introduced in 17.1.1.', 'Default value when not specified in API or module is interpreted by Avi Controller as False.'], 'type': 'bool'}",
    "attach_ip_retry_interval": "{'description': ['Number of attach_ip_retry_interval.', 'Default value when not specified in API or module is interpreted by Avi Controller as 360.', 'Units(SEC).']}",
    "attach_ip_retry_limit": "{'description': ['Number of attach_ip_retry_limit.', 'Default value when not specified in API or module is interpreted by Avi Controller as 4.']}",
    "avi_api_patch_op": "{'description': ['Patch operation to use when using avi_api_update_method as patch.'], 'version_added': '2.5', 'choices': ['add', 'replace', 'delete']}",
    "avi_api_update_method": "{'description': ['Default method for object update is HTTP PUT.', 'Setting to patch will override that behavior to use HTTP PATCH.'], 'version_added': '2.5', 'default': 'put', 'choices': ['put', 'patch']}",
    "avi_credentials": "{'description': ['Avi Credentials dictionary which can be used in lieu of enumerating Avi Controller login details.'], 'version_added': '2.5'}",
    "bm_use_ansible": "{'description': ['Use ansible for se creation in baremetal.', 'Field introduced in 17.2.2.', 'Default value when not specified in API or module is interpreted by Avi Controller as True.'], 'version_added': '2.5', 'type': 'bool'}",
    "cluster_ip_gratuitous_arp_period": "{'description': ['Number of cluster_ip_gratuitous_arp_period.', 'Default value when not specified in API or module is interpreted by Avi Controller as 60.', 'Units(MIN).']}",
    "controller": "{'description': ['IP address or hostname of the controller. The default value is the environment variable C(AVI_CONTROLLER).'], 'default': ''}",
    "crashed_se_reboot": "{'description': ['Number of crashed_se_reboot.', 'Default value when not specified in API or module is interpreted by Avi Controller as 900.', 'Units(SEC).']}",
    "dead_se_detection_timer": "{'description': ['Number of dead_se_detection_timer.', 'Default value when not specified in API or module is interpreted by Avi Controller as 360.', 'Units(SEC).']}",
    "dns_refresh_period": "{'description': ['Number of dns_refresh_period.', 'Default value when not specified in API or module is interpreted by Avi Controller as 60.', 'Units(MIN).']}",
    "dummy": "{'description': ['Number of dummy.']}",
    "enable_memory_balancer": "{'description': ['Enable/disable memory balancer.', 'Field introduced in 17.2.8.', 'Default value when not specified in API or module is interpreted by Avi Controller as True.'], 'version_added': '2.6', 'type': 'bool'}",
    "fatal_error_lease_time": "{'description': ['Number of fatal_error_lease_time.', 'Default value when not specified in API or module is interpreted by Avi Controller as 120.', 'Units(SEC).']}",
    "max_dead_se_in_grp": "{'description': ['Number of max_dead_se_in_grp.', 'Default value when not specified in API or module is interpreted by Avi Controller as 1.']}",
    "max_pcap_per_tenant": "{'description': ['Maximum number of pcap files stored per tenant.', 'Default value when not specified in API or module is interpreted by Avi Controller as 4.']}",
    "max_seq_attach_ip_failures": "{'description': ['Maximum number of consecutive attach ip failures that halts vs placement.', 'Field introduced in 17.2.2.', 'Default value when not specified in API or module is interpreted by Avi Controller as 3.'], 'version_added': '2.5'}",
    "max_seq_vnic_failures": "{'description': ['Number of max_seq_vnic_failures.', 'Default value when not specified in API or module is interpreted by Avi Controller as 3.']}",
    "password": "{'description': ['Password of Avi user in Avi controller. The default value is the environment variable C(AVI_PASSWORD).'], 'default': ''}",
    "persistence_key_rotate_period": "{'description': ['Allowed values are 1-1051200.', "Special values are 0 - 'disabled'.", 'Default value when not specified in API or module is interpreted by Avi Controller as 60.', 'Units(MIN).']}",
    "portal_token": "{'description': ['Token used for uploading tech-support to portal.', 'Field introduced in 16.4.6,17.1.2.'], 'version_added': '2.4'}",
    "query_host_fail": "{'description': ['Number of query_host_fail.', 'Default value when not specified in API or module is interpreted by Avi Controller as 180.', 'Units(SEC).']}",
    "safenet_hsm_version": "{'description': ['Version of the safenet package installed on the controller.', 'Field introduced in 16.5.2,17.2.3.'], 'version_added': '2.5'}",
    "se_create_timeout": "{'description': ['Number of se_create_timeout.', 'Default value when not specified in API or module is interpreted by Avi Controller as 900.', 'Units(SEC).']}",
    "se_failover_attempt_interval": "{'description': ['Interval between attempting failovers to an se.', 'Default value when not specified in API or module is interpreted by Avi Controller as 300.', 'Units(SEC).']}",
    "se_offline_del": "{'description': ['Number of se_offline_del.', 'Default value when not specified in API or module is interpreted by Avi Controller as 172000.', 'Units(SEC).']}",
    "se_vnic_cooldown": "{'description': ['Number of se_vnic_cooldown.', 'Default value when not specified in API or module is interpreted by Avi Controller as 120.', 'Units(SEC).']}",
    "secure_channel_cleanup_timeout": "{'description': ['Number of secure_channel_cleanup_timeout.', 'Default value when not specified in API or module is interpreted by Avi Controller as 60.', 'Units(MIN).']}",
    "secure_channel_controller_token_timeout": "{'description': ['Number of secure_channel_controller_token_timeout.', 'Default value when not specified in API or module is interpreted by Avi Controller as 60.', 'Units(MIN).']}",
    "secure_channel_se_token_timeout": "{'description': ['Number of secure_channel_se_token_timeout.', 'Default value when not specified in API or module is interpreted by Avi Controller as 60.', 'Units(MIN).']}",
    "seupgrade_fabric_pool_size": "{'description': ['Pool size used for all fabric commands during se upgrade.', 'Default value when not specified in API or module is interpreted by Avi Controller as 20.']}",
    "seupgrade_segroup_min_dead_timeout": "{'description': ['Time to wait before marking segroup upgrade as stuck.', 'Default value when not specified in API or module is interpreted by Avi Controller as 360.', 'Units(SEC).']}",
    "ssl_certificate_expiry_warning_days": "{'description': ['Number of days for ssl certificate expiry warning.', 'Units(DAYS).']}",
    "state": "{'description': ['The state that should be applied on the entity.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "tenant": "{'description': ['Name of tenant used for all Avi API calls and context of object.'], 'default': 'admin'}",
    "tenant_uuid": "{'description': ['UUID of tenant used for all Avi API calls and context of object.'], 'default': ''}",
    "unresponsive_se_reboot": "{'description': ['Number of unresponsive_se_reboot.', 'Default value when not specified in API or module is interpreted by Avi Controller as 300.', 'Units(SEC).']}",
    "upgrade_dns_ttl": "{'description': ['Time to account for dns ttl during upgrade.', 'This is in addition to vs_scalein_timeout_for_upgrade in se_group.', 'Field introduced in 17.1.1.', 'Default value when not specified in API or module is interpreted by Avi Controller as 5.', 'Units(SEC).']}",
    "upgrade_lease_time": "{'description': ['Number of upgrade_lease_time.', 'Default value when not specified in API or module is interpreted by Avi Controller as 360.', 'Units(SEC).']}",
    "url": "{'description': ['Avi controller URL of the object.']}",
    "username": "{'description': ['Username used for accessing Avi controller. The default value is the environment variable C(AVI_USERNAME).'], 'default': ''}",
    "uuid": "{'description': ['Unique object identifier of the object.']}",
    "vnic_op_fail_time": "{'description': ['Number of vnic_op_fail_time.', 'Default value when not specified in API or module is interpreted by Avi Controller as 180.', 'Units(SEC).']}",
    "vs_apic_scaleout_timeout": "{'description': ['Time to wait for the scaled out se to become ready before marking the scaleout done, applies to apic configuration only.', 'Default value when not specified in API or module is interpreted by Avi Controller as 360.', 'Units(SEC).']}",
    "vs_awaiting_se_timeout": "{'description': ['Number of vs_awaiting_se_timeout.', 'Default value when not specified in API or module is interpreted by Avi Controller as 60.', 'Units(SEC).']}",
    "vs_key_rotate_period": "{'description': ['Allowed values are 1-1051200.', "Special values are 0 - 'disabled'.", 'Default value when not specified in API or module is interpreted by Avi Controller as 60.', 'Units(MIN).']}",
    "vs_se_attach_ip_fail": "{'description': ['Time to wait before marking attach ip operation on an se as failed.', 'Field introduced in 17.2.2.', 'Default value when not specified in API or module is interpreted by Avi Controller as 3600.', 'Units(SEC).'], 'version_added': '2.5'}",
    "vs_se_bootup_fail": "{'description': ['Number of vs_se_bootup_fail.', 'Default value when not specified in API or module is interpreted by Avi Controller as 480.', 'Units(SEC).']}",
    "vs_se_create_fail": "{'description': ['Number of vs_se_create_fail.', 'Default value when not specified in API or module is interpreted by Avi Controller as 1500.', 'Units(SEC).']}",
    "vs_se_ping_fail": "{'description': ['Number of vs_se_ping_fail.', 'Default value when not specified in API or module is interpreted by Avi Controller as 60.', 'Units(SEC).']}",
    "vs_se_vnic_fail": "{'description': ['Number of vs_se_vnic_fail.', 'Default value when not specified in API or module is interpreted by Avi Controller as 300.', 'Units(SEC).']}",
    "vs_se_vnic_ip_fail": "{'description': ['Number of vs_se_vnic_ip_fail.', 'Default value when not specified in API or module is interpreted by Avi Controller as 120.', 'Units(SEC).']}",
    "warmstart_se_reconnect_wait_time": "{'description': ['Number of warmstart_se_reconnect_wait_time.', 'Default value when not specified in API or module is interpreted by Avi Controller as 300.', 'Units(SEC).']}",
}
```

## Examples


``` yaml

- name: Example to create ControllerProperties object
  avi_controllerproperties:
    controller: 10.10.25.42
    username: admin
    password: something
    state: present
    name: sample_controllerproperties

```

## License

TODO

## Author Information
  - ['Gaurav Rastogi (grastogi@avinetworks.com)']
