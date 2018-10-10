# Ansible module: ansible.module_azure_rm_appserviceplan


Manage App Service Plan

## Description

Create, update and delete instance of App Service Plan.

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
    "is_linux": "{'description': ['Describe whether to host webapp on Linux worker.'], 'type': 'bool', 'default': False}",
    "location": "{'description': ['Resource location. If not set, location from the resource group will be used as default.']}",
    "name": "{'description': ['Unique name of the app service plan to create or update.'], 'required': True}",
    "number_of_workers": "{'description': ['Describe number of workers to be allocated.']}",
    "password": "{'description': ['Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.']}",
    "profile": "{'description': ['Security profile found in ~/.azure/credentials file.']}",
    "resource_group": "{'description': ['Name of the resource group to which the resource belongs.'], 'required': True}",
    "secret": "{'description': ['Azure client secret. Use when authenticating with a Service Principal.']}",
    "sku": "{'description': ['The pricing tiers, e.g., F1, D1, B1, B2, B3, S1, P1, P1V2 etc.', 'Please see U(https://azure.microsoft.com/en-us/pricing/details/app-service/plans/) for more detail.', 'For linux app service plan, please see U(https://azure.microsoft.com/en-us/pricing/details/app-service/linux/) for more detail.']}",
    "state": "{'description': ['Assert the state of the app service plan.', "Use 'present' to create or update an app service plan and 'absent' to delete it."], 'default': 'present', 'choices': ['absent', 'present']}",
    "subscription_id": "{'description': ['Your Azure subscription Id.']}",
    "tags": "{'description': ['Dictionary of string:string pairs to assign as metadata to the object. Metadata tags on the object will be updated with any provided values. To remove tags set append_tags option to false.\n']}",
    "tenant": "{'description': ['Azure tenant ID. Use when authenticating with a Service Principal.']}",
}
```

## Examples


``` yaml

    - name: Create a windows app service plan
      azure_rm_appserviceplan:
        name: "windowsplan1"
        resource_group: "appserviceplan_rg"
        location: "eastus"
        sku: S1

    - name: Create a linux app service plan
      azure_rm_appserviceplan:
        resource_group: "appserviceplan_rg"
        name: "linuxplan1"
        location: "eastus"
        sku: S1
        is_linux: true
        number_of_workers: 1

    - name: update sku of existing windows app service plan
      azure_rm_appserviceplan:
        name: "windowsplan2"
        resource_group: "appserviceplan_rg"
        location: "eastus"
        sku: S2

```

## License

TODO

## Author Information
  - ['Yunge Zhu(@yungezz)']
