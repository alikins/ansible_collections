# Ansible module: ansible.module_azure_rm_postgresqldatabase


Manage PostgreSQL Database instance

## Description

Create, update and delete instance of PostgreSQL Database.

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
    "charset": "{'description': ['The charset of the database. Check PostgreSQL documentation for possible values.', "This is only set on creation, use I(force_update) to recreate a database if the values don't match."]}",
    "client_id": "{'description': ['Azure client ID. Use when authenticating with a Service Principal.']}",
    "cloud_environment": "{'description': ['For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, C(AzureChinaCloud), C(AzureUSGovernment)), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the C(AZURE_CLOUD_ENVIRONMENT) environment variable.'], 'default': 'AzureCloud', 'version_added': 2.4}",
    "collation": "{'description': ['The collation of the database. Check PostgreSQL documentation for possible values.', "This is only set on creation, use I(force_update) to recreate a database if the values don't match."]}",
    "force_update": "{'description': ["When set to C(true), will delete and recreate the existing PostgreSQL database if any of the properties don't match what is set.", 'When set to C(false), no change will occur to the database even if any of the properties do not match.'], 'type': 'bool', 'default': False}",
    "name": "{'description': ['The name of the database.'], 'required': True}",
    "password": "{'description': ['Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.']}",
    "profile": "{'description': ['Security profile found in ~/.azure/credentials file.']}",
    "resource_group": "{'description': ['The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.'], 'required': True}",
    "secret": "{'description': ['Azure client secret. Use when authenticating with a Service Principal.']}",
    "server_name": "{'description': ['The name of the server.'], 'required': True}",
    "state": "{'description': ["Assert the state of the PostgreSQL database. Use 'present' to create or update a database and 'absent' to delete it."], 'default': 'present', 'choices': ['absent', 'present']}",
    "subscription_id": "{'description': ['Your Azure subscription Id.']}",
    "tenant": "{'description': ['Azure tenant ID. Use when authenticating with a Service Principal.']}",
}
```

## Examples


``` yaml

  - name: Create (or update) PostgreSQL Database
    azure_rm_postgresqldatabase:
      resource_group: TestGroup
      server_name: testserver
      name: db1

```

## License

TODO

## Author Information
  - ['Zim Kalinowski (@zikalino)']
