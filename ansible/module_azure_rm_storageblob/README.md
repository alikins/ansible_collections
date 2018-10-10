# Ansible module: ansible.module_azure_rm_storageblob


Manage blob containers and blob objects

## Description

Create, update and delete blob containers and blob objects. Use to upload a file and store it as a blob object, or download a blob object to a file.

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
    "blob": "{'description': ['Name of a blob object within the container.'], 'aliases': ['blob_name']}",
    "blob_type": "{'description': ['Type of Blob Object.'], 'default': 'block', 'choices': ['block', 'page'], 'version_added': '2.5'}",
    "cache_control": "{'description': ['Set the blob cache-control header.']}",
    "cert_validation_mode": "{'description': ['Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing C(ignore). Can also be set via credential file profile or the C(AZURE_CERT_VALIDATION) environment variable.'], 'choices': ['validate', 'ignore'], 'version_added': 2.5}",
    "client_id": "{'description': ['Azure client ID. Use when authenticating with a Service Principal.']}",
    "cloud_environment": "{'description': ['For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, C(AzureChinaCloud), C(AzureUSGovernment)), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the C(AZURE_CLOUD_ENVIRONMENT) environment variable.'], 'default': 'AzureCloud', 'version_added': 2.4}",
    "container": "{'description': ['Name of a blob container within the storage account.'], 'required': True, 'aliases': ['container_name']}",
    "content_disposition": "{'description': ['Set the blob content-disposition header.']}",
    "content_encoding": "{'description': ['Set the blob encoding header.']}",
    "content_language": "{'description': ['Set the blob content-language header.']}",
    "content_md5": "{'description': ['Set the blob md5 hash value.']}",
    "content_type": "{'description': ["Set the blob content-type header. For example, 'image/png'."]}",
    "dest": "{'description': ["Destination file path. Use with state 'present' to download a blob."], 'aliases': ['destination']}",
    "force": "{'description': ['Overwrite existing blob or file when uploading or downloading. Force deletion of a container that contains blobs.'], 'type': 'bool', 'default': False}",
    "password": "{'description': ['Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.']}",
    "profile": "{'description': ['Security profile found in ~/.azure/credentials file.']}",
    "public_access": "{'description': ["Determine a container's level of public access. By default containers are private. Can only be set at time of container creation."], 'choices': ['container', 'blob']}",
    "resource_group": "{'description': ['Name of the resource group to use.'], 'required': True, 'aliases': ['resource_group_name']}",
    "secret": "{'description': ['Azure client secret. Use when authenticating with a Service Principal.']}",
    "src": "{'description': ["Source file path. Use with state 'present' to upload a blob."], 'aliases': ['source']}",
    "state": "{'description': ['Assert the state of a container or blob.', "Use state 'absent' with a container value only to delete a container. Include a blob value to remove a specific blob. A container will not be deleted, if it contains blobs. Use the force option to override, deleting the container and all associated blobs.", "Use state 'present' to create or update a container and upload or download a blob. If the container does not exist, it will be created. If it exists, it will be updated with configuration options. Provide a blob name and either src or dest to upload or download. Provide a src path to upload and a dest path to download. If a blob (uploading) or a file (downloading) already exists, it will not be overwritten unless the force parameter is true."], 'default': 'present', 'choices': ['absent', 'present']}",
    "storage_account_name": "{'description': ['Name of the storage account to use.'], 'required': True, 'aliases': ['account_name', 'storage_account']}",
    "subscription_id": "{'description': ['Your Azure subscription Id.']}",
    "tags": "{'description': ['Dictionary of string:string pairs to assign as metadata to the object. Metadata tags on the object will be updated with any provided values. To remove tags set append_tags option to false.\n']}",
    "tenant": "{'description': ['Azure tenant ID. Use when authenticating with a Service Principal.']}",
}
```

## Examples


``` yaml

- name: Remove container foo
  azure_rm_storageblob:
    resource_group: testing
    storage_account_name: clh0002
    container: foo
    state: absent

- name: Create container foo and upload a file
  azure_rm_storageblob:
    resource_group: Testing
    storage_account_name: clh0002
    container: foo
    blob: graylog.png
    src: ./files/graylog.png
    public_access: container
    content_type: 'application/image'

- name: Download the file
  azure_rm_storageblob:
    resource_group: Testing
    storage_account_name: clh0002
    container: foo
    blob: graylog.png
    dest: ~/tmp/images/graylog.png

```

## License

TODO

## Author Information
  - ['Chris Houseknecht (@chouseknecht)', 'Matt Davis (@nitzmahone)']
  - ['Chris Houseknecht (@chouseknecht)', 'Matt Davis (@nitzmahone)']
