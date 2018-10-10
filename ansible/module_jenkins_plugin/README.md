# Ansible module: ansible.module_jenkins_plugin


Add or remove Jenkins plugin

## Description

Ansible module which helps to manage Jenkins plugins.

## Requirements

TODO

## Arguments

``` json
{
    "client_cert": "{'description': ['PEM formatted certificate chain file to be used for SSL client authentication. This file can also include the key as well, and if the key is included, C(client_key) is not required.']}",
    "client_key": "{'description': ['PEM formatted file that contains your private key to be used for SSL client authentication. If C(client_cert) contains both the certificate and key, this option is not required.']}",
    "force": "{'description': ['If C(yes) do not get a cached copy.'], 'aliases': ['thirsty'], 'type': 'bool', 'default': False}",
    "force_basic_auth": "{'description': ['Credentials specified with I(url_username) and I(url_password) should be passed in HTTP Header.'], 'default': False, 'type': 'bool'}",
    "group": "{'description': ['Name of the Jenkins group on the OS.'], 'default': 'jenkins'}",
    "http_agent": "{'description': ['Header to identify as, generally appears in web server logs.'], 'default': 'ansible-httpget'}",
    "jenkins_home": "{'description': ['Home directory of the Jenkins user.'], 'default': '/var/lib/jenkins'}",
    "mode": "{'description': ['File mode applied on versioned plugins.']}",
    "name": "{'description': ['Plugin name.']}",
    "owner": "{'description': ['Name of the Jenkins user on the OS.'], 'default': 'jenkins'}",
    "state": "{'description': ['Desired plugin state.', 'If the C(latest) is set, the check for new version will be performed every time. This is suitable to keep the plugin up-to-date.'], 'choices': ['absent', 'present', 'pinned', 'unpinned', 'enabled', 'disabled', 'latest'], 'default': 'present'}",
    "timeout": "{'description': ['Server connection timeout in secs.'], 'default': 30}",
    "updates_expiration": "{'description': ['Number of seconds after which a new copy of the I(update-center.json) file is downloaded. This is used to avoid the need to download the plugin to calculate its checksum when C(latest) is specified.', 'Set it to C(0) if no cache file should be used. In that case, the plugin file will always be downloaded to calculate its checksum when C(latest) is specified.'], 'default': 86400}",
    "updates_url": "{'description': ['URL of the Update Centre.', 'Used as the base URL to download the plugins and the I(update-center.json) JSON file.'], 'default': 'https://updates.jenkins-ci.org'}",
    "url": "{'description': ['URL of the Jenkins server.'], 'default': 'http://localhost:8080'}",
    "url_password": "{'description': ['The password for use in HTTP basic authentication.', 'If the I(url_username) parameter is not specified, the I(url_password) parameter will not be used.']}",
    "url_username": "{'description': ['The username for use in HTTP basic authentication.', 'This parameter can be used without I(url_password) for sites that allow empty passwords']}",
    "use_proxy": "{'description': ['If C(no), it will not use a proxy, even if one is defined in an environment variable on the target hosts.'], 'type': 'bool', 'default': True}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
    "version": "{'description': ['Plugin version number.', 'If this option is specified, all plugin dependencies must be installed manually.', 'It might take longer to verify that the correct version is installed. This is especially true if a specific version number is specified.', 'Quote the version to prevent the value to be interpreted as float. For example if C(1.20) would be unquoted, it would become C(1.2).']}",
    "with_dependencies": "{'description': ['Defines whether to install plugin dependencies.', 'This option takes effect only if the I(version) is not defined.'], 'type': 'bool', 'default': True}",
}
```

## Examples


``` yaml

- name: Install plugin
  jenkins_plugin:
    name: build-pipeline-plugin

- name: Install plugin without its dependencies
  jenkins_plugin:
    name: build-pipeline-plugin
    with_dependencies: no

- name: Make sure the plugin is always up-to-date
  jenkins_plugin:
    name: token-macro
    state: latest

- name: Install specific version of the plugin
  jenkins_plugin:
    name: token-macro
    version: "1.15"

- name: Pin the plugin
  jenkins_plugin:
    name: token-macro
    state: pinned

- name: Unpin the plugin
  jenkins_plugin:
    name: token-macro
    state: unpinned

- name: Enable the plugin
  jenkins_plugin:
    name: token-macro
    state: enabled

- name: Disable the plugin
  jenkins_plugin:
    name: token-macro
    state: disabled

- name: Uninstall plugin
  jenkins_plugin:
    name: build-pipeline-plugin
    state: absent

#
# Example of how to authenticate
#
- name: Install plugin
  jenkins_plugin:
    name: build-pipeline-plugin
    url_username: admin
    url_password: p4ssw0rd
    url: http://localhost:8888

#
# Example of a Play which handles Jenkins restarts during the state changes
#
- name: Jenkins Master play
  hosts: jenkins-master
  vars:
    my_jenkins_plugins:
      token-macro:
        enabled: yes
      build-pipeline-plugin:
        version: "1.4.9"
        pinned: no
        enabled: yes
  tasks:
    - name: Install plugins without a specific version
      jenkins_plugin:
        name: "{{ item.key }}"
      register: my_jenkins_plugin_unversioned
      when: >
        'version' not in item.value
      with_dict: "{{ my_jenkins_plugins }}"

    - name: Install plugins with a specific version
      jenkins_plugin:
        name: "{{ item.key }}"
        version: "{{ item.value['version'] }}"
      register: my_jenkins_plugin_versioned
      when: >
        'version' in item.value
      with_dict: "{{ my_jenkins_plugins }}"

    - name: Initiate the fact
      set_fact:
        jenkins_restart_required: no

    - name: Check if restart is required by any of the versioned plugins
      set_fact:
        jenkins_restart_required: yes
      when: item.changed
      with_items: "{{ my_jenkins_plugin_versioned.results }}"

    - name: Check if restart is required by any of the unversioned plugins
      set_fact:
        jenkins_restart_required: yes
      when: item.changed
      with_items: "{{ my_jenkins_plugin_unversioned.results }}"

    - name: Restart Jenkins if required
      service:
        name: jenkins
        state: restarted
      when: jenkins_restart_required

    - name: Wait for Jenkins to start up
      uri:
        url: http://localhost:8080
        status_code: 200
        timeout: 5
      register: jenkins_service_status
      # Keep trying for 5 mins in 5 sec intervals
      retries: 60
      delay: 5
      until: >
         'status' in jenkins_service_status and
         jenkins_service_status['status'] == 200
      when: jenkins_restart_required

    - name: Reset the fact
      set_fact:
        jenkins_restart_required: no
      when: jenkins_restart_required

    - name: Plugin pinning
      jenkins_plugin:
        name: "{{ item.key }}"
        state: "{{ 'pinned' if item.value['pinned'] else 'unpinned'}}"
      when: >
        'pinned' in item.value
      with_dict: "{{ my_jenkins_plugins }}"

    - name: Plugin enabling
      jenkins_plugin:
        name: "{{ item.key }}"
        state: "{{ 'enabled' if item.value['enabled'] else 'disabled'}}"
      when: >
        'enabled' in item.value
      with_dict: "{{ my_jenkins_plugins }}"

```

## License

TODO

## Author Information
  - ['Jiri Tyr (@jtyr)']
