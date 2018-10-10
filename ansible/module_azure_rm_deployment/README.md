# Ansible module: ansible.module_azure_rm_deployment


Create or destroy Azure Resource Manager template deployments

## Description

Create or destroy Azure Resource Manager template deployments via the Azure SDK for Python. You can find some quick start templates in GitHub here https://github.com/azure/azure-quickstart-templates. For more information on Azure Resource Manager templates see https://azure.microsoft.com/en-us/documentation/articles/resource-group-template-deploy/.

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
    "cert_validation_mode": "{'description': ['Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing C(ignore). Can also be set via credential file profile or the C(AZURE_CERT_VALIDATION) environment variable.'], 'choices': ['validate', 'ignore'], 'version_added': 2.5}",
    "client_id": "{'description': ['Azure client ID. Use when authenticating with a Service Principal.']}",
    "cloud_environment": "{'description': ['For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, C(AzureChinaCloud), C(AzureUSGovernment)), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the C(AZURE_CLOUD_ENVIRONMENT) environment variable.'], 'default': 'AzureCloud', 'version_added': 2.4}",
    "deployment_mode": "{'description': ['In incremental mode, resources are deployed without deleting existing resources that are not included in the template. In complete mode resources are deployed and existing resources in the resource group not included in the template are deleted.'], 'default': 'incremental', 'choices': ['complete', 'incremental']}",
    "deployment_name": "{'description': ["The name of the deployment to be tracked in the resource group deployment history. Re-using a deployment name will overwrite the previous value in the resource group's deployment history."], 'default': 'ansible-arm'}",
    "location": "{'description': ['The geo-locations in which the resource group will be located.'], 'default': 'westus'}",
    "parameters": "{'description': ['A hash of all the required template variables for the deployment template. This parameter is mutually exclusive with \'parameters_link\'. Either one of them is required if "state" parameter is "present".'], 'type': 'dict'}",
    "parameters_link": "{'description': ['Uri of file containing the parameters body. This parameter is mutually exclusive with \'parameters\'. Either one of them is required if "state" parameter is "present".']}",
    "password": "{'description': ['Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.']}",
    "profile": "{'description': ['Security profile found in ~/.azure/credentials file.']}",
    "resource_group_name": "{'description': ['The resource group name to use or create to host the deployed template'], 'required': True, 'aliases': ['resource_group']}",
    "secret": "{'description': ['Azure client secret. Use when authenticating with a Service Principal.']}",
    "state": "{'description': ['If state is "present", template will be created. If state is "present" and if deployment exists, it will be updated. If state is "absent", stack will be removed.'], 'default': 'present', 'choices': ['present', 'absent']}",
    "subscription_id": "{'description': ['Your Azure subscription Id.']}",
    "tags": "{'description': ['Dictionary of string:string pairs to assign as metadata to the object. Metadata tags on the object will be updated with any provided values. To remove tags set append_tags option to false.\n']}",
    "template": "{'description': ['A hash containing the templates inline. This parameter is mutually exclusive with \'template_link\'. Either one of them is required if "state" parameter is "present".'], 'type': 'dict'}",
    "template_link": "{'description': ['Uri of file containing the template body. This parameter is mutually exclusive with \'template\'. Either one of them is required if "state" parameter is "present".']}",
    "tenant": "{'description': ['Azure tenant ID. Use when authenticating with a Service Principal.']}",
    "wait_for_deployment_completion": "{'description': ['Whether or not to block until the deployment has completed.'], 'type': 'bool', 'default': True}",
    "wait_for_deployment_polling_period": "{'description': ['Time (in seconds) to wait between polls when waiting for deployment completion.'], 'default': 10}",
}
```

## Examples


``` yaml

# Destroy a template deployment
- name: Destroy Azure Deploy
  azure_rm_deployment:
    state: absent
    subscription_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    resource_group_name: dev-ops-cle

# Create or update a template deployment based on uris using parameter and template links
- name: Create Azure Deploy
  azure_rm_deployment:
    state: present
    resource_group_name: dev-ops-cle
    template_link: 'https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-vm-simple-linux/azuredeploy.json'
    parameters_link: 'https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-vm-simple-linux/azuredeploy.parameters.json'

