# Ansible callback: ansible.callback_sumologic


Sends task result events to Sumologic

## Description

This callback plugin will send task results as JSON formatted events to a Sumologic HTTP collector source

## Requirements

TODO

## Arguments

``` json
{
    "url": "{'description': ['URL to the Sumologic HTTP collector source'], 'env': [{'name': 'SUMOLOGIC_URL'}], 'ini': [{'section': 'callback_sumologic', 'key': 'url'}]}",
}
```

## Examples


``` yaml

examples: >
  To enable, add this to your ansible.cfg file in the defaults block
    [defaults]
    callback_whitelist = sumologic

  Set the environment variable
    export SUMOLOGIC_URL=https://endpoint1.collection.us2.sumologic.com/receiver/v1/http/R8moSv1d8EW9LAUFZJ6dbxCFxwLH6kfCdcBfddlfxCbLuL-BN5twcTpMk__pYy_cDmp==

  Set the ansible.cfg variable in the callback_sumologic block
    [callback_sumologic]
    url = https://endpoint1.collection.us2.sumologic.com/receiver/v1/http/R8moSv1d8EW9LAUFZJ6dbxCFxwLH6kfCdcBfddlfxCbLuL-BN5twcTpMk__pYy_cDmp==

```

## License

TODO

## Author Information
  - ['Ryan Currah (@ryancurrah)']
