# Ansible module: ansible.module_gcp_compute_target_pool


Creates a GCP TargetPool

## Description

Represents a TargetPool resource, used for Load Balancing.

## Requirements

TODO

## Arguments

``` json
{
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "backup_pool": "{'description': ['This field is applicable only when the containing target pool is serving a forwarding rule as the primary pool, and its failoverRatio field is properly set to a value between [0, 1].', 'backupPool and failoverRatio together define the fallback behavior of the primary target pool: if the ratio of the healthy instances in the primary pool is at or below failoverRatio, traffic arriving at the load-balanced IP will be directed to the backup pool.', 'In case where failoverRatio and backupPool are not set, or all the instances in the backup pool are unhealthy, the traffic will be directed back to the primary pool in the "force" mode, where traffic will be spread to the healthy instances with the best effort, or to all instances when no instance is healthy.'], 'required': False}",
    "description": "{'description': ['An optional description of this resource.'], 'required': False}",
    "failover_ratio": "{'description': ['This field is applicable only when the containing target pool is serving a forwarding rule as the primary pool (i.e., not as a backup pool to some other target pool). The value of the field must be in [0, 1].', 'If set, backupPool must also be set. They together define the fallback behavior of the primary target pool: if the ratio of the healthy instances in the primary pool is at or below this number, traffic arriving at the load-balanced IP will be directed to the backup pool.', 'In case where failoverRatio is not set or all the instances in the backup pool are unhealthy, the traffic will be directed back to the primary pool in the "force" mode, where traffic will be spread to the healthy instances with the best effort, or to all instances when no instance is healthy.'], 'required': False}",
    "health_check": "{'description': ['A reference to a HttpHealthCheck resource.', 'A member instance in this pool is considered healthy if and only if the health checks pass. If not specified it means all member instances will be considered healthy at all times.'], 'required': False}",
    "instances": "{'description': ['A list of virtual machine instances serving this pool.', 'They must live in zones contained in the same region as this pool.'], 'required': False}",
    "name": "{'description': ['Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.'], 'required': True}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "region": "{'description': ['The region where the target pool resides.'], 'required': True}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "session_affinity": "{'description': ['Session affinity option. Must be one of these values:  - NONE: Connections from the same client IP may go to any instance in   the pool.', '- CLIENT_IP: Connections from the same client IP will go to the same   instance in the pool while that instance remains healthy.', '- CLIENT_IP_PROTO: Connections from the same client IP with the same   IP protocol will go to the same instance in the pool while that   instance remains healthy.'], 'required': False, 'choices': ['NONE', 'CLIENT_IP', 'CLIENT_IP_PROTO']}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
}
```

## Examples


``` yaml

- name: create a target pool
  gcp_compute_target_pool:
      name: "test_object"
      region: us-west1
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
