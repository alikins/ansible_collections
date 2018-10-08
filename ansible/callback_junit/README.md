# Ansible callback: ansible.callback_junit


write playbook output to a JUnit file

## Description

This callback writes playbook output to a JUnit formatted XML file.
Tasks show up in the report as follows: 'ok': pass 'failed' with 'EXPECTED FAILURE' in the task name: pass 'failed' with 'TOGGLE RESULT' in the task name: pass 'ok' with 'TOGGLE RESULT' in the task name: failure 'failed' due to an exception: error 'failed' for other reasons: failure 'skipped': skipped

## Requirements

TODO

## Arguments

``` json
{
    "fail_on_change": "{'name': 'JUnit fail on change', 'default': False, 'description': ['Consider any tasks reporting "changed" as a junit test failure'], 'env': [{'name': 'JUNIT_FAIL_ON_CHANGE'}]}",
    "fail_on_ignore": "{'name': 'JUnit fail on ignore', 'default': False, 'description': ['Consider failed tasks as a junit test failure even if ignore_on_error is set'], 'env': [{'name': 'JUNIT_FAIL_ON_IGNORE'}]}",
    "include_setup_tasks_in_report": "{'name': 'JUnit include setup tasks in report', 'default': True, 'description': ['Should the setup tasks be included in the final report'], 'env': [{'name': 'JUNIT_INCLUDE_SETUP_TASKS_IN_REPORT'}]}",
    "output_dir": "{'name': 'JUnit output dir', 'default': '~/.ansible.log', 'description': ['Directory to write XML files to.'], 'env': [{'name': 'JUNIT_OUTPUT_DIR'}]}",
    "task_class": "{'name': 'JUnit Task class', 'default': False, 'description': ['Configure the output to be one class per yaml file'], 'env': [{'name': 'JUNIT_TASK_CLASS'}]}",
    "task_relative_path": "{'name': 'JUnit Task relative path', 'default': 'none', 'description': ['Configure the output to use relative paths to given directory'], 'version_added': '2.8', 'env': [{'name': 'JUNIT_TASK_RELATIVE_PATH'}]}",
}
```

## Examples



## License

TODO

## Author Information
  - ['UNKNOWN']
