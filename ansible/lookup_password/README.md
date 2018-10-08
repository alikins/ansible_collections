# Ansible lookup: ansible.lookup_password


retrieve or generate a random password, stored in a file

## Description

Generates a random plaintext password and stores it in a file at a given filepath.
If the file exists previously, it will retrieve its contents, behaving just like with_file.
Usage of variables like C("{{ inventory_hostname }}") in the filepath can be used to set up random passwords per host, which simplifies password management in C("host_vars") variables.
A special case is using /dev/null as a path. The password lookup will generate a new random password each time, but will not write it to /dev/null. This can be used when you need a password without storing it on the controller.

## Requirements

TODO

## Arguments

``` json
{
    "_terms": "{'description': ['path to the file that stores/will store the passwords'], 'required': True}",
    "chars": "{'version_added': '1.4', 'description': ['Define comma separated list of names that compose a custom character set in the generated passwords.', 'By default generated passwords contain a random mix of upper and lowercase ASCII letters, the numbers 0-9 and punctuation (". , : - _").', "They can be either parts of Python's string module attributes (ascii_letters,digits, etc) or are used literally ( :, -).", "To enter comma use two commas ',,' somewhere - preferably at the end. Quotes and double quotes are not supported."], 'type': 'string'}",
    "encrypt": "{'description': ['Which hash scheme to encrypt the returning password, should be one hash scheme from C(passlib.hash).', 'If not provided, the password will be returned in plain text.', 'Note that the password is always stored as plain text, only the returning password is encrypted.', 'Encrypt also forces saving the salt value for idempotence.', 'Note that before 2.6 this option was incorrectly labeled as a boolean for a long time.'], 'default': 'None'}",
    "length": "{'description': ['The length of the generated password.'], 'default': 20, 'type': 'integer'}",
}
```

## Examples


``` yaml

- name: create a mysql user with a random password
  mysql_user:
    name: "{{ client }}"
    password: "{{ lookup('password', 'credentials/' + client + '/' + tier + '/' + role + '/mysqlpassword length=15') }}"
    priv: "{{ client }}_{{ tier }}_{{ role }}.*:ALL"

- name: create a mysql user with a random password using only ascii letters
  mysql_user:
    name: "{{ client }}"
    password: "{{ lookup('password', '/tmp/passwordfile chars=ascii_letters') }}"
    priv: '{{ client }}_{{ tier }}_{{ role }}.*:ALL'

- name: create a mysql user with a random password using only digits
  mysql_user:
    name: "{{ client }}"
    password: "{{ lookup('password', '/tmp/passwordfile chars=digits') }}"
    priv: "{{ client }}_{{ tier }}_{{ role }}.*:ALL"

- name: create a mysql user with a random password using many different char sets
  mysql_user:
    name: "{{ client }}"
    password: "{{ lookup('password', '/tmp/passwordfile chars=ascii_letters,digits,hexdigits,punctuation') }}"
    priv: "{{ client }}_{{ tier }}_{{ role }}.*:ALL"

```

## License

TODO

## Author Information
  - ['Daniel Hokka Zakrisson <daniel@hozac.com>', 'Javier Candeira <javier@candeira.com>', 'Maykel Moya <mmoya@speedyrails.com>']
  - ['Daniel Hokka Zakrisson <daniel@hozac.com>', 'Javier Candeira <javier@candeira.com>', 'Maykel Moya <mmoya@speedyrails.com>']
  - ['Daniel Hokka Zakrisson <daniel@hozac.com>', 'Javier Candeira <javier@candeira.com>', 'Maykel Moya <mmoya@speedyrails.com>']
