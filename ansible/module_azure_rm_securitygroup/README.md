# Ansible module: ansible.module_azure_rm_securitygroup


Manage Azure network security groups

## Description

Create, update or delete a network security group. A security group contains Access Control List (ACL) rules that allow or deny network traffic to subnets or individual network interfaces. A security group is created with a set of default security rules and an empty set of security rules. Shape traffic flow by adding rules to the empty set of security rules.

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
    "default_rules": "{'description': ['The set of default rules automatically added to a security group at creation. In general default rules will not be modified. Modify rules to shape the flow of traffic to or from a subnet or NIC. See rules below for the makeup of a rule dict.']}",
    "location": "{'description': ['Valid azure location. Defaults to location of the resource group.']}",
    "name": "{'description': ['Name of the security group to operate on.']}",
    "password": "{'description': ['Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.']}",
    "profile": "{'description': ['Security profile found in ~/.azure/credentials file.']}",
    "purge_default_rules": "{'description': ['Remove any existing rules not matching those defined in the default_rules parameter.'], 'type': 'bool', 'default': False}",
    "purge_rules": "{'description': ['Remove any existing rules not matching those defined in the rules parameters.'], 'type': 'bool', 'default': False}",
    "resource_group": "{'description': ['Name of the resource group the security group belongs to.'], 'required': True}",
    "rules": "{'description': ['Set of rules shaping traffic flow to or from a subnet or NIC. Each rule is a dictionary.'], 'suboptions': {'name': {'description': ['Unique name for the rule.'], 'required': True}, 'description': {'description': ["Short description of the rule's purpose."]}, 'protocol': {'description': 'Accepted traffic protocol.', 'choices': ['Udp', 'Tcp', '*'], 'default': '*'}, 'source_port_range': {'description': ['Port or range of ports from which traffic originates.', 'It can accept string type or a list of string type.'], 'default': '*'}, 'destination_port_range': {'description': ['Port or range of ports to which traffic is headed.', 'It can accept string type or a list of string type.'], 'default': '*'}, 'source_address_prefix': {'description': ['The CIDR or source IP range.', 'Asterisk C(*) can also be used to match all source IPs.', 'Default tags such as C(VirtualNetwork), C(AzureLoadBalancer) and C(Internet) can also be used.', 'If this is an ingress rule, specifies where network traffic originates from.', 'It can accept string type or a list of string type.'], 'default': '*'}, 'destination_address_prefix': {'description': ['The destination address prefix.', 'CIDR or destination IP range.', 'Asterisk C(*) can also be used to match all source IPs.', 'Default tags such as C(VirtualNetwork), C(AzureLoadBalancer) and C(Internet) can also be used.', 'It can accept string type or a list of string type.'], 'default': '*'}, 'access': {'description': ['Whether or not to allow the traffic flow.'], 'choices': ['Allow', 'Deny'], 'default': 'Allow'}, 'priority': {'description': ['Order in which to apply the rule. Must a unique integer between 100 and 4096 inclusive.'], 'required': True}, 'direction': {'description': ['Indicates the direction of the traffic flow.'], 'choices': ['Inbound', 'Outbound'], 'default': 'Inbound'}}}",
    "secret": "{'description': ['Azure client secret. Use when authenticating with a Service Principal.']}",
    "state": "{'description': ["Assert the state of the security group. Set to 'present' to create or update a security group. Set to 'absent' to remove a security group."], 'default': 'present', 'choices': ['absent', 'present']}",
    "subscription_id": "{'description': ['Your Azure subscription Id.']}",
    "tags": "{'description': ['Dictionary of string:string pairs to assign as metadata to the object. Metadata tags on the object will be updated with any provided values. To remove tags set append_tags option to false.\n']}",
    "tenant": "{'description': ['Azure tenant ID. Use when authenticating with a Service Principal.']}",
}
```

## Examples


``` yaml


# Create a security group
- azure_rm_securitygroup:
      resource_group: mygroup
      name: mysecgroup
      purge_rules: yes
      rules:
          - name: DenySSH
            protocol: Tcp
            destination_port_range: 22
            access: Deny
            priority: 100
            direction: Inbound
          - name: 'AllowSSH'
            protocol: Tcp
            source_address_prefix:
              - '174.109.158.0/24'
              - '174.109.159.0/24'
            destination_port_range: 22
            access: Allow
            priority: 101
            direction: Inbound
          - name: 'AllowMultiplePorts'
            protocol: Tcp
            source_address_prefix:
              - '174.109.158.0/24'
              - '174.109.159.0/24'
            destination_port_range:
              - 80
              - 443
            access: Allow
            priority: 102

# Update rules on existing security group
- azure_rm_securitygroup:
      resource_group: mygroup
      name: mysecgroup
      rules:
          - name: DenySSH
            protocol: Tcp
            destination_port_range: 22-23
            access: Deny
            priority: 100
            direction: Inbound
          - name: AllowSSHFromHome
            protocol: Tcp
            source_address_prefix: '174.109.158.0/24'
            destination_port_range: 22-23
            access: Allow
            priority: 102
            direction: Inbound
      tags:
          testing: testing
          delete: on-exit

# Delete security group
- azure_rm_securitygroup:
      resource_group: mygroup
      name: mysecgroup
      state: absent

```

## License

TODO

## Author Information
  - ['Chris Houseknecht (@chouseknecht)', 'Matt Davis (@nitzmahone)']
  - ['Chris Houseknecht (@chouseknecht)', 'Matt Davis (@nitzmahone)']
