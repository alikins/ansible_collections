# Ansible module: ansible.module_azure_rm_virtualmachine


Manage Azure virtual machines

## Description

Create, update, stop and start a virtual machine. Provide an existing storage account and network interface or allow the module to create these for you. If you choose not to provide a network interface, the resource group must contain a virtual network with at least one subnet.
Before Ansible 2.5, this required an image found in the Azure Marketplace which can be discovered with M(azure_rm_virtualmachineimage_facts). In Ansible 2.5 and newer, custom images can be used as well, see the examples for more details.
If you need to use the I(custom_data) option, many images in the marketplace are not cloud-init ready. Thus, data sent to I(custom_data) would be ignored. If the image you are attempting to use is not listed in U(https://docs.microsoft.com/en-us/azure/virtual-machines/linux/using-cloud-init#cloud-init-overview), follow these steps U(https://docs.microsoft.com/en-us/azure/virtual-machines/linux/cloudinit-prepare-custom-image).

## Requirements

TODO

## Arguments

``` json
{
    "accept_terms": "{'description': ['Accept terms for marketplace images that require it', 'Only Azure service admin/account admin users can purchase images from the marketplace'], 'type': 'bool', 'default': False, 'version_added': '2.7'}",
    "ad_user": "{'description': ['Active Directory username. Use when authenticating with an Active Directory user rather than service principal.']}",
    "adfs_authority_url": "{'description': ['Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority.'], 'required': False, 'default': None, 'version_added': 2.6}",
    "admin_password": "{'description': ['Password for the admin username. Not required if the os_type is Linux and SSH password authentication is disabled by setting ssh_password_enabled to false.']}",
    "admin_username": "{'description': ['Admin username used to access the host after it is created. Required when creating a VM.']}",
    "allocated": "{'description': ["Toggle that controls if the machine is allocated/deallocated, only useful with state='present'."], 'default': True, 'type': 'bool'}",
    "api_profile": "{'description': ['Selects an API profile to use when communicating with Azure services. Default value of C(latest) is appropriate for public clouds; future values will allow use with Azure Stack.'], 'default': 'latest', 'version_added': 2.5}",
    "append_tags": "{'description': ["Use to control if tags field is canonical or just appends to existing tags. When canonical, any tags not found in the tags parameter will be removed from the object's metadata."], 'type': 'bool', 'default': True}",
    "auth_source": "{'description': ['Controls the source of the credentials to use for authentication.', 'If not specified, ANSIBLE_AZURE_AUTH_SOURCE environment variable will be used and default to C(auto) if variable is not defined.', 'C(auto) will follow the default precedence of module parameters -> environment variables -> default profile in credential file C(~/.azure/credentials).', 'When set to C(cli), the credentials will be sources from the default Azure CLI profile.', 'Can also be set via the C(ANSIBLE_AZURE_AUTH_SOURCE) environment variable.', 'When set to C(msi), the host machine must be an azure resource with an enabled MSI extension. C(subscription_id) or the environment variable C(AZURE_SUBSCRIPTION_ID) can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.', 'The C(msi) was added in Ansible 2.6.'], 'choices': ['auto', 'cli', 'credential_file', 'env', 'msi'], 'version_added': 2.5}",
    "availability_set": "{'description': ['Name or ID of an existing availability set to add the VM to. The availability_set should be in the same resource group as VM.'], 'version_added': '2.5'}",
    "cert_validation_mode": "{'description': ['Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing C(ignore). Can also be set via credential file profile or the C(AZURE_CERT_VALIDATION) environment variable.'], 'choices': ['validate', 'ignore'], 'version_added': 2.5}",
    "client_id": "{'description': ['Azure client ID. Use when authenticating with a Service Principal.']}",
    "cloud_environment": "{'description': ['For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, C(AzureChinaCloud), C(AzureUSGovernment)), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the C(AZURE_CLOUD_ENVIRONMENT) environment variable.'], 'default': 'AzureCloud', 'version_added': 2.4}",
    "custom_data": "{'description': ['Data which is made available to the virtual machine and used by e.g., cloud-init.'], 'version_added': '2.5'}",
    "data_disks": "{'description': ['Describes list of data disks.'], 'version_added': '2.4', 'suboptions': {'lun': {'description': ['The logical unit number for data disk'], 'default': 0, 'version_added': '2.4'}, 'disk_size_gb': {'description': ['The initial disk size in GB for blank data disks'], 'version_added': '2.4'}, 'managed_disk_type': {'description': ['Managed data disk type'], 'choices': ['Standard_LRS', 'Premium_LRS'], 'version_added': '2.4'}, 'storage_account_name': {'description': ["Name of an existing storage account that supports creation of VHD blobs. If not specified for a new VM, a new storage account named <vm name>01 will be created using storage type 'Standard_LRS'."], 'version_added': '2.4'}, 'storage_container_name': {'description': ['Name of the container to use within the storage account to store VHD blobs. If no name is specified a default container will created.'], 'default': 'vhds', 'version_added': '2.4'}, 'storage_blob_name': {'description': ["Name fo the storage blob used to hold the VM's OS disk image. If no name is provided, defaults to the VM name + '.vhd'. If you provide a name, it must end with '.vhd'"], 'version_added': '2.4'}, 'caching': {'description': ['Type of data disk caching.'], 'choices': ['ReadOnly', 'ReadWrite'], 'default': 'ReadOnly', 'version_added': '2.4'}}}",
    "image": "{'description': ['Specifies the image used to build the VM.', 'If a string, the image is sourced from a custom image based on the name.', 'If a dict with the keys C(publisher), C(offer), C(sku), and C(version), the image is sourced from a Marketplace image. NOTE: set image.version to C(latest) to get the most recent version of a given image.', 'If a dict with the keys C(name) and C(resource_group), the image is sourced from a custom image based on the C(name) and C(resource_group) set. NOTE: the key C(resource_group) is optional and if omitted, all images in the subscription will be searched for by C(name).', 'Custom image support was added in Ansible 2.5'], 'required': True}",
    "location": "{'description': ['Valid Azure location. Defaults to location of the resource group.']}",
    "managed_disk_type": "{'description': ['Managed OS disk type'], 'choices': ['Standard_LRS', 'Premium_LRS'], 'version_added': '2.4'}",
    "name": "{'description': ['Name of the virtual machine.'], 'required': True}",
    "network_interface_names": "{'description': ['List of existing network interface names to add to the VM.', 'Item can be a str of name or resource id of the network interface.', 'Item can also be a dict contains C(resource_group) and C(name) of the network interface.', 'If a network interface name is not provided when the VM is created, a default network interface will be created.', 'In order for the module to create a new network interface, at least one Virtual Network with one Subnet must exist.'], 'aliases': ['network_interfaces']}",
    "open_ports": "{'description': ['If a network interface is created when creating the VM, a security group will be created as well. For Linux hosts a rule will be added to the security group allowing inbound TCP connections to the default SSH port 22, and for Windows hosts ports 3389 and 5986 will be opened. Override the default open ports by providing a list of ports.']}",
    "os_disk_caching": "{'description': ['Type of OS disk caching.'], 'choices': ['ReadOnly', 'ReadWrite'], 'default': 'ReadOnly', 'aliases': ['disk_caching']}",
    "os_disk_name": "{'description': ['OS disk name'], 'version_added': '2.8'}",
    "os_disk_size_gb": "{'description': ['Type of OS disk size in GB.'], 'version_added': '2.7'}",
    "os_type": "{'description': ['Base type of operating system.'], 'choices': ['Windows', 'Linux'], 'default': 'Linux'}",
    "password": "{'description': ['Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.']}",
    "plan": "{'description': ['A dictionary describing a third-party billing plan for an instance'], 'version_added': 2.5, 'suboptions': {'name': {'description': ['billing plan name'], 'required': True}, 'product': {'description': ['product name'], 'required': True}, 'publisher': {'description': ['publisher offering the plan'], 'required': True}, 'promotion_code': {'description': ['optional promotion code']}}}",
    "profile": "{'description': ['Security profile found in ~/.azure/credentials file.']}",
    "public_ip_allocation_method": "{'description': ["If a public IP address is created when creating the VM (because a Network Interface was not provided), determines if the public IP address remains permanently associated with the Network Interface. If set to 'Dynamic' the public IP address may change any time the VM is rebooted or power cycled.", 'The C(Disabled) choice was added in Ansible 2.6.'], 'choices': ['Dynamic', 'Static', 'Disabled'], 'default': 'Static', 'aliases': ['public_ip_allocation']}",
    "remove_on_absent": "{'description': ["When removing a VM using state 'absent', also remove associated resources", "It can be 'all' or a list with any of the following: ['network_interfaces', 'virtual_storage', 'public_ips']", 'Any other input will be ignored'], 'default': ['all']}",
    "resource_group": "{'description': ['Name of the resource group containing the virtual machine.'], 'required': True}",
    "restarted": "{'description': ["Use with state 'present' to restart a running VM."], 'type': 'bool'}",
    "secret": "{'description': ['Azure client secret. Use when authenticating with a Service Principal.']}",
    "short_hostname": "{'description': ['Name assigned internally to the host. On a linux VM this is the name returned by the `hostname` command. When creating a virtual machine, short_hostname defaults to name.']}",
    "ssh_password_enabled": "{'description': ['When the os_type is Linux, setting ssh_password_enabled to false will disable SSH password authentication and require use of SSH keys.'], 'default': True, 'type': 'bool'}",
    "ssh_public_keys": "{'description': ['For os_type Linux provide a list of SSH keys. Each item in the list should be a dictionary where the dictionary contains two keys: path and key_data. Set the path to the default location of the authorized_keys files. On an Enterprise Linux host, for example, the path will be /home/<admin username>/.ssh/authorized_keys. Set key_data to the actual value of the public key.']}",
    "started": "{'description': ["Use with state 'present' to start the machine. Set to false to have the machine be 'stopped'."], 'default': True, 'type': 'bool'}",
    "state": "{'description': ['Assert the state of the virtual machine.', "State 'present' will check that the machine exists with the requested configuration. If the configuration of the existing machine does not match, the machine will be updated. Use options started, allocated and restarted to change the machine's power state.", "State 'absent' will remove the virtual machine."], 'default': 'present', 'choices': ['absent', 'present']}",
    "storage_account_name": "{'description': ["Name of an existing storage account that supports creation of VHD blobs. If not specified for a new VM, a new storage account named <vm name>01 will be created using storage type 'Standard_LRS'."], 'aliases': ['storage_account']}",
    "storage_blob_name": "{'description': ["Name fo the storage blob used to hold the VM's OS disk image. If no name is provided, defaults to the VM name + '.vhd'. If you provide a name, it must end with '.vhd'"], 'aliases': ['storage_blob']}",
    "storage_container_name": "{'description': ['Name of the container to use within the storage account to store VHD blobs. If no name is specified a default container will created.'], 'default': 'vhds', 'aliases': ['storage_container']}",
    "subnet_name": "{'description': ['When creating a virtual machine, if a network interface name is not provided, one will be created.', 'The new network interface will be assigned to the first subnet found in the virtual network.', 'Use this parameter to provide a specific subnet instead.', 'If the subnet is in another resource group, specific resource group by C(virtual_network_resource_group).'], 'aliases': ['subnet']}",
    "subscription_id": "{'description': ['Your Azure subscription Id.']}",
    "tags": "{'description': ['Dictionary of string:string pairs to assign as metadata to the object. Metadata tags on the object will be updated with any provided values. To remove tags set append_tags option to false.\n']}",
    "tenant": "{'description': ['Azure tenant ID. Use when authenticating with a Service Principal.']}",
    "virtual_network_name": "{'description': ['When creating a virtual machine, if a network interface name is not provided, one will be created.', 'The network interface will be assigned to the first virtual network found in the resource group.', 'Use this parameter to provide a specific virtual network instead.', 'If the virtual network in in another resource group, specific resource group by C(virtual_network_resource_group).'], 'aliases': ['virtual_network']}",
    "virtual_network_resource_group": "{'description': ['When creating a virtual machine, if a specific virtual network from another resource group should be used, use this parameter to specify the resource group to use.'], 'version_added': '2.4'}",
    "vm_size": "{'description': ["A valid Azure VM size value. For example, 'Standard_D4'. The list of choices varies depending on the subscription and location. Check your subscription for available choices. Required when creating a VM."]}",
}
```

## Examples


``` yaml


- name: Create VM with defaults
  azure_rm_virtualmachine:
    resource_group: Testing
    name: testvm10
    admin_username: chouseknecht
    admin_password: <your password here>
    image:
      offer: CentOS
      publisher: OpenLogic
      sku: '7.1'
      version: latest

- name: Create an availability set for managed disk vm
  azure_rm_availabilityset:
    name: avs-managed-disk
    resource_group: Testing
    platform_update_domain_count: 5
    platform_fault_domain_count: 2
    sku: Aligned

- name: Create a VM with managed disk
  azure_rm_virtualmachine:
    resource_group: Testing
    name: vm-managed-disk
    admin_username: adminUser
    availability_set: avs-managed-disk
    managed_disk_type: Standard_LRS
    image:
      offer: CoreOS
      publisher: CoreOS
      sku: Stable
      version: latest
    vm_size: Standard_D4

- name: Create a VM with existing storage account and NIC
  azure_rm_virtualmachine:
    resource_group: Testing
    name: testvm002
    vm_size: Standard_D4
    storage_account: testaccount001
    admin_username: adminUser
    ssh_public_keys:
      - path: /home/adminUser/.ssh/authorized_keys
        key_data: < insert yor ssh public key here... >
    network_interfaces: testvm001
    image:
      offer: CentOS
      publisher: OpenLogic
      sku: '7.1'
      version: latest

- name: Create a VM with OS and multiple data managed disks
  azure_rm_virtualmachine:
    resource_group: Testing
    name: testvm001
    vm_size: Standard_D4
    managed_disk_type: Standard_LRS
    admin_username: adminUser
    ssh_public_keys:
      - path: /home/adminUser/.ssh/authorized_keys
        key_data: < insert yor ssh public key here... >
    image:
      offer: CoreOS
      publisher: CoreOS
      sku: Stable
      version: latest
    data_disks:
        - lun: 0
          disk_size_gb: 64
          managed_disk_type: Standard_LRS
        - lun: 1
          disk_size_gb: 128
          managed_disk_type: Premium_LRS

- name: Create a VM with OS and multiple data storage accounts
  azure_rm_virtualmachine:
    resource_group: Testing
    name: testvm001
    vm_size: Standard_DS1_v2
    admin_username: adminUser
    ssh_password_enabled: false
    ssh_public_keys:
    - path: /home/adminUser/.ssh/authorized_keys
      key_data: < insert yor ssh public key here... >
    network_interfaces: testvm001
    storage_container: osdisk
    storage_blob: osdisk.vhd
    image:
      offer: CoreOS
      publisher: CoreOS
      sku: Stable
      version: latest
    data_disks:
    - lun: 0
      disk_size_gb: 64
      storage_container_name: datadisk1
      storage_blob_name: datadisk1.vhd
    - lun: 1
      disk_size_gb: 128
      storage_container_name: datadisk2
      storage_blob_name: datadisk2.vhd

- name: Create a VM with a custom image
  azure_rm_virtualmachine:
    resource_group: Testing
    name: testvm001
    vm_size: Standard_DS1_v2
    admin_username: adminUser
    admin_password: password01
    image: customimage001

- name: Create a VM with a custom image from a particular resource group
  azure_rm_virtualmachine:
    resource_group: Testing
    name: testvm001
    vm_size: Standard_DS1_v2
    admin_username: adminUser
    admin_password: password01
    image:
      name: customimage001
      resource_group: Testing

- name: Create VM with spcified OS disk size
  azure_rm_virtualmachine:
    resource_group: Testing
    name: big-os-disk
    admin_username: chouseknecht
    admin_password: <your password here>
    os_disk_size_gb: 512
    image:
      offer: CentOS
      publisher: OpenLogic
      sku: '7.1'
      version: latest

- name: Create VM with OS and Plan, accepting the terms
  azure_rm_virtualmachine:
    resource_group: Testing
    name: f5-nva
    admin_username: chouseknecht
    admin_password: <your password here>
    image:
      publisher: f5-networks
      offer: f5-big-ip-best
      sku: f5-bigip-virtual-edition-200m-best-hourly
      version: latest
    plan:
      name: f5-bigip-virtual-edition-200m-best-hourly
      product: f5-big-ip-best
      publisher: f5-networks

- name: Power Off
  azure_rm_virtualmachine:
    resource_group: Testing
    name: testvm002
    started: no

- name: Deallocate
  azure_rm_virtualmachine:
    resource_group: Testing
    name: testvm002
    allocated: no

- name: Power On
  azure_rm_virtualmachine:
    resource_group:
    name: testvm002

- name: Restart
  azure_rm_virtualmachine:
    resource_group:
    name: testvm002
    restarted: yes

- name: remove vm and all resources except public ips
  azure_rm_virtualmachine:
    resource_group: Testing
    name: testvm002
    state: absent
    remove_on_absent:
        - network_interfaces
        - virtual_storage

```

## License

TODO

## Author Information
  - ['Chris Houseknecht (@chouseknecht)', 'Matt Davis (@nitzmahone)']
  - ['Chris Houseknecht (@chouseknecht)', 'Matt Davis (@nitzmahone)']
