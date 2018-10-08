# Ansible callback: ansible.callback_grafana_annotations


send ansible events as annotations on charts to grafana over http api

## Description

This callback will report start, failed and stats events to Grafana as annotations (https://grafana.com)

## Requirements

TODO

## Arguments

``` json
{
    "grafana_api_key": "{'description': ['Grafana API key, allowing to authenticate when posting on the HTTP API. If not provided, grafana_login and grafana_password will be required.'], 'env': [{'name': 'GRAFANA_API_KEY'}], 'ini': [{'section': 'callback_grafana_annotations', 'key': 'grafana_api_key'}]}",
    "grafana_dashboard_id": "{'description': ['The grafana dashboard id where the annotation shall be created.'], 'env': [{'name': 'GRAFANA_DASHBOARD_ID'}], 'ini': [{'section': 'callback_grafana_annotations', 'key': 'grafana_dashboard_id'}]}",
    "grafana_panel_id": "{'description': ['The grafana panel id where the annotation shall be created.'], 'env': [{'name': 'GRAFANA_PANEL_ID'}], 'ini': [{'section': 'callback_grafana_annotations', 'key': 'grafana_panel_id'}]}",
    "grafana_password": "{'description': ['Grafana password used for authentication. Ignored if grafana_api_key is provided.'], 'env': [{'name': 'GRAFANA_PASSWORD'}], 'ini': [{'section': 'callback_grafana_annotations', 'key': 'grafana_password'}], 'default': 'ansible'}",
    "grafana_url": "{'description': ['Grafana annotations api URL'], 'required': True, 'env': [{'name': 'GRAFANA_URL'}], 'ini': [{'section': 'callback_grafana_annotations', 'key': 'grafana_url'}]}",
    "grafana_user": "{'description': ['Grafana user used for authentication. Ignored if grafana_api_key is provided.'], 'env': [{'name': 'GRAFANA_USER'}], 'ini': [{'section': 'callback_grafana_annotations', 'key': 'grafana_user'}], 'default': 'ansible'}",
    "http_agent": "{'description': ["The HTTP 'User-agent' value to set in HTTP requets."], 'env': [{'name': 'HTTP_AGENT'}], 'ini': [{'section': 'callback_grafana_annotations', 'key': 'http_agent'}], 'default': 'Ansible (grafana_annotations callback)'}",
    "validate_grafana_certs": "{'description': ['validate the SSL certificate of the Grafana server. (For HTTPS url)'], 'env': [{'name': 'GRAFANA_VALIDATE_CERT'}], 'ini': [{'section': 'callback_grafana_annotations', 'key': 'validate_grafana_certs'}], 'default': True, 'type': 'bool'}",
}
```

## Examples



## License

TODO

## Author Information
  - ['Rémi REY (@rrey)']