# Create or update a template deployment based on a uri to the template and parameters specified inline.
# This deploys a VM with SSH support for a given public key, then stores the result in 'azure_vms'. The result is then
# used to create a new host group. This host group is then used to wait for each instance to respond to the public IP SSH.
---
- hosts: localhost
  connection: local
  gather_facts: no
  tasks:
    - name: Destroy Azure Deploy
      azure_rm_deployment:
        state: absent
        subscription_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
        resource_group_name: dev-ops-cle

    - name: Create Azure Deploy
      azure_rm_deployment:
        state: present
        subscription_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
        resource_group_name: dev-ops-cle
        parameters:
          newStorageAccountName:
            value: devopsclestorage1
          adminUsername:
            value: devopscle
          dnsNameForPublicIP:
            value: devopscleazure
          location:
            value: West US
          vmSize:
            value: Standard_A2
          vmName:
            value: ansibleSshVm
          sshKeyData:
            value: YOUR_SSH_PUBLIC_KEY
        template_link: 'https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-vm-sshkey/azuredeploy.json'
      register: azure

    - name: Add new instance to host group
      add_host:
        hostname: "{{ item['ips'][0].public_ip }}"
        groupname: azure_vms
      loop: "{{ azure.deployment.instances }}"

    - hosts: azure_vms
      user: devopscle
      tasks:
        - name: Wait for SSH to come up
          wait_for:
            port: 22
            timeout: 2000
            state: started
        - name: echo the hostname of the vm
          shell: hostname

# Deploy an Azure WebApp running a hello world'ish node app
- name: Create Azure WebApp Deployment at http://devopscleweb.azurewebsites.net/hello.js
  azure_rm_deployment:
    state: present
    subscription_id: cbbdaed0-fea9-4693-bf0c-d446ac93c030
    resource_group_name: dev-ops-cle-webapp
    parameters:
      repoURL:
        value: 'https://github.com/devigned/az-roadshow-oss.git'
      siteName:
        value: devopscleweb
      hostingPlanName:
        value: someplan
      siteLocation:
        value: westus
      sku:
        value: Standard
    template_link: 'https://raw.githubusercontent.com/azure/azure-quickstart-templates/master/201-web-app-github-deploy/azuredeploy.json'

