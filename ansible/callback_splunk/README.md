# Ansible callback: ansible.callback_splunk


Sends task result events to Splunk HTTP Event Collector

## Description

This callback plugin will send task results as JSON formatted events to a Splunk HTTP collector.
The companion Splunk Monitoring & Diagnostics App is available here "https://splunkbase.splunk.com/app/4023/"
Credit to "Ryan Currah (@ryancurrah)" for original source upon which this is based.

## Requirements

TODO

## Arguments

``` json
{
    "authtoken": "{'description': ['Token to authenticate the connection to the Splunk HTTP collector'], 'env': [{'name': 'SPLUNK_AUTHTOKEN'}], 'ini': [{'section': 'callback_splunk', 'key': 'authtoken'}]}",
    "url": "{'description': ['URL to the Splunk HTTP collector source'], 'env': [{'name': 'SPLUNK_URL'}], 'ini': [{'section': 'callback_splunk', 'key': 'url'}]}",
}
```

## Examples


``` yaml

examples: >
  To enable, add this to your ansible.cfg file in the defaults block
    [defaults]
    callback_whitelist = splunk
  Set the environment variable
    export SPLUNK_URL=http://mysplunkinstance.datapaas.io:8088/services/collector/event
    export SPLUNK_AUTHTOKEN=f23blad6-5965-4537-bf69-5b5a545blabla88
  Set the ansible.cfg variable in the callback_splunk block
    [callback_splunk]
    url = http://mysplunkinstance.datapaas.io:8088/services/collector/event
    authtoken = f23blad6-5965-4537-bf69-5b5a545blabla88

```

## License

TODO

## Author Information
  - ['Stuart Hirst <support@convergingdata.com>']
