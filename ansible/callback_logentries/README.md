# Ansible callback: ansible.callback_logentries


Sends events to Logentries

## Description

This callback plugin will generate JSON objects and send them to Logentries via TCP for auditing/debugging purposes.
Before 2.4, if you wanted to use an ini configuration, the file must be placed in the same directory as this plugin and named logentries.ini
In 2.4 and above you can just put it in the main Ansible configuration file.

## Requirements

TODO

## Arguments

``` json
{
    "api": "{'description': ['URI to the Logentries API'], 'env': [{'name': 'LOGENTRIES_API'}], 'default': 'data.logentries.com', 'ini': [{'section': 'callback_logentries', 'key': 'api'}]}",
    "flatten": "{'description': ['flatten complex data structures into a single dictionary with complex keys'], 'type': 'boolean', 'default': False, 'env': [{'name': 'LOGENTRIES_FLATTEN'}], 'ini': [{'section': 'callback_logentries', 'key': 'flatten'}]}",
    "port": "{'description': ['HTTP port to use when connecting to the API'], 'env': [{'name': 'LOGENTRIES_PORT'}], 'default': 80, 'ini': [{'section': 'callback_logentries', 'key': 'port'}]}",
    "tls_port": "{'description': ['Port to use when connecting to the API when TLS is enabled'], 'env': [{'name': 'LOGENTRIES_TLS_PORT'}], 'default': 443, 'ini': [{'section': 'callback_logentries', 'key': 'tls_port'}]}",
    "token": "{'description': ['The logentries "TCP token"'], 'env': [{'name': 'LOGENTRIES_ANSIBLE_TOKEN'}], 'required': True, 'ini': [{'section': 'callback_logentries', 'key': 'token'}]}",
    "use_tls": "{'description': ['Toggle to decide whether to use TLS to encrypt the communications with the API server'], 'env': [{'name': 'LOGENTRIES_USE_TLS'}], 'default': False, 'type': 'boolean', 'ini': [{'section': 'callback_logentries', 'key': 'use_tls'}]}",
}
```

## Examples


``` yaml

examples: >
  To enable, add this to your ansible.cfg file in the defaults block

    [defaults]
    callback_whitelist = logentries

  Either set the environment variables
    export LOGENTRIES_API=data.logentries.com
    export LOGENTRIES_PORT=10000
    export LOGENTRIES_ANSIBLE_TOKEN=dd21fc88-f00a-43ff-b977-e3a4233c53af

  Or in the main Ansible config file
    [callback_logentries]
    api = data.logentries.com
    port = 10000
    tls_port = 20000
    use_tls = no
    token = dd21fc88-f00a-43ff-b977-e3a4233c53af
    flatten = False

```

## License

TODO

## Author Information
  - ['UNKNOWN']
