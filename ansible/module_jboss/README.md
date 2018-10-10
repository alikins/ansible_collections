# Ansible module: ansible.module_jboss


deploy applications to JBoss

## Description

Deploy applications to JBoss standalone using the filesystem

## Requirements

TODO

## Arguments

``` json
{
    "deploy_path": "{'required': False, 'default': '/var/lib/jbossas/standalone/deployments', 'description': ['The location in the filesystem where the deployment scanner listens']}",
    "deployment": "{'required': True, 'description': ['The name of the deployment']}",
    "src": "{'required': False, 'description': ['The remote path of the application ear or war to deploy']}",
    "state": "{'required': False, 'choices': ['present', 'absent'], 'default': 'present', 'description': ['Whether the application should be deployed or undeployed']}",
}
```

## Examples


``` yaml

# Deploy a hello world application
- jboss:
    src: /tmp/hello-1.0-SNAPSHOT.war
    deployment: hello.war
    state: present

# Update the hello world application
- jboss:
    src: /tmp/hello-1.1-SNAPSHOT.war
    deployment: hello.war
    state: present

# Undeploy the hello world application
- jboss:
    deployment: hello.war
    state: absent

```

## License

TODO

## Author Information
  - ['Jeroen Hoekx (@jhoekx)']
