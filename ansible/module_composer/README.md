# Ansible module: ansible.module_composer


Dependency Manager for PHP

## Description

Composer is a tool for dependency management in PHP. It allows you to declare the dependent libraries your project needs and it will install them in your project for you.


## Requirements

TODO

## Arguments

``` json
{
    "apcu_autoloader": "{'version_added': '2.7', 'description': ['Uses APCu to cache found/not-found classes'], 'default': False, 'type': 'bool', 'aliases': ['apcu-autoloader']}",
    "arguments": "{'version_added': '2.0', 'description': ['Composer arguments like required package, version and so on.']}",
    "classmap_authoritative": "{'version_added': '2.7', 'description': ['Autoload classes from classmap only.', 'Implicitely enable optimize_autoloader.', 'Recommended especially for production, but can take a bit of time to run.'], 'default': False, 'type': 'bool', 'aliases': ['classmap-authoritative']}",
    "command": "{'version_added': '1.8', 'description': ['Composer command like "install", "update" and so on.'], 'default': 'install'}",
    "executable": "{'version_added': '2.4', 'description': ['Path to PHP Executable on the remote host, if PHP is not in PATH.'], 'aliases': ['php_path']}",
    "global_command": "{'version_added': '2.4', 'description': ['Runs the specified command globally.'], 'type': 'bool', 'default': False, 'aliases': ['global-command']}",
    "ignore_platform_reqs": "{'version_added': '2.0', 'description': ['Ignore php, hhvm, lib-* and ext-* requirements and force the installation even if the local machine does not fulfill these.'], 'default': False, 'type': 'bool', 'aliases': ['ignore-platform-reqs']}",
    "no_dev": "{'description': ['Disables installation of require-dev packages (see --no-dev).'], 'default': True, 'type': 'bool', 'aliases': ['no-dev']}",
    "no_plugins": "{'description': ['Disables all plugins ( see --no-plugins ).'], 'default': False, 'type': 'bool', 'aliases': ['no-plugins']}",
    "no_scripts": "{'description': ['Skips the execution of all scripts defined in composer.json (see --no-scripts).'], 'default': False, 'type': 'bool', 'aliases': ['no-scripts']}",
    "optimize_autoloader": "{'description': ['Optimize autoloader during autoloader dump (see --optimize-autoloader).', 'Convert PSR-0/4 autoloading to classmap to get a faster autoloader.', 'Recommended especially for production, but can take a bit of time to run.'], 'default': True, 'type': 'bool', 'aliases': ['optimize-autoloader']}",
    "prefer_dist": "{'description': ['Forces installation from package dist even for dev versions (see --prefer-dist).'], 'default': False, 'type': 'bool', 'aliases': ['prefer-dist']}",
    "prefer_source": "{'description': ['Forces installation from package sources when possible (see --prefer-source).'], 'default': False, 'type': 'bool', 'aliases': ['prefer-source']}",
    "working_dir": "{'description': ['Directory of your project (see --working-dir). This is required when the command is not run globally.', 'Will be ignored if C(global_command=true).'], 'aliases': ['working-dir']}",
}
```

## Examples


``` yaml

# Downloads and installs all the libs and dependencies outlined in the /path/to/project/composer.lock
- composer:
    command: install
    working_dir: /path/to/project

- composer:
    command: require
    arguments: my/package
    working_dir: /path/to/project

# Clone project and install with all dependencies
- composer:
    command: create-project
    arguments: package/package /path/to/project ~1.0
    working_dir: /path/to/project
    prefer_dist: yes

# Installs package globally
- composer:
    command: require
    global_command: yes
    arguments: my/package

```

## License

TODO

## Author Information
  - ['Dimitrios Tydeas Mengidis (@dmtrs)', 'René Moser (@resmo)']
  - ['Dimitrios Tydeas Mengidis (@dmtrs)', 'René Moser (@resmo)']
