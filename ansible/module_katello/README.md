# Ansible module: ansible.module_katello


Manage Katello Resources

## Description

Allows the management of Katello resources inside your Foreman server.

## Requirements

TODO

## Arguments

``` json
{
    "action": "{'description': ['action associated to the entity resource to set or edit in dictionary format.', 'Possible Action in relation to Entitys.', 'sync (available when entity=product or entity=repository)', 'publish (available when entity=content_view)', 'promote (available when entity=content_view)'], 'choices': ['sync', 'publish', 'promote'], 'required': False}",
    "entity": "{'description': ['The Foreman resource that the action will be performed on (e.g. organization, host).'], 'choices': ['repository', 'manifest', 'repository_set', 'sync_plan', 'content_view', 'lifecycle_environment', 'activation_key'], 'required': True}",
    "params": "{'description': ['Parameters associated to the entity resource and action, to set or edit in dictionary format.', 'Each choice may be only available with specific entitys and actions.', 'Possible Choices are in the format of param_name ([entry,action,action,...],[entity,..],...).', 'The action "None" means no action specified.', 'Possible Params in relation to entity and action.', 'name ([product,sync,None], [repository,sync], [repository_set,None], [sync_plan,None],', '[content_view,promote,publish,None], [lifecycle_environment,None], [activation_key,None])', 'organization ([product,sync,None] ,[repository,sync,None], [repository_set,None], [sync_plan,None], ', '[content_view,promote,publish,None], [lifecycle_environment,None], [activation_key,None])', 'content ([manifest,None])', 'product ([repository,sync,None], [repository_set,None], [sync_plan,None])', 'basearch ([repository_set,None])', 'releaserver ([repository_set,None])', 'sync_date ([sync_plan,None])', 'interval ([sync_plan,None])', 'repositories ([content_view,None])', 'from_environment ([content_view,promote])', 'to_environment([content_view,promote])', 'prior ([lifecycle_environment,None])', 'content_view ([activation_key,None])', 'lifecycle_environment ([activation_key,None])'], 'required': True}",
    "password": "{'description': ['Password for user accessing Foreman server.'], 'required': True}",
    "server_url": "{'description': ['URL of Foreman server.'], 'required': True}",
    "task_timeout": "{'description': ['The timeout in seconds to wait for the started Foreman action to finish.', 'If the timeout is reached and the Foreman action did not complete, the ansible task fails. However the foreman action does not get canceled.'], 'default': 1000, 'version_added': '2.7', 'required': False}",
    "username": "{'description': ['Username on Foreman server.'], 'required': True}",
    "verify_ssl": "{'description': ['verify the ssl/https connection (e.g for a valid certificate)'], 'default': False, 'type': 'bool', 'required': False}",
}
```

## Examples


``` yaml

---
# Simple Example:

- name: Create Product
  katello:
      username: admin
      password: admin
      server_url: https://fakeserver.com
      entity: product
      params:
        name: Centos 7
  delegate_to: localhost

# Abstraction Example:
# katello.yml
---
- name: "{{ name }}"
  katello:
      username: admin
      password: admin
      server_url: https://fakeserver.com
      entity: "{{ entity }}"
      params: "{{ params }}"
  delegate_to: localhost

# tasks.yml
---
- include: katello.yml
  vars:
    name: Create Dev Environment
    entity: lifecycle_environment
    params:
      name: Dev
      prior: Library
      organization: Default Organization

- include: katello.yml
  vars:
    name: Create Centos Product
    entity: product
    params:
      name: Centos 7
      organization: Default Organization

- include: katello.yml
  vars:
    name: Create 7.2 Repository
    entity: repository
    params:
      name: Centos 7.2
      product: Centos 7
      organization: Default Organization
      content_type: yum
      url: http://mirror.centos.org/centos/7/os/x86_64/

- include: katello.yml
  vars:
      name: Create Centos 7 View
      entity: content_view
      params:
        name: Centos 7 View
        organization: Default Organization
        repositories:
          - name: Centos 7.2
            product: Centos 7

- include: katello.yml
  vars:
      name: Enable RHEL Product
      entity: repository_set
      params:
        name: Red Hat Enterprise Linux 7 Server (RPMs)
        product: Red Hat Enterprise Linux Server
        organization: Default Organization
        basearch: x86_64
        releasever: 7

- include: katello.yml
  vars:
      name: Promote Contentview Environment with longer timout
      task_timeout: 10800
      entity: content_view
      action: promote
      params:
        name: MyContentView
        organization: MyOrganisation
        from_environment: Testing
        to_environment: Production

# Best Practices

# In Foreman, things can be done in paralell.
# When a conflicting action is already running,
# the task will fail instantly instead of waiting for the already running action to complete.
# So you sould use a "until success" loop to catch this.

- name: Promote Contentview Environment with increased Timeout
  katello:
  username: ansibleuser
  password: supersecret
  task_timeout: 10800
  entity: content_view
  action: promote
  params:
    name: MyContentView
    organization: MyOrganisation
    from_environment: Testing
    to_environment: Production
  register: task_result
  until: task_result is success
  retries: 9
  delay: 120


```

## License

TODO

## Author Information
  - ['Eric D Helms (@ehelms)']
