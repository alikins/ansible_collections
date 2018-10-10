# Ansible module: ansible.module_gce_lb


create/destroy GCE load-balancer resources

## Description

This module can create and destroy Google Compute Engine C(loadbalancer) and C(httphealthcheck) resources.  The primary LB resource is the C(load_balancer) resource and the health check parameters are all prefixed with I(httphealthcheck). The full documentation for Google Compute Engine load balancing is at U(https://developers.google.com/compute/docs/load-balancing/).  However, the ansible module simplifies the configuration by following the libcloud model. Full install/configuration instructions for the gce* modules can be found in the comments of ansible/test/gce_tests.py.

## Requirements

TODO

## Arguments

``` json
{
    "credentials_file": "{'version_added': '2.1.0', 'description': ['path to the JSON file associated with the service account email']}",
    "external_ip": "{'description': ['the external static IPv4 (or auto-assigned) address for the LB']}",
    "httphealthcheck_healthy_count": "{'description': ['number of consecutive successful checks before marking a node healthy'], 'default': 2}",
    "httphealthcheck_host": "{'description': ['host header to pass through on HTTP check requests']}",
    "httphealthcheck_interval": "{'description': ['the duration in seconds between each health check request'], 'default': 5}",
    "httphealthcheck_name": "{'description': ['the name identifier for the HTTP health check']}",
    "httphealthcheck_path": "{'description': ['the url path to use for HTTP health checking'], 'default': '/'}",
    "httphealthcheck_port": "{'description': ['the TCP port to use for HTTP health checking'], 'default': 80}",
    "httphealthcheck_timeout": "{'description': ['the timeout in seconds before a request is considered a failed check'], 'default': 5}",
    "httphealthcheck_unhealthy_count": "{'description': ['number of consecutive failed checks before marking a node unhealthy'], 'default': 2}",
    "members": "{'description': ["a list of zone/nodename pairs, e.g ['us-central1-a/www-a', ...]"], 'aliases': ['nodes']}",
    "name": "{'description': ['name of the load-balancer resource']}",
    "pem_file": "{'version_added': '1.6', 'description': ["path to the pem file associated with the service account email This option is deprecated. Use 'credentials_file'."]}",
    "port_range": "{'description': ['the port (range) to forward, e.g. 80 or 8000-8888 defaults to all ports']}",
    "project_id": "{'version_added': '1.6', 'description': ['your GCE project ID']}",
    "protocol": "{'description': ['the protocol used for the load-balancer packet forwarding, tcp or udp'], 'default': 'tcp', 'choices': ['tcp', 'udp']}",
    "region": "{'description': ['the GCE region where the load-balancer is defined']}",
    "service_account_email": "{'version_added': '1.6', 'description': ['service account email']}",
    "state": "{'description': ['desired state of the LB'], 'default': 'present', 'choices': ['active', 'present', 'absent', 'deleted']}",
}
```

## Examples


``` yaml

# Simple example of creating a new LB, adding members, and a health check
- local_action:
    module: gce_lb
    name: testlb
    region: us-central1
    members: ["us-central1-a/www-a", "us-central1-b/www-b"]
    httphealthcheck_name: hc
    httphealthcheck_port: 80
    httphealthcheck_path: "/up"

```

## License

TODO

## Author Information
  - ['Eric Johnson (@erjohnso) <erjohnso@google.com>']
