# Ansible module: ansible.module_azure_rm_virtualmachine_extension


Managed Azure Virtual Machine extension

## Description

Create, update and delete Azure Virtual Machine Extension

## Requirements

TODO

## Arguments

``` json
{
    "ad_user": "{'description': ['Active Directory username. Use when authenticating with an Active Directory user rather than service principal.']}",
    "adfs_authority_url": "{'description': ['Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority.'], 'required': False, 'default': None, 'version_added': 2.6}",
    "api_profile": "{'description': ['Selects an API profile to use when communicating with Azure services. Default value of C(latest) is appropriate for public clouds; future values will allow use with Azure Stack.'], 'default': 'latest', 'version_added': 2.5}",
    "auth_source": "{'description': ['Controls the source of the credentials to use for authentication.', 'If not specified, ANSIBLE_AZURE_AUTH_SOURCE environment variable will be used and default to C(auto) if variable is not defined.', 'C(auto) will follow the default precedence of module parameters -> environment variables -> default profile in credential file C(~/.azure/credentials).', 'When set to C(cli), the credentials will be sources from the default Azure CLI profile.', 'Can also be set via the C(ANSIBLE_AZURE_AUTH_SOURCE) environment variable.', 'When set to C(msi), the host machine must be an azure resource with an enabled MSI extension. C(subscription_id) or the environment variable C(AZURE_SUBSCRIPTION_ID) can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.', 'The C(msi) was added in Ansible 2.6.'], 'choices': ['auto', 'cli', 'credential_file', 'env', 'msi'], 'version_added': 2.5}",
    "auto_upgrade_minor_version": "{'description': ['Whether the extension handler should be automatically upgraded across minor versions.'], 'required': False, 'type': 'bool'}",
    "cert_validation_mode": "{'description': ['Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing C(ignore). Can also be set via credential file profile or the C(AZURE_CERT_VALIDATION) environment variable.'], 'choices': ['validate', 'ignore'], 'version_added': 2.5}",
    "client_id": "{'description': ['Azure client ID. Use when authenticating with a Service Principal.']}",
    "cloud_environment": "{'description': ['For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, C(AzureChinaCloud), C(AzureUSGovernment)), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the C(AZURE_CLOUD_ENVIRONMENT) environment variable.'], 'default': 'AzureCloud', 'version_added': 2.4}",
    "location": "{'description': ['Valid azure location. Defaults to location of the resource group.'], 'required': False}",
    "name": "{'description': ['Name of the vm extension'], 'required': True}",
    "password": "{'description': ['Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.']}",
    "profile": "{'description': ['Security profile found in ~/.azure/credentials file.']}",
    "protected_settings": "{'description': ['Json formatted protected settings for the extension.'], 'required': False}",
    "publisher": "{'description': ['The name of the extension handler publisher.'], 'required': False}",
    "resource_group": "{'description': ['Name of a resource group where the vm extension exists or will be created.'], 'required': True}",
    "secret": "{'description': ['Azure client secret. Use when authenticating with a Service Principal.']}",
    "settings": "{'description': ['Json formatted public settings for the extension.'], 'required': False}",
    "state": "{'description': ["Assert the state of the vm extension. Use 'present' to create or update a vm extension and 'absent' to delete a vm extension."], 'default': 'present', 'choices': ['absent', 'present'], 'required': False}",
    "subscription_id": "{'description': ['Your Azure subscription Id.']}",
    "tenant": "{'description': ['Azure tenant ID. Use when authenticating with a Service Principal.']}",
    "type_handler_version": "{'description': ['The type version of the extension handler.'], 'required': False}",
    "virtual_machine_extension_type": "{'description': ['The type of the extension handler.'], 'required': False}",
    "virtual_machine_name": "{'description': ['The name of the virtual machine where the extension should be create or updated.'], 'required': False}",
}
```

## Examples


``` yaml

    - name: Create VM Extension
      azure_rm_virtualmachine_extension:
        name: myvmextension
        location: eastus
        resource_group: Testing
        virtual_machine_name: myvm
        publisher: Microsoft.Azure.Extensions
        virtual_machine_extension_type: CustomScript
        type_handler_version: 2.0
        settings: '{"commandToExecute": "hostname"}'
        auto_upgrade_minor_version: true

    - name: Delete VM Extension
      azure_rm_virtualmachine_extension:
        name: myvmextension
        location: eastus
        resource_group: Testing
        virtual_machine_name: myvm
        state: absent

```

## License

TODO

## Author Information
  - ['Sertac Ozercan (@sozercan)', 'Julien Stroheker (@julienstroheker)']
  - ['Sertac Ozercan (@sozercan)', 'Julien Stroheker (@julienstroheker)']
