# Ansible module: ansible.module_gcp_url_map


Create, Update or Destory a Url_Map

## Description

Create, Update or Destory a Url_Map. See U(https://cloud.google.com/compute/docs/load-balancing/http/url-map) for an overview. More details on the Url_Map API can be found at U(https://cloud.google.com/compute/docs/reference/latest/urlMaps#resource).

## Requirements

TODO

## Arguments

``` json
{
    "default_service": "{'description': ['Default Backend Service if no host rules match.'], 'required': True}",
    "host_rules": "{'description': ['The list of HostRules to use against the URL. Contains a list of hosts and an associated path_matcher.', "The 'hosts' parameter is a list of host patterns to match. They must be valid hostnames, except * will match any string of ([a-z0-9-.]*). In that case, * must be the first character and must be followed in the pattern by either - or ..", "The 'path_matcher' parameter is name of the PathMatcher to use to match the path portion of the URL if the hostRule matches the URL's host portion."], 'required': False}",
    "path_matchers": "{'description': ['The list of named PathMatchers to use against the URL. Contains path_rules, which is a list of paths and an associated service. A default_service can also be specified for each path_matcher.', "The 'name' parameter to which this path_matcher is referred by the host_rule.", "The 'default_service' parameter is the name of the BackendService resource. This will be used if none of the path_rules defined by this path_matcher is matched by the URL's path portion.", "The 'path_rules' parameter is a list of dictionaries containing a list of paths and a service to direct traffic to. Each path item must start with / and the only place a * is allowed is at the end following a /. The string fed to the path matcher does not include any text after the first ? or"], 'required': False}",
    "url_map_name": "{'description': ['Name of the Url_Map.'], 'required': True}",
}
```

## Examples


``` yaml

- name: Create Minimal Url_Map
  gcp_url_map:
    service_account_email: "{{ service_account_email }}"
    credentials_file: "{{ credentials_file }}"
    project_id: "{{ project_id }}"
    url_map_name: my-url_map
    default_service: my-backend-service
    state: present
- name: Create UrlMap with pathmatcher
  gcp_url_map:
    service_account_email: "{{ service_account_email }}"
    credentials_file: "{{ credentials_file }}"
    project_id: "{{ project_id }}"
    url_map_name: my-url-map-pm
    default_service: default-backend-service
    path_matchers:
    - name: 'path-matcher-one'
      description: 'path matcher one'
      default_service: 'bes-pathmatcher-one-default'
      path_rules:
      - service: 'my-one-bes'
        paths:
        - '/data'
        - '/aboutus'
    host_rules:
      - hosts:
        - '*.'
        path_matcher: 'path-matcher-one'
    state: "present"

```

## License

TODO

## Author Information
  - ['Tom Melendez (@supertom) <tom@supertom.com>']
