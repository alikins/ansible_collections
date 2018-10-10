# Ansible module: ansible.module_gcp_container_cluster


Creates a GCP Cluster

## Description

A Google Container Engine cluster.

## Requirements

TODO

## Arguments

``` json
{
    "addons_config": "{'description': ['Configurations for the various addons available to run in the cluster.'], 'required': False, 'suboptions': {'http_load_balancing': {'description': ['Configuration for the HTTP (L7) load balancing controller addon, which makes it easy to set up HTTP load balancers for services in a cluster.'], 'required': False, 'suboptions': {'disabled': {'description': ['Whether the HTTP Load Balancing controller is enabled in the cluster. When enabled, it runs a small pod in the cluster that manages the load balancers.'], 'required': False, 'type': 'bool'}}}, 'horizontal_pod_autoscaling': {'description': ['Configuration for the horizontal pod autoscaling feature, which increases or decreases the number of replica pods a replication controller has based on the resource usage of the existing pods.'], 'required': False, 'suboptions': {'disabled': {'description': ['Whether the Horizontal Pod Autoscaling feature is enabled in the cluster. When enabled, it ensures that a Heapster pod is running in the cluster, which is also used by the Cloud Monitoring service.'], 'required': False, 'type': 'bool'}}}}}",
    "auth_kind": "{'description': ['The type of credential used.'], 'required': True, 'choices': ['machineaccount', 'serviceaccount', 'application']}",
    "cluster_ipv4_cidr": "{'description': ['The IP address range of the container pods in this cluster, in CIDR notation (e.g. 10.96.0.0/14). Leave blank to have one automatically chosen or specify a /14 block in 10.0.0.0/8.'], 'required': False}",
    "description": "{'description': ['An optional description of this cluster.'], 'required': False}",
    "initial_node_count": "{'description': ['The number of nodes to create in this cluster. You must ensure that your Compute Engine resource quota is sufficient for this number of instances. You must also have available firewall and routes quota. For requests, this field should only be used in lieu of a "nodePool" object, since this configuration (along with the "nodeConfig") will be used to create a "NodePool" object with an auto-generated name. Do not use this and a nodePool at the same time.'], 'required': True}",
    "location": "{'description': ["The list of Google Compute Engine locations in which the cluster's nodes should be located."], 'required': False}",
    "logging_service": "{'description': ['The logging service the cluster should use to write logs. Currently available options:  logging.googleapis.com - the Google Cloud Logging service.', 'none - no logs will be exported from the cluster.', 'if left as an empty string,logging.googleapis.com will be used.'], 'required': False, 'choices': ['logging.googleapis.com', 'none']}",
    "master_auth": "{'description': ['The authentication information for accessing the master endpoint.'], 'required': False, 'suboptions': {'username': {'description': ['The username to use for HTTP basic authentication to the master endpoint.'], 'required': False}, 'password': {'description': ['The password to use for HTTP basic authentication to the master endpoint. Because the master endpoint is open to the Internet, you should create a strong password.'], 'required': False}, 'cluster_ca_certificate': {'description': ['Base64-encoded public certificate that is the root of trust for the cluster.'], 'required': False}, 'client_certificate': {'description': ['Base64-encoded public certificate used by clients to authenticate to the cluster endpoint.'], 'required': False}, 'client_key': {'description': ['Base64-encoded private key used by clients to authenticate to the cluster endpoint.'], 'required': False}}}",
    "monitoring_service": "{'description': ['The monitoring service the cluster should use to write metrics.', 'Currently available options:  monitoring.googleapis.com - the Google Cloud Monitoring service.', 'none - no metrics will be exported from the cluster.', 'if left as an empty string, monitoring.googleapis.com will be used.'], 'required': False, 'choices': ['monitoring.googleapis.com', 'none']}",
    "name": "{'description': ['The name of this cluster. The name must be unique within this project and zone, and can be up to 40 characters. Must be Lowercase letters, numbers, and hyphens only. Must start with a letter. Must end with a number or a letter.'], 'required': False}",
    "network": "{'description': ['The name of the Google Compute Engine network to which the cluster is connected. If left unspecified, the default network will be used.', "To ensure it exists and it is operations, configure the network using 'gcompute_network' resource."], 'required': False}",
    "node_config": "{'description': ["Parameters used in creating the cluster's nodes.", 'For requests, this field should only be used in lieu of a "nodePool" object, since this configuration (along with the "initialNodeCount") will be used to create a "NodePool" object with an auto-generated name. Do not use this and a nodePool at the same time. For responses, this field will be populated with the node configuration of the first node pool. If unspecified, the defaults are used.'], 'required': False, 'suboptions': {'machine_type': {'description': ['The name of a Google Compute Engine machine type (e.g.', 'n1-standard-1).  If unspecified, the default machine type is n1-standard-1.'], 'required': False}, 'disk_size_gb': {'description': ['Size of the disk attached to each node, specified in GB. The smallest allowed disk size is 10GB. If unspecified, the default disk size is 100GB.'], 'required': False}, 'oauth_scopes': {'description': ['The set of Google API scopes to be made available on all of the node VMs under the "default" service account.', 'The following scopes are recommended, but not required, and by default are not included:  U(https://www.googleapis.com/auth/compute) is required for mounting persistent storage on your nodes.', 'U(https://www.googleapis.com/auth/devstorage.read_only) is required for communicating with gcr.io (the Google Container Registry).', 'If unspecified, no scopes are added, unless Cloud Logging or Cloud Monitoring are enabled, in which case their required scopes will be added.'], 'required': False}, 'service_account': {'description': ['The Google Cloud Platform Service Account to be used by the node VMs.  If no Service Account is specified, the "default" service account is used.'], 'required': False}, 'metadata': {'description': ['The metadata key/value pairs assigned to instances in the cluster.', 'Keys must conform to the regexp [a-zA-Z0-9-_]+ and be less than 128 bytes in length. These are reflected as part of a URL in the metadata server. Additionally, to avoid ambiguity, keys must not conflict with any other metadata keys for the project or be one of the four reserved keys: "instance-template", "kube-env", "startup-script", and "user-data"  Values are free-form strings, and only have meaning as interpreted by the image running in the instance. The only restriction placed on them is that each value\'s size must be less than or equal to 32 KB.', 'The total size of all keys and values must be less than 512 KB.', 'An object containing a list of "key": value pairs.', 'Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.'], 'required': False}, 'image_type': {'description': ['The image type to use for this node.  Note that for a given image type, the latest version of it will be used.'], 'required': False}, 'labels': {'description': ['The map of Kubernetes labels (key/value pairs) to be applied to each node. These will added in addition to any default label(s) that Kubernetes may apply to the node. In case of conflict in label keys, the applied set may differ depending on the Kubernetes version -- it\'s best to assume the behavior is undefined and conflicts should be avoided. For more information, including usage and the valid values, see: U(http://kubernetes.io/v1.1/docs/user-guide/labels.html) An object containing a list of "key": value pairs.', 'Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.'], 'required': False}, 'local_ssd_count': {'description': ['The number of local SSD disks to be attached to the node.', 'The limit for this value is dependant upon the maximum number of disks available on a machine per zone. See:  U(https://cloud.google.com/compute/docs/disks/local-ssd#local_ssd_limits)  for more information.'], 'required': False}, 'tags': {'description': ['The list of instance tags applied to all nodes. Tags are used to identify valid sources or targets for network firewalls and are specified by the client during cluster or node pool creation. Each tag within the list must comply with RFC1035.'], 'required': False}, 'preemptible': {'description': ['Whether the nodes are created as preemptible VM instances. See: U(https://cloud.google.com/compute/docs/instances/preemptible) for more inforamtion about preemptible VM instances.'], 'required': False, 'type': 'bool'}}}",
    "project": "{'description': ['The Google Cloud Platform project to use.'], 'default': None}",
    "scopes": "{'description': ['Array of scopes to be used.']}",
    "service_account_email": "{'description': ['An optional service account email address if machineaccount is selected and the user does not wish to use the default email.']}",
    "service_account_file": "{'description': ['The path of a Service Account JSON file if serviceaccount is selected as type.']}",
    "state": "{'description': ['Whether the given object should exist in GCP'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "subnetwork": "{'description': ['The name of the Google Compute Engine subnetwork to which the cluster is connected.'], 'required': False}",
    "zone": "{'description': ['The zone where the cluster is deployed.'], 'required': True}",
}
```

## Examples


``` yaml

- name: create a cluster
  gcp_container_cluster:
      name: "test_object"
      initial_node_count: 2
      master_auth:
        username: cluster_admin
        password: my-secret-password
      node_config:
        machine_type: n1-standard-4
        disk_size_gb: 500
      zone: us-central1-a
      project: "test_project"
      auth_kind: "service_account"
      service_account_file: "/tmp/auth.pem"
      state: present

```

## License

TODO

## Author Information
  - ['Google Inc. (@googlecloudplatform)']
