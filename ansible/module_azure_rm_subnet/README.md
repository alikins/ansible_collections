# Ansible module: ansible.module_azure_rm_subnet


Manage Azure subnets

## Description

Create, update or delete a subnet within a given virtual network. Allows setting and updating the address prefix CIDR, which must be valid within the context of the virtual network. Use the azure_rm_networkinterface module to associate interfaces with the subnet and assign specific IP addresses.

## Requirements

TODO

## Arguments

``` json
{
    "ad_user": "{'description': ['Active Directory username. Use when authenticating with an Active Directory user rather than service principal.']}",
    "address_prefix_cidr": "{'description': ['CIDR defining the IPv4 address space of the subnet. Must be valid within the context of the virtual network.'], 'required': True, 'aliases': ['address_prefix']}",
    "adfs_authority_url": "{'description': ['Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority.'], 'required': False, 'default': None, 'version_added': 2.6}",
    "api_profile": "{'description': ['Selects an API profile to use when communicating with Azure services. Default value of C(latest) is appropriate for public clouds; future values will allow use with Azure Stack.'], 'default': 'latest', 'version_added': 2.5}",
    "append_tags": "{'description': ["Use to control if tags field is canonical or just appends to existing tags. When canonical, any tags not found in the tags parameter will be removed from the object's metadata."], 'type': 'bool', 'default': True}",
    "auth_source": "{'description': ['Controls the source of the credentials to use for authentication.', 'If not specified, ANSIBLE_AZURE_AUTH_SOURCE environment variable will be used and default to C(auto) if variable is not defined.', 'C(auto) will follow the default precedence of module parameters -> environment variables -> default profile in credential file C(~/.azure/credentials).', 'When set to C(cli), the credentials will be sources from the default Azure CLI profile.', 'Can also be set via the C(ANSIBLE_AZURE_AUTH_SOURCE) environment variable.', 'When set to C(msi), the host machine must be an azure resource with an enabled MSI extension. C(subscription_id) or the environment variable C(AZURE_SUBSCRIPTION_ID) can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.', 'The C(msi) was added in Ansible 2.6.'], 'choices': ['auto', 'cli', 'credential_file', 'env', 'msi'], 'version_added': 2.5}",
    "cert_validation_mode": "{'description': ['Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing C(ignore). Can also be set via credential file profile or the C(AZURE_CERT_VALIDATION) environment variable.'], 'choices': ['validate', 'ignore'], 'version_added': 2.5}",
    "client_id": "{'description': ['Azure client ID. Use when authenticating with a Service Principal.']}",
    "cloud_environment": "{'description': ['For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, C(AzureChinaCloud), C(AzureUSGovernment)), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the C(AZURE_CLOUD_ENVIRONMENT) environment variable.'], 'default': 'AzureCloud', 'version_added': 2.4}",
    "name": "{'description': ['Name of the subnet.'], 'required': True}",
    "password": "{'description': ['Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.']}",
    "profile": "{'description': ['Security profile found in ~/.azure/credentials file.']}",
    "resource_group": "{'description': ['Name of resource group.'], 'required': True}",
    "route_table": "{'description': ['The reference of the RouteTable resource.', 'It can accept both a str or a dict.', 'The str can be the name or resource id of the route table.', 'The dict can contains C(name) and C(resource_group) of the route_table.'], 'version_added': '2.7'}",
    "secret": "{'description': ['Azure client secret. Use when authenticating with a Service Principal.']}",
    "security_group": "{'description': ['Existing security group with which to associate the subnet.', 'It can be the security group name which is in the same resource group.', 'It can be the resource Id.', 'It can be a dict which contains C(name) and C(resource_group) of the security group.'], 'aliases': ['security_group_name']}",
    "state": "{'description': ["Assert the state of the subnet. Use 'present' to create or update a subnet and 'absent' to delete a subnet."], 'default': 'present', 'choices': ['absent', 'present']}",
    "subscription_id": "{'description': ['Your Azure subscription Id.']}",
    "tags": "{'description': ['Dictionary of string:string pairs to assign as metadata to the object. Metadata tags on the object will be updated with any provided values. To remove tags set append_tags option to false.\n']}",
    "tenant": "{'description': ['Azure tenant ID. Use when authenticating with a Service Principal.']}",
    "virtual_network_name": "{'description': ['Name of an existing virtual network with which the subnet is or will be associated.'], 'required': True, 'aliases': ['virtual_network']}",
}
```

## Examples


``` yaml

    - name: Create a subnet
      azure_rm_subnet:
        name: foobar
        virtual_network_name: My_Virtual_Network
        resource_group: Testing
        address_prefix_cidr: "10.1.0.0/24"

    - name: Create a subnet refer nsg from other resource group
      azure_rm_subnet:
        name: foobar
        virtual_network_name: My_Virtual_Network
        resource_group: Testing
        address_prefix_cidr: "10.1.0.0/16"
        security_group:
          name: secgroupfoo
          resource_group: Testing1
        route_table: route

    - name: Delete a subnet
      azure_rm_subnet:
        name: foobar
        virtual_network_name: My_Virtual_Network
        resource_group: Testing
        state: absent

```

## License

TODO

## Author Information
  - ['Chris Houseknecht (@chouseknecht)', 'Matt Davis (@nitzmahone)']
  - ['Chris Houseknecht (@chouseknecht)', 'Matt Davis (@nitzmahone)']
