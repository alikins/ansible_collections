# Ansible module: ansible.module_azure_rm_sqldatabase


Manage SQL Database instance

## Description

Create, update and delete instance of SQL Database.

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
    "collation": "{'description': ['The collation of the database. If I(create_mode) is not C(default), this value is ignored.']}",
    "create_mode": "{'description': ['Specifies the mode of database creation.', 'C(default): regular database creation.', 'C(copy): creates a database as a copy of an existing database.', 'C(online_secondary)/C(non_readable_secondary): creates a database as a (readable or nonreadable) secondary replica of an existing database.', 'C(point_in_time_restore): Creates a database by restoring a point in time backup of an existing database.', 'C(recovery): Creates a database by restoring a geo-replicated backup.', 'C(restore): Creates a database by restoring a backup of a deleted database.', 'C(restore_long_term_retention_backup): Creates a database by restoring from a long term retention vault.', 'C(copy), C(non_readable_secondary), C(online_secondary) and C(restore_long_term_retention_backup) are not supported for C(data_warehouse) edition.'], 'choices': ['copy', 'default', 'non_readable_secondary', 'online_secondary', 'point_in_time_restore', 'recovery', 'restore', 'restore_long_term_retention_backup']}",
    "edition": "{'description': ["The edition of the database. The DatabaseEditions enumeration contains all the valid editions. If I(create_mode) is C(non_readable_secondary) or C(online_secondary), this value is ignored. To see possible values, query the capabilities API (/subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationID}/capabilities) referred to by operationId: 'Capabilities_ListByLocation.'."], 'choices': ['web', 'business', 'basic', 'standard', 'premium', 'free', 'stretch', 'data_warehouse', 'system', 'system2']}",
    "elastic_pool_name": "{'description': ['The name of the elastic pool the database is in. Not supported for C(data_warehouse) edition.']}",
    "force_update": "{'description': ['SQL Database will be updated if given parameters differ from existing resource state.', 'To force SQL Database update in any circumstances set this parameter to True.'], 'type': 'bool'}",
    "location": "{'description': ['Resource location. If not set, location from the resource group will be used as C(default).']}",
    "max_size_bytes": "{'description': ["The max size of the database expressed in bytes. If I(create_mode) is not C(default), this value is ignored. To see possible values, query the capabilities API (/subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationID}/capabilities) referred to by operationId: 'Capabilities_ListByLocation.'"]}",
    "name": "{'description': ['The name of the database to be operated on (updated or created).'], 'required': True}",
    "password": "{'description': ['Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.']}",
    "profile": "{'description': ['Security profile found in ~/.azure/credentials file.']}",
    "read_scale": "{'description': ['If the database is a geo-secondary, indicates whether read-only connections are allowed to this database or not. Not supported for C(data_warehouse) edition.'], 'type': 'bool', 'default': False}",
    "recovery_services_recovery_point_resource_id": "{'description': ['Required if I(create_mode) is C(restore_long_term_retention_backup), then this value is required. Specifies the resource ID of the recovery point to restore from.']}",
    "resource_group": "{'description': ['The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.'], 'required': True}",
    "restore_point_in_time": "{'description': ["Required if I(create_mode) is C(point_in_time_restore), this value is required. If I(create_mode) is C(restore), this value is optional. Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database. Must be greater than or equal to the source database's earliestRestoreDate value."]}",
    "sample_name": "{'description': ['Indicates the name of the sample schema to apply when creating this database. If I(create_mode) is not C(default), this value is ignored. Not supported for C(data_warehouse) edition.'], 'choices': ['adventure_works_lt']}",
    "secret": "{'description': ['Azure client secret. Use when authenticating with a Service Principal.']}",
    "server_name": "{'description': ['The name of the server.'], 'required': True}",
    "source_database_deletion_date": "{'description': ["Required if I(create_mode) is C(restore) and I(source_database_id) is the deleted database's original resource id when it existed (as opposed to its current restorable dropped database id), then this value is required. Specifies the time that the database was deleted."]}",
    "source_database_id": "{'description': ['Required unless I(create_mode) is C(default) or C(restore_long_term_retention_backup).', 'Specifies the resource ID of the source database']}",
    "state": "{'description': ["Assert the state of the SQL Database. Use 'present' to create or update an SQL Database and 'absent' to delete it."], 'default': 'present', 'choices': ['absent', 'present']}",
    "subscription_id": "{'description': ['Your Azure subscription Id.']}",
    "tenant": "{'description': ['Azure tenant ID. Use when authenticating with a Service Principal.']}",
    "zone_redundant": "{'description': ['Is this database is zone redundant? It means the replicas of this database will be spread across multiple availability zones.'], 'type': 'bool', 'default': False}",
}
```

## Examples


``` yaml

  - name: Create (or update) SQL Database
    azure_rm_sqldatabase:
      resource_group: sqlcrudtest-4799
      server_name: sqlcrudtest-5961
      name: testdb
      location: eastus

  - name: Restore SQL Database
    azure_rm_sqldatabase:
      resource_group: sqlcrudtest-4799
      server_name: sqlcrudtest-5961
      name: restoreddb
      location: eastus
      create_mode: restore
      restorable_dropped_database_id: "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default-SQL-SouthEastAsia/providers/Microsoft.Sql/s
                                      ervers/testsvr/restorableDroppedDatabases/testdb2,131444841315030000"

  - name: Create SQL Database in Copy Mode
    azure_rm_sqldatabase:
      resource_group: sqlcrudtest-4799
      server_name: sqlcrudtest-5961
      name: copydb
      location: eastus
      create_mode: copy
      source_database_id: "/subscriptions/00000000-1111-2222-3333-444444444444/resourceGroups/Default-SQL-SouthEastAsia/providers/Microsoft.Sql/servers/tests
                          vr/databases/testdb"


```

## License

TODO

## Author Information
  - ['Zim Kalinowski (@zikalino)']
