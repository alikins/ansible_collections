# Ansible module: ansible.module_sendgrid


Sends an email with the SendGrid API

## Description

Sends an email with a SendGrid account through their API, not through the SMTP service.

## Requirements

TODO

## Arguments

``` json
{
    "api_key": "{'description': ['sendgrid API key to use instead of username/password'], 'version_added': 2.2}",
    "attachments": "{'description': ['a list of relative or explicit paths of files you want to attach (7MB limit as per SendGrid docs)'], 'version_added': 2.2}",
    "bcc": "{'description': ['a list of email addresses to bcc'], 'version_added': 2.2}",
    "cc": "{'description': ['a list of email addresses to cc'], 'version_added': 2.2}",
    "from_address": "{'description': ['the address in the "from" field for the email'], 'required': True}",
    "from_name": "{'description': ["the name you want to appear in the from field, i.e 'John Doe'"], 'version_added': 2.2}",
    "headers": "{'description': ['a dict to pass on as headers'], 'version_added': 2.2}",
    "html_body": "{'description': ['whether the body is html content that should be rendered'], 'version_added': 2.2, 'type': 'bool', 'default': False}",
    "password": "{'description': ['password that corresponds to the username', 'Since 2.2 it is only required if api_key is not supplied.']}",
    "subject": "{'description': ['the desired subject for the email'], 'required': True}",
    "to_addresses": "{'description': ['a list with one or more recipient email addresses'], 'required': True}",
    "username": "{'description': ['username for logging into the SendGrid account.', 'Since 2.2 it is only required if api_key is not supplied.']}",
}
```

## Examples


``` yaml

# send an email to a single recipient that the deployment was successful
- sendgrid:
    username: "{{ sendgrid_username }}"
    password: "{{ sendgrid_password }}"
    from_address: "ansible@mycompany.com"
    to_addresses:
      - "ops@mycompany.com"
    subject: "Deployment success."
    body: "The most recent Ansible deployment was successful."
  delegate_to: localhost

# send an email to more than one recipient that the build failed
- sendgrid:
      username: "{{ sendgrid_username }}"
      password: "{{ sendgrid_password }}"
      from_address: "build@mycompany.com"
      to_addresses:
        - "ops@mycompany.com"
        - "devteam@mycompany.com"
      subject: "Build failure!."
      body: "Unable to pull source repository from Git server."
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Matt Makai (@makaimc)']
