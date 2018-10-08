# Ansible shell: ansible.shell_powershell


Windows Powershell

## Description

The only option when using 'winrm' as a connection plugin

## Requirements

TODO

## Arguments

``` json
{
    "async_dir": "{'description': ['Directory in which ansible will keep async job information.', 'Before Ansible 2.8, this was set to C(remote_tmp + "\\.ansible_async").'], 'default': '%USERPROFILE%\\.ansible_async', 'ini': [{'section': 'powershell', 'key': 'async_dir'}], 'vars': [{'name': 'ansible_async_dir'}], 'version_added': '2.8'}",
    "environment": "{'description': ['Dictionary of environment variables and their values to use when executing commands.'], 'type': 'dict', 'default': {}}",
    "remote_tmp": "{'description': ['Temporary directory to use on targets when copying files to the host.'], 'default': '%TEMP%', 'ini': [{'section': 'powershell', 'key': 'remote_tmp'}], 'vars': [{'name': 'ansible_remote_tmp'}]}",
    "set_module_language": "{'description': ['Controls if we set the locale for moduels when executing on the target.', 'Windows only supports C(no) as an option.'], 'type': 'bool', 'default': False, 'choices': ['no']}",
}
```

## Examples



## License

TODO

## Author Information
  - ['UNKNOWN']
