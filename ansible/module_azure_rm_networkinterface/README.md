# Ansible module: ansible.module_azure_rm_networkinterface


Manage Azure network interfaces

## Description

Create, update or delete a network interface. When creating a network interface you must provide the name of an existing virtual network, the name of an existing subnet within the virtual network. A default security group and public IP address will be created automatically, or you can provide the name of an existing security group and public IP address. See the examples below for more details.

## Requirements

TODO

## Arguments

``` json
{
    "ad_user": "{'description': ['Active Directory username. Use when authenticating with an Active Directory user rather than service principal.']}",
    "adfs_authority_url": "{'description': ['Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority.'], 'required': False, 'default': None, 'version_added': 2.6}",
    "api_profile": "{'description': ['Selects an API profile to use when communicating with Azure services. Default value of C(latest) is appropriate for public clouds; future values will allow use with Azure Stack.'], 'default': 'latest', 'version_added': 2.5}",
    "append_tags": "{'description': ["Use to control if tags field is canonical or just appends to existing tags. When canonical, any tags not found in the tags parameter will be removed from the object's metadata."], 'type': 'bool', 'default': True}",
    "auth_source": "{'description': ['Controls the source of the credentials to use for authentication.', 'If not specified, ANSIBLE_AZURE_AUTH_SOURCE environment variable will be used and default to C(auto) if variable is not defined.', 'C(auto) will follow the default precedence of module parameters -> environment variables -> default profile in credential file C(~/.azure/credentials).', 'When set to C(cli), the credentials will be sources from the default Azure CLI profile.', 'Can also be set via the C(ANSIBLE_AZURE_AUTH_SOURCE) environment variable.', 'When set to C(msi), the host machine must be an azure resource with an enabled MSI extension. C(subscription_id) or the environment variable C(AZURE_SUBSCRIPTION_ID) can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.', 'The C(msi) was added in Ansible 2.6.'], 'choices': ['auto', 'cli', 'credential_file', 'env', 'msi'], 'version_added': 2.5}",
    "cert_validation_mode": "{'description': ['Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing C(ignore). Can also be set via credential file profile or the C(AZURE_CERT_VALIDATION) environment variable.'], 'choices': ['validate', 'ignore'], 'version_added': 2.5}",
    "client_id": "{'description': ['Azure client ID. Use when authenticating with a Service Principal.']}",
    "cloud_environment": "{'description': ['For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, C(AzureChinaCloud), C(AzureUSGovernment)), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the C(AZURE_CLOUD_ENVIRONMENT) environment variable.'], 'default': 'AzureCloud', 'version_added': 2.4}",
    "create_with_security_group": "{'description': ['Specifies whether a default security group should be be created with the NIC. Only applies when creating a new NIC.'], 'type': 'bool', 'version_added': 2.6, 'default': True}",
    "dns_servers": "{'description': ['Which DNS servers should the NIC lookup', "List of IP's"], 'type': 'list', 'version_added': 2.7}",
    "enable_accelerated_networking": "{'description': ['Specifies whether the network interface should be created with the accelerated networking feature or not'], 'type': 'bool', 'version_added': 2.7, 'default': False}",
    "enable_ip_forwarding": "{'description': ['Whether to enable IP forwarding'], 'aliases': ['ip_forwarding'], 'type': 'bool', 'default': False, 'version_added': 2.7}",
    "ip_configurations": "{'description': ['List of ip configuration if contains mutilple configuration, should contain configuration object include field private_ip_address, private_ip_allocation_method, public_ip_address_name, public_ip, public_ip_allocation_method, name'], 'suboptions': {'name': {'description': ['Name of the ip configuration.'], 'required': True}, 'private_ip_address': {'description': ['Private ip address for the ip configuration.']}, 'private_ip_allocation_method': {'description': ['private ip allocation method.'], 'choices': ['Dynamic', 'Static'], 'default': 'Dynamic'}, 'public_ip_address_name': {'description': ['Name of the public ip address. None for disable ip address.']}, 'public_ip_allocation_method': {'description': ['public ip allocation method.'], 'choices': ['Dynamic', 'Static'], 'default': 'Dynamic'}, 'load_balancer_backend_address_pools': {'description': ['List of an existing load-balancer backend address pool id to associate with the network interface.', 'It can be write as a resource id.', 'Also can be a dict of I(name) and I(load_balancer).'], 'version_added': 2.6}, 'primary': {'description': ['Whether the ip configuration is the primary one in the list.'], 'type': 'bool', 'default': 'no'}}, 'version_added': 2.5}",
    "location": "{'description': ['Valid azure location. Defaults to location of the resource group.'], 'required': False}",
    "name": "{'description': ['Name of the network interface.'], 'required': True}",
    "open_ports": "{'description': ['When a default security group is created for a Linux host a rule will be added allowing inbound TCP connections to the default SSH port 22, and for a Windows host rules will be added allowing inbound access to RDP ports 3389 and 5986. Override the default ports by providing a list of open ports.']}",
    "os_type": "{'description': ["Determines any rules to be added to a default security group. When creating a network interface, if no security group name is provided, a default security group will be created. If the os_type is 'Windows', a rule will be added allowing RDP access. If the os_type is 'Linux', a rule allowing SSH access will be added."], 'choices': ['Windows', 'Linux'], 'default': 'Linux'}",
    "password": "{'description': ['Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.']}",
    "private_ip_address": "{'description': ['(Deprecate) Valid IPv4 address that falls within the specified subnet.', 'This option will be deprecated in 2.9, use I(ip_configurations) instead.']}",
    "private_ip_allocation_method": "{'description': ["(Deprecate) Specify whether or not the assigned IP address is permanent. NOTE: when creating a network interface specifying a value of 'Static' requires that a private_ip_address value be provided. You can update the allocation method to 'Static' after a dynamic private ip address has been assigned.", 'This option will be deprecated in 2.9, use I(ip_configurations) instead.'], 'default': 'Dynamic', 'choices': ['Dynamic', 'Static']}",
    "profile": "{'description': ['Security profile found in ~/.azure/credentials file.']}",
    "public_ip": "{'description': ['(Deprecate) When creating a network interface, if no public IP address name is provided a default public IP address will be created. Set to false, if you do not want a public IP address automatically created.', 'This option will be deprecated in 2.9, use I(ip_configurations) instead.'], 'type': 'bool', 'default': True}",
    "public_ip_address_name": "{'description': ['(Deprecate) Name of an existing public IP address object to associate with the security group.', 'This option will be deprecated in 2.9, use I(ip_configurations) instead.'], 'aliases': ['public_ip_address', 'public_ip_name']}",
    "public_ip_allocation_method": "{'description': ['(Deprecate) If a public_ip_address_name is not provided, a default public IP address will be created. The allocation method determines whether or not the public IP address assigned to the network interface is permanent.', 'This option will be deprecated in 2.9, use I(ip_configurations) instead.'], 'choices': ['Dynamic', 'Static'], 'default': 'Dynamic'}",
    "resource_group": "{'description': ['Name of a resource group where the network interface exists or will be created.'], 'required': True}",
    "secret": "{'description': ['Azure client secret. Use when authenticating with a Service Principal.']}",
    "security_group": "{'description': ['An existing security group with which to associate the network interface. If not provided, a default security group will be created when C(create_with_security_group) is true.', 'It can be the name of security group.', 'Make sure the security group is in the same resource group when you only give its name.', 'It can be the resource id.', "It can be a dict contains security_group's C(name) and C(resource_group)."], 'aliases': ['security_group_name']}",
    "state": "{'description': ["Assert the state of the network interface. Use 'present' to create or update an interface and 'absent' to delete an interface."], 'default': 'present', 'choices': ['absent', 'present'], 'required': False}",
    "subnet_name": "{'description': ['Name of an existing subnet within the specified virtual network. Required when creating a network interface', "Use the C(virtual_network)'s resource group."], 'aliases': ['subnet'], 'required': True}",
    "subscription_id": "{'description': ['Your Azure subscription Id.']}",
    "tags": "{'description': ['Dictionary of string:string pairs to assign as metadata to the object. Metadata tags on the object will be updated with any provided values. To remove tags set append_tags option to false.\n']}",
    "tenant": "{'description': ['Azure tenant ID. Use when authenticating with a Service Principal.']}",
    "virtual_network": "{'description': ['An existing virtual network with which the network interface will be associated. Required when creating a network interface.', "It can be the virtual network's name.", 'Make sure your virtual network is in the same resource group as NIC when you give only the name.', "It can be the virtual network's resource id.", 'It can be a dict which contains C(name) and C(resource_group) of the virtual network.'], 'aliases': ['virtual_network_name'], 'required': True}",
}
```

