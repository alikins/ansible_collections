# Ansible module: ansible.module_azure_rm_resource


Create any Azure resource

## Description

Create, update or delete any Azure resource using Azure REST API.
This module gives access to resources that are not supported via Ansible modules.
Refer to https://docs.microsoft.com/en-us/rest/api/ regarding details related to specific resource REST API.

## Requirements

TODO

## Arguments

``` json
{
    "ad_user": "{'description': ['Active Directory username. Use when authenticating with an Active Directory user rather than service principal.']}",
    "adfs_authority_url": "{'description': ['Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority.'], 'required': False, 'default': None, 'version_added': 2.6}",
    "api_profile": "{'description': ['Selects an API profile to use when communicating with Azure services. Default value of C(latest) is appropriate for public clouds; future values will allow use with Azure Stack.'], 'default': 'latest', 'version_added': 2.5}",
    "api_version": "{'description': ['Specific API version to be used.'], 'required': True}",
    "auth_source": "{'description': ['Controls the source of the credentials to use for authentication.', 'If not specified, ANSIBLE_AZURE_AUTH_SOURCE environment variable will be used and default to C(auto) if variable is not defined.', 'C(auto) will follow the default precedence of module parameters -> environment variables -> default profile in credential file C(~/.azure/credentials).', 'When set to C(cli), the credentials will be sources from the default Azure CLI profile.', 'Can also be set via the C(ANSIBLE_AZURE_AUTH_SOURCE) environment variable.', 'When set to C(msi), the host machine must be an azure resource with an enabled MSI extension. C(subscription_id) or the environment variable C(AZURE_SUBSCRIPTION_ID) can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.', 'The C(msi) was added in Ansible 2.6.'], 'choices': ['auto', 'cli', 'credential_file', 'env', 'msi'], 'version_added': 2.5}",
    "body": "{'description': ['The body of the http request/response to the web service.']}",
    "cert_validation_mode": "{'description': ['Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing C(ignore). Can also be set via credential file profile or the C(AZURE_CERT_VALIDATION) environment variable.'], 'choices': ['validate', 'ignore'], 'version_added': 2.5}",
    "client_id": "{'description': ['Azure client ID. Use when authenticating with a Service Principal.']}",
    "cloud_environment": "{'description': ['For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, C(AzureChinaCloud), C(AzureUSGovernment)), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the C(AZURE_CLOUD_ENVIRONMENT) environment variable.'], 'default': 'AzureCloud', 'version_added': 2.4}",
    "idempotency": "{'description': ['If enabled, idempotency check will be done by using GET method first and then comparing with I(body)'], 'default': False, 'type': 'bool'}",
    "method": "{'description': ['The HTTP method of the request or response. It MUST be uppercase.'], 'choices': ['GET', 'PUT', 'POST', 'HEAD', 'PATCH', 'DELETE', 'MERGE'], 'default': 'PUT'}",
    "password": "{'description': ['Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.']}",
    "profile": "{'description': ['Security profile found in ~/.azure/credentials file.']}",
    "provider": "{'description': ['Provider type.', 'Required if URL is not specified.']}",
    "resource_group": "{'description': ['Resource group to be used.', 'Required if URL is not specified.']}",
    "resource_name": "{'description': ['Resource name.', 'Required if URL Is not specified.']}",
    "resource_type": "{'description': ['Resource type.', 'Required if URL is not specified.']}",
    "secret": "{'description': ['Azure client secret. Use when authenticating with a Service Principal.']}",
    "state": "{'description': ['Assert the state of the resource. Use C(present) to create or update resource or C(absent) to delete resource.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "status_code": "{'description': ['A valid, numeric, HTTP status code that signifies success of the request. Can also be comma separated list of status codes.'], 'default': [200, 201, 202]}",
    "subresource": "{'description': ['List of subresources'], 'suboptions': {'namespace': {'description': ['Subresource namespace']}, 'type': {'description': ['Subresource type']}, 'name': {'description': ['Subresource name']}}}",
    "subscription_id": "{'description': ['Your Azure subscription Id.']}",
    "tenant": "{'description': ['Azure tenant ID. Use when authenticating with a Service Principal.']}",
    "url": "{'description': ['Azure RM Resource URL.']}",
}
```

## Examples


``` yaml

  - name: Update scaleset info using azure_rm_resource
    azure_rm_resource:
      resource_group: "{{ resource_group }}"
      provider: compute
      resource_type: virtualmachinescalesets
      resource_name: "{{ scaleset_name }}"
      api_version: "2017-12-01"
      body: "{{ body }}"

```

## License

TODO

## Author Information
  - ['Zim Kalinowski (@zikalino)']
