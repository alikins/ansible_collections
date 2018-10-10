# Ansible module: ansible.module_yarn


Manage node.js packages with Yarn

## Description

Manage node.js packages with the Yarn package manager (https://yarnpkg.com/)

## Requirements

TODO

## Arguments

``` json
{
    "executable": "{'description': ['The executable location for yarn.'], 'required': False}",
    "global": "{'description': ['Install the node.js library globally'], 'required': False, 'default': False, 'type': 'bool'}",
    "ignore_scripts": "{'description': ['Use the --ignore-scripts flag when installing.'], 'required': False, 'type': 'bool', 'default': False}",
    "name": "{'description': ['The name of a node.js library to install', 'If omitted all packages in package.json are installed.'], 'required': False}",
    "path": "{'description': ['The base path where Node.js libraries will be installed.', 'This is where the node_modules folder lives.'], 'required': False}",
    "production": "{'description': ['Install dependencies in production mode.', 'Yarn will ignore any dependencies under devDependencies in package.json'], 'required': False, 'type': 'bool', 'default': False}",
    "registry": "{'description': ['The registry to install modules from.'], 'required': False}",
    "state": "{'description': ['Installation state of the named node.js library', 'If absent is selected, a name option must be provided'], 'required': False, 'default': 'present', 'choices': ['present', 'absent', 'latest']}",
    "version": "{'description': ['The version of the library to be installed.', 'Must be in semver format. If "latest" is desired, use "state" arg instead'], 'required': False}",
}
```

## Examples


``` yaml

- name: Install "imagemin" node.js package.
  yarn:
    name: imagemin
    path: /app/location

- name: Install "imagemin" node.js package on version 5.3.1
  yarn:
    name: imagemin
    version: '5.3.1'
    path: /app/location

- name: Install "imagemin" node.js package globally.
  yarn:
    name: imagemin
    global: yes

- name: Remove the globally-installed package "imagemin".
  yarn:
    name: imagemin
    global: yes
    state: absent

- name: Install "imagemin" node.js package from custom registry.
  yarn:
    name: imagemin
    registry: 'http://registry.mysite.com'

- name: Install packages based on package.json.
  yarn:
    path: /app/location

- name: Update all packages in package.json to their latest version.
  yarn:
    path: /app/location
    state: latest

```

## License

TODO

## Author Information
  - ['David Gunter (@verkaufer)', 'Chris Hoffman (@chrishoffman, creator of NPM Ansible module)']
  - ['David Gunter (@verkaufer)', 'Chris Hoffman (@chrishoffman, creator of NPM Ansible module)']
