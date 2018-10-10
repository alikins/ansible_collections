# Ansible module: ansible.module_os_coe_cluster_template


Add/Remove COE cluster template from OpenStack Cloud

## Description

Add or Remove COE cluster template from the OpenStack Container Infra service.

## Requirements

TODO

## Arguments

``` json
{
    "api_timeout": "{'description': ['How long should the socket layer wait before timing out for API calls. If this is omitted, nothing will be passed to the requests library.'], 'required': False}",
    "auth": "{'description': ["Dictionary containing auth information as needed by the cloud's auth plugin strategy. For the default I(password) plugin, this would contain I(auth_url), I(username), I(password), I(project_name) and any information about domains if the cloud supports them. For other plugins, this param will need to contain whatever parameters that auth plugin requires. This parameter is not needed if a named cloud is provided or OpenStack OS_* environment variables are present."], 'required': False}",
    "auth_type": "{'description': ['Name of the auth plugin to use. If the cloud uses something other than password authentication, the name of the plugin should be indicated here and the contents of the I(auth) parameter should be updated accordingly.'], 'required': False}",
    "availability_zone": "{'description': ['Ignored. Present for backwards compatibility']}",
    "cacert": "{'description': ['A path to a CA Cert bundle that can be used as part of verifying SSL API requests.'], 'required': False}",
    "cert": "{'description': ['A path to a client certificate to use as part of the SSL transaction.'], 'required': False}",
    "cloud": "{'description': ['Named cloud or cloud config to operate against. If I(cloud) is a string, it references a named cloud config as defined in an OpenStack clouds.yaml file. Provides default values for I(auth) and I(auth_type). This parameter is not needed if I(auth) is provided or if OpenStack OS_* environment variables are present. If I(cloud) is a dict, it contains a complete cloud configuration like would be in a section of clouds.yaml.'], 'required': False}",
    "coe": "{'description': ['The Container Orchestration Engine for this clustertemplate'], 'choices': ['kubernetes', 'swarm', 'mesos']}",
    "dns_nameserver": "{'description': ['The DNS nameserver address'], 'default': '8.8.8.8'}",
    "docker_storage_driver": "{'description': ['Docker storage driver'], 'choices': ['devicemapper', 'overlay']}",
    "docker_volume_size": "{'description': ['The size in GB of the docker volume']}",
    "external_network_id": "{'description': ['The external network to attach to the Cluster']}",
    "fixed_network": "{'description': ['The fixed network name to attach to the Cluster']}",
    "fixed_subnet": "{'description': ['The fixed subnet name to attach to the Cluster']}",
    "flavor_id": "{'description': ['The flavor of the minion node for this ClusterTemplate']}",
    "floating_ip_enabled": "{'description': ['Indicates whether created clusters should have a floating ip or not'], 'type': 'bool', 'default': True}",
    "http_proxy": "{'description': ['Address of a proxy that will receive all HTTP requests and relay them The format is a URL including a port number']}",
    "https_proxy": "{'description': ['Address of a proxy that will receive all HTTPS requests and relay them. The format is a URL including a port number']}",
    "image_id": "{'description': ['Image id the cluster will be based on']}",
    "interface": "{'description': ['Endpoint URL type to fetch from the service catalog.'], 'choices': ['public', 'internal', 'admin'], 'required': False, 'default': 'public', 'aliases': ['endpoint_type'], 'version_added': '2.3'}",
    "key": "{'description': ['A path to a client key to use as part of the SSL transaction.'], 'required': False}",
    "keypair_id": "{'description': ['Name or ID of the keypair to use.']}",
    "labels": "{'description': ['One or more key/value pairs']}",
    "master_flavor_id": "{'description': ['The flavor of the master node for this ClusterTemplate']}",
    "master_lb_enabled": "{'description': ['Indicates whether created clusters should have a load balancer for master nodes or not'], 'type': 'bool', 'default': False}",
    "name": "{'description': ['Name that has to be given to the cluster template'], 'required': True}",
    "network_driver": "{'description': ['The name of the driver used for instantiating container networks'], 'choices': ['flannel', 'calico', 'docker']}",
    "no_proxy": "{'description': ['A comma separated list of IPs for which proxies should not be used in the cluster']}",
    "public": "{'description': ['Indicates whether the ClusterTemplate is public or not'], 'type': 'bool', 'default': False}",
    "region_name": "{'description': ['Name of the region.'], 'required': False}",
    "registry_enabled": "{'description': ['Indicates whether the docker registry is enabled'], 'type': 'bool', 'default': False}",
    "server_type": "{'description': ['Server type for this ClusterTemplate'], 'choices': ['vm', 'bm'], 'default': 'vm'}",
    "state": "{'description': ['Indicate desired state of the resource.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "timeout": "{'description': ['How long should ansible wait for the requested resource.'], 'required': False, 'default': 180}",
    "tls_disabled": "{'description': ['Indicates whether the TLS should be disabled'], 'type': 'bool', 'default': False}",
    "verify": "{'description': ['Whether or not SSL API requests should be verified. Before 2.3 this defaulted to True.'], 'type': 'bool', 'required': False, 'aliases': ['validate_certs']}",
    "volume_driver": "{'description': ['The name of the driver used for instantiating container volumes'], 'choices': ['cinder', 'rexray']}",
    "wait": "{'description': ['Should ansible wait until the requested resource is complete.'], 'type': 'bool', 'required': False, 'default': True}",
}
```

## Examples


``` yaml

# Create a new Kubernetes cluster template
- os_coe_cluster_template:
    name: k8s
    coe: kubernetes
    keypair_id: mykey
    image_id: 2a8c9888-9054-4b06-a1ca-2bb61f9adb72
    public: no

```

## License

TODO

## Author Information
  - ['Feilong Wang (@flwang)']
