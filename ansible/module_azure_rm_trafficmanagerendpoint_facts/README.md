# Ansible module: ansible.module_azure_rm_trafficmanagerendpoint_facts


Get Azure Traffic Manager endpoint facts

## Description

Get facts for a specific Traffic Manager endpoints or all endpoints  in a Traffic Manager profile

## Requirements

TODO

## Arguments

``` json
{
    "ad_user": "{'description': ['Active Directory username. Use when authenticating with an Active Directory user rather than service principal.']}",
    "adfs_authority_url": "{'description': ['Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority.'], 'required': False, 'default': None, 'version_added': 2.6}",
    "api_profile": "{'description': ['Selects an API profile to use when communicating with Azure services. Default value of C(latest) is appropriate for public clouds; future values will allow use with Azure Stack.'], 'default': 'latest', 'version_added': 2.5}",
    "auth_source": "{'description': ['Controls the source of the credentials to use for authentication.', 'If not specified, ANSIBLE_AZURE_AUTH_SOURCE environment variable will be used and default to C(auto) if variable is not defined.', 'C(auto) will follow the default precedence of module parameters -> environment variables -> default profile in credential file C(~/.azure/credentials).', 'When set to C(cli), the credentials will be sources from the default Azure CLI profile.', 'Can also be set via the C(ANSIBLE_AZURE_AUTH_SOURCE) environment variable.', 'When set to C(msi), the host machine must be an azure resource with an enabled MSI extension. C(subscription_id) or the environment variable C(AZURE_SUBSCRIPTION_ID) can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.', 'The C(msi) was added in Ansible 2.6.'], 'choices': ['auto', 'cli', 'credential_file', 'env', 'msi'], 'version_added': 2.5}",
    "cert_validation_mode": "{'description': ['Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing C(ignore). Can also be set via credential file profile or the C(AZURE_CERT_VALIDATION) environment variable.'], 'choices': ['validate', 'ignore'], 'version_added': 2.5}",
    "client_id": "{'description': ['Azure client ID. Use when authenticating with a Service Principal.']}",
    "cloud_environment": "{'description': ['For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, C(AzureChinaCloud), C(AzureUSGovernment)), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the C(AZURE_CLOUD_ENVIRONMENT) environment variable.'], 'default': 'AzureCloud', 'version_added': 2.4}",
    "name": "{'description': ['Limit results to a specific Traffic Manager endpoint.']}",
    "password": "{'description': ['Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.']}",
    "profile": "{'description': ['Security profile found in ~/.azure/credentials file.']}",
    "profile_name": "{'description': ['Name of Traffic Manager Profile'], 'required': True}",
    "resource_group": "{'description': ['The resource group to search for the desired Traffic Manager profile'], 'required': True}",
    "secret": "{'description': ['Azure client secret. Use when authenticating with a Service Principal.']}",
    "subscription_id": "{'description': ['Your Azure subscription Id.']}",
    "tenant": "{'description': ['Azure tenant ID. Use when authenticating with a Service Principal.']}",
    "type": "{'description': ['Type of endpoint.'], 'choices': ['azure_endpoints', 'external_endpoints', 'nested_endpoints']}",
}
```

## Examples


``` yaml

    - name: Get endpoints facts of a Traffic Manager profile
      azure_rm_trafficmanagerendpoint_facts:
        resource_group: TestRG
        profile_name: Testing

    - name: Get specific endpoint of a Traffic Manager profie
      azure_rm_trafficmanager_facts:
        resource_group: TestRG
        profile_name: Testing
        name: test_external_endpoint


```

## License

TODO

## Author Information
  - ['Hai Cao <t-haicao@microsoft.com>', 'Yunge Zhu <yungez@microsoft.com>']
  - ['Hai Cao <t-haicao@microsoft.com>', 'Yunge Zhu <yungez@microsoft.com>']
