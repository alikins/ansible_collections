# Ansible module: ansible.module_azure_rm_webapp


Manage Web App instance

## Description

Create, update and delete instance of Web App.

## Requirements

TODO

## Arguments

``` json
{
    "ad_user": "{'description': ['Active Directory username. Use when authenticating with an Active Directory user rather than service principal.']}",
    "adfs_authority_url": "{'description': ['Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority.'], 'required': False, 'default': None, 'version_added': 2.6}",
    "api_profile": "{'description': ['Selects an API profile to use when communicating with Azure services. Default value of C(latest) is appropriate for public clouds; future values will allow use with Azure Stack.'], 'default': 'latest', 'version_added': 2.5}",
    "app_settings": "{'description': ['Configure web app application settings. Suboptions are in key value pair format.']}",
    "app_state": "{'description': ['Start/Stop/Restart the web app.'], 'type': 'str', 'choices': ['started', 'stopped', 'restarted'], 'default': 'started'}",
    "append_tags": "{'description': ["Use to control if tags field is canonical or just appends to existing tags. When canonical, any tags not found in the tags parameter will be removed from the object's metadata."], 'type': 'bool', 'default': True}",
    "auth_source": "{'description': ['Controls the source of the credentials to use for authentication.', 'If not specified, ANSIBLE_AZURE_AUTH_SOURCE environment variable will be used and default to C(auto) if variable is not defined.', 'C(auto) will follow the default precedence of module parameters -> environment variables -> default profile in credential file C(~/.azure/credentials).', 'When set to C(cli), the credentials will be sources from the default Azure CLI profile.', 'Can also be set via the C(ANSIBLE_AZURE_AUTH_SOURCE) environment variable.', 'When set to C(msi), the host machine must be an azure resource with an enabled MSI extension. C(subscription_id) or the environment variable C(AZURE_SUBSCRIPTION_ID) can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.', 'The C(msi) was added in Ansible 2.6.'], 'choices': ['auto', 'cli', 'credential_file', 'env', 'msi'], 'version_added': 2.5}",
    "cert_validation_mode": "{'description': ['Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing C(ignore). Can also be set via credential file profile or the C(AZURE_CERT_VALIDATION) environment variable.'], 'choices': ['validate', 'ignore'], 'version_added': 2.5}",
    "client_affinity_enabled": "{'description': ['True to enable client affinity; False to stop sending session affinity cookies, which route client requests in the same session to the same instance.'], 'type': 'bool', 'default': True}",
    "client_id": "{'description': ['Azure client ID. Use when authenticating with a Service Principal.']}",
    "cloud_environment": "{'description': ['For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, C(AzureChinaCloud), C(AzureUSGovernment)), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the C(AZURE_CLOUD_ENVIRONMENT) environment variable.'], 'default': 'AzureCloud', 'version_added': 2.4}",
    "container_settings": "{'description': ['Web app container settings.'], 'suboptions': {'name': {'description': 'Name of container. eg. "imagename:tag"'}, 'registry_server_url': {'description': 'Container registry server url. eg. mydockerregistry.io'}, 'registry_server_user': {'description': 'The container registry server user name.'}, 'registry_server_password': {'description': ['The container registry server password.']}}}",
    "deployment_source": "{'description': ['Deployment source for git'], 'suboptions': {'url': {'description': ['Repository url of deployment source.']}, 'branch': {'description': ['The branch name of the repository.']}}}",
    "dns_registration": "{'description': ['If true web app hostname is not registered with DNS on creation.'], 'type': 'bool'}",
    "frameworks": "{'description': ['Set of run time framework settings. Each setting is a dictionary.', 'See U(https://docs.microsoft.com/en-us/azure/app-service/app-service-web-overview) for more info.'], 'suboptions': {'name': {'description': ['Name of the framework.', 'Supported framework list for Windows web app and Linux web app is different.', 'For Windows web app, supported names(June 2018) java, net_framework, php, python, node. Multiple framework can be set at same time.', 'For Linux web app, supported names(June 2018) java, ruby, php, dotnetcore, node. Only one framework can be set.', 'Java framework is mutually exclusive with others.'], 'choices': ['java', 'net_framework', 'php', 'python', 'ruby', 'dotnetcore', 'node']}, 'version': {'description': ['Version of the framework. For Linux web app supported value, see U(https://aka.ms/linux-stacks) for more info.', "net_framework supported value sample, 'v4.0' for .NET 4.6 and 'v3.0' for .NET 3.5.", 'php supported value sample, 5.5, 5.6, 7.0.', 'python supported value sample, e.g., 5.5, 5.6, 7.0.', 'node supported value sample, 6.6, 6.9.', 'dotnetcore supported value sample, 1.0, 1,1, 1.2.', 'ruby supported value sample, 2.3.', 'java supported value sample, 1.8, 1.9 for windows web app. 8 for linux web app.']}, 'settings': {'description': ['List of settings of the framework.'], 'suboptions': {'java_container': {'description': 'Name of Java container. This is supported by specific framework C(java) only. e.g. Tomcat, Jetty.'}, 'java_container_version': {'description': ['Version of Java container. This is supported by specific framework C(java) only.', 'For Tomcat, e.g. 8.0, 8.5, 9.0. For Jetty, e.g. 9.1, 9.3.']}}}}}",
    "https_only": "{'description': ['Configures web site to accept only https requests.'], 'type': 'bool'}",
    "location": "{'description': ['Resource location. If not set, location from the resource group will be used as default.']}",
    "name": "{'description': ['Unique name of the app to create or update. To create or update a deployment slot, use the {slot} parameter.'], 'required': True}",
    "password": "{'description': ['Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.']}",
    "plan": "{'description': ['App service plan. Required for creation.', 'It can be name of existing app service plan in same resource group as web app.', 'It can be resource id of existing app service plan. eg., /subscriptions/<subs_id>/resourceGroups/<resource_group>/providers/Microsoft.Web/serverFarms/<plan_name>', 'It can be a dict which contains C(name), C(resource_group), C(sku), C(is_linux) and C(number_of_workers).', 'C(name). Name of app service plan.', 'C(resource_group). Resource group name of app service plan.', 'C(sku). SKU of app service plan. For allowed sku, please refer to U(https://azure.microsoft.com/en-us/pricing/details/app-service/linux/).', 'C(is_linux). Indicates Linux app service plan. type bool. default False.', 'C(number_of_workers). Number of workers.']}",
    "profile": "{'description': ['Security profile found in ~/.azure/credentials file.']}",
    "purge_app_settings": "{'description': ['Purge any existing application settings. Replace web app application settings with app_settings.'], 'type': 'bool'}",
    "resource_group": "{'description': ['Name of the resource group to which the resource belongs.'], 'required': True}",
    "scm_type": "{'description': ['Repository type of deployment source. Eg. LocalGit, GitHub.', 'Please see U(https://docs.microsoft.com/en-us/rest/api/appservice/webapps/createorupdate#scmtype) for more info.']}",
    "secret": "{'description': ['Azure client secret. Use when authenticating with a Service Principal.']}",
    "skip_custom_domain_verification": "{'description': ['If true, custom (non *.azurewebsites.net) domains associated with web app are not verified.'], 'type': 'bool'}",
    "startup_file": "{'description': ["The web's startup file.", 'This only applies for linux web app.']}",
    "state": "{'description': ['Assert the state of the Web App.', "Use 'present' to create or update a Web App and 'absent' to delete it."], 'default': 'present', 'choices': ['absent', 'present']}",
    "subscription_id": "{'description': ['Your Azure subscription Id.']}",
    "tags": "{'description': ['Dictionary of string:string pairs to assign as metadata to the object. Metadata tags on the object will be updated with any provided values. To remove tags set append_tags option to false.\n']}",
    "tenant": "{'description': ['Azure tenant ID. Use when authenticating with a Service Principal.']}",
    "ttl_in_seconds": "{'description': ['Time to live in seconds for web app default domain name.']}",
}
```

