# Ansible module: ansible.module_apt_repository


Add and remove APT repositories

## Description

Add or remove an APT repositories in Ubuntu and Debian.

## Requirements

TODO

## Arguments

``` json
{
    "codename": "{'description': ['Override the distribution codename to use for PPA repositories. Should usually only be set when working with a PPA on a non-Ubuntu target (e.g. Debian or Mint)'], 'version_added': '2.3'}",
    "filename": "{'description': ['Sets the name of the source list file in sources.list.d. Defaults to a file name based on the repository source url. The .list extension will be automatically added.'], 'version_added': '2.1'}",
    "mode": "{'description': ['The octal mode for newly created files in sources.list.d'], 'default': '0644', 'version_added': '1.6'}",
    "repo": "{'description': ['A source string for the repository.'], 'required': True}",
    "state": "{'description': ['A source string state.'], 'choices': ['absent', 'present'], 'default': 'present'}",
    "update_cache": "{'description': ['Run the equivalent of C(apt-get update) when a change occurs.  Cache updates are run after making changes.'], 'type': 'bool', 'default': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates for the target repo will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True, 'version_added': '1.8'}",
}
```

## Examples


``` yaml

# Add specified repository into sources list.
- apt_repository:
    repo: deb http://archive.canonical.com/ubuntu hardy partner
    state: present

# Add specified repository into sources list using specified filename.
- apt_repository:
    repo: deb http://dl.google.com/linux/chrome/deb/ stable main
    state: present
    filename: google-chrome

# Add source repository into sources list.
- apt_repository:
    repo: deb-src http://archive.canonical.com/ubuntu hardy partner
    state: present

# Remove specified repository from sources list.
- apt_repository:
    repo: deb http://archive.canonical.com/ubuntu hardy partner
    state: absent

# Add nginx stable repository from PPA and install its signing key.
# On Ubuntu target:
- apt_repository:
    repo: ppa:nginx/stable

# On Debian target
- apt_repository:
    repo: 'ppa:nginx/stable'
    codename: trusty

```

## License

TODO

## Author Information
  - ['Alexander Saltanov (@sashka)']
