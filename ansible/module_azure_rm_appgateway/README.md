# Ansible module: ansible.module_azure_rm_appgateway


Manage Application Gateway instance

## Description

Create, update and delete instance of Application Gateway.

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
    "authentication_certificates": "{'description': ['Authentication certificates of the application gateway resource.'], 'suboptions': {'data': {'description': ['Certificate public data - base64 encoded pfx']}, 'name': {'description': ['Name of the resource that is unique within a resource group. This name can be used to access the resource.']}}}",
    "backend_address_pools": "{'description': ['List of backend address pool of the application gateway resource.'], 'suboptions': {'backend_addresses': {'description': ['List of backend addresses'], 'suboptions': {'fqdn': {'description': ['Fully qualified domain name (FQDN).']}, 'ip_address': {'description': ['IP address']}}}, 'name': {'description': ['Resource that is unique within a resource group. This name can be used to access the resource.']}}}",
    "backend_http_settings_collection": "{'description': ['Backend http settings of the application gateway resource.'], 'suboptions': {'port': {'description': ['Port']}, 'protocol': {'description': ['Protocol.'], 'choices': ['http', 'https']}, 'cookie_based_affinity': {'description': ['Cookie based affinity.'], 'choices': ['enabled', 'disabled']}, 'request_timeout': {'description': ['Request timeout in seconds. Application Gateway will fail the request if response is not received within RequestTimeout. Acceptable va lues are from 1 second to 86400 seconds.']}, 'authentication_certificates': {'description': ['List of references to application gateway authentication certificates.'], 'suboptions': {'id': {'description': ['Resource ID.']}}}, 'host_name': {'description': ['Host header to be sent to the backend servers.']}, 'pick_host_name_from_backend_address': {'description': ['Whether to pick host header should be picked from the host name of the backend server. Default value is false.']}, 'affinity_cookie_name': {'description': ['Cookie name to use for the affinity cookie.']}, 'path': {'description': ['Path which should be used as a prefix for all C(http) requests. Null means no path will be prefixed. Default value is null.']}, 'name': {'description': ['Name of the resource that is unique within a resource group. This name can be used to access the resource.']}}}",
    "cert_validation_mode": "{'description': ['Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing C(ignore). Can also be set via credential file profile or the C(AZURE_CERT_VALIDATION) environment variable.'], 'choices': ['validate', 'ignore'], 'version_added': 2.5}",
    "client_id": "{'description': ['Azure client ID. Use when authenticating with a Service Principal.']}",
    "cloud_environment": "{'description': ['For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, C(AzureChinaCloud), C(AzureUSGovernment)), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the C(AZURE_CLOUD_ENVIRONMENT) environment variable.'], 'default': 'AzureCloud', 'version_added': 2.4}",
    "frontend_ip_configurations": "{'description': ['Frontend IP addresses of the application gateway resource.'], 'suboptions': {'private_ip_address': {'description': ['PrivateIPAddress of the network interface IP Configuration.']}, 'private_ip_allocation_method': {'description': ['PrivateIP allocation method.'], 'choices': ['static', 'dynamic']}, 'subnet': {'description': ['Reference of the subnet resource.']}, 'public_ip_address': {'description': ['Reference of the PublicIP resource.']}, 'name': {'description': ['Name of the resource that is unique within a resource group. This name can be used to access the resource.']}}}",
    "frontend_ports": "{'description': ['List of frontend ports of the application gateway resource.'], 'suboptions': {'port': {'description': ['Frontend port']}, 'name': {'description': ['Name of the resource that is unique within a resource group. This name can be used to access the resource.']}}}",
    "gateway_ip_configurations": "{'description': ['List of subnets used by the application gateway.'], 'suboptions': {'subnet': {'description': ['Reference of the subnet resource. A subnet from where application gateway gets its private address.']}, 'name': {'description': ['Name of the resource that is unique within a resource group. This name can be used to access the resource.']}}}",
    "http_listeners": "{'description': ['List of HTTP listeners of the application gateway resource.'], 'suboptions': {'frontend_ip_configuration': {'description': ['Frontend IP configuration resource of an application gateway.']}, 'frontend_port': {'description': ['Frontend port resource of an application gateway.']}, 'protocol': {'description': ['Protocol.'], 'choices': ['http', 'https']}, 'host_name': {'description': ['Host name of C(http) listener.']}, 'ssl_certificate': {'description': ['SSL certificate resource of an application gateway.']}, 'require_server_name_indication': {'description': ['Applicable only if I(protocol) is C(https). Enables SNI for multi-hosting.']}, 'name': {'description': ['Name of the resource that is unique within a resource group. This name can be used to access the resource.']}}}",
    "location": "{'description': ['Resource location. If not set, location from the resource group will be used as default.']}",
    "name": "{'description': ['The name of the application gateway.'], 'required': True}",
    "password": "{'description': ['Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.']}",
    "profile": "{'description': ['Security profile found in ~/.azure/credentials file.']}",
    "request_routing_rules": "{'description': ['List of request routing rules of the application gateway resource.'], 'suboptions': {'rule_type': {'description': ['Rule I(type).'], 'choices': ['basic', 'path_based_routing']}, 'backend_address_pool': {'description': ['Backend address pool resource of the application gateway.']}, 'backend_http_settings': {'description': ['Frontend port resource of the application gateway.']}, 'http_listener': {'description': ['Http listener resource of the application gateway.']}, 'name': {'description': ['Name of the resource that is unique within a resource group. This name can be used to access the resource.']}}}",
    "resource_group": "{'description': ['The name of the resource group.'], 'required': True}",
    "secret": "{'description': ['Azure client secret. Use when authenticating with a Service Principal.']}",
    "sku": "{'description': ['SKU of the application gateway resource.'], 'suboptions': {'name': {'description': ['Name of an application gateway SKU.'], 'choices': ['standard_small', 'standard_medium', 'standard_large', 'waf_medium', 'waf_large']}, 'tier': {'description': ['Tier of an application gateway.'], 'choices': ['standard', 'waf']}, 'capacity': {'description': ['Capacity (instance count) of an application gateway.']}}}",
    "ssl_certificates": "{'description': ['SSL certificates of the application gateway resource.'], 'suboptions': {'data': {'description': ['Base-64 encoded pfx certificate.']}, 'password': {'description': ['Password for the pfx file specified in I(data).']}, 'name': {'description': ['Name of the resource that is unique within a resource group. This name can be used to access the resource.']}}}",
    "ssl_policy": "{'description': ['SSL policy of the application gateway resource.'], 'suboptions': {'disabled_ssl_protocols': {'description': ['List of SSL protocols to be disabled on application gateway.'], 'choices': ['tls_v1_0', 'tls_v1_1', 'tls_v1_2']}, 'policy_type': {'description': ['Type of SSL Policy.'], 'choices': ['predefined', 'custom']}, 'policy_name': {'description': ['Name of Ssl C(predefined) policy.'], 'choices': ['ssl_policy20150501', 'ssl_policy20170401', 'ssl_policy20170401_s']}, 'cipher_suites': {'description': ['List of SSL cipher suites to be enabled in the specified order to application gateway.'], 'choices': ['tls_ecdhe_rsa_with_aes_256_gcm_sha384', 'tls_ecdhe_rsa_with_aes_128_gcm_sha256', 'tls_ecdhe_rsa_with_aes_256_cbc_sha384', 'tls_ecdhe_rsa_with_aes_128_cbc_sha256', 'tls_ecdhe_rsa_with_aes_256_cbc_sha', 'tls_ecdhe_rsa_with_aes_128_cbc_sha', 'tls_dhe_rsa_with_aes_256_gcm_sha384', 'tls_dhe_rsa_with_aes_128_gcm_sha256', 'tls_dhe_rsa_with_aes_256_cbc_sha', 'tls_dhe_rsa_with_aes_128_cbc_sha', 'tls_rsa_with_aes_256_gcm_sha384', 'tls_rsa_with_aes_128_gcm_sha256', 'tls_rsa_with_aes_256_cbc_sha256', 'tls_rsa_with_aes_128_cbc_sha256', 'tls_rsa_with_aes_256_cbc_sha', 'tls_rsa_with_aes_128_cbc_sha', 'tls_ecdhe_ecdsa_with_aes_256_gcm_sha384', 'tls_ecdhe_ecdsa_with_aes_128_gcm_sha256', 'tls_ecdhe_ecdsa_with_aes_256_cbc_sha384', 'tls_ecdhe_ecdsa_with_aes_128_cbc_sha256', 'tls_ecdhe_ecdsa_with_aes_256_cbc_sha', 'tls_ecdhe_ecdsa_with_aes_128_cbc_sha', 'tls_dhe_dss_with_aes_256_cbc_sha256', 'tls_dhe_dss_with_aes_128_cbc_sha256', 'tls_dhe_dss_with_aes_256_cbc_sha', 'tls_dhe_dss_with_aes_128_cbc_sha', 'tls_rsa_with_3des_ede_cbc_sha', 'tls_dhe_dss_with_3des_ede_cbc_sha']}, 'min_protocol_version': {'description': ['Minimum version of Ssl protocol to be supported on application gateway.'], 'choices': ['tls_v1_0', 'tls_v1_1', 'tls_v1_2']}}}",
    "state": "{'description': ["Assert the state of the Public IP. Use 'present' to create or update a and 'absent' to delete."], 'default': 'present', 'choices': ['absent', 'present']}",
    "subscription_id": "{'description': ['Your Azure subscription Id.']}",
    "tags": "{'description': ['Dictionary of string:string pairs to assign as metadata to the object. Metadata tags on the object will be updated with any provided values. To remove tags set append_tags option to false.\n']}",
    "tenant": "{'description': ['Azure tenant ID. Use when authenticating with a Service Principal.']}",
}
```

## Examples


``` yaml

- name: Create instance of Application Gateway
  azure_rm_appgateway:
    resource_group: myresourcegroup
    name: myappgateway
    sku:
      name: standard_small
      tier: standard
      capacity: 2
    gateway_ip_configurations:
      - subnet:
          id: "{{ subnet_id }}"
        name: app_gateway_ip_config
    frontend_ip_configurations:
      - subnet:
          id: "{{ subnet_id }}"
        name: sample_gateway_frontend_ip_config
    frontend_ports:
      - port: 90
        name: ag_frontend_port
    backend_address_pools:
      - backend_addresses:
          - ip_address: 10.0.0.4
        name: test_backend_address_pool
    backend_http_settings_collection:
      - port: 80
        protocol: http
        cookie_based_affinity: enabled
        name: sample_appgateway_http_settings
    http_listeners:
      - frontend_ip_configuration: sample_gateway_frontend_ip_config
        frontend_port: ag_frontend_port
        name: sample_http_listener
    request_routing_rules:
      - rule_type: Basic
        backend_address_pool: test_backend_address_pool
        backend_http_settings: sample_appgateway_http_settings
        http_listener: sample_http_listener
        name: rule1

```

## License

TODO

## Author Information
  - ['Zim Kalinowski (@zikalino)']
