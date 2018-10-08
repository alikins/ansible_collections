# Ansible inventory: ansible.inventory_azure_rm


Azure Resource Manager inventory plugin

## Description

Query VM details from Azure Resource Manager
Requires a YAML configuration file whose name ends with '.azure_rm.yaml'
By default, sets C(ansible_host) to the first public IP address found (preferring the primary NIC). If no public IPs are found, the first private IP (also preferring the primary NIC). The default may be overridden via C(hostvar_expressions); see examples.

## Requirements

TODO

## Arguments

``` json
{
    "ad_user": "{'description': ['Active Directory username. Use when authenticating with an Active Directory user rather than service principal.']}",
    "adfs_authority_url": "{'description': ['Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority.'], 'required': False, 'default': None, 'version_added': 2.6}",
    "api_profile": "{'description': ['Selects an API profile to use when communicating with Azure services. Default value of C(latest) is appropriate for public clouds; future values will allow use with Azure Stack.'], 'default': 'latest', 'version_added': 2.5}",
    "auth_source": "{'description': ['Controls the source of the credentials to use for authentication.', 'If not specified, ANSIBLE_AZURE_AUTH_SOURCE environment variable will be used and default to C(auto) if variable is not defined.', 'C(auto) will follow the default precedence of module parameters -> environment variables -> default profile in credential file C(~/.azure/credentials).', 'When set to C(cli), the credentials will be sources from the default Azure CLI profile.', 'Can also be set via the C(ANSIBLE_AZURE_AUTH_SOURCE) environment variable.', 'When set to C(msi), the host machine must be an azure resource with an enabled MSI extension. C(subscription_id) or the environment variable C(AZURE_SUBSCRIPTION_ID) can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.', 'The C(msi) was added in Ansible 2.6.'], 'choices': ['auto', 'cli', 'credential_file', 'env', 'msi'], 'version_added': 2.5}",
    "batch_fetch": "{'description': ['To improve performance, results are fetched using an unsupported batch API. Disabling C(batch_fetch) uses a much slower serial fetch, resulting in many more round-trips. Generally only useful for troubleshooting.'], 'default': True}",
    "cert_validation_mode": "{'description': ['Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing C(ignore). Can also be set via credential file profile or the C(AZURE_CERT_VALIDATION) environment variable.'], 'choices': ['validate', 'ignore'], 'version_added': 2.5}",
    "client_id": "{'description': ['Azure client ID. Use when authenticating with a Service Principal.']}",
    "cloud_environment": "{'description': ['For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, C(AzureChinaCloud), C(AzureUSGovernment)), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the C(AZURE_CLOUD_ENVIRONMENT) environment variable.'], 'default': 'AzureCloud', 'version_added': 2.4}",
    "conditional_groups": "{'description': ['A mapping of group names to Jinja2 expressions. When the mapped expression is true, the host is added to the named group.']}",
    "default_host_filters": "{'description': ['A default set of filters that is applied in addition to the conditions in C(exclude_host_filters) to exclude powered-off and not-fully-provisioned hosts. Set this to a different value or empty list if you need to include hosts in these states.'], 'default': ['powerstate != "running"', 'provisioning_state != "succeeded"']}",
    "exclude_host_filters": "{'description': ['Excludes hosts from the inventory with a list of Jinja2 conditional expressions. Each expression in the list is evaluated for each host; when the expression is true, the host is excluded from the inventory.'], 'default': []}",
    "fail_on_template_errors": "{'description': ['When false, template failures during group and filter processing are silently ignored (eg, if a filter or group expression refers to an undefined host variable)'], 'choices': [True, False], 'default': True}",
    "hostvar_expressions": "{'description': ["A mapping of hostvar names to Jinja2 expressions. The value for each host is the result of the Jinja2 expression (which may refer to any of the host's existing variables at the time this inventory plugin runs)."]}",
    "include_vm_resource_groups": "{'description': ["A list of resource group names to search for virtual machines. '\\*' will include all resource groups in the subscription."], 'default': ['*']}",
    "include_vmss_resource_groups": "{'description': ["A list of resource group names to search for virtual machine scale sets (VMSSs). '\\*' will include all resource groups in the subscription."], 'default': []}",
    "keyed_groups": "{'description': ['Creates groups based on the value of a host variable. Requires a list of dictionaries, defining C(key) (the source dictionary-typed variable), C(prefix) (the prefix to use for the new group name), and optionally C(separator) (which defaults to C(_))']}",
    "password": "{'description': ['Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.']}",
    "plugin": "{'description': ["marks this as an instance of the 'azure_rm' plugin"], 'required': True, 'choices': ['azure_rm']}",
    "profile": "{'description': ['Security profile found in ~/.azure/credentials file.']}",
    "secret": "{'description': ['Azure client secret. Use when authenticating with a Service Principal.']}",
    "subscription_id": "{'description': ['Your Azure subscription Id.']}",
    "tenant": "{'description': ['Azure tenant ID. Use when authenticating with a Service Principal.']}",
}
```