# Create or update a template deployment based on an inline template and parameters
- name: Create Azure Deploy
  azure_rm_deployment:
    state: present
    subscription_id: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    resource_group_name: dev-ops-cle

    template:
      $schema: "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#"
      contentVersion: "1.0.0.0"
      parameters:
        newStorageAccountName:
          type: "string"
          metadata:
            description: "Unique DNS Name for the Storage Account where the Virtual Machine's disks will be placed."
        adminUsername:
          type: "string"
          metadata:
            description: "User name for the Virtual Machine."
        adminPassword:
          type: "securestring"
          metadata:
            description: "Password for the Virtual Machine."
        dnsNameForPublicIP:
          type: "string"
          metadata:
            description: "Unique DNS Name for the Public IP used to access the Virtual Machine."
        ubuntuOSVersion:
          type: "string"
          defaultValue: "14.04.2-LTS"
          allowedValues:
            - "12.04.5-LTS"
            - "14.04.2-LTS"
            - "15.04"
          metadata:
            description: >
                         The Ubuntu version for the VM. This will pick a fully patched image of this given Ubuntu version.
                         Allowed values: 12.04.5-LTS, 14.04.2-LTS, 15.04."
      variables:
        location: "West US"
        imagePublisher: "Canonical"
        imageOffer: "UbuntuServer"
        OSDiskName: "osdiskforlinuxsimple"
        nicName: "myVMNic"
        addressPrefix: "192.0.2.0/24"
        subnetName: "Subnet"
        subnetPrefix: "10.0.0.0/24"
        storageAccountType: "Standard_LRS"
        publicIPAddressName: "myPublicIP"
        publicIPAddressType: "Dynamic"
        vmStorageAccountContainerName: "vhds"
        vmName: "MyUbuntuVM"
        vmSize: "Standard_D1"
        virtualNetworkName: "MyVNET"
        vnetID: "[resourceId('Microsoft.Network/virtualNetworks',variables('virtualNetworkName'))]"
        subnetRef: "[concat(variables('vnetID'),'/subnets/',variables('subnetName'))]"
      resources:
        - type: "Microsoft.Storage/storageAccounts"
          name: "[parameters('newStorageAccountName')]"
          apiVersion: "2015-05-01-preview"
          location: "[variables('location')]"
          properties:
            accountType: "[variables('storageAccountType')]"
        - apiVersion: "2015-05-01-preview"
          type: "Microsoft.Network/publicIPAddresses"
          name: "[variables('publicIPAddressName')]"
          location: "[variables('location')]"
          properties:
            publicIPAllocationMethod: "[variables('publicIPAddressType')]"
            dnsSettings:
              domainNameLabel: "[parameters('dnsNameForPublicIP')]"
        - type: "Microsoft.Network/virtualNetworks"
          apiVersion: "2015-05-01-preview"
          name: "[variables('virtualNetworkName')]"
          location: "[variables('location')]"
          properties:
            addressSpace:
              addressPrefixes:
                - "[variables('addressPrefix')]"
            subnets:
              -
                name: "[variables('subnetName')]"
                properties:
                  addressPrefix: "[variables('subnetPrefix')]"
        - type: "Microsoft.Network/networkInterfaces"
          apiVersion: "2015-05-01-preview"
          name: "[variables('nicName')]"
          location: "[variables('location')]"
          dependsOn:
            - "[concat('Microsoft.Network/publicIPAddresses/', variables('publicIPAddressName'))]"
            - "[concat('Microsoft.Network/virtualNetworks/', variables('virtualNetworkName'))]"
          properties:
            ipConfigurations:
              -
                name: "ipconfig1"
                properties:
                  privateIPAllocationMethod: "Dynamic"
                  publicIPAddress:
                    id: "[resourceId('Microsoft.Network/publicIPAddresses',variables('publicIPAddressName'))]"
                  subnet:
                    id: "[variables('subnetRef')]"
        - type: "Microsoft.Compute/virtualMachines"
          apiVersion: "2015-06-15"
          name: "[variables('vmName')]"
          location: "[variables('location')]"
          dependsOn:
            - "[concat('Microsoft.Storage/storageAccounts/', parameters('newStorageAccountName'))]"
            - "[concat('Microsoft.Network/networkInterfaces/', variables('nicName'))]"
          properties:
            hardwareProfile:
              vmSize: "[variables('vmSize')]"
            osProfile:
              computername: "[variables('vmName')]"
              adminUsername: "[parameters('adminUsername')]"
              adminPassword: "[parameters('adminPassword')]"
            storageProfile:
              imageReference:
                publisher: "[variables('imagePublisher')]"
                offer: "[variables('imageOffer')]"
                sku: "[parameters('ubuntuOSVersion')]"
                version: "latest"
              osDisk:
                name: "osdisk"
                vhd:
                  uri: >
                       [concat('http://',parameters('newStorageAccountName'),'.blob.core.windows.net/',variables('vmStorageAccountContainerName'),'/',
                       variables('OSDiskName'),'.vhd')]
                caching: "ReadWrite"
                createOption: "FromImage"
            networkProfile:
              networkInterfaces:
                -
                  id: "[resourceId('Microsoft.Network/networkInterfaces',variables('nicName'))]"
            diagnosticsProfile:
              bootDiagnostics:
                enabled: "true"
                storageUri: "[concat('http://',parameters('newStorageAccountName'),'.blob.core.windows.net')]"
    parameters:
      newStorageAccountName:
        value: devopsclestorage
      adminUsername:
        value: devopscle
      adminPassword:
        value: Password1!
      dnsNameForPublicIP:
        value: devopscleazure

```

## License

TODO

## Author Information
  - ['David Justice (@devigned)', 'Laurent Mazuel (@lmazuel)', 'Andre Price (@obsoleted)']
  - ['David Justice (@devigned)', 'Laurent Mazuel (@lmazuel)', 'Andre Price (@obsoleted)']
  - ['David Justice (@devigned)', 'Laurent Mazuel (@lmazuel)', 'Andre Price (@obsoleted)']
