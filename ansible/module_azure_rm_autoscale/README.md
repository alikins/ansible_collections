# Ansible module: ansible.module_azure_rm_autoscale


Manage Azure autoscale setting

## Description

Create, delete an autoscale setting.

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
    "enabled": "{'type': 'bool', 'description': ['Specifies whether automatic scaling is enabled for the resource.'], 'default': True}",
    "location": "{'description': ['location of the resource.']}",
    "name": "{'required': True, 'description': ['name of the resource.']}",
    "notifications": "{'description': ['the collection of notifications.'], 'suboptions': {'custom_emails': {'description': 'the custom e-mails list. This value can be null or empty, in which case this attribute will be ignored.'}, 'send_to_subscription_administrator': {'type': 'bool', 'description': 'A value indicating whether to send email to subscription administrator.'}, 'webhooks': {'description': 'The list of webhook notifications service uri.'}, 'send_to_subscription_co_administrators': {'type': 'bool', 'description': 'A value indicating whether to send email to subscription co-administrators.'}}}",
    "password": "{'description': ['Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.']}",
    "profile": "{'description': ['Security profile found in ~/.azure/credentials file.']}",
    "profiles": "{'description': ['The collection of automatic scaling profiles that specify different scaling parameters for different time periods.', 'A maximum of 20 profiles can be specified.'], 'suboptions': {'name': {'required': True, 'description': 'the name of the profile.'}, 'count': {'required': True, 'description': ['The number of instances that will be set if metrics are not available for evaluation.', 'The default is only used if the current instance count is lower than the default.']}, 'min_count': {'description': 'the minimum number of instances for the resource.'}, 'max_count': {'description': 'the maximum number of instances for the resource.'}, 'recurrence_frequency': {'default': 'None', 'description': ['How often the schedule profile should take effect.', 'If this value is Week, meaning each week will have the same set of profiles.', 'This element is not used if the FixedDate element is used.'], 'choices': ['None', 'Second', 'Minute', 'Hour', 'Day', 'Week', 'Month', 'Year']}, 'recurrence_timezone': {'description': ['The timezone of repeating times at which this profile begins.', 'This element is not used if the FixedDate element is used.']}, 'recurrence_days': {'description': ['The days of repeating times at which this profile begins.', 'This element is not used if the FixedDate element is used.']}, 'recurrence_hours': {'description': ['The hours of repeating times at which this profile begins.', 'This element is not used if the FixedDate element is used.']}, 'recurrence_mins': {'description': ['The mins of repeating times at which this profile begins.', 'This element is not used if the FixedDate element is used.']}, 'fixed_date_timezone': {'description': ['The specific date-time timezone for the profile.', 'This element is not used if the Recurrence element is used.']}, 'fixed_date_start': {'description': ['The specific date-time start for the profile.', 'This element is not used if the Recurrence element is used.']}, 'fixed_date_end': {'description': ['The specific date-time end for the profile.', 'This element is not used if the Recurrence element is used.']}, 'rules': {'description': ['The collection of rules that provide the triggers and parameters for the scaling action.', 'A maximum of 10 rules can be specified.'], 'suboptions': {'time_aggregation': {'default': 'Average', 'description': 'How the data that is collected should be combined over time.', 'choices': ['Average', 'Minimum', 'Maximum', 'Total', 'Count']}, 'time_window': {'required': True, 'description': ['The range of time(minutes) in which instance data is collected.', 'This value must be greater than the delay in metric collection, which can vary from resource-to-resource.', 'Must be between 5 ~ 720.']}, 'direction': {'description': 'Whether the scaling action increases or decreases the number of instances.', 'choices': ['Increase', 'Decrease']}, 'metric_name': {'required': True, 'description': 'The name of the metric that defines what the rule monitors.'}, 'metric_resource_uri': {'description': 'The resource identifier of the resource the rule monitors.'}, 'value': {'description': ['The number of instances that are involved in the scaling action.', 'This value must be 1 or greater.']}, 'operator': {'default': 'GreaterThan', 'description': 'The operator that is used to compare the metric data and the threshold.', 'choices': ['Equals', 'NotEquals', 'GreaterThan', 'GreaterThanOrEqual', 'LessThan', 'LessThanOrEqual']}, 'cooldown': {'description': ['The amount of time (minutes) to wait since the last scaling action before this action occurs.', 'It must be between 1 ~ 10080.']}, 'time_grain': {'required': True, 'description': ['The granularity(minutes) of metrics the rule monitors.', 'Must be one of the predefined values returned from metric definitions for the metric.', 'Must be between 1 ~ 720.']}, 'statistic': {'default': 'Average', 'description': 'How the metrics from multiple instances are combined.', 'choices': ['Average', 'Min', 'Max', 'Sum']}, 'threshold': {'default': 70, 'description': 'The threshold of the metric that triggers the scale action.'}, 'type': {'description': 'The type of action that should occur when the scale rule fires.', 'choices': ['PercentChangeCount', 'ExactCount', 'ChangeCount']}}}}}",
    "resource_group": "{'required': True, 'description': ['resource group of the resource.']}",
    "secret": "{'description': ['Azure client secret. Use when authenticating with a Service Principal.']}",
    "state": "{'default': 'present', 'description': ["Assert the state of the virtual network. Use 'present' to create or update and 'absent' to delete."], 'choices': ['present', 'absent']}",
    "subscription_id": "{'description': ['Your Azure subscription Id.']}",
    "tags": "{'description': ['Dictionary of string:string pairs to assign as metadata to the object. Metadata tags on the object will be updated with any provided values. To remove tags set append_tags option to false.\n']}",
    "target": "{'description': ['The identifier of the resource to apply autoscale setting.', 'It could be the resource id string.', 'It also could be a dict contains the C(name), C(subscription_id), C(namespace), C(types), C(resource_group) of the resource.']}",
    "tenant": "{'description': ['Azure tenant ID. Use when authenticating with a Service Principal.']}",
}
```

## Examples


``` yaml

