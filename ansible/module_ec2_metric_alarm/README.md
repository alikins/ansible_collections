# Ansible module: ansible.module_ec2_metric_alarm


Create/update or delete AWS Cloudwatch 'metric alarms'

## Description

Can create or delete AWS metric alarms.
Metrics you wish to alarm on must already exist.

## Requirements

TODO

## Arguments

``` json
{
    "alarm_actions": "{'description': ["A list of the names action(s) taken when the alarm is in the 'alarm' status"], 'required': False}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "comparison": "{'description': ['Determines how the threshold value is compared'], 'required': False, 'choices': ['<=', '<', '>', '>=']}",
    "description": "{'description': ['A longer description of the alarm'], 'required': False}",
    "dimensions": "{'description': ['Describes to what the alarm is applied'], 'required': False}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "evaluation_periods": "{'description': ['The number of times in which the metric is evaluated before final calculation'], 'required': False}",
    "insufficient_data_actions": "{'description': ["A list of the names of action(s) to take when the alarm is in the 'insufficient_data' status"], 'required': False}",
    "metric": "{'description': ['Name of the monitored metric (e.g. CPUUtilization)', 'Metric must already exist'], 'required': False}",
    "name": "{'description': ['Unique name for the alarm'], 'required': True}",
    "namespace": "{'description': ["Name of the appropriate namespace ('AWS/EC2', 'System/Linux', etc.), which determines the category it will appear under in cloudwatch"], 'required': False}",
    "ok_actions": "{'description': ["A list of the names of action(s) to take when the alarm is in the 'ok' status"], 'required': False}",
    "period": "{'description': ['The time (in seconds) between metric evaluations'], 'required': False}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['register or deregister the alarm'], 'required': True, 'choices': ['present', 'absent']}",
    "statistic": "{'description': ['Operation applied to the metric', 'Works in conjunction with period and evaluation_periods to determine the comparison value'], 'required': False, 'choices': ['SampleCount', 'Average', 'Sum', 'Minimum', 'Maximum']}",
    "threshold": "{'description': ['Sets the min/max bound for triggering the alarm'], 'required': False}",
    "unit": "{'description': ["The threshold's unit of measurement"], 'required': False, 'choices': ['Seconds', 'Microseconds', 'Milliseconds', 'Bytes', 'Kilobytes', 'Megabytes', 'Gigabytes', 'Terabytes', 'Bits', 'Kilobits', 'Megabits', 'Gigabits', 'Terabits', 'Percent', 'Count', 'Bytes/Second', 'Kilobytes/Second', 'Megabytes/Second', 'Gigabytes/Second', 'Terabytes/Second', 'Bits/Second', 'Kilobits/Second', 'Megabits/Second', 'Gigabits/Second', 'Terabits/Second', 'Count/Second', 'None']}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
}
```

## Examples


``` yaml

  - name: create alarm
    ec2_metric_alarm:
      state: present
      region: ap-southeast-2
      name: "cpu-low"
      metric: "CPUUtilization"
      namespace: "AWS/EC2"
      statistic: Average
      comparison: "<="
      threshold: 5.0
      period: 300
      evaluation_periods: 3
      unit: "Percent"
      description: "This will alarm when a bamboo slave's cpu usage average is lower than 5% for 15 minutes "
      dimensions: {'InstanceId':'i-XXX'}
      alarm_actions: ["action1","action2"]



```

## License

TODO

## Author Information
  - ['Zacharie Eakin (@zeekin)']
