# Ansible lookup: ansible.lookup_grafana_dashboard


list or search grafana dashboards

## Description

This lookup returns a list of grafana dashboards with possibility to filter them by query.

## Requirements

TODO

## Arguments

``` json
{
    "grafana_api_key": "{'description': ['api key of grafana.', 'when C(grafana_api_key) is set, the options C(grafan_user), C(grafana_password) and C(grafana_org_id) are ignored.', 'Attention, please remove the two == at the end of the grafana_api_key', 'because ansible lookup plugins options are splited on = (see example).'], 'env': [{'name': 'GRAFANA_API_KEY'}]}",
    "grafana_org_id": "{'description': ['grafana organisation id.'], 'env': [{'name': 'GRAFANA_ORG_ID'}], 'default': 1}",
    "grafana_password": "{'description': ['grafana authentication password.'], 'env': [{'name': 'GRAFANA_PASSWORD'}], 'default': 'admin'}",
    "grafana_url": "{'description': ['url of grafana.'], 'env': [{'name': 'GRAFANA_URL'}], 'default': 'http://127.0.0.1:3000'}",
    "grafana_user": "{'description': ['grafana authentication user.'], 'env': [{'name': 'GRAFANA_USER'}], 'default': 'admin'}",
    "search": "{'description': ['optional filter for dashboard search.'], 'env': [{'name': 'GRAFANA_DASHBOARD_SEARCH'}]}",
}
```

## Examples


``` yaml

- name: get project foo grafana dashboards
  set_fact:
    grafana_dashboards: "{{ lookup('grafana_dashboard', 'grafana_url=http://grafana.company.com grafana_user=admin grafana_password=admin search=foo') }}"

- name: get all grafana dashboards
  set_fact:
    grafana_dashboards: "{{ lookup('grafana_dashboard', 'grafana_url=http://grafana.company.com grafana_api_key=' ~ grafana_api_key|replace('==', '')) }}"

```

## License

TODO

## Author Information
  - ['Thierry Salle (@seuf)']
