# Ansible module: ansible.module_digital_ocean_tag


Create and remove tag(s) to DigitalOcean resource

## Description

Create and remove tag(s) to DigitalOcean resource.

## Requirements

TODO

## Arguments

``` json
{
    "name": "{'description': ['The name of the tag. The supported characters for names include alphanumeric characters, dashes, and underscores.'], 'required': True}",
    "oauth_token": "{'description': ['DigitalOcean OAuth token.', 'There are several other environment variables which can be used to provide this value.', "i.e., - 'DO_API_TOKEN', 'DO_API_KEY', 'DO_OAUTH_TOKEN' and 'OAUTH_TOKEN'"], 'required': False, 'aliases': ['api_token']}",
    "resource_id": "{'description': ['The ID of the resource to operate on.', 'The data type of resource_id is changed from integer to string, from version 2.5.'], 'aliases': ['droplet_id']}",
    "resource_type": "{'description': ['The type of resource to operate on. Currently, only tagging of droplets is supported.'], 'default': 'droplet', 'choices': ['droplet']}",
    "state": "{'description': ['Whether the tag should be present or absent on the resource.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "timeout": "{'description': ["The timeout in seconds used for polling DigitalOcean's API."], 'default': 30}",
    "validate_certs": "{'description': ['If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

- name: create a tag
  digital_ocean_tag:
    name: production
    state: present

- name: tag a resource; creating the tag if it does not exist
  digital_ocean_tag:
    name: "{{ item }}"
    resource_id: "73333005"
    state: present
  with_items:
    - staging
    - dbserver

- name: untag a resource
  digital_ocean_tag:
    name: staging
    resource_id: "73333005"
    state: absent

# Deleting a tag also untags all the resources that have previously been
# tagged with it
- name: remove a tag
  digital_ocean_tag:
    name: dbserver
    state: absent

```

## License

TODO

## Author Information
  - ['Victor Volle (@kontrafiktion)']
