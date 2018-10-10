# Ansible module: ansible.module_nuage_vspk


Manage Nuage VSP environments

## Description

Manage or find Nuage VSP entities, this includes create, update, delete, assign, unassign and find, with all supported properties.

## Requirements

TODO

## Arguments

``` json
{
    "auth": "{'description': ['Dict with the authentication information required to connect to a Nuage VSP environment.', 'Requires a I(api_username) parameter (example csproot).', 'Requires either a I(api_password) parameter (example csproot) or a I(api_certificate) and I(api_key) parameters, which point to the certificate and key files for certificate based authentication.', 'Requires a I(api_enterprise) parameter (example csp).', 'Requires a I(api_url) parameter (example https://10.0.0.10:8443).', 'Requires a I(api_version) parameter (example v4_0).'], 'required': True}",
    "children": "{'description': ['Can be used to specify a set of child entities.', 'A mandatory property of each child is the I(type).', 'Supported optional properties of each child are I(id), I(properties) and I(match_filter).', 'The function of each of these properties is the same as in the general task definition.', 'This can be used recursively', 'Only useable in case I(state=present).']}",
    "command": "{'description': ['Specifies a command to be executed.', 'With I(command=find), if I(parent_id) and I(parent_type) are defined, it will only search within the parent. Otherwise, if allowed, will search in the root object.', 'With I(command=find), if I(id) is specified, it will only return the single entity matching the id.', 'With I(command=find), otherwise, if I(match_filter) is define, it will use that filter to search.', 'With I(command=find), otherwise, if I(properties) are defined, it will do an AND search using all properties.', 'With I(command=change_password), a password of a user can be changed. Warning - In case the password is the same as the existing, it will throw an error.', 'With I(command=wait_for_job), the module will wait for a job to either have a status of SUCCESS or ERROR. In case an ERROR status is found, the module will exit with an error.', 'With I(command=wait_for_job), the job will always be returned, even if the state is ERROR situation.', 'Either I(state) or I(command) needs to be defined, both can not be defined at the same time.'], 'choices': ['find', 'change_password', 'wait_for_job', 'get_csp_enterprise']}",
    "id": "{'description': ['The ID of the entity you want to work on.', 'In combination with I(command=find), it will only return the single entity.', 'In combination with I(state), it will either update or delete this entity.', 'Will take precedence over I(match_filter) and I(properties) whenever an entity needs to be found.']}",
    "match_filter": "{'description': ['A filter used when looking (both in I(command) and I(state) for entities, in the format the Nuage VSP API expects.', 'If I(match_filter) is defined, it will take precedence over the I(properties), but not on the I(id)']}",
    "parent_id": "{'description': ['The ID of the parent of the entity you want to work on.', 'When I(state) is specified, the entity will be gathered from this parent, if it exists, unless an I(id) is specified.', 'When I(command=find) is specified, the entity will be searched for in this parent, unless an I(id) is specified.', 'If specified, I(parent_type) also needs to be specified.']}",
    "parent_type": "{'description': ['The type of parent the ID is specified for (example Enterprise).', 'This should match the objects CamelCase class name in VSPK-Python.', 'This Class name can be found on U(https://nuagenetworks.github.io/vspkdoc/index.html).', 'If specified, I(parent_id) also needs to be specified.']}",
    "properties": "{'description': ['Properties are the key, value pairs of the different properties an entity has.', 'If no I(id) and no I(match_filter) is specified, these are used to find or determine if the entity exists.']}",
    "state": "{'description': ['Specifies the desired state of the entity.', 'If I(state=present), in case the entity already exists, will update the entity if it is needed.', 'If I(state=present), in case the relationship with the parent is a member relationship, will assign the entity as a member of the parent.', 'If I(state=absent), in case the relationship with the parent is a member relationship, will unassign the entity as a member of the parent.', 'Either I(state) or I(command) needs to be defined, both can not be defined at the same time.'], 'choices': ['present', 'absent']}",
    "type": "{'description': ['The type of entity you want to work on (example Enterprise).', 'This should match the objects CamelCase class name in VSPK-Python.', 'This Class name can be found on U(https://nuagenetworks.github.io/vspkdoc/index.html).'], 'required': True}",
}
```

## Examples


