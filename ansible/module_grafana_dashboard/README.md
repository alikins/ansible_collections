# Ansible module: ansible.module_grafana_dashboard


Manage Grafana dashboards

## Description

Create, update, delete, export Grafana dashboards via API.

## Requirements

TODO

## Arguments

``` json
{
    "client_cert": "{'description': ['PEM formatted certificate chain file to be used for SSL client authentication.', 'This file can also include the key as well, and if the key is included, client_key is not required'], 'version_added': 2.7}",
    "client_key": "{'description': ['PEM formatted file that contains your private key to be used for SSL client', 'authentication. If client_cert contains both the certificate and key, this option is not required'], 'version_added': 2.7}",
    "grafana_api_key": "{'description': ['The Grafana API key.', 'If set, I(grafana_user) and I(grafana_password) will be ignored.']}",
    "message": "{'description': ['Set a commit message for the version history.', 'Only used when C(state) is C(present).']}",
    "org_id": "{'description': ['The Grafana Organisation ID where the dashboard will be imported / exported.', 'Not used when I(grafana_api_key) is set, because the grafana_api_key only belongs to one organisation..'], 'default': 1}",
    "overwrite": "{'description': ['Override existing dashboard when state is present.'], 'type': 'bool', 'default': False}",
    "path": "{'description': ['The path to the json file containing the Grafana dashboard to import or export.']}",
    "slug": "{'description': ['Deprecated since Grafana 5. Use grafana dashboard uid instead.', "slug of the dashboard. It's the friendly url name of the dashboard.", 'When C(state) is C(present), this parameter can override the slug in the meta section of the json file.', 'If you want to import a json dashboard exported directly from the interface (not from the api), you have to specify the slug parameter because there is no meta section in the exported json.']}",
    "state": "{'description': ['State of the dashboard.'], 'required': True, 'choices': ['absent', 'export', 'present'], 'default': 'present'}",
    "uid": "{'version_added': 2.7, 'description': ['uid of the dasboard to export when C(state) is C(export) or C(absent).']}",
    "url": "{'description': ['The Grafana URL.'], 'required': True, 'aliases': ['grafana_url'], 'version_added': 2.7}",
    "url_password": "{'description': ['The Grafana API password.'], 'default': 'admin', 'aliases': ['grafana_password'], 'version_added': 2.7}",
    "url_username": "{'description': ['The Grafana API user.'], 'default': 'admin', 'aliases': ['grafana_user'], 'version_added': 2.7}",
    "use_proxy": "{'description': ['Boolean of whether or not to use proxy.'], 'default': True, 'type': 'bool', 'version_added': 2.7}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated.', 'This should only be used on personally controlled sites using self-signed certificates.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- hosts: localhost
  connection: local
  tasks:
    - name: Import Grafana dashboard foo
      grafana_dashboard:
        grafana_url: http://grafana.company.com
        grafana_api_key: "{{ grafana_api_key }}"
        state: present
        message: Updated by ansible
        overwrite: yes
        path: /path/to/dashboards/foo.json

    - name: Export dashboard
      grafana_dashboard:
        grafana_url: http://grafana.company.com
        grafana_user: "admin"
        grafana_password: "{{ grafana_password }}"
        org_id: 1
        state: export
        uid: "000000653"
        path: "/path/to/dashboards/000000653.json"

```

## License

TODO

## Author Information
  - ['Thierry Sallé (@seuf)']
