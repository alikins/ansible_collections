# Ansible module: ansible.module_spotinst_aws_elastigroup


Create, update or delete Spotinst AWS Elastigroups

## Description

Can create, update, or delete Spotinst AWS Elastigroups Launch configuration is part of the elastigroup configuration, so no additional modules are necessary for handling the launch configuration. You will have to have a credentials file in this location - <home>/.spotinst/credentials The credentials file must contain a row that looks like this token = <YOUR TOKEN> Full documentation available at https://help.spotinst.com/hc/en-us/articles/115003530285-Ansible-

## Requirements

TODO

## Arguments

``` json
{
    "account_id": "{'description': ['(String) Optional parameter that allows to set an account-id inside the module configuration By default this is retrieved from the credentials path']}",
    "availability_vs_cost": "{'choices': ['availabilityOriented', 'costOriented', 'balanced'], 'description': ['(String) The strategy orientation.'], 'required': True}",
    "availability_zones": "{'description': ['(List of Objects) a list of hash/dictionaries of Availability Zones that are configured in the elastigroup; \'[{"key":"value", "key":"value"}]\'; keys allowed are name (String), subnet_id (String), placement_group_name (String),'], 'required': True}",
    "block_device_mappings": "{'description': ['(List of Objects) a list of hash/dictionaries of Block Device Mappings for elastigroup instances; You can specify virtual devices and EBS volumes.; \'[{"key":"value", "key":"value"}]\'; keys allowed are device_name (List of Strings), virtual_name (String), no_device (String), ebs (Object, expects the following keys- delete_on_termination(Boolean), encrypted(Boolean), iops (Integer), snapshot_id(Integer), volume_type(String), volume_size(Integer))']}",
    "chef": "{'description': ['(Object) The Chef integration configuration.; Expects the following keys - chef_server (String), organization (String), user (String), pem_key (String), chef_version (String)']}",
    "credentials_path": "{'description': ['(String) Optional parameter that allows to set a non-default credentials path. Default is ~/.spotinst/credentials']}",
    "down_scaling_policies": "{'description': ['(List of Objects) a list of hash/dictionaries of scaling policies to configure in the elastigroup; \'[{"key":"value", "key":"value"}]\'; keys allowed are - policy_name (String, required), namespace (String, required), metric_name (String, required), dimensions ((List of Objects), Keys allowed are name (String, required) and value (String)), statistic (String, required), evaluation_periods (String, required), period (String, required), threshold (String, required), cooldown (String, required), unit (String, required), operator (String, required), action_type (String, required), adjustment (String), max_target_capacity (String), target (String), maximum (String), minimum (String)']}",
    "draining_timeout": "{'description': ['(Integer) Time for instance to be drained from incoming requests and deregistered from ELB before termination.']}",
    "ebs_optimized": "{'description': ['(Boolean) Enable EBS optimization for supported instances which are not enabled by default.; Note - additional charges will be applied.']}",
    "ebs_volume_pool": "{'description': ['(List of Objects) a list of hash/dictionaries of EBS devices to reattach to the elastigroup when available; \'[{"key":"value", "key":"value"}]\'; keys allowed are - volume_ids (List of Strings), device_name (String)']}",
    "ecs": "{'description': ['(Object) The ECS integration configuration.; Expects the following key - cluster_name (String)']}",
    "elastic_ips": "{'description': ['(List of Strings) List of ElasticIps Allocation Ids (Example C(eipalloc-9d4e16f8)) to associate to the group instances']}",
    "fallback_to_od": "{'description': ['(Boolean) In case of no spots available, Elastigroup will launch an On-demand instance instead']}",
    "health_check_grace_period": "{'description': ['(Integer) The amount of time, in seconds, after the instance has launched to start and check its health.'], 'default': 300}",
    "health_check_type": "{'choices': ['ELB', 'HCS', 'TARGET_GROUP', 'MLB', 'EC2'], 'description': ['(String) The service to use for the health check.']}",
    "health_check_unhealthy_duration_before_replacement": "{'description': ['(Integer) Minimal mount of time instance should be unhealthy for us to consider it unhealthy.']}",
    "iam_role_arn": "{'description': ['(String) The instance profile iamRole arn', 'Only use iam_role_arn, or iam_role_name']}",
    "iam_role_name": "{'description': ['(String) The instance profile iamRole name', 'Only use iam_role_arn, or iam_role_name']}",
    "id": "{'description': ['(String) The group id if it already exists and you want to update, or delete it. This will not work unless the uniqueness_by field is set to id. When this is set, and the uniqueness_by field is set, the group will either be updated or deleted, but not created.']}",
    "ignore_changes": "{'choices': ['image_id', 'target'], 'description': ['(List of Strings) list of fields on which changes should be ignored when updating']}",
    "image_id": "{'description': ['(String) The image Id used to launch the instance.; In case of conflict between Instance type and image type, an error will be returned'], 'required': True}",
    "key_pair": "{'description': ['(String) Specify a Key Pair to attach to the instances'], 'required': True}",
    "kubernetes": "{'description': ['(Object) The Kubernetes integration configuration. Expects the following keys - api_server (String), token (String)']}",
    "lifetime_period": "{'description': ['(String) lifetime period']}",
    "load_balancers": "{'description': ['(List of Strings) List of classic ELB names']}",
    "max_size": "{'description': ['(Integer) The upper limit number of instances that you can scale up to'], 'required': True}",
    "mesosphere": "{'description': ['(Object) The Mesosphere integration configuration. Expects the following key - api_server (String)']}",
    "min_size": "{'description': ['(Integer) The lower limit number of instances that you can scale down to'], 'required': True}",
    "monitoring": "{'description': ['(Boolean) Describes whether instance Enhanced Monitoring is enabled'], 'required': True}",
    "name": "{'description': ['(String) Unique name for elastigroup to be created, updated or deleted'], 'required': True}",
    "network_interfaces": "{'description': ['(List of Objects) a list of hash/dictionaries of network interfaces to add to the elastigroup; \'[{"key":"value", "key":"value"}]\'; keys allowed are - description (String), device_index (Integer), secondary_private_ip_address_count (Integer), associate_public_ip_address (Boolean), delete_on_termination (Boolean), groups (List of Strings), network_interface_id (String), private_ip_address (String), subnet_id (String), associate_ipv6_address (Boolean), private_ip_addresses (List of Objects, Keys are privateIpAddress (String, required) and primary (Boolean))']}",
    "on_demand_count": "{'description': ['(Integer) Required if risk is not set', 'Number of on demand instances to launch. All other instances will be spot instances.; Either set this parameter or the risk parameter']}",
    "on_demand_instance_type": "{'description': ['(String) On-demand instance type that will be provisioned'], 'required': True}",
    "opsworks": "{'description': ['(Object) The elastigroup OpsWorks integration configration.; Expects the following key - layer_id (String)']}",
    "persistence": "{'description': ['(Object) The Stateful elastigroup configration.; Accepts the following keys - should_persist_root_device (Boolean), should_persist_block_devices (Boolean), should_persist_private_ip (Boolean)']}",
    "product": "{'choices': ['Linux/UNIX', 'SUSE Linux', 'Windows', 'Linux/UNIX (Amazon VPC)', 'SUSE Linux (Amazon VPC)', 'Windows'], 'description': ['(String) Operation system type._'], 'required': True}",
    "rancher": "{'description': ['(Object) The Rancher integration configuration.; Expects the following keys - access_key (String), secret_key (String), master_host (String)']}",
    "right_scale": "{'description': ['(Object) The Rightscale integration configuration.; Expects the following keys - account_id (String), refresh_token (String)']}",
    "risk": "{'description': ['(Integer) required if on demand is not set. The percentage of Spot instances to launch (0 - 100).']}",
    "roll_config": "{'description': ['(Object) Roll configuration.; If you would like the group to roll after updating, please use this feature. Accepts the following keys - batch_size_percentage(Integer, Required), grace_period - (Integer, Required), health_check_type(String, Optional)']}",
    "scheduled_tasks": "{'description': ['(List of Objects) a list of hash/dictionaries of scheduled tasks to configure in the elastigroup; \'[{"key":"value", "key":"value"}]\'; keys allowed are - adjustment (Integer), scale_target_capacity (Integer), scale_min_capacity (Integer), scale_max_capacity (Integer), adjustment_percentage (Integer), batch_size_percentage (Integer), cron_expression (String), frequency (String), grace_period (Integer), task_type (String, required), is_enabled (Boolean)']}",
    "security_group_ids": "{'description': ['(List of Strings) One or more security group IDs. ; In case of update it will override the existing Security Group with the new given array'], 'required': True}",
    "shutdown_script": "{'description': ['(String) The Base64-encoded shutdown script that executes prior to instance termination. Encode before setting.']}",
    "signals": "{'description': ['(List of Objects) a list of hash/dictionaries of signals to configure in the elastigroup; keys allowed are - name (String, required), timeout (Integer)']}",
    "spin_up_time": "{'description': ['(Integer) spin up time, in seconds, for the instance']}",
    "spot_instance_types": "{'description': ['(List of Strings) Spot instance type that will be provisioned.'], 'required': True}",
    "state": "{'choices': ['present', 'absent'], 'description': ['(String) create or delete the elastigroup']}",
    "tags": "{'description': ['(List of tagKey:tagValue paris) a list of tags to configure in the elastigroup. Please specify list of keys and values (key colon value);']}",
    "target": "{'description': ['(Integer) The number of instances to launch'], 'required': True}",
    "target_group_arns": "{'description': ['(List of Strings) List of target group arns instances should be registered to']}",
    "target_tracking_policies": "{'description': ['(List of Objects) a list of hash/dictionaries of target tracking policies to configure in the elastigroup; \'[{"key":"value", "key":"value"}]\'; keys allowed are - policy_name (String, required), namespace (String, required), source (String, required), metric_name (String, required), statistic (String, required), unit (String, required), cooldown (String, required), target (String, required)']}",
    "tenancy": "{'choices': ['default', 'dedicated'], 'description': ['(String) dedicated vs shared tenancy']}",
    "terminate_at_end_of_billing_hour": "{'description': ['(Boolean) terminate at the end of billing hour']}",
    "uniqueness_by": "{'choices': ['id', 'name'], 'description': ['(String) If your group names are not unique, you may use this feature to update or delete a specific group. Whenever this property is set, you must set a group_id in order to update or delete a group, otherwise a group will be created.']}",
    "unit": "{'choices': ['instance', 'weight'], 'description': ['(String) The capacity unit to launch instances by.'], 'required': True}",
    "up_scaling_policies": "{'description': ['(List of Objects) a list of hash/dictionaries of scaling policies to configure in the elastigroup; \'[{"key":"value", "key":"value"}]\'; keys allowed are - policy_name (String, required), namespace (String, required), metric_name (String, required), dimensions (List of Objects, Keys allowed are name (String, required) and value (String)), statistic (String, required) evaluation_periods (String, required), period (String, required), threshold (String, required), cooldown (String, required), unit (String, required), operator (String, required), action_type (String, required), adjustment (String), min_target_capacity (String), target (String), maximum (String), minimum (String)']}",
    "user_data": "{'description': ['(String) Base64-encoded MIME user data. Encode before setting the value.']}",
    "utilize_reserved_instances": "{'description': ['(Boolean) In case of any available Reserved Instances, Elastigroup will utilize your reservations before purchasing Spot instances.']}",
    "wait_for_instances": "{'description': ['(Boolean) Whether or not the elastigroup creation / update actions should wait for the instances to spin']}",
    "wait_timeout": "{'description': ['(Integer) How long the module should wait for instances before failing the action.; Only works if wait_for_instances is True.']}",
}
```

