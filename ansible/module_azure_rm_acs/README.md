# Ansible module: ansible.module_azure_rm_acs


Manage an Azure Container Service Instance (ACS)

## Description

Create, update and delete an Azure Container Service Instance.

## Requirements

TODO

## Arguments

``` json
{
    "ad_user": "{'description': ['Active Directory username. Use when authenticating with an Active Directory user rather than service principal.']}",
    "adfs_authority_url": "{'description': ['Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority.'], 'required': False, 'default': None, 'version_added': 2.6}",
    "agent_pool_profiles": "{'description': ['The agent pool profile suboptions.'], 'required': True, 'suboptions': {'name': {'description': ['Unique name of the agent pool profile in the context of the subscription and resource group.'], 'required': True}, 'count': {'description': ['Number of agents (VMs) to host docker containers. Allowed values must be in the range of 1 to 100 (inclusive).'], 'required': True}, 'dns_prefix': {'description': ['The DNS Prefix given to Agents in this Agent Pool.'], 'required': True}, 'vm_size': {'description': ["The VM Size of each of the Agent Pool VM's (e.g. Standard_F1 / Standard_D2v2)."], 'required': True}}}",
    "api_profile": "{'description': ['Selects an API profile to use when communicating with Azure services. Default value of C(latest) is appropriate for public clouds; future values will allow use with Azure Stack.'], 'default': 'latest', 'version_added': 2.5}",
    "append_tags": "{'description': ["Use to control if tags field is canonical or just appends to existing tags. When canonical, any tags not found in the tags parameter will be removed from the object's metadata."], 'type': 'bool', 'default': True}",
    "auth_source": "{'description': ['Controls the source of the credentials to use for authentication.', 'If not specified, ANSIBLE_AZURE_AUTH_SOURCE environment variable will be used and default to C(auto) if variable is not defined.', 'C(auto) will follow the default precedence of module parameters -> environment variables -> default profile in credential file C(~/.azure/credentials).', 'When set to C(cli), the credentials will be sources from the default Azure CLI profile.', 'Can also be set via the C(ANSIBLE_AZURE_AUTH_SOURCE) environment variable.', 'When set to C(msi), the host machine must be an azure resource with an enabled MSI extension. C(subscription_id) or the environment variable C(AZURE_SUBSCRIPTION_ID) can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.', 'The C(msi) was added in Ansible 2.6.'], 'choices': ['auto', 'cli', 'credential_file', 'env', 'msi'], 'version_added': 2.5}",
    "cert_validation_mode": "{'description': ['Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing C(ignore). Can also be set via credential file profile or the C(AZURE_CERT_VALIDATION) environment variable.'], 'choices': ['validate', 'ignore'], 'version_added': 2.5}",
    "client_id": "{'description': ['Azure client ID. Use when authenticating with a Service Principal.']}",
    "cloud_environment": "{'description': ['For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, C(AzureChinaCloud), C(AzureUSGovernment)), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the C(AZURE_CLOUD_ENVIRONMENT) environment variable.'], 'default': 'AzureCloud', 'version_added': 2.4}",
    "diagnostics_profile": "{'description': ["Should VM Diagnostics be enabled for the Container Service VM's."], 'required': True, 'type': 'bool'}",
    "linux_profile": "{'description': ['The linux profile suboptions.'], 'required': True, 'suboptions': {'admin_username': {'description': ['The Admin Username for the Cluster.'], 'required': True}, 'ssh_key': {'description': ['The Public SSH Key used to access the cluster.'], 'required': True}}}",
    "location": "{'description': ['Valid azure location. Defaults to location of the resource group.']}",
    "master_profile": "{'description': ['Master profile suboptions.'], 'required': True, 'suboptions': {'count': {'description': ['Number of masters (VMs) in the container service cluster. Allowed values are 1, 3, and 5.'], 'required': True, 'choices': [1, 3, 5]}, 'vm_size': {'description': ["The VM Size of each of the Agent Pool VM's (e.g. Standard_F1 / Standard_D2v2)."], 'required': True, 'version_added': 2.5}, 'dns_prefix': {'description': ['The DNS Prefix to use for the Container Service master nodes.'], 'required': True}}}",
    "name": "{'description': ['Name of the Container Services instance.'], 'required': True}",
    "orchestration_platform": "{'description': ['Specifies the Container Orchestration Platform to use. Currently can be either DCOS, Kubernetes or Swarm.'], 'choices': ['DCOS', 'Kubernetes', 'Swarm'], 'required': True}",
    "password": "{'description': ['Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.']}",
    "profile": "{'description': ['Security profile found in ~/.azure/credentials file.']}",
    "resource_group": "{'description': ['Name of a resource group where the Container Services exists or will be created.'], 'required': True}",
    "secret": "{'description': ['Azure client secret. Use when authenticating with a Service Principal.']}",
    "service_principal": "{'description': ['The service principal suboptions.'], 'suboptions': {'client_id': {'description': ['The ID for the Service Principal.']}, 'client_secret': {'description': ['The secret password associated with the service principal.']}}}",
    "state": "{'description': ["Assert the state of the ACS. Use 'present' to create or update an ACS and 'absent' to delete it."], 'default': 'present', 'choices': ['absent', 'present']}",
    "subscription_id": "{'description': ['Your Azure subscription Id.']}",
    "tags": "{'description': ['Dictionary of string:string pairs to assign as metadata to the object. Metadata tags on the object will be updated with any provided values. To remove tags set append_tags option to false.\n']}",
    "tenant": "{'description': ['Azure tenant ID. Use when authenticating with a Service Principal.']}",
}
```