- name: Create an auto scale
  azure_rm_autoscale:
      target: "/subscriptions/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX/resourceGroups/foo/providers/Microsoft.Compute/virtualMachineScaleSets/vmss"
      enabled: true
      profiles:
      - count: '1'
        recurrence_days:
        - Monday
        name: Auto created scale condition
        recurrence_timezone: China Standard Time
        recurrence_mins:
        - '0'
        min_count: '1'
        max_count: '1'
        recurrence_frequency: Week
        recurrence_hours:
        - '18'
      name: scale
      resource_group: foo

- name: Create an auto scale with compicated profile
  azure_rm_autoscale:
      target: "/subscriptions/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX/resourceGroups/foo/providers/Microsoft.Compute/virtualMachineScaleSets/vmss"
      enabled: true
      profiles:
      - count: '1'
        recurrence_days:
        - Monday
        name: Auto created scale condition 0
        rules:
        - Time_aggregation: Average
          time_window: 10
          direction: Increase
          metric_name: Percentage CPU
          metric_resource_uri: "/subscriptions/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX/resourceGroups/foo/providers/Microsoft.Compute/virtualMachineScaleSets/vmss"
          value: '1'
          threshold: 70
          cooldown: 5
          time_grain: 1
          statistic: Average
          operator: GreaterThan
          type: ChangeCount
        max_count: '1'
        recurrence_mins:
        - '0'
        min_count: '1'
        recurrence_timezone: China Standard Time
        recurrence_frequency: Week
        recurrence_hours:
        - '6'
      notifications:
      - email_admin: True
        email_co_admin: False
        custom_emails:
        - yuwzho@microsoft.com
      name: scale
      resource_group: foo

- name: Delete an Azure Auto Scale Setting
  azure_rm_autoscale:
    state: absent
    resource_group: foo
    name: scale

```

## License

TODO

## Author Information
  - ['Yuwei Zhou (@yuwzho)']