## Examples


``` yaml

# The following host variables are always available:
# public_ipv4_addresses: all public IP addresses, with the primary IP config from the primary NIC first
# public_dns_hostnames: all public DNS hostnames, with the primary IP config from the primary NIC first
# private_ipv4_addresses: all private IP addressses, with the primary IP config from the primary NIC first
# id: the VM's Azure resource ID, eg /subscriptions/00000000-0000-0000-1111-1111aaaabb/resourceGroups/my_rg/providers/Microsoft.Compute/virtualMachines/my_vm
# location: the VM's Azure location, eg 'westus', 'eastus'
# name: the VM's resource name, eg 'myvm'
# powerstate: the VM's current power state, eg: 'running', 'stopped', 'deallocated'
# provisioning_state: the VM's current provisioning state, eg: 'succeeded'
# tags: dictionary of the VM's defined tag values
# resource_type: the VM's resource type, eg: 'Microsoft.Compute/virtualMachine', 'Microsoft.Compute/virtualMachineScaleSets/virtualMachines'
# vmid: the VM's internal SMBIOS ID, eg: '36bca69d-c365-4584-8c06-a62f4a1dc5d2'
# vmss: if the VM is a member of a scaleset (vmss), a dictionary including the id and name of the parent scaleset


# sample 'myazuresub.azure_rm.yaml'

# required for all azure_rm inventory plugin configs
plugin: azure_rm

# forces this plugin to use a CLI auth session instead of the automatic auth source selection (eg, prevents the
# presence of 'ANSIBLE_AZURE_RM_X' environment variables from overriding CLI auth)
auth_source: cli

# fetches VMs from an explicit list of resource groups instead of default all (- '*')
include_vm_resource_groups:
- myrg1
- myrg2

# fetches VMs from VMSSs in all resource groups (defaults to no VMSS fetch)
include_vmss_resource_groups:
- '*'

# places a host in the named group if the associated condition evaluates to true
conditional_groups:
  # since this will be true for every host, every host sourced from this inventory plugin config will be in the
  # group 'all_the_hosts'
  all_the_hosts: true
  # if the VM's "name" variable contains "dbserver", it will be placed in the 'db_hosts' group
  db_hosts: "'dbserver' in name"

# adds variables to each host found by this inventory plugin, whose values are the result of the associated expression
hostvar_expressions:
  my_host_var:
  # A statically-valued expression has to be both single and double-quoted, or use escaped quotes, since the outer
  # layer of quotes will be consumed by YAML. Without the second set of quotes, it interprets 'staticvalue' as a
  # variable instead of a string literal.
  some_statically_valued_var: "'staticvalue'"
  # overrides the default ansible_host value with a custom Jinja2 expression, in this case, the first DNS hostname, or
  # if none are found, the first public IP address.
  ansible_host: (public_dns_hostnames + public_ipv4_addresses) | first

# places hosts in dynamically-created groups based on a variable value.
keyed_groups:
# places each host in a group named 'tag_(tag name)_(tag value)' for each tag on a VM.
- prefix: tag
  key: tags
# places each host in a group named 'azure_loc_(location name)', depending on the VM's location
- prefix: azure_loc
  key: location
# places host in a group named 'some_tag_X' using the value of the 'sometag' tag on a VM as X, and defaulting to the
# value 'none' (eg, the group 'some_tag_none') if the 'sometag' tag is not defined for a VM.
- prefix: some_tag
  key: tags.sometag | default('none')

# excludes a host from the inventory when any of these expressions is true, can refer to any vars defined on the host
exclude_host_filters:
# excludes hosts in the eastus region
- location in ['eastus']
# excludes hosts that are powered off
- powerstate != 'running'

```

## License

TODO

## Author Information
  - ['UNKNOWN']
