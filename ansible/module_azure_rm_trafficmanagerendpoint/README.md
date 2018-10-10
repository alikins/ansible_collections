# Ansible module: ansible.module_azure_rm_trafficmanagerendpoint


Manage Azure Traffic Manager endpoint

## Description

Create, update and delete Azure Traffic Manager endpoint.

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
    "enabled": "{'description': ['The status of the endpoint.'], 'type': 'bool', 'default': True}",
    "geo_mapping": "{'description': ['The list of countries/regions mapped to this endpoint when traffic manager profile has routing_method of C(geographic).'], 'type': 'str'}",
    "location": "{'description': ["Specifies the location of the external or nested endpoints when using the 'Performance' traffic routing method."], 'type': 'str'}",
    "min_child_endpoints": "{'description': ['The minimum number of endpoints that must be available in the child profile in order for the parent profile to be considered available.', 'Only applicable to endpoint of I(type) (nested_endpoints).'], 'type': 'int'}",
    "name": "{'description': ['The name of the endpoint.'], 'type': 'str', 'required': True}",
    "password": "{'description': ['Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.']}",
    "priority": "{'description': ['The priority of this endpoint when traffic manager profile has routing_method of C(priority).', 'Possible values are from 1 to 1000, lower values represent higher priority.', 'This is an optional parameter. If specified, it must be specified on all endpoints.', 'No two endpoints can share the same priority value.'], 'type': 'int'}",
    "profile": "{'description': ['Security profile found in ~/.azure/credentials file.']}",
    "profile_name": "{'description': ['Name of Traffic Manager profile where this endpoints attaches to.'], 'type': 'str', 'required': True}",
    "resource_group": "{'description': ['Name of a resource group where the Traffic Manager endpoint exists or will be created.'], 'type': 'str', 'required': True}",
    "secret": "{'description': ['Azure client secret. Use when authenticating with a Service Principal.']}",
    "state": "{'description': ['Assert the state of the Traffic Manager endpoint. Use C(present) to create or update a Traffic Manager endpoint and C(absent) to delete it.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "subscription_id": "{'description': ['Your Azure subscription Id.']}",
    "target": "{'description': ['The fully-qualified DNS name of the endpoint.'], 'type': 'str'}",
    "target_resource_id": "{'description': ['The Azure Resource URI of the of the endpoint.', 'Not applicable to endpoints of I(type) C(external_endpoints).'], 'type': 'str'}",
    "tenant": "{'description': ['Azure tenant ID. Use when authenticating with a Service Principal.']}",
    "type": "{'description': ['The type of the endpoint.'], 'required': True, 'choices': ['azure_endpoints', 'external_endpoints', 'nested_endpoints']}",
    "weight": "{'description': ['The weight of this endpoint when traffic manager profile has routing_method of C(weighted).', 'Possible values are from 1 to 1000.'], 'type': 'int'}",
}
```

## Examples


``` yaml

  - name: create a endpoint for a traffic manager profile
    azure_rm_trafficmanagerendpoint:
        resource_group: testresourcegroup
        profile_name: myprofilename
        name: testendpoint1
        type: external_endpoints
        location: westus
        priority: 2
        weight: 1
        target: 1.2.3.4

```

## License

TODO

## Author Information
  - ['Hai Cao <t-haicao@microsoft.com>', 'Yunge Zhu <yungez@microsoft.com>']
  - ['Hai Cao <t-haicao@microsoft.com>', 'Yunge Zhu <yungez@microsoft.com>']
