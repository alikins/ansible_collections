# Ansible module: ansible.module_cron


Manage cron.d and crontab entries

## Description

Use this module to manage crontab and environment variables entries. This module allows you to create environment variables and named crontab entries, update, or delete them.
When crontab jobs are managed: the module includes one line with the description of the crontab entry C("#Ansible: <name>") corresponding to the "name" passed to the module, which is used by future ansible/module calls to find/check the state. The "name" parameter should be unique, and changing the "name" value will result in a new cron task being created (or a different one being removed).
When environment variables are managed: no comment line is added, but, when the module needs to find/check the state, it uses the "name" parameter to find the environment variable definition line.
When using symbols such as %, they must be properly escaped.

## Requirements

TODO

## Arguments

``` json
{
    "backup": "{'description': ['If set, create a backup of the crontab before it is modified. The location of the backup is returned in the C(backup_file) variable by this module.'], 'type': 'bool', 'default': False}",
    "cron_file": "{'description': ["If specified, uses this file instead of an individual user's crontab. If this is a relative path, it is interpreted with respect to /etc/cron.d. (If it is absolute, it will typically be /etc/crontab). Many linux distros expect (and some require) the filename portion to consist solely of upper- and lower-case letters, digits, underscores, and hyphens. To use the C(cron_file) parameter you must specify the C(user) as well."]}",
    "day": "{'description': ['Day of the month the job should run ( 1-31, *, */2, etc )'], 'default': '*', 'aliases': ['dom']}",
    "disabled": "{'description': ['If the job should be disabled (commented out) in the crontab.', 'Only has effect if C(state=present).'], 'type': 'bool', 'default': False, 'version_added': '2.0'}",
    "env": "{'description': ['If set, manages a crontab\'s environment variable. New variables are added on top of crontab. "name" and "value" parameters are the name and the value of environment variable.'], 'type': 'bool', 'default': False, 'version_added': '2.1'}",
    "hour": "{'description': ['Hour when the job should run ( 0-23, *, */2, etc )'], 'default': '*'}",
    "insertafter": "{'description': ['Used with C(state=present) and C(env). If specified, the environment variable will be inserted after the declaration of specified environment variable.'], 'version_added': '2.1'}",
    "insertbefore": "{'description': ['Used with C(state=present) and C(env). If specified, the environment variable will be inserted before the declaration of specified environment variable.'], 'version_added': '2.1'}",
    "job": "{'description': ['The command to execute or, if env is set, the value of environment variable. The command should not contain line breaks. Required if state=present.'], 'aliases': ['value']}",
    "minute": "{'description': ['Minute when the job should run ( 0-59, *, */2, etc )'], 'default': '*'}",
    "month": "{'description': ['Month of the year the job should run ( 1-12, *, */2, etc )'], 'default': '*'}",
    "name": "{'description': ['Description of a crontab entry or, if env is set, the name of environment variable. Required if state=absent. Note that if name is not set and state=present, then a new crontab entry will always be created, regardless of existing ones.']}",
    "reboot": "{'description': ['If the job should be run at reboot. This option is deprecated. Users should use special_time.'], 'type': 'bool', 'default': False}",
    "special_time": "{'description': ['Special time specification nickname.'], 'choices': ['reboot', 'yearly', 'annually', 'monthly', 'weekly', 'daily', 'hourly'], 'version_added': '1.3'}",
    "state": "{'description': ['Whether to ensure the job or environment variable is present or absent.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "user": "{'description': ['The specific user whose crontab should be modified.'], 'default': 'root'}",
    "weekday": "{'description': ['Day of the week that the job should run ( 0-6 for Sunday-Saturday, *, etc )'], 'default': '*', 'aliases': ['dow']}",
}
```

## Examples


``` yaml

- name: Ensure a job that runs at 2 and 5 exists. Creates an entry like "0 5,2 * * ls -alh > /dev/null"
  cron:
    name: "check dirs"
    minute: "0"
    hour: "5,2"
    job: "ls -alh > /dev/null"

- name: 'Ensure an old job is no longer present. Removes any job that is prefixed by "#Ansible: an old job" from the crontab'
  cron:
    name: "an old job"
    state: absent

- name: Creates an entry like "@reboot /some/job.sh"
  cron:
    name: "a job for reboot"
    special_time: reboot
    job: "/some/job.sh"

- name: Creates an entry like "PATH=/opt/bin" on top of crontab
  cron:
    name: PATH
    env: yes
    job: /opt/bin

- name: Creates an entry like "APP_HOME=/srv/app" and insert it after PATH declaration
  cron:
    name: APP_HOME
    env: yes
    job: /srv/app
    insertafter: PATH

- name: Creates a cron file under /etc/cron.d
  cron:
    name: yum autoupdate
    weekday: 2
    minute: 0
    hour: 12
    user: root
    job: "YUMINTERACTIVE=0 /usr/sbin/yum-autoupdate"
    cron_file: ansible_yum-autoupdate

- name: Removes a cron file from under /etc/cron.d
  cron:
    name: "yum autoupdate"
    cron_file: ansible_yum-autoupdate
    state: absent

- name: Removes "APP_HOME" environment variable from crontab
  cron:
    name: APP_HOME
    env: yes
    state: absent

```

## License

TODO

## Author Information
  - ['Dane Summers (@dsummersl)', 'Mike Grozak', 'Patrick Callahan', 'Evan Kaufman (@EvanK)', 'Luca Berruti (@lberruti)']
  - ['Dane Summers (@dsummersl)', 'Mike Grozak', 'Patrick Callahan', 'Evan Kaufman (@EvanK)', 'Luca Berruti (@lberruti)']
  - ['Dane Summers (@dsummersl)', 'Mike Grozak', 'Patrick Callahan', 'Evan Kaufman (@EvanK)', 'Luca Berruti (@lberruti)']
  - ['Dane Summers (@dsummersl)', 'Mike Grozak', 'Patrick Callahan', 'Evan Kaufman (@EvanK)', 'Luca Berruti (@lberruti)']
  - ['Dane Summers (@dsummersl)', 'Mike Grozak', 'Patrick Callahan', 'Evan Kaufman (@EvanK)', 'Luca Berruti (@lberruti)']
