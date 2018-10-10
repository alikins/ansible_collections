# Ansible module: ansible.module_mail


Send an email

## Description

This module is useful for sending emails from playbooks.
One may wonder why automate sending emails?  In complex environments there are from time to time processes that cannot be automated, either because you lack the authority to make it so, or because not everyone agrees to a common approach.
If you cannot automate a specific step, but the step is non-blocking, sending out an email to the responsible party to make them perform their part of the bargain is an elegant way to put the responsibility in someone else's lap.
Of course sending out a mail can be equally useful as a way to notify one or more people in a team that a specific action has been (successfully) taken.

## Requirements

TODO

## Arguments

``` json
{
    "attach": "{'description': ['A list of pathnames of files to attach to the message.', 'Attached files will have their content-type set to C(application/octet-stream).'], 'type': 'list', 'default': []}",
    "bcc": "{'description': ["The email-address(es) the mail is being 'blind' copied to.", 'This is a list, which may contain address and phrase portions.'], 'type': 'list'}",
    "body": "{'description': ['The body of the email being sent.'], 'type': 'str', 'default': '$subject'}",
    "cc": "{'description': ['The email-address(es) the mail is being copied to.', 'This is a list, which may contain address and phrase portions.'], 'type': 'list'}",
    "charset": "{'description': ['The character set of email being sent.'], 'type': 'str', 'default': 'utf-8'}",
    "from": "{'description': ['The email-address the mail is sent from. May contain address and phrase.'], 'type': 'str', 'default': 'root'}",
    "headers": "{'description': ['A list of headers which should be added to the message.', 'Each individual header is specified as C(header=value) (see example below).'], 'type': 'list', 'default': []}",
    "host": "{'description': ['The mail server.'], 'type': 'str', 'default': 'localhost'}",
    "password": "{'description': ['If SMTP requires password.'], 'type': 'str', 'version_added': '1.9'}",
    "port": "{'description': ['The mail server port.', 'This must be a valid integer between 1 and 65534'], 'type': 'int', 'default': 25}",
    "secure": "{'description': ["If C(always), the connection will only send email if the connection is Encrypted. If the server doesn't accept the encrypted connection it will fail.", 'If C(try), the connection will attempt to setup a secure SSL/TLS session, before trying to send.', 'If C(never), the connection will not attempt to setup a secure SSL/TLS session, before sending', 'If C(starttls), the connection will try to upgrade to a secure SSL/TLS connection, before sending. If it is unable to do so it will fail.'], 'type': 'str', 'choices': ['always', 'never', 'starttls', 'try'], 'default': 'try', 'version_added': '2.3'}",
    "subject": "{'description': ['The subject of the email being sent.'], 'required': True, 'type': 'str'}",
    "subtype": "{'description': ['The minor mime type, can be either C(plain) or C(html).', 'The major type is always C(text).'], 'type': 'str', 'choices': ['html', 'plain'], 'default': 'plain', 'version_added': '2.0'}",
    "timeout": "{'description': ['Sets the timeout in seconds for connection attempts.'], 'type': 'int', 'default': 20, 'version_added': '2.3'}",
    "to": "{'description': ['The email-address(es) the mail is being sent to.', 'This is a list, which may contain address and phrase portions.'], 'type': 'list', 'default': 'root', 'aliases': ['recipients']}",
    "username": "{'description': ['If SMTP requires username.'], 'type': 'str', 'version_added': '1.9'}",
}
```

## Examples


``` yaml

- name: Example playbook sending mail to root
  mail:
    subject: System {{ ansible_hostname }} has been successfully provisioned.
  delegate_to: localhost

- name: Sending an e-mail using Gmail SMTP servers
  mail:
    host: smtp.gmail.com
    port: 587
    username: username@gmail.com
    password: mysecret
    to: John Smith <john.smith@example.com>
    subject: Ansible-report
    body: System {{ ansible_hostname }} has been successfully provisioned.
  delegate_to: localhost

- name: Send e-mail to a bunch of users, attaching files
  mail:
    host: 127.0.0.1
    port: 2025
    subject: Ansible-report
    body: Hello, this is an e-mail. I hope you like it ;-)
    from: jane@example.net (Jane Jolie)
    to:
    - John Doe <j.d@example.org>
    - Suzie Something <sue@example.com>
    cc: Charlie Root <root@localhost>
    attach:
    - /etc/group
    - /tmp/avatar2.png
    headers:
    - Reply-To=john@example.com
    - X-Special="Something or other"
    charset: us-ascii
  delegate_to: localhost

- name: Sending an e-mail using the remote machine, not the Ansible controller node
  mail:
    host: localhost
    port: 25
    to: John Smith <john.smith@example.com>
    subject: Ansible-report
    body: System {{ ansible_hostname }} has been successfully provisioned.

- name: Sending an e-mail using Legacy SSL to the remote machine
  mail:
    host: localhost
    port: 25
    to: John Smith <john.smith@example.com>
    subject: Ansible-report
    body: System {{ ansible_hostname }} has been successfully provisioned.
    secure: always

- name: Sending an e-mail using StartTLS to the remote machine
  mail:
    host: localhost
    port: 25
    to: John Smith <john.smith@example.com>
    subject: Ansible-report
    body: System {{ ansible_hostname }} has been successfully provisioned.
    secure: starttls

```

## License

TODO

## Author Information
  - ['Dag Wieers (@dagwieers)']
