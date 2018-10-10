# Ansible module: ansible.module_layman


Manage Gentoo overlays

## Description

Uses Layman to manage an additional repositories for the Portage package manager on Gentoo Linux. Please note that Layman must be installed on a managed node prior using this module.

## Requirements

TODO

## Arguments

``` json
{
    "list_url": "{'description': ["An URL of the alternative overlays list that defines the overlay to install. This list will be fetched and saved under C(${overlay_defs})/${name}.xml), where C(overlay_defs) is readed from the Layman's configuration."]}",
    "name": "{'description': ["The overlay id to install, synchronize, or uninstall. Use 'ALL' to sync all of the installed overlays (can be used only when C(state=updated))."], 'required': True}",
    "state": "{'description': ['Whether to install (C(present)), sync (C(updated)), or uninstall (C(absent)) the overlay.'], 'default': 'present', 'choices': ['present', 'absent', 'updated']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be set to C(no) when no other option exists.  Prior to 1.9.3 the code defaulted to C(no).'], 'type': 'bool', 'default': True, 'version_added': '1.9.3'}",
}
```

## Examples


``` yaml

# Install the overlay 'mozilla' which is on the central overlays list.
- layman:
    name: mozilla

# Install the overlay 'cvut' from the specified alternative list.
- layman:
    name: cvut
    list_url: 'http://raw.github.com/cvut/gentoo-overlay/master/overlay.xml'

# Update (sync) the overlay 'cvut', or install if not installed yet.
- layman:
    name: cvut
    list_url: 'http://raw.github.com/cvut/gentoo-overlay/master/overlay.xml'
    state: updated

# Update (sync) all of the installed overlays.
- layman:
    name: ALL
    state: updated

# Uninstall the overlay 'cvut'.
- layman:
    name: cvut
    state: absent

```

## License

TODO

## Author Information
  - ['Jakub Jirutka (@jirutka)']
