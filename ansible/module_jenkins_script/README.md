# Ansible module: ansible.module_jenkins_script


Executes a groovy script in the jenkins instance

## Description

The C(jenkins_script) module takes a script plus a dict of values to use within the script and returns the result of the script being run.

## Requirements

TODO

## Arguments

``` json
{
    "args": "{'description': ['A dict of key-value pairs used in formatting the script using string.Template (see https://docs.python.org/2/library/string.html#template-strings).']}",
    "password": "{'description': ['The password to connect to the jenkins server with.']}",
    "script": "{'description': ['The groovy script to be executed. This gets passed as a string Template if args is defined.'], 'required': True}",
    "timeout": "{'description': ['The request timeout in seconds'], 'default': 10, 'version_added': '2.4'}",
    "url": "{'description': ['The jenkins server to execute the script against. The default is a local jenkins instance that is not being proxied through a webserver.'], 'default': 'http://localhost:8080'}",
    "user": "{'description': ['The username to connect to the jenkins server with.']}",
    "validate_certs": "{'description': ['If set to C(no), the SSL certificates will not be validated. This should only set to C(no) used on personally controlled sites using self-signed certificates as it avoids verifying the source site.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Obtaining a list of plugins
  jenkins_script:
    script: 'println(Jenkins.instance.pluginManager.plugins)'
    user: admin
    password: admin

- name: Setting master using a variable to hold a more complicate script
  set_fact:
    setmaster_mode: |
        import jenkins.model.*
        instance = Jenkins.getInstance()
        instance.setMode(${jenkins_mode})
        instance.save()

- name: use the variable as the script
  jenkins_script:
    script: "{{ setmaster_mode }}"
    args:
      jenkins_mode: Node.Mode.EXCLUSIVE

- name: interacting with an untrusted HTTPS connection
  jenkins_script:
    script: "println(Jenkins.instance.pluginManager.plugins)"
    user: admin
    password: admin
    url: https://localhost
    validate_certs: no

```

## License

TODO

## Author Information
  - ['James Hogarth (@hogarthj)']