## Examples


``` yaml

    - name: Create an azure container services instance running Kubernetes
      azure_rm_acs:
        name: acctestcontservice1
        location: eastus
        resource_group: Testing
        orchestration_platform: Kubernetes
        master_profile:
            - count: 3
              dns_prefix: acsk8smasterdns
              vm_size: Standard_D2_v2
        linux_profile:
            - admin_username: azureuser
              ssh_key: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAA...
        service_principal:
            - client_id: "cf72ca99-f6b9-4004-b0e0-bee10c521948"
              client_secret: "mySPNp@ssw0rd!"
        agent_pool_profiles:
            - name: default
              count: 5
              dns_prefix: acsk8sagent
              vm_size: Standard_D2_v2
        diagnostics_profile: false
        tags:
            Environment: Production

    - name: Create an azure container services instance running DCOS
      azure_rm_acs:
        name: acctestcontservice2
        location: eastus
        resource_group: Testing
        orchestration_platform: DCOS
        master_profile:
            - count: 3
              dns_prefix: acsdcosmasterdns
              vm_size: Standard_D2_v2
        linux_profile:
            - admin_username: azureuser
              ssh_key: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAA...
        agent_pool_profiles:
            - name: default
              count: 5
              dns_prefix: acscdcosagent
              vm_size: Standard_D2_v2
        diagnostics_profile: false
        tags:
            Environment: Production

    - name: Create an azure container services instance running Swarm
      azure_rm_acs:
        name: acctestcontservice3
        location: eastus
        resource_group: Testing
        orchestration_platform: Swarm
        master_profile:
            - count: 3
              dns_prefix: acsswarmmasterdns
              vm_size: Standard_D2_v2
        linux_profile:
            - admin_username: azureuser
              ssh_key: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAA...
        agent_pool_profiles:
            - name: default
              count: 5
              dns_prefix: acsswarmagent
              vm_size: Standard_D2_v2
        diagnostics_profile: false
        tags:
            Environment: Production

# Deletes the specified container service in the specified subscription and resource group.
# The operation does not delete other resources created as part of creating a container service,
# including storage accounts, VMs, and availability sets. All the other resources created with the container
# service are part of the same resource group and can be deleted individually.
    - name: Remove an azure container services instance
      azure_rm_acs:
        name: acctestcontservice3
        location: eastus
        resource_group: Testing
        state: absent
        orchestration_platform: Swarm
        master_profile:
            - count: 1
              vm_size: Standard_A0
              dns_prefix: acstestingmasterdns5
        linux_profile:
            - admin_username: azureuser
              ssh_key: ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAA...
        agent_pool_profiles:
            - name: default
              count: 4
              dns_prefix: acctestagent15
              vm_size: Standard_A0
        diagnostics_profile: false
        tags:
            Ansible: azure_rm_acs

```

## License

TODO

## Author Information
  - ['Julien Stroheker (@julienstroheker)']
