# Ansible module: ansible.module_python_requirements_facts


Show python path and assert dependency versions

## Description

Get info about available Python requirements on the target host, including listing required libraries and gathering versions.

## Requirements

TODO

## Arguments

``` json
{
    "dependencies": "{'description': ['A list of version-likes or module names to check for installation. Supported operators: <, >, <=, >=, or ==. The bare module name like I(ansible), the module with a specific version like I(boto3==1.6.1), or a partial version like I(requests>2) are all valid specifications.\n']}",
}
```

## Examples


``` yaml

- name: show python lib/site paths
  python_requirements_facts:
- name: check for modern boto3 and botocore versions
  python_requirements_facts:
    dependencies:
    - boto3>1.6
    - botocore<2

```

## License

TODO

## Author Information
  - ['Will Thames (@willthames)', 'Ryan Scott Brown (@ryan_sb)']
  - ['Will Thames (@willthames)', 'Ryan Scott Brown (@ryan_sb)']
