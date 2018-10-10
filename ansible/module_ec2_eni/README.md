# Ansible module: ansible.module_ec2_eni


Create and optionally attach an Elastic Network Interface (ENI) to an instance

## Description

Create and optionally attach an Elastic Network Interface (ENI) to an instance. If an ENI ID or private_ip is provided, the existing ENI (if any) will be modified. The 'attached' parameter controls the attachment status of the network interface.

## Requirements

TODO

## Arguments

``` json
{
    "allow_reassignment": "{'description': ['Indicates whether to allow an IP address that is already assigned to another network interface or instance to be reassigned to the specified network interface.'], 'required': False, 'default': False, 'type': 'bool', 'version_added': 2.7}",
    "attached": "{'description': ["Specifies if network interface should be attached or detached from instance. If omitted, attachment status won't change"], 'version_added': 2.2, 'type': 'bool'}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "delete_on_termination": "{'description': ['Delete the interface when the instance it is attached to is terminated. You can only specify this flag when the interface is being modified, not on creation.'], 'required': False, 'type': 'bool'}",
    "description": "{'description': ['Optional description of the ENI.']}",
    "device_index": "{'description': ['The index of the device for the network interface attachment on the instance.'], 'default': 0}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "eni_id": "{'description': ['The ID of the ENI (to modify); if null and state is present, a new eni will be created.']}",
    "force_detach": "{'description': ['Force detachment of the interface. This applies either when explicitly detaching the interface by setting instance_id to None or when deleting an interface with state=absent.'], 'default': False, 'type': 'bool'}",
    "instance_id": "{'description': ["Instance ID that you wish to attach ENI to. Since version 2.2, use the 'attached' parameter to attach or detach an ENI. Prior to 2.2, to detach an ENI from an instance, use 'None'."]}",
    "private_ip_address": "{'description': ['Private IP address.']}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "purge_secondary_private_ip_addresses": "{'description': ['To be used with I(secondary_private_ip_addresses) to determine whether or not to remove any secondary IP addresses other than those specified. Set secondary_private_ip_addresses to an empty list to purge all secondary addresses.'], 'default': False, 'type': 'bool', 'version_added': 2.5}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "secondary_private_ip_address_count": "{'description': ['The number of secondary IP addresses to assign to the network interface. This option is mutually exclusive of secondary_private_ip_addresses'], 'required': False, 'version_added': 2.2}",
    "secondary_private_ip_addresses": "{'description': ['A list of IP addresses to assign as secondary IP addresses to the network interface. This option is mutually exclusive of secondary_private_ip_address_count'], 'required': False, 'version_added': 2.2}",
    "security_groups": "{'description': ['List of security groups associated with the interface. Only used when state=present. Since version 2.2, you can specify security groups by ID or by name or a combination of both. Prior to 2.2, you can specify only by ID.']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "source_dest_check": "{'description': ['By default, interfaces perform source/destination checks. NAT instances however need this check to be disabled. You can only specify this flag when the interface is being modified, not on creation.'], 'required': False, 'type': 'bool'}",
    "state": "{'description': ['Create or delete ENI'], 'default': 'present', 'choices': ['present', 'absent']}",
    "subnet_id": "{'description': ['ID of subnet in which to create the ENI.']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

# Note: These examples do not set authentication details, see the AWS Guide for details.

# Create an ENI. As no security group is defined, ENI will be created in default security group
- ec2_eni:
    private_ip_address: 172.31.0.20
    subnet_id: subnet-xxxxxxxx
    state: present

# Create an ENI and attach it to an instance
- ec2_eni:
    instance_id: i-xxxxxxx
    device_index: 1
    private_ip_address: 172.31.0.20
    subnet_id: subnet-xxxxxxxx
    state: present

# Create an ENI with two secondary addresses
- ec2_eni:
    subnet_id: subnet-xxxxxxxx
    state: present
    secondary_private_ip_address_count: 2

# Assign a secondary IP address to an existing ENI
# This will purge any existing IPs
- ec2_eni:
    subnet_id: subnet-xxxxxxxx
    eni_id: eni-yyyyyyyy
    state: present
    secondary_private_ip_addresses:
      - 172.16.1.1

# Remove any secondary IP addresses from an existing ENI
- ec2_eni:
    subnet_id: subnet-xxxxxxxx
    eni_id: eni-yyyyyyyy
    state: present
    secondary_private_ip_address_count: 0

# Destroy an ENI, detaching it from any instance if necessary
- ec2_eni:
    eni_id: eni-xxxxxxx
    force_detach: yes
    state: absent

# Update an ENI
- ec2_eni:
    eni_id: eni-xxxxxxx
    description: "My new description"
    state: present

# Update an ENI identifying it by private_ip_address and subnet_id
- ec2_eni:
    subnet_id: subnet-xxxxxxx
    private_ip_address: 172.16.1.1
    description: "My new description"

# Detach an ENI from an instance
- ec2_eni:
    eni_id: eni-xxxxxxx
    instance_id: None
    state: present

### Delete an interface on termination
# First create the interface
- ec2_eni:
    instance_id: i-xxxxxxx
    device_index: 1
    private_ip_address: 172.31.0.20
    subnet_id: subnet-xxxxxxxx
    state: present
  register: eni

# Modify the interface to enable the delete_on_terminaton flag
- ec2_eni:
    eni_id: "{{ eni.interface.id }}"
    delete_on_termination: true


```

## License

TODO

## Author Information
  - ['Rob White (@wimnat)']
