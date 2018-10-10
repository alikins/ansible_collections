# Ansible module: ansible.module_gcp_compute_backend_service


Creates a GCP BackendService

## Description

Creates a BackendService resource in the specified project using the data included in the request.

## Requirements

TODO

## Arguments

``` json
{
    "affinity_cookie_ttl_sec": "{'description': ['Lifetime of cookies in seconds if session_affinity is GENERATED_COOKIE. If set to 0, the cookie is non-persistent and lasts only until the end of the browser session (or equivalent). The maximum allowed value for TTL is one day.', 'When the load balancing scheme is INTERNAL, this field is not used.'], 'required': False}",
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "backends": "{'description': ['The list of backends that serve this BackendService.'], 'required': False, 'suboptions': {'balancing_mode': {'description': ['Specifies the balancing mode for this backend.', 'For global HTTP(S) or TCP/SSL load balancing, the default is UTILIZATION. Valid values are UTILIZATION, RATE (for HTTP(S)) and CONNECTION (for TCP/SSL).', 'This cannot be used for internal load balancing.'], 'required': False, 'choices': ['UTILIZATION', 'RATE', 'CONNECTION']}, 'capacity_scaler': {'description': ["A multiplier applied to the group's maximum servicing capacity (based on UTILIZATION, RATE or CONNECTION).", 'Default value is 1, which means the group will serve up to 100% of its configured capacity (depending on balancingMode). A setting of 0 means the group is completely drained, offering 0% of its available Capacity. Valid range is [0.0,1.0].', 'This cannot be used for internal load balancing.'], 'required': False}, 'description': {'description': ['An optional description of this resource.', 'Provide this property when you create the resource.'], 'required': False}, 'group': {'description': ['This instance group defines the list of instances that serve traffic. Member virtual machine instances from each instance group must live in the same zone as the instance group itself.', 'No two backends in a backend service are allowed to use same Instance Group resource.', 'When the BackendService has load balancing scheme INTERNAL, the instance group must be in a zone within the same region as the BackendService.'], 'required': False}, 'max_connections': {'description': ['The max number of simultaneous connections for the group. Can be used with either CONNECTION or UTILIZATION balancing modes.', 'For CONNECTION mode, either maxConnections or maxConnectionsPerInstance must be set.', 'This cannot be used for internal load balancing.'], 'required': False}, 'max_connections_per_instance': {'description': ['The max number of simultaneous connections that a single backend instance can handle. This is used to calculate the capacity of the group. Can be used in either CONNECTION or UTILIZATION balancing modes.', 'For CONNECTION mode, either maxConnections or maxConnectionsPerInstance must be set.', 'This cannot be used for internal load balancing.'], 'required': False}, 'max_rate': {'description': ['The max requests per second (RPS) of the group.', 'Can be used with either RATE or UTILIZATION balancing modes, but required if RATE mode. For RATE mode, either maxRate or maxRatePerInstance must be set.', 'This cannot be used for internal load balancing.'], 'required': False}, 'max_rate_per_instance': {'description': ['The max requests per second (RPS) that a single backend instance can handle. This is used to calculate the capacity of the group. Can be used in either balancing mode. For RATE mode, either maxRate or maxRatePerInstance must be set.', 'This cannot be used for internal load balancing.'], 'required': False}, 'max_utilization': {'description': ['Used when balancingMode is UTILIZATION. This ratio defines the CPU utilization target for the group. The default is 0.8. Valid range is [0.0, 1.0].', 'This cannot be used for internal load balancing.'], 'required': False}}}",
    "cdn_policy": "{'description': ['Cloud CDN configuration for this BackendService.'], 'required': False, 'suboptions': {'cache_key_policy': {'description': ['The CacheKeyPolicy for this CdnPolicy.'], 'required': False, 'suboptions': {'include_host': {'description': ['If true requests to different hosts will be cached separately.'], 'required': False, 'type': 'bool'}, 'include_protocol': {'description': ['If true, http and https requests will be cached separately.'], 'required': False, 'type': 'bool'}, 'include_query_string': {'description': ['If true, include query string parameters in the cache key according to query_string_whitelist and query_string_blacklist. If neither is set, the entire query string will be included.', 'If false, the query string will be excluded from the cache key entirely.'], 'required': False, 'type': 'bool'}, 'query_string_blacklist': {'description': ['Names of query string parameters to exclude in cache keys.', 'All other parameters will be included. Either specify query_string_whitelist or query_string_blacklist, not both.', "'&' and '=' will be percent encoded and not treated as delimiters."], 'required': False}, 'query_string_whitelist': {'description': ['Names of query string parameters to include in cache keys.', 'All other parameters will be excluded. Either specify query_string_whitelist or query_string_blacklist, not both.', "'&' and '=' will be percent encoded and not treated as delimiters."], 'required': False}}}}}",
    "connection_draining": "{'description': ['Settings for connection draining.'], 'required': False, 'suboptions': {'draining_timeout_sec': {'description': ['Time for which instance will be drained (not accept new connections, but still work to finish started).'], 'required': False}}}",
    "description": "{'description': ['An optional description of this resource.'], 'required': False}",
    "enable_cdn": "{'description': ['If true, enable Cloud CDN for this BackendService.', 'When the load balancing scheme is INTERNAL, this field is not used.'], 'required': False, 'type': 'bool'}",
    "health_checks": "{'description': ['The list of URLs to the HttpHealthCheck or HttpsHealthCheck resource for health checking this BackendService. Currently at most one health check can be specified, and a health check is required.', 'For internal load balancing, a URL to a HealthCheck resource must be specified instead.'], 'required': False}",
    "iap": "{'description': ['Settings for enabling Cloud Identity Aware Proxy.'], 'required': False, 'version_added': 2.7, 'suboptions': {'enabled': {'description': ['Enables IAP.'], 'required': False, 'type': 'bool'}, 'oauth2_client_id': {'description': ['OAuth2 Client ID for IAP.'], 'required': False}, 'oauth2_client_secret': {'description': ['OAuth2 Client Secret for IAP.'], 'required': False}, 'oauth2_client_secret_sha256': {'description': ['OAuth2 Client Secret SHA-256 for IAP.'], 'required': False}}}",
    "load_balancing_scheme": "{'description': ['Indicates whether the backend service will be used with internal or external load balancing. A backend service created for one type of load balancing cannot be used with the other.'], 'required': False, 'version_added': 2.7, 'choices': ['INTERNAL', 'EXTERNAL']}",
    "name": "{'description': ['Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.'], 'required': False}",
    "port_name": "{'description': ['Name of backend port. The same name should appear in the instance groups referenced by this service. Required when the load balancing scheme is EXTERNAL.', 'When the load balancing scheme is INTERNAL, this field is not used.'], 'required': False}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "protocol": "{'description': ['The protocol this BackendService uses to communicate with backends.', 'Possible values are HTTP, HTTPS, TCP, and SSL. The default is HTTP.', 'For internal load balancing, the possible values are TCP and UDP, and the default is TCP.'], 'required': False, 'choices': ['HTTP', 'HTTPS', 'TCP', 'SSL']}",
    "region": "{'description': ['The region where the regional backend service resides.', 'This field is not applicable to global backend services.'], 'required': False}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "session_affinity": "{'description': ['Type of session affinity to use. The default is NONE.', 'When the load balancing scheme is EXTERNAL, can be NONE, CLIENT_IP, or GENERATED_COOKIE.', 'When the load balancing scheme is INTERNAL, can be NONE, CLIENT_IP, CLIENT_IP_PROTO, or CLIENT_IP_PORT_PROTO.', 'When the protocol is UDP, this field is not used.'], 'required': False, 'choices': ['NONE', 'CLIENT_IP', 'GENERATED_COOKIE', 'CLIENT_IP_PROTO', 'CLIENT_IP_PORT_PROTO']}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout_sec": "{'description': ['How many seconds to wait for the backend before considering it a failed request. Default is 30 seconds. Valid range is [1, 86400].'], 'required': False, 'aliases': ['timeout_seconds']}",
}
```

## Examples


``` yaml

- name: create a instance group
  gcp_compute_instance_group:
      name: "instancegroup-backendservice"
      zone: us-central1-a
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: instancegroup

- name: create a http health check
  gcp_compute_http_health_check:
      name: "httphealthcheck-backendservice"
      healthy_threshold: 10
      port: 8080
      timeout_sec: 2
      unhealthy_threshold: 5
      project: "{{ gcp_project }}"
      auth_kind: "{{ gcp_cred_kind }}"
      service_account_file: "{{ gcp_cred_file }}"
      state: present
  register: healthcheck

- name: create a backend service
  gcp_compute_backend_service:
      name: "test_object"
      backends:
      - group: "{{ instancegroup }}"
      health_checks:
      - "{{ healthcheck.selfLink }}"
      enable_cdn: true
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