## Examples


``` yaml

# Basic configuration YAML example

- hosts: localhost
  tasks:
    - name: create elastigroup
      spotinst_aws_elastigroup:
          state: present
          risk: 100
          availability_vs_cost: balanced
          availability_zones:
            - name: us-west-2a
              subnet_id: subnet-2b68a15c
          image_id: ami-f173cc91
          key_pair: spotinst-oregon
          max_size: 15
          min_size: 0
          target: 0
          unit: instance
          monitoring: True
          name: ansible-group
          on_demand_instance_type: c3.large
          product: Linux/UNIX
          load_balancers:
            - test-lb-1
          security_group_ids:
            - sg-8f4b8fe9
          spot_instance_types:
            - c3.large
          do_not_update:
            - image_id
            - target
      register: result
    - debug: var=result

# In this example, we create an elastigroup and wait 600 seconds to retrieve the instances, and use their private ips

- hosts: localhost
  tasks:
    - name: create elastigroup
      spotinst_aws_elastigroup:
          state: present
          account_id: act-1a9dd2b
          risk: 100
          availability_vs_cost: balanced
          availability_zones:
            - name: us-west-2a
              subnet_id: subnet-2b68a15c
          tags:
            - Environment: someEnvValue
            - OtherTagKey: otherValue
          image_id: ami-f173cc91
          key_pair: spotinst-oregon
          max_size: 5
          min_size: 0
          target: 0
          unit: instance
          monitoring: True
          name: ansible-group-tal
          on_demand_instance_type: c3.large
          product: Linux/UNIX
          security_group_ids:
            - sg-8f4b8fe9
          block_device_mappings:
            - device_name: '/dev/sda1'
              ebs:
                volume_size: 100
                volume_type: gp2
          spot_instance_types:
            - c3.large
          do_not_update:
            - image_id
          wait_for_instances: True
          wait_timeout: 600
      register: result

    - name: Store private ips to file
      shell: echo {{ item.private_ip }}\n >> list-of-private-ips
      with_items: "{{ result.instances }}"
    - debug: var=result

# In this example, we create an elastigroup with multiple block device mappings, tags, and also an account id
# In organizations with more than one account, it is required to specify an account_id

- hosts: localhost
  tasks:
    - name: create elastigroup
      spotinst_aws_elastigroup:
          state: present
          account_id: act-1a9dd2b
          risk: 100
          availability_vs_cost: balanced
          availability_zones:
            - name: us-west-2a
              subnet_id: subnet-2b68a15c
          tags:
            - Environment: someEnvValue
            - OtherTagKey: otherValue
          image_id: ami-f173cc91
          key_pair: spotinst-oregon
          max_size: 5
          min_size: 0
          target: 0
          unit: instance
          monitoring: True
          name: ansible-group-tal
          on_demand_instance_type: c3.large
          product: Linux/UNIX
          security_group_ids:
            - sg-8f4b8fe9
          block_device_mappings:
            - device_name: '/dev/xvda'
              ebs:
                volume_size: 60
                volume_type: gp2
            - device_name: '/dev/xvdb'
              ebs:
                volume_size: 120
                volume_type: gp2
          spot_instance_types:
            - c3.large
          do_not_update:
            - image_id
          wait_for_instances: True
          wait_timeout: 600
      register: result

    - name: Store private ips to file
      shell: echo {{ item.private_ip }}\n >> list-of-private-ips
      with_items: "{{ result.instances }}"
    - debug: var=result

# In this example we have set up block device mapping with ephemeral devices

- hosts: localhost
  tasks:
    - name: create elastigroup
      spotinst_aws_elastigroup:
          state: present
          risk: 100
          availability_vs_cost: balanced
          availability_zones:
            - name: us-west-2a
              subnet_id: subnet-2b68a15c
          image_id: ami-f173cc91
          key_pair: spotinst-oregon
          max_size: 15
          min_size: 0
          target: 0
          unit: instance
          block_device_mappings:
            - device_name: '/dev/xvda'
              virtual_name: ephemeral0
            - device_name: '/dev/xvdb/'
              virtual_name: ephemeral1
          monitoring: True
          name: ansible-group
          on_demand_instance_type: c3.large
          product: Linux/UNIX
          load_balancers:
            - test-lb-1
          security_group_ids:
            - sg-8f4b8fe9
          spot_instance_types:
            - c3.large
          do_not_update:
            - image_id
            - target
      register: result
    - debug: var=result

# In this example we create a basic group configuration with a network interface defined.
# Each network interface must have a device index

- hosts: localhost
  tasks:
    - name: create elastigroup
      spotinst_aws_elastigroup:
          state: present
          risk: 100
          availability_vs_cost: balanced
          network_interfaces:
            - associate_public_ip_address: true
              device_index: 0
          availability_zones:
            - name: us-west-2a
              subnet_id: subnet-2b68a15c
          image_id: ami-f173cc91
          key_pair: spotinst-oregon
          max_size: 15
          min_size: 0
          target: 0
          unit: instance
          monitoring: True
          name: ansible-group
          on_demand_instance_type: c3.large
          product: Linux/UNIX
          load_balancers:
            - test-lb-1
          security_group_ids:
            - sg-8f4b8fe9
          spot_instance_types:
            - c3.large
          do_not_update:
            - image_id
            - target
      register: result
    - debug: var=result


# In this example we create a basic group configuration with a target tracking scaling policy defined

- hosts: localhost
  tasks:
    - name: create elastigroup
      spotinst_aws_elastigroup:
          account_id: act-92d45673
          state: present
          risk: 100
          availability_vs_cost: balanced
          availability_zones:
            - name: us-west-2a
              subnet_id: subnet-79da021e
          image_id: ami-f173cc91
          fallback_to_od: true
          tags:
            - Creator: ValueOfCreatorTag
            - Environment: ValueOfEnvironmentTag
          key_pair: spotinst-labs-oregon
          max_size: 10
          min_size: 0
          target: 2
          unit: instance
          monitoring: True
          name: ansible-group-1
          on_demand_instance_type: c3.large
          product: Linux/UNIX
          security_group_ids:
            - sg-46cdc13d
          spot_instance_types:
            - c3.large
          target_tracking_policies:
            - policy_name: target-tracking-1
              namespace: AWS/EC2
              metric_name: CPUUtilization
              statistic: average
              unit: percent
              target: 50
              cooldown: 120
          do_not_update:
            - image_id
      register: result
    - debug: var=result


```

## License

TODO

## Author Information
  - ['Spotinst']