``` yaml

# This can be executed as a single role, with the following vars
# vars:
#   auth:
#     api_username: csproot
#     api_password: csproot
#     api_enterprise: csp
#     api_url: https://10.0.0.10:8443
#     api_version: v5_0
#   enterprise_name: Ansible-Enterprise
#   enterprise_new_name: Ansible-Updated-Enterprise
#
# or, for certificate based authentication
# vars:
#   auth:
#     api_username: csproot
#     api_certificate: /path/to/user-certificate.pem
#     api_key: /path/to/user-Key.pem
#     api_enterprise: csp
#     api_url: https://10.0.0.10:8443
#     api_version: v5_0
#   enterprise_name: Ansible-Enterprise
#   enterprise_new_name: Ansible-Updated-Enterprise

# Creating a new enterprise
- name: Create Enterprise
  connection: local
  nuage_vspk:
    auth: "{{ nuage_auth }}"
    type: Enterprise
    state: present
    properties:
      name: "{{ enterprise_name }}-basic"
  register: nuage_enterprise

# Checking if an Enterprise with the new name already exists
- name: Check if an Enterprise exists with the new name
  connection: local
  nuage_vspk:
    auth: "{{ nuage_auth }}"
    type: Enterprise
    command: find
    properties:
      name: "{{ enterprise_new_name }}-basic"
  ignore_errors: yes
  register: nuage_check_enterprise

# Updating an enterprise's name
- name: Update Enterprise name
  connection: local
  nuage_vspk:
    auth: "{{ nuage_auth }}"
    type: Enterprise
    id: "{{ nuage_enterprise.id }}"
    state: present
    properties:
      name: "{{ enterprise_new_name }}-basic"
  when: nuage_check_enterprise is failed

# Creating a User in an Enterprise
- name: Create admin user
  connection: local
  nuage_vspk:
    auth: "{{ nuage_auth }}"
    type: User
    parent_id: "{{ nuage_enterprise.id }}"
    parent_type: Enterprise
    state: present
    match_filter: "userName == 'ansible-admin'"
    properties:
      email: "ansible@localhost.local"
      first_name: "Ansible"
      last_name: "Admin"
      password: "ansible-password"
      user_name: "ansible-admin"
  register: nuage_user

# Updating password for User
- name: Update admin password
  connection: local
  nuage_vspk:
    auth: "{{ nuage_auth }}"
    type: User
    id: "{{ nuage_user.id }}"
    command: change_password
    properties:
      password: "ansible-new-password"
  ignore_errors: yes

# Finding a group in an enterprise
- name: Find Administrators group in Enterprise
  connection: local
  nuage_vspk:
    auth: "{{ nuage_auth }}"
    type: Group
    parent_id: "{{ nuage_enterprise.id }}"
    parent_type: Enterprise
    command: find
    properties:
      name: "Administrators"
  register: nuage_group

# Assign the user to the group
- name: Assign admin user to administrators
  connection: local
  nuage_vspk:
    auth: "{{ nuage_auth }}"
    type: User
    id: "{{ nuage_user.id }}"
    parent_id: "{{ nuage_group.id }}"
    parent_type: Group
    state: present

# Creating multiple DomainTemplates
- name: Create multiple DomainTemplates
  connection: local
  nuage_vspk:
    auth: "{{ nuage_auth }}"
    type: DomainTemplate
    parent_id: "{{ nuage_enterprise.id }}"
    parent_type: Enterprise
    state: present
    properties:
      name: "{{ item }}"
      description: "Created by Ansible"
  with_items:
    - "Template-1"
    - "Template-2"

# Finding all DomainTemplates
- name: Fetching all DomainTemplates
  connection: local
  nuage_vspk:
    auth: "{{ nuage_auth }}"
    type: DomainTemplate
    parent_id: "{{ nuage_enterprise.id }}"
    parent_type: Enterprise
    command: find
  register: nuage_domain_templates

# Deleting all DomainTemplates
- name: Deleting all found DomainTemplates
  connection: local
  nuage_vspk:
    auth: "{{ nuage_auth }}"
    type: DomainTemplate
    state: absent
    id: "{{ item.ID }}"
  with_items: "{{ nuage_domain_templates.entities }}"
  when: nuage_domain_templates.entities is defined

# Unassign user from group
- name: Unassign admin user to administrators
  connection: local
  nuage_vspk:
    auth: "{{ nuage_auth }}"
    type: User
    id: "{{ nuage_user.id }}"
    parent_id: "{{ nuage_group.id }}"
    parent_type: Group
    state: absent

# Deleting an enterprise
- name: Delete Enterprise
  connection: local
  nuage_vspk:
    auth: "{{ nuage_auth }}"
    type: Enterprise
    id: "{{ nuage_enterprise.id }}"
    state: absent

# Setup an enterprise with Children
- name: Setup Enterprise and domain structure
  connection: local
  nuage_vspk:
    auth: "{{ nuage_auth }}"
    type: Enterprise
    state: present
    properties:
      name: "Child-based-Enterprise"
    children:
    - type: L2DomainTemplate
      properties:
        name: "Unmanaged-Template"
      children:
      - type: EgressACLTemplate
        match_filter: "name == 'Allow All'"
        properties:
          name: "Allow All"
          active: true
          default_allow_ip: true
          default_allow_non_ip: true
          default_install_acl_implicit_rules: true
          description: "Created by Ansible"
          priority_type: "TOP"
      - type: IngressACLTemplate
        match_filter: "name == 'Allow All'"
        properties:
          name: "Allow All"
          active: true
          default_allow_ip: true
          default_allow_non_ip: true
          description: "Created by Ansible"
          priority_type: "TOP"

```

## License

TODO

## Author Information
  - ['Philippe Dellaert (@pdellaert)']
