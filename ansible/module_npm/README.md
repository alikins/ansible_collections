# Ansible module: ansible.module_npm


Manage node.js packages with npm

## Description

Manage node.js packages with Node Package Manager (npm)

## Requirements

TODO

## Arguments

``` json
{
    "executable": "{'description': ['The executable location for npm.', 'This is useful if you are using a version manager, such as nvm'], 'required': False}",
    "global": "{'description': ['Install the node.js library globally'], 'required': False, 'default': False, 'type': 'bool'}",
    "ignore_scripts": "{'description': ['Use the C(--ignore-scripts) flag when installing.'], 'required': False, 'type': 'bool', 'default': False, 'version_added': '1.8'}",
    "name": "{'description': ['The name of a node.js library to install'], 'required': False}",
    "path": "{'description': ['The base path where to install the node.js libraries'], 'required': False}",
    "production": "{'description': ['Install dependencies in production mode, excluding devDependencies'], 'required': False, 'type': 'bool', 'default': False}",
    "registry": "{'description': ['The registry to install modules from.'], 'required': False, 'version_added': '1.6'}",
    "state": "{'description': ['The state of the node.js library'], 'required': False, 'default': 'present', 'choices': ['present', 'absent', 'latest']}",
    "version": "{'description': ['The version to be installed'], 'required': False}",
}
```

## Examples


``` yaml

- name: Install "coffee-script" node.js package.
  npm:
    name: coffee-script
    path: /app/location

- name: Install "coffee-script" node.js package on version 1.6.1.
  npm:
    name: coffee-script
    version: '1.6.1'
    path: /app/location

- name: Install "coffee-script" node.js package globally.
  npm:
    name: coffee-script
    global: yes

- name: Remove the globally package "coffee-script".
  npm:
    name: coffee-script
    global: yes
    state: absent

- name: Install "coffee-script" node.js package from custom registry.
  npm:
    name: coffee-script
    registry: 'http://registry.mysite.com'

- name: Install packages based on package.json.
  npm:
    path: /app/location

- name: Update packages based on package.json to their latest version.
  npm:
    path: /app/location
    state: latest

- name: Install packages based on package.json using the npm installed with nvm v0.10.1.
  npm:
    path: /app/location
    executable: /opt/nvm/v0.10.1/bin/npm
    state: present

```

## License

TODO

## Author Information
  - ['Chris Hoffman (@chrishoffman)']
