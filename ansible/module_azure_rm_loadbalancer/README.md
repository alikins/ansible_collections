# Ansible module: ansible.module_azure_rm_loadbalancer


Manage Azure load balancers

## Description

Create, update and delete Azure load balancers

## Requirements

TODO

## Arguments

``` json
{
    "ad_user": "{'description': ['Active Directory username. Use when authenticating with an Active Directory user rather than service principal.']}",
    "adfs_authority_url": "{'description': ['Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority.'], 'required': False, 'default': None, 'version_added': 2.6}",
    "api_profile": "{'description': ['Selects an API profile to use when communicating with Azure services. Default value of C(latest) is appropriate for public clouds; future values will allow use with Azure Stack.'], 'default': 'latest', 'version_added': 2.5}",
    "append_tags": "{'description': ["Use to control if tags field is canonical or just appends to existing tags. When canonical, any tags not found in the tags parameter will be removed from the object's metadata."], 'type': 'bool', 'default': True}",
    "auth_source": "{'description': ['Controls the source of the credentials to use for authentication.', 'If not specified, ANSIBLE_AZURE_AUTH_SOURCE environment variable will be used and default to C(auto) if variable is not defined.', 'C(auto) will follow the default precedence of module parameters -> environment variables -> default profile in credential file C(~/.azure/credentials).', 'When set to C(cli), the credentials will be sources from the default Azure CLI profile.', 'Can also be set via the C(ANSIBLE_AZURE_AUTH_SOURCE) environment variable.', 'When set to C(msi), the host machine must be an azure resource with an enabled MSI extension. C(subscription_id) or the environment variable C(AZURE_SUBSCRIPTION_ID) can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.', 'The C(msi) was added in Ansible 2.6.'], 'choices': ['auto', 'cli', 'credential_file', 'env', 'msi'], 'version_added': 2.5}",
    "backend_address_pools": "{'description': ['List of backend address pools'], 'suboptions': {'name': {'description': 'Name of the backend address pool.', 'required': True}}, 'version_added': 2.5}",
    "backend_port": "{'description': ['(deprecated) Backend port that will be exposed for the load balancer.', 'This option has been deprecated, and will be removed in 2.9. Use I(load_balancing_rules) instead.']}",
    "cert_validation_mode": "{'description': ['Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing C(ignore). Can also be set via credential file profile or the C(AZURE_CERT_VALIDATION) environment variable.'], 'choices': ['validate', 'ignore'], 'version_added': 2.5}",
    "client_id": "{'description': ['Azure client ID. Use when authenticating with a Service Principal.']}",
    "cloud_environment": "{'description': ['For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, C(AzureChinaCloud), C(AzureUSGovernment)), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the C(AZURE_CLOUD_ENVIRONMENT) environment variable.'], 'default': 'AzureCloud', 'version_added': 2.4}",
    "frontend_ip_configurations": "{'description': ['List of frontend IPs to be used'], 'suboptions': {'name': {'description': 'Name of the frontend ip configuration.', 'required': True}, 'public_ip_address': {'description': 'Name of an existing public IP address object in the current resource group to associate with the security group.'}, 'private_ip_address': {'description': 'The reference of the Public IP resource.', 'version_added': 2.6}, 'private_ip_allocation_method': {'description': 'The Private IP allocation method.', 'choices': ['Static', 'Dynamic'], 'version_added': 2.6}, 'subnet': {'description': ['The reference of the subnet resource.', "Should be an existing subnet's resource id."], 'version_added': 2.6}}, 'version_added': 2.5}",
    "frontend_port": "{'description': ['(deprecated) Frontend port that will be exposed for the load balancer.', 'This option has been deprecated, and will be removed in 2.9. Use I(load_balancing_rules) instead.']}",
    "idle_timeout": "{'description': ['(deprecated) Timeout for TCP idle connection in minutes.', 'This option has been deprecated, and will be removed in 2.9. Use I(load_balancing_rules) instead.'], 'default': 4}",
    "inbound_nat_pools": "{'description': ['Defines an external port range for inbound NAT to a single backend port on NICs associated with a load balancer.', 'Inbound NAT rules are created automatically for each NIC associated with the Load Balancer using an external port from this range.', 'Defining an Inbound NAT pool on your Load Balancer is mutually exclusive with defining inbound Nat rules.', 'Inbound NAT pools are referenced from virtual machine scale sets.', 'NICs that are associated with individual virtual machines cannot reference an inbound NAT pool.', 'They have to reference individual inbound NAT rules.'], 'suboptions': {'name': {'description': 'Name of the inbound NAT pool.', 'required': True}, 'frontend_ip_configuration_name': {'description': 'A reference to frontend IP addresses.', 'required': True}, 'protocol': {'description': 'IP protocol for the NAT pool', 'choices': ['Tcp', 'Udp', 'All'], 'default': 'Tcp'}, 'frontend_port_range_start': {'description': ['The first port in the range of external ports that will be used to provide inbound NAT to NICs associated with the load balancer.', 'Acceptable values range between 1 and 65534.'], 'required': True}, 'frontend_port_range_end': {'description': ['The last port in the range of external ports that will be used to provide inbound NAT to NICs associated with the load balancer.', 'Acceptable values range between 1 and 65535.'], 'required': True}, 'backend_port': {'description': ['The port used for internal connections on the endpoint.', 'Acceptable values are between 1 and 65535.']}}, 'version_added': 2.5}",
    "load_balancing_rules": "{'description': ['Object collection representing the load balancing rules Gets the provisioning.'], 'suboptions': {'name': {'description': 'name of the load balancing rule.', 'required': True}, 'frontend_ip_configuration': {'description': 'A reference to frontend IP addresses.', 'required': True}, 'backend_address_pool': {'description': 'A reference to a pool of DIPs. Inbound traffic is randomly load balanced across IPs in the backend IPs.', 'required': True}, 'probe': {'description': 'The name of the load balancer probe this rule should use for health checks.', 'required': True}, 'protocol': {'description': 'IP protocol for the load balancing rule.', 'choices': ['Tcp', 'Udp', 'All'], 'default': 'Tcp'}, 'load_distribution': {'description': ['The session persistence policy for this rule; C(Default) is no persistence.'], 'choices': ['Default', 'SourceIP', 'SourceIPProtocol'], 'default': 'Default'}, 'frontend_port': {'description': ['The port for the external endpoint.', 'Frontend port numbers must be unique across all rules within the load balancer.', 'Acceptable values are between 0 and 65534.', 'Note that value 0 enables "Any Port"']}, 'backend_port': {'description': ['The port used for internal connections on the endpoint.', 'Acceptable values are between 0 and 65535.', 'Note that value 0 enables "Any Port"']}, 'idle_timeout': {'description': ['The timeout for the TCP idle connection.', 'The value can be set between 4 and 30 minutes.', 'The default value is 4 minutes.', 'This element is only used when the protocol is set to TCP.']}, 'enable_floating_ip': {'description': ['Configures SNAT for the VMs in the backend pool to use the publicIP address specified in the frontend of the load balancing rule.']}}, 'version_added': 2.5}",
    "load_distribution": "{'description': ['(deprecated) The type of load distribution that the load balancer will employ.', 'This option has been deprecated, and will be removed in 2.9. Use I(load_balancing_rules) instead.'], 'choices': ['Default', 'SourceIP', 'SourceIPProtocol']}",
    "location": "{'description': ['Valid azure location. Defaults to location of the resource group.']}",
    "name": "{'description': ['Name of the load balancer.'], 'required': True}",
    "natpool_backend_port": "{'description': ['(deprecated) Backend port used by the NAT pool.', 'This option has been deprecated, and will be removed in 2.9. Use I(inbound_nat_pools) instead.']}",
    "natpool_frontend_port_end": "{'description': ['(deprecated) End of the port range for a NAT pool.', 'This option has been deprecated, and will be removed in 2.9. Use I(inbound_nat_pools) instead.']}",
    "natpool_frontend_port_start": "{'description': ['(deprecated) Start of the port range for a NAT pool.', 'This option has been deprecated, and will be removed in 2.9. Use I(inbound_nat_pools) instead.']}",
    "natpool_protocol": "{'description': ['(deprecated) The protocol for the NAT pool.', 'This option has been deprecated, and will be removed in 2.9. Use I(inbound_nat_pools) instead.']}",
    "password": "{'description': ['Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.']}",
    "probe_fail_count": "{'description': ['(deprecated) The amount of probe failures for the load balancer to make a health determination.', 'This option has been deprecated, and will be removed in 2.9. Use I(probes) instead.'], 'default': 3}",
    "probe_interval": "{'description': ['(deprecated) Time (in seconds) between endpoint health probes.', 'This option has been deprecated, and will be removed in 2.9. Use I(probes) instead.'], 'default': 15}",
    "probe_port": "{'description': ['(deprecated) The port that the health probe will use.', 'This option has been deprecated, and will be removed in 2.9. Use I(probes) instead.']}",
    "probe_protocol": "{'description': ['(deprecated) The protocol to use for the health probe.', 'This option has been deprecated, and will be removed in 2.9. Use I(probes) instead.'], 'choices': ['Tcp', 'Http']}",
    "probe_request_path": "{'description': ['(deprecated) The URL that an HTTP probe will use (only relevant if probe_protocol is set to Http).', 'This option has been deprecated, and will be removed in 2.9. Use I(probes) instead.']}",
    "probes": "{'description': ['List of probe definitions used to check endpoint health.'], 'suboptions': {'name': {'description': 'Name of the probe.', 'required': True}, 'port': {'description': 'Probe port for communicating the probe. Possible values range from 1 to 65535, inclusive.', 'required': True}, 'protocol': {'description': ['The protocol of the end point to be probed.', "If 'Tcp' is specified, a received ACK is required for the probe to be successful.", "If 'Http' is specified, a 200 OK response from the specified URL is required for the probe to be successful."], 'choices': ['Tcp', 'Http'], 'default': 'Tcp'}, 'interval': {'description': ['The interval, in seconds, for how frequently to probe the endpoint for health status.', 'Slightly less than half the allocated timeout period, which allows two full probes before taking the instance out of rotation.', 'The default value is 15, the minimum value is 5.'], 'default': 15}, 'fail_count': {'description': ['The number of probes where if no response, will result in stopping further traffic from being delivered to the endpoint.', 'This values allows endpoints to be taken out of rotation faster or slower than the typical times used in Azure.'], 'default': 3, 'aliases': ['number_of_probes']}, 'request_path': {'description': ['The URI used for requesting health status from the VM.', 'Path is required if a protocol is set to http. Otherwise, it is not allowed.']}}, 'version_added': 2.5}",
    "profile": "{'description': ['Security profile found in ~/.azure/credentials file.']}",
    "protocol": "{'description': ['(deprecated) The protocol (TCP or UDP) that the load balancer will use.', 'This option has been deprecated, and will be removed in 2.9. Use I(load_balancing_rules) instead.'], 'choices': ['Tcp', 'Udp']}",
    "public_ip_address_name": "{'description': ['(deprecated) Name of an existing public IP address object to associate with the security group.', 'This option has been deprecated, and will be removed in 2.9. Use I(frontend_ip_configurations) instead.'], 'aliases': ['public_ip_address', 'public_ip_name', 'public_ip']}",
    "resource_group": "{'description': ['Name of a resource group where the load balancer exists or will be created.'], 'required': True}",
    "secret": "{'description': ['Azure client secret. Use when authenticating with a Service Principal.']}",
    "sku": "{'description': ['The load balancer SKU.'], 'choices': ['Basic', 'Standard'], 'version_added': 2.6}",
    "state": "{'description': ['Assert the state of the load balancer. Use C(present) to create/update a load balancer, or C(absent) to delete one.'], 'default': 'present', 'choices': ['absent', 'present']}",
    "subscription_id": "{'description': ['Your Azure subscription Id.']}",
    "tags": "{'description': ['Dictionary of string:string pairs to assign as metadata to the object. Metadata tags on the object will be updated with any provided values. To remove tags set append_tags option to false.\n']}",
    "tenant": "{'description': ['Azure tenant ID. Use when authenticating with a Service Principal.']}",
}
```

## Examples


``` yaml

- name: create load balancer
  azure_rm_loadbalancer:
    resource_group: testrg
    name: testloadbalancer1
    frontend_ip_configurations:
      - name: frontendipconf0
        public_ip_address: testpip
    backend_address_pools:
      - name: backendaddrpool0
    probes:
      - name: prob0
        port: 80
    inbound_nat_pools:
      - name: inboundnatpool0
        frontend_ip_configuration_name: frontendipconf0
        protocol: Tcp
        frontend_port_range_start: 80
        frontend_port_range_end: 81
        backend_port: 8080
    load_balancing_rules:
      - name: lbrbalancingrule0
        frontend_ip_configuration: frontendipconf0
        backend_address_pool: backendaddrpool0
        frontend_port: 80
        backend_port: 80
        probe: prob0

```

## License

TODO

## Author Information
  - ['Thomas Stringer (@tstringer)', 'Yuwei Zhou (@yuwzho)']
  - ['Thomas Stringer (@tstringer)', 'Yuwei Zhou (@yuwzho)']
