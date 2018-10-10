# Ansible module: ansible.module_one_vm


Creates or terminates OpenNebula instances

## Description

Manages OpenNebula instances

## Requirements

TODO

## Arguments

``` json
{
    "api_password": "{'description': ['Password of the user to login into OpenNebula RPC server. If not set']}",
    "api_url": "{'description': ['URL of the OpenNebula RPC server.', 'It is recommended to use HTTPS so that the username/password are not', 'transferred over the network unencrypted.', 'If not set then the value of the C(ONE_URL) environment variable is used.']}",
    "api_username": "{'description': ['Name of the user to login into the OpenNebula RPC server. If not set', 'then the value of the C(ONE_USERNAME) environment variable is used.']}",
    "attributes": "{'description': ['A dictionary of key/value attributes to add to new instances, or for', 'setting C(state) of instances with these attributes.', 'Keys are case insensitive and OpenNebula automatically converts them to upper case.', "Be aware C(NAME) is a special attribute which sets the name of the VM when it's deployed.", 'C(#) character(s) can be appended to the C(NAME) and the module will automatically add', 'indexes to the names of VMs.', "For example':' C(NAME':' foo-###) would create VMs with names C(foo-000), C(foo-001),...", 'When used with C(count_attributes) and C(exact_count) the module will', 'match the base name without the index part.'], 'default': {}}",
    "count": "{'description': ['Number of instances to launch'], 'default': 1}",
    "count_attributes": "{'description': ['A dictionary of key/value attributes that can only be used with', 'C(exact_count) to determine how many nodes based on a specific', 'attributes criteria should be deployed. This can be expressed in', 'multiple ways and is shown in the EXAMPLES section.']}",
    "count_labels": "{'description': ['A list of labels that can only be used with C(exact_count) to determine', 'how many nodes based on a specific labels criteria should be deployed.', 'This can be expressed in multiple ways and is shown in the EXAMPLES', 'section.']}",
    "cpu": "{'description': ['Percentage of CPU divided by 100 required for the new instance. Half a', 'processor is written 0.5.']}",
    "disk_saveas": "{'description': ['Creates an image from a VM disk.', 'It is a dictionary where you have to specife C(name) of the new image.', 'Optionally you can specife C(disk_id) of the disk you want to save. By default C(disk_id) is 0.', "I(NOTE)':' This operation will only be performed on the first VM (if more than one VM ID is passed)", 'and the VM has to be in the C(poweredoff) state.', 'Also this operation will fail if an image with specified C(name) already exists.']}",
    "disk_size": "{'description': ['The size of the disk created for new instances (in MB, GB, TB,...).', "NOTE':' This option can be used only if the VM template specified with", 'C(template_id)/C(template_name) has exactly one disk.']}",
    "exact_count": "{'description': ['Indicates how many instances that match C(count_attributes) and', 'C(count_labels) parameters should be deployed. Instances are either', 'created or terminated based on this value.', "NOTE':' Instances with the least IDs will be terminated first."]}",
    "group_id": "{'description': ['ID of the group which will be set as the group of the instance']}",
    "hard": "{'description': ['Reboot, power-off or terminate instances C(hard)'], 'default': False, 'type': 'bool'}",
    "instance_ids": "{'description': ["A list of instance ids used for states':' C(absent), C(running), C(rebooted), C(poweredoff)"], 'aliases': ['ids']}",
    "labels": "{'description': ['A list of labels to associate with new instances, or for setting', 'C(state) of instances with these labels.'], 'default': []}",
    "memory": "{'description': ['The size of the memory for new instances (in MB, GB, ...)']}",
    "mode": "{'description': ['Set permission mode of the instance in octet format, e.g. C(600) to give owner C(use) and C(manage) and nothing to group and others.']}",
    "networks": "{'description': ['A list of dictionaries with network parameters. See examples for more details.'], 'default': []}",
    "owner_id": "{'description': ['ID of the user which will be set as the owner of the instance']}",
    "state": "{'description': ['C(present) - create instances from a template specified with C(template_id)/C(template_name).', 'C(running) - run instances', 'C(poweredoff) - power-off instances', 'C(rebooted) - reboot instances', 'C(absent) - terminate instances'], 'choices': ['present', 'absent', 'running', 'rebooted', 'poweredoff'], 'default': 'present'}",
    "template_id": "{'description': ['ID of a VM template to use to create a new instance']}",
    "template_name": "{'description': ['Name of VM template to use to create a new instace']}",
    "vcpu": "{'description': ['Number of CPUs (cores) new VM will have.']}",
    "wait": "{'description': ['Wait for the instance to reach its desired state before returning. Keep', 'in mind if you are waiting for instance to be in running state it', "doesn't mean that you will be able to SSH on that machine only that", "boot process have started on that instance, see 'wait_for' example for", 'details.'], 'default': True, 'type': 'bool'}",
    "wait_timeout": "{'description': ['How long before wait gives up, in seconds'], 'default': 300}",
}
```