## Examples


``` yaml

    - name: Create a windows web app with non-exist app service plan
      azure_rm_webapp:
        resource_group: myresourcegroup
        name: mywinwebapp
        plan:
          resource_group: myappserviceplan_rg
          name: myappserviceplan
          is_linux: false
          sku: S1

    - name: Create a docker web app with some app settings, with docker image
      azure_rm_webapp:
        resource_group: myresourcegroup
        name: mydockerwebapp
        plan:
          resource_group: appserviceplan_test
          name: myappplan
          is_linux: true
          sku: S1
          number_of_workers: 2
        app_settings:
          testkey: testvalue
          testkey2: testvalue2
        container_settings:
          name: ansible/ansible:ubuntu1404

    - name: Create a docker web app with private acr registry
      azure_rm_webapp:
        resource_group: myresourcegroup
        name: mydockerwebapp
        plan: myappplan
        app_settings:
          testkey: testvalue
        container_settings:
          name: ansible/ubuntu1404
          registry_server_url: myregistry.io
          registry_server_user: user
          registry_server_password: pass

    - name: Create a linux web app with Node 6.6 framework
      azure_rm_webapp:
        resource_group: myresourcegroup
        name: mylinuxwebapp
        plan:
          resource_group: appserviceplan_test
          name: myappplan
        app_settings:
          testkey: testvalue
        frameworks:
          - name: "node"
            version: "6.6"

    - name: Create a windows web app with node, php
      azure_rm_webapp:
        resource_group: myresourcegroup
        name: mywinwebapp
        plan:
          resource_group: appserviceplan_test
          name: myappplan
        app_settings:
          testkey: testvalue
        frameworks:
          - name: "node"
            version: 6.6
          - name: "php"
            version: "7.0"

    - name: Create a linux web app with java framework
      azure_rm_webapp:
        resource_group: myresourcegroup
        name: mylinuxwebapp
        plan:
          resource_group: appserviceplan_test
          name: myappplan
        app_settings:
          testkey: testvalue
        frameworks:
          - name: "java"
            version: "8"
            settings:
              java_container: "Tomcat"
              java_container_version: "8.5"

```

## License

TODO

## Author Information
  - ['Yunge Zhu(@yungezz)']
