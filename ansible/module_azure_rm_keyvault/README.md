# Ansible module: ansible.module_azure_rm_keyvault


Manage Key Vault instance

## Description

Create, update and delete instance of Key Vault.

## Requirements

TODO

## Arguments

``` json
{
    "access_policies": "{'description': ["An array of 0 to 16 identities that have access to the key vault. All identities in the array must use the same tenant ID as the key vault's tenant ID."], 'suboptions': {'tenant_id': {'description': ['The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault.', 'Current keyvault C(tenant_id) value will be used if not specified.']}, 'object_id': {'description': ['The object ID of a user, service principal or security group in the Azure Active Directory tenant for the vault. The object ID must be unique for the list of access policies.', 'Please note this is not application id. Object id can be obtained by running "az ad show sp --id <application id>".'], 'required': True}, 'application_id': {'description': ['Application ID of the client making request on behalf of a principal']}, 'keys': {'description': ['List of permissions to keys'], 'choices': ['encrypt', 'decrypt', 'wrapkey', 'unwrapkey', 'sign', 'verify', 'get', 'list', 'create', 'update', 'import', 'delete', 'backup', 'restore', 'recover', 'purge']}, 'secrets': {'description': ['List of permissions to secrets'], 'choices': ['get', 'list', 'set', 'delete', 'backup', 'restore', 'recover', 'purge']}, 'certificates': {'description': ['List of permissions to certificates'], 'choices': ['get', 'list', 'delete', 'create', 'import', 'update', 'managecontacts', 'getissuers', 'listissuers', 'setissuers', 'deleteissuers', 'manageissuers', 'recover', 'purge']}, 'storage': {'description': ['List of permissions to storage accounts']}}}",
    "ad_user": "{'description': ['Active Directory username. Use when authenticating with an Active Directory user rather than service principal.']}",
    "adfs_authority_url": "{'description': ['Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority.'], 'required': False, 'default': None, 'version_added': 2.6}",
    "api_profile": "{'description': ['Selects an API profile to use when communicating with Azure services. Default value of C(latest) is appropriate for public clouds; future values will allow use with Azure Stack.'], 'default': 'latest', 'version_added': 2.5}",
    "append_tags": "{'description': ["Use to control if tags field is canonical or just appends to existing tags. When canonical, any tags not found in the tags parameter will be removed from the object's metadata."], 'type': 'bool', 'default': True}",
    "auth_source": "{'description': ['Controls the source of the credentials to use for authentication.', 'If not specified, ANSIBLE_AZURE_AUTH_SOURCE environment variable will be used and default to C(auto) if variable is not defined.', 'C(auto) will follow the default precedence of module parameters -> environment variables -> default profile in credential file C(~/.azure/credentials).', 'When set to C(cli), the credentials will be sources from the default Azure CLI profile.', 'Can also be set via the C(ANSIBLE_AZURE_AUTH_SOURCE) environment variable.', 'When set to C(msi), the host machine must be an azure resource with an enabled MSI extension. C(subscription_id) or the environment variable C(AZURE_SUBSCRIPTION_ID) can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.', 'The C(msi) was added in Ansible 2.6.'], 'choices': ['auto', 'cli', 'credential_file', 'env', 'msi'], 'version_added': 2.5}",
    "cert_validation_mode": "{'description': ['Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing C(ignore). Can also be set via credential file profile or the C(AZURE_CERT_VALIDATION) environment variable.'], 'choices': ['validate', 'ignore'], 'version_added': 2.5}",
    "client_id": "{'description': ['Azure client ID. Use when authenticating with a Service Principal.']}",
    "cloud_environment": "{'description': ['For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, C(AzureChinaCloud), C(AzureUSGovernment)), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the C(AZURE_CLOUD_ENVIRONMENT) environment variable.'], 'default': 'AzureCloud', 'version_added': 2.4}",
    "enable_soft_delete": "{'description': ['Property to specify whether the soft delete functionality is enabled for this key vault.'], 'type': 'bool'}",
    "enabled_for_deployment": "{'description': ['Property to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault.'], 'type': 'bool'}",
    "enabled_for_disk_encryption": "{'description': ['Property to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys.'], 'type': 'bool'}",
    "enabled_for_template_deployment": "{'description': ['Property to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault.'], 'type': 'bool'}",
    "location": "{'description': ['Resource location. If not set, location from the resource group will be used as default.']}",
    "password": "{'description': ['Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.']}",
    "profile": "{'description': ['Security profile found in ~/.azure/credentials file.']}",
    "recover_mode": "{'description': ['Create vault in recovery mode.'], 'type': 'bool'}",
    "resource_group": "{'description': ['The name of the Resource Group to which the server belongs.'], 'required': True}",
    "secret": "{'description': ['Azure client secret. Use when authenticating with a Service Principal.']}",
    "sku": "{'description': ['SKU details'], 'suboptions': {'family': {'description': ['SKU family name'], 'required': True}, 'name': {'description': ['SKU name to specify whether the key vault is a standard vault or a premium vault.'], 'required': True, 'choices': ['standard', 'premium']}}}",
    "state": "{'description': ["Assert the state of the KeyVault. Use 'present' to create or update an KeyVault and 'absent' to delete it."], 'default': 'present', 'choices': ['absent', 'present']}",
    "subscription_id": "{'description': ['Your Azure subscription Id.']}",
    "tags": "{'description': ['Dictionary of string:string pairs to assign as metadata to the object. Metadata tags on the object will be updated with any provided values. To remove tags set append_tags option to false.\n']}",
    "tenant": "{'description': ['Azure tenant ID. Use when authenticating with a Service Principal.']}",
    "vault_name": "{'description': ['Name of the vault'], 'required': True}",
    "vault_tenant": "{'description': ['The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault.']}",
}
```

## Examples


``` yaml

  - name: Create instance of Key Vault
    azure_rm_keyvault:
      resource_group: myresourcegroup
      vault_name: samplekeyvault
      enabled_for_deployment: yes
      vault_tenant: 72f98888-8666-4144-9199-2d7cd0111111
      sku:
        name: standard
      access_policies:
        - tenant_id: 72f98888-8666-4144-9199-2d7cd0111111
          object_id: 99998888-8666-4144-9199-2d7cd0111111
          keys:
            - get
            - list

```

## License

TODO

## Author Information
  - ['Zim Kalinowski (@zikalino)']