## Examples


``` yaml

    - name: Create a network interface with minimal parameters
      azure_rm_networkinterface:
        name: nic001
        resource_group: Testing
        virtual_network: vnet001
        subnet_name: subnet001
        ip_configurations:
          - name: ipconfig1
            public_ip_address_name: publicip001
            primary: True

    - name: Create a network interface with private IP address only (no Public IP)
      azure_rm_networkinterface:
        name: nic001
        resource_group: Testing
        virtual_network: vnet001
        subnet_name: subnet001
        create_with_security_group: False
        ip_configurations:
          - name: ipconfig1
            primary: True

    - name: Create a network interface for use in a Windows host (opens RDP port) with custom RDP port
      azure_rm_networkinterface:
        name: nic002
        resource_group: Testing
        virtual_network: vnet001
        subnet_name: subnet001
        os_type: Windows
        rdp_port: 3399
        security_group: "/subscriptions/XXXXXXX/resourceGroups/Testing/providers/Microsoft.Network/networkSecurityGroups/nsg001"
        ip_configurations:
          - name: ipconfig1
            public_ip_address_name: publicip001
            primary: True

    - name: Create a network interface using existing security group and public IP
      azure_rm_networkinterface:
        name: nic003
        resource_group: Testing
        virtual_network: vnet001
        subnet_name: subnet001
        security_group: secgroup001
        ip_configurations:
          - name: ipconfig1
            public_ip_address_name: publicip001
            primary: True

    - name: Create a network with mutilple ip configurations
      azure_rm_networkinterface:
        name: nic004
        resource_group: Testing
        subnet_name: subnet001
        virtual_network: vnet001
        security_group:
          name: testnic002
          resource_group: Testing1
        ip_configurations:
          - name: ipconfig1
            public_ip_address_name: publicip001
            primary: True
          - name: ipconfig2
            load_balancer_backend_address_pools:
              - "{{ loadbalancer001.state.backend_address_pools[0].id }}"
              - name: backendaddrpool1
                load_balancer: loadbalancer001

    - name: Create a network interface in accelerated networking mode
      azure_rm_networkinterface:
        name: nic005
        resource_group: Testing
        virtual_network_name: vnet001
        subnet_name: subnet001
        enable_accelerated_networking: True

    - name: Create a network interface with IP forwarding
      azure_rm_networkinterface:
        name: nic001
        resource_group: Testing
        virtual_network: vnet001
        subnet_name: subnet001
        ip_forwarding: True
        ip_configurations:
          - name: ipconfig1
            public_ip_address_name: publicip001
            primary: True

    - name: Create a network interface with dns servers
      azure_rm_networkinterface:
        name: nic009
        resource_group: Testing
        virtual_network: vnet001
        subnet_name: subnet001
        dns_servers:
          - 8.8.8.8

    - name: Delete network interface
      azure_rm_networkinterface:
        resource_group: Testing
        name: nic003
        state: absent

```

## License

TODO

## Author Information
  - ['Chris Houseknecht (@chouseknecht)', 'Matt Davis (@nitzmahone)', 'Yuwei Zhou (@yuwzho)']
  - ['Chris Houseknecht (@chouseknecht)', 'Matt Davis (@nitzmahone)', 'Yuwei Zhou (@yuwzho)']
  - ['Chris Houseknecht (@chouseknecht)', 'Matt Davis (@nitzmahone)', 'Yuwei Zhou (@yuwzho)']
