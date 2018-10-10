# Ansible module: ansible.module_django_manage


Manages a Django application

## Description

Manages a Django application using the I(manage.py) application frontend to I(django-admin). With the I(virtualenv) parameter, all management commands will be executed by the given I(virtualenv) installation.

## Requirements

TODO

## Arguments

``` json
{
    "app_path": "{'description': ['The path to the root of the Django application where B(manage.py) lives.'], 'required': True}",
    "apps": "{'description': ["A list of space-delimited apps to target. Used by the 'test' command."], 'required': False}",
    "cache_table": "{'description': ["The name of the table used for database-backed caching. Used by the 'createcachetable' command."], 'required': False}",
    "clear": "{'description': ['Clear the existing files before trying to copy or link the original file.', "Used only with the 'collectstatic' command. The C(--noinput) argument will be added automatically."], 'required': False, 'default': False, 'type': 'bool'}",
    "command": "{'choices': ['cleanup', 'collectstatic', 'flush', 'loaddata', 'migrate', 'runfcgi', 'syncdb', 'test', 'validate'], 'description': ['The name of the Django management command to run. Built in commands are cleanup, collectstatic, flush, loaddata, migrate, runfcgi, syncdb, test, and validate.', "Other commands can be entered, but will fail if they're unknown to Django.  Other commands that may prompt for user input should be run with the I(--noinput) flag."], 'required': True}",
    "database": "{'description': ["The database to target. Used by the 'createcachetable', 'flush', 'loaddata', and 'syncdb' commands."], 'required': False}",
    "failfast": "{'description': ["Fail the command immediately if a test fails. Used by the 'test' command."], 'required': False, 'default': False, 'type': 'bool'}",
    "fixtures": "{'description': ["A space-delimited list of fixture file names to load in the database. B(Required) by the 'loaddata' command."], 'required': False}",
    "link": "{'description': ["Will create links to the files instead of copying them, you can only use this parameter with 'collectstatic' command"], 'required': False, 'version_added': '1.3'}",
    "merge": "{'description': ["Will run out-of-order or missing migrations as they are not rollback migrations, you can only use this parameter with 'migrate' command"], 'required': False, 'version_added': '1.3'}",
    "pythonpath": "{'description': ['A directory to add to the Python path. Typically used to include the settings module if it is located external to the application directory.'], 'required': False}",
    "settings": "{'description': ["The Python path to the application's settings module, such as 'myapp.settings'."], 'required': False}",
    "skip": "{'description': ['Will skip over out-of-order missing migrations, you can only use this parameter with I(migrate)'], 'required': False, 'version_added': '1.3'}",
    "virtualenv": "{'description': ['An optional path to a I(virtualenv) installation to use while running the manage application.'], 'aliases': ['virtualenv']}",
}
```

## Examples


``` yaml

# Run cleanup on the application installed in 'django_dir'.
- django_manage:
    command: cleanup
    app_path: "{{ django_dir }}"

# Load the initial_data fixture into the application
- django_manage:
    command: loaddata
    app_path: "{{ django_dir }}"
    fixtures: "{{ initial_data }}"

# Run syncdb on the application
- django_manage:
    command: syncdb
    app_path: "{{ django_dir }}"
    settings: "{{ settings_app_name }}"
    pythonpath: "{{ settings_dir }}"
    virtualenv: "{{ virtualenv_dir }}"

# Run the SmokeTest test case from the main app. Useful for testing deploys.
- django_manage:
    command: test
    app_path: "{{ django_dir }}"
    apps: main.SmokeTest

# Create an initial superuser.
- django_manage:
    command: "createsuperuser --noinput --username=admin --email=admin@example.com"
    app_path: "{{ django_dir }}"

```

## License

TODO

## Author Information
  - ['Scott Anderson (@tastychutney)']
