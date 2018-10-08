# Ansible callback: ansible.callback_cgroup_memory_recap


Profiles maximum memory usage of tasks and full execution using cgroups

## Description

This is an ansible callback plugin that profiles maximum memory usage of ansible and individual tasks, and displays a recap at the end using cgroups

## Requirements

TODO

## Arguments

``` json
{
    "cur_mem_file": "{'required': True, 'description': ['Path to C(memory.usage_in_bytes) file. Example C(/sys/fs/cgroup/memory/ansible_profile/memory.usage_in_bytes)'], 'env': [{'name': 'CGROUP_CUR_MEM_FILE'}], 'ini': [{'section': 'callback_cgroupmemrecap', 'key': 'cur_mem_file'}]}",
    "max_mem_file": "{'required': True, 'description': ['Path to cgroups C(memory.max_usage_in_bytes) file. Example C(/sys/fs/cgroup/memory/ansible_profile/memory.max_usage_in_bytes)'], 'env': [{'name': 'CGROUP_MAX_MEM_FILE'}], 'ini': [{'section': 'callback_cgroupmemrecap', 'key': 'max_mem_file'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['UNKNOWN']
