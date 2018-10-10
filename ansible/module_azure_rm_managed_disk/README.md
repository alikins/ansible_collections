# Ansible module: ansible.module_azure_rm_managed_disk


Manage Azure Manage Disks

## Description

Create, update and delete an Azure Managed Disk

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
    "create_option": "{'description': ['Allowed values: empty, import, copy. C(import) from a VHD file in I(source_uri) and C(copy) from previous managed disk I(source_resource_uri).'], 'choices': ['empty', 'import', 'copy']}",
    "disk_size_gb": "{'description': ["Size in GB of the managed disk to be created. If I(create_option) is C(copy) then the value must be greater than or equal to the source's size."]}",
    "location": "{'description': ['Valid Azure location. Defaults to location of the resource group.']}",
    "managed_by": "{'description': ['Name of an existing virtual machine with which the disk is or will be associated, this VM should be in the same resource group.', 'To detach a disk from a vm, keep undefined.'], 'version_added': 2.5}",
    "name": "{'description': ['Name of the managed disk.'], 'required': True}",
    "os_type": "{'description': ['Type of Operating System: C(linux) or C(windows). Used when I(create_option) is either C(copy) or C(import) and the source is an OS disk.'], 'choices': ['linux', 'windows']}",
    "password": "{'description': ['Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.']}",
    "profile": "{'description': ['Security profile found in ~/.azure/credentials file.']}",
    "resource_group": "{'description': ['Name of a resource group where the managed disk exists or will be created.'], 'required': True}",
    "secret": "{'description': ['Azure client secret. Use when authenticating with a Service Principal.']}",
    "source_resource_uri": "{'description': ['The resource ID of the managed disk to copy when I(create_option) is C(copy).']}",
    "source_uri": "{'description': ['URI to a valid VHD file to be used when I(create_option) is C(import).']}",
    "state": "{'description': ["Assert the state of the managed disk. Use C(present) to create or update a managed disk and 'absent' to delete a managed disk."], 'default': 'present', 'choices': ['absent', 'present']}",
    "storage_account_type": "{'description': ['Type of storage for the managed disk: C(Standard_LRS)  or C(Premium_LRS). If not specified the disk is created C(Standard_LRS).'], 'choices': ['Standard_LRS', 'Premium_LRS']}",
    "subscription_id": "{'description': ['Your Azure subscription Id.']}",
    "tags": "{'description': ['Tags to assign to the managed disk.']}",
    "tenant": "{'description': ['Azure tenant ID. Use when authenticating with a Service Principal.']}",
}
```

## Examples


``` yaml

    - name: Create managed disk
      azure_rm_managed_disk:
        name: mymanageddisk
        location: eastus
        resource_group: Testing
        disk_size_gb: 4

    - name: Mount the managed disk to VM
      azure_rm_managed_disk:
        name: mymanageddisk
        location: eastus
        resource_group: Testing
        disk_size_gb: 4
        managed_by: testvm001

    - name: Unmount the managed disk to VM
      azure_rm_managed_disk:
        name: mymanageddisk
        location: eastus
        resource_group: Testing
        disk_size_gb: 4

    - name: Delete managed disk
      azure_rm_manage_disk:
        name: mymanageddisk
        location: eastus
        resource_group: Testing
        state: absent

```

## License

TODO

## Author Information
  - ['Bruno Medina (@brusMX)']