## Examples


``` yaml

# Create a new instance
- one_vm:
    template_id: 90
  register: result

# Print VM properties
- debug:
    msg: result

# Deploy a new VM and set its name to 'foo'
- one_vm:
    template_name: 'app1_template'
    attributes:
      name: foo

# Deploy a new VM and set its group_id and mode
- one_vm:
    template_id: 90
    group_id: 16
    mode: 660

# Change VM's permissions to 640
- one_vm:
    instance_ids: 5
    mode: 640

# Deploy 2 new instances and set memory, vcpu, disk_size and 3 networks
- one_vm:
    template_id: 15
    disk_size: 35.2 GB
    memory: 4 GB
    vcpu: 4
    count: 2
    networks:
      - NETWORK_ID: 27
      - NETWORK: "default-network"
        NETWORK_UNAME: "app-user"
        SECURITY_GROUPS: "120,124"
      - NETWORK_ID: 27
        SECURITY_GROUPS: "10"

# Deploy an new instance with attribute 'bar: bar1' and set its name to 'foo'
- one_vm:
    template_id: 53
    attributes:
      name: foo
      bar: bar1

# Enforce that 2 instances with attributes 'foo1: app1' and 'foo2: app2' are deployed
- one_vm:
    template_id: 53
    attributes:
      foo1: app1
      foo2: app2
    exact_count: 2
    count_attributes:
      foo1: app1
      foo2: app2

# Enforce that 4 instances with an attribute 'bar' are deployed
- one_vm:
    template_id: 53
    attributes:
      name: app
      bar: bar2
    exact_count: 4
    count_attributes:
      bar:

# Deploy 2 new instances with attribute 'foo: bar' and labels 'app1' and 'app2' and names in format 'fooapp-##'
# Names will be: fooapp-00 and fooapp-01
- one_vm:
    template_id: 53
    attributes:
      name: fooapp-##
      foo: bar
    labels:
      - app1
      - app2
    count: 2

# Deploy 2 new instances with attribute 'app: app1' and names in format 'fooapp-###'
# Names will be: fooapp-002 and fooapp-003
- one_vm:
    template_id: 53
    attributes:
      name: fooapp-###
      app: app1
    count: 2

# Reboot all instances with name in format 'fooapp-#'
# Instances 'fooapp-00', 'fooapp-01', 'fooapp-002' and 'fooapp-003' will be rebooted
- one_vm:
    attributes:
      name: fooapp-#
    state: rebooted

# Enforce that only 1 instance with name in format 'fooapp-#' is deployed
# The task will delete oldest instances, so only the 'fooapp-003' will remain
- one_vm:
    template_id: 53
    exact_count: 1
    count_attributes:
      name: fooapp-#

# Deploy an new instance with a network
- one_vm:
    template_id: 53
    networks:
      - NETWORK_ID: 27
  register: vm

# Wait for SSH to come up
- wait_for_connection:
  delegate_to: '{{ vm.instances[0].networks[0].ip }}'

# Terminate VMs by ids
- one_vm:
    instance_ids:
      - 153
      - 160
    state: absent

# Reboot all VMs that have labels 'foo' and 'app1'
- one_vm:
    labels:
      - foo
      - app1
    state: rebooted

# Fetch all VMs that have name 'foo' and attribute 'app: bar'
- one_vm:
    attributes:
      name: foo
      app: bar
  register: results

# Deploy 2 new instances with labels 'foo1' and 'foo2'
- one_vm:
    template_name: app_template
    labels:
      - foo1
      - foo2
    count: 2

# Enforce that only 1 instance with label 'foo1' will be running
- one_vm:
    template_name: app_template
    labels:
      - foo1
    exact_count: 1
    count_labels:
      - foo1

# Terminate all instances that have attribute foo
- one_vm:
    template_id: 53
    exact_count: 0
    count_attributes:
      foo:

# Power-off the VM and save VM's disk with id=0 to the image with name 'foo-image'
- one_vm:
    instance_ids: 351
    state: powered-off
    disk_saveas:
      name: foo-image

# Save VM's disk with id=1 to the image with name 'bar-image'
- one_vm:
    instance_ids: 351
    disk_saveas:
      name: bar-image
      disk_id: 1

```

## License

TODO

## Author Information
  - ['Milan Ilic (@ilicmilan)']
