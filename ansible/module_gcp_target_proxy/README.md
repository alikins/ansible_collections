# Ansible module: ansible.module_gcp_target_proxy


Create, Update or Destroy a Target_Proxy

## Description

Create, Update or Destroy a Target_Proxy. See U(https://cloud.google.com/compute/docs/load-balancing/http/target-proxies) for an overview. More details on the Target_Proxy API can be found at U(https://cloud.google.com/compute/docs/reference/latest/targetHttpProxies#resource-representations).

## Requirements

TODO

## Arguments

``` json
{
    "target_proxy_name": "{'description': ['Name of the Target_Proxy.'], 'required': True}",
    "target_proxy_type": "{'description': ['Type of Target_Proxy. HTTP, HTTPS or SSL. Only HTTP is currently supported.'], 'required': True}",
    "url_map_name": "{'description': ['Name of the Url Map.  Required if type is HTTP or HTTPS proxy.'], 'required': False}",
}
```

## Examples


``` yaml

- name: Create Minimum HTTP Target_Proxy
  gcp_target_proxy:
    service_account_email: "{{ service_account_email }}"
    credentials_file: "{{ credentials_file }}"
    project_id: "{{ project_id }}"
    target_proxy_name: my-target_proxy
    target_proxy_type: HTTP
    url_map_name: my-url-map
    state: present

```

## License

TODO

## Author Information
  - ['Tom Melendez (@supertom) <tom@supertom.com>']
