# Ansible module: ansible.module_digital_ocean_domain


Create/delete a DNS domain in DigitalOcean

## Description

Create/delete a DNS domain in DigitalOcean.

## Requirements

TODO

## Arguments

``` json
{
    "id": "{'description': ['Numeric, the droplet id you want to operate on.'], 'aliases': ['droplet_id']}",
    "ip": "{'description': ["An 'A' record for '@' ($ORIGIN) will be created with the value 'ip'.  'ip' is an IP version 4 address."]}",
    "name": "{'description': ['String, this is the name of the droplet - must be formatted by hostname rules, or the name of a SSH key, or the name of a domain.']}",
    "oauth_token": "{'description': ['DigitalOcean OAuth token.', 'There are several other environment variables which can be used to provide this value.', "i.e., - 'DO_API_TOKEN', 'DO_API_KEY', 'DO_OAUTH_TOKEN' and 'OAUTH_TOKEN'"], 'required': False, 'aliases': ['api_token']}",
    "state": "{'description': ['Indicate desired state of the target.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "timeout": "{'description': ["The timeout in seconds used for polling DigitalOcean's API."], 'default': 30}",
    "validate_certs": "{'description': ['If set to C(no), the SSL certificates will not be validated.', 'This should only set to C(no) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml

# Create a domain

- digital_ocean_domain:
    state: present
    name: my.digitalocean.domain
    ip: 127.0.0.1

# Create a droplet and a corresponding domain

- digital_ocean:
    state: present
    name: test_droplet
    size_id: 1gb
    region_id: sgp1
    image_id: ubuntu-14-04-x64


  register: test_droplet

- digital_ocean_domain:
    state: present
    name: "{{ test_droplet.droplet.name }}.my.domain"
    ip: "{{ test_droplet.droplet.ip_address }}"


```

## License

TODO

## Author Information
  - ['Michael Gregson (@mgregson)']
