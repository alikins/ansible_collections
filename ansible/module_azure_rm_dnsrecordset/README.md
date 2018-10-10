# Ansible module: ansible.module_azure_rm_dnsrecordset


Create, delete and update DNS record sets and records

## Description

Creates, deletes, and updates DNS records sets and records within an existing Azure DNS Zone.

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
    "password": "{'description': ['Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.']}",
    "profile": "{'description': ['Security profile found in ~/.azure/credentials file.']}",
    "record_mode": "{'description': ['whether existing record values not sent to the module should be purged'], 'default': 'purge', 'choices': ['append', 'purge']}",
    "record_type": "{'description': ['the type of record set to create or delete'], 'choices': ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'SRV', 'TXT', 'PTR'], 'required': True}",
    "records": "{'description': ['list of records to be created depending on the type of record (set)'], 'suboptions': {'preference': {'description': ['used for creating an MX record set/records']}, 'priority': {'description': ['used for creating an SRV record set/records']}, 'weight': {'description': ['used for creating an SRV record set/records']}, 'port': {'description': ['used for creating an SRV record set/records']}, 'entry': {'description': ['primary data value for all record types.']}}}",
    "relative_name": "{'description': ['relative name of the record set'], 'required': True}",
    "resource_group": "{'description': ['name of resource group'], 'required': True}",
    "secret": "{'description': ['Azure client secret. Use when authenticating with a Service Principal.']}",
    "state": "{'description': ['Assert the state of the record set. Use C(present) to create or update and C(absent) to delete.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "subscription_id": "{'description': ['Your Azure subscription Id.']}",
    "tags": "{'description': ['Dictionary of string:string pairs to assign as metadata to the object. Metadata tags on the object will be updated with any provided values. To remove tags set append_tags option to false.\n']}",
    "tenant": "{'description': ['Azure tenant ID. Use when authenticating with a Service Principal.']}",
    "time_to_live": "{'description': ['time to live of the record set in seconds'], 'default': 3600}",
    "zone_name": "{'description': ['name of the existing DNS zone in which to manage the record set'], 'required': True}",
}
```

## Examples


``` yaml


- name: ensure an "A" record set with multiple records
  azure_rm_dnsrecordset:
    resource_group: Testing
    relative_name: www
    zone_name: testing.com
    record_type: A
    state: present
    records:
      - entry: 192.168.100.101
      - entry: 192.168.100.102
      - entry: 192.168.100.103

- name: delete a record set
  azure_rm_dnsrecordset:
    resource_group: Testing
    record_type: A
    relative_name: www
    zone_name: testing.com
    state: absent

- name: create multiple "A" record sets with multiple records
  azure_rm_dnsrecordset:
    resource_group: Testing
    zone_name: testing.com
    state: present
    relative_name: "{{ item.name }}"
    record_type: "{{ item.type }}"
    records: "{{ item.records }}"
  with_items:
    - { name: 'servera', type: 'A', records: [ { entry: '10.10.10.20' }, { entry: '10.10.10.21' }] }
    - { name: 'serverb', type: 'A', records: [ { entry: '10.10.10.30' }, { entry: '10.10.10.41' }] }
    - { name: 'serverc', type: 'A', records: [ { entry: '10.10.10.40' }, { entry: '10.10.10.41' }] }

- name: create SRV records in a new record set
  azure_rm_dnsrecordset:
    resource_group: Testing
    relative_name: _sip._tcp.testing.com
    zone_name: testing.com
    time_to_live: 7200
    record_type: SRV
    state: present
    records:
    - entry: sip.testing.com
      preference: 10
      priority: 20
      weight: 10
      port: 5060

- name: create PTR record in a new record set
  azure_rm_dnsrecordset:
    resource_group: Testing
    relative_name: 192.168.100.101.in-addr.arpa
    zone_name: testing.com
    record_type: PTR
    records:
    - entry: servera.testing.com

- name: create TXT record in a new record set
  azure_rm_dnsrecordset:
    resource_group: Testing
    relative_name: mail.testing.com
    zone_name: testing.com
    record_type: TXT
    records:
    - entry: 'v=spf1 a -all'


```

## License

TODO

## Author Information
  - ['Obezimnaka Boms (@ozboms)', 'Matt Davis (@nitzmahone)']
  - ['Obezimnaka Boms (@ozboms)', 'Matt Davis (@nitzmahone)']
