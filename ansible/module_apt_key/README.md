# Ansible module: ansible.module_apt_key


Add or remove an apt key

## Description

Add or remove an I(apt) key, optionally downloading it.

## Requirements

TODO

## Arguments

``` json
{
    "data": "{'description': ['The keyfile contents to add to the keyring.']}",
    "file": "{'description': ['The path to a keyfile on the remote server to add to the keyring.']}",
    "id": "{'description': ['The identifier of the key.', 'Including this allows check mode to correctly report the changed state.', "If specifying a subkey's id be aware that apt-key does not understand how to remove keys via a subkey id.  Specify the primary key's id instead.", 'This parameter is required when C(state) is set to C(absent).']}",
    "keyring": "{'description': ['The full path to specific keyring file in /etc/apt/trusted.gpg.d/'], 'version_added': '1.3'}",
    "keyserver": "{'description': ['The keyserver to retrieve key from.'], 'version_added': '1.6'}",
    "state": "{'description': ['Ensures that the key is present (added) or absent (revoked).'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "url": "{'description': ['The URL to retrieve key from.']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates for the target url will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Add an apt key by id from a keyserver
  apt_key:
    keyserver: keyserver.ubuntu.com
    id: 36A1D7869245C8950F966E92D8576A8BA88D21E9

- name: Add an Apt signing key, uses whichever key is at the URL
  apt_key:
    url: https://ftp-master.debian.org/keys/archive-key-6.0.asc
    state: present

- name: Add an Apt signing key, will not download if present
  apt_key:
    id: 9FED2BCBDCD29CDF762678CBAED4B06F473041FA
    url: https://ftp-master.debian.org/keys/archive-key-6.0.asc
    state: present

- name: Remove a Apt specific signing key, leading 0x is valid
  apt_key:
    id: 0x9FED2BCBDCD29CDF762678CBAED4B06F473041FA
    state: absent

# Use armored file since utf-8 string is expected. Must be of "PGP PUBLIC KEY BLOCK" type.
- name: Add a key from a file on the Ansible server.
  apt_key:
    data: "{{ lookup('file', 'apt.asc') }}"
    state: present

- name: Add an Apt signing key to a specific keyring file
  apt_key:
    id: 9FED2BCBDCD29CDF762678CBAED4B06F473041FA
    url: https://ftp-master.debian.org/keys/archive-key-6.0.asc
    keyring: /etc/apt/trusted.gpg.d/debian.gpg

- name: Add Apt signing key on remote server to keyring
  apt_key:
    id: 9FED2BCBDCD29CDF762678CBAED4B06F473041FA
    file: /tmp/apt.gpg
    state: present

```

## License

TODO

## Author Information
  - ['Jayson Vantuyl (@jvantuyl)']
