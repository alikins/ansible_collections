# Ansible module: ansible.module_twilio


Sends a text message to a mobile phone through Twilio

## Description

Sends a text message to a phone number through the Twilio messaging API.

## Requirements

TODO

## Arguments

``` json
{
    "account_sid": "{'description': ["user's Twilio account token found on the account page"], 'required': True}",
    "auth_token": "{'description': ["user's Twilio authentication token"], 'required': True}",
    "from_number": "{'description': ['the Twilio number to send the text message from, format +15551112222'], 'required': True}",
    "media_url": "{'description': ['a URL with a picture, video or sound clip to send with an MMS (multimedia message) instead of a plain SMS'], 'required': False}",
    "msg": "{'description': ['the body of the text message'], 'required': True}",
    "to_numbers": "{'description': ['one or more phone numbers to send the text message to, format +15551112222'], 'required': True, 'aliases': ['to_number']}",
}
```

## Examples


``` yaml

# send an SMS about the build status to (555) 303 5681
# note: replace account_sid and auth_token values with your credentials
# and you have to have the 'from_number' on your Twilio account
- twilio:
    msg: All servers with webserver role are now configured.
    account_sid: ACXXXXXXXXXXXXXXXXX
    auth_token: ACXXXXXXXXXXXXXXXXX
    from_number: +15552014545
    to_number: +15553035681
  delegate_to: localhost

# send an SMS to multiple phone numbers about the deployment
# note: replace account_sid and auth_token values with your credentials
# and you have to have the 'from_number' on your Twilio account
- twilio:
    msg: This server configuration is now complete.
    account_sid: ACXXXXXXXXXXXXXXXXX
    auth_token: ACXXXXXXXXXXXXXXXXX
    from_number: +15553258899
    to_numbers:
      - +15551113232
      - +12025551235
      - +19735559010
  delegate_to: localhost

# send an MMS to a single recipient with an update on the deployment
# and an image of the results
# note: replace account_sid and auth_token values with your credentials
# and you have to have the 'from_number' on your Twilio account
- twilio:
    msg: Deployment complete!
    account_sid: ACXXXXXXXXXXXXXXXXX
    auth_token: ACXXXXXXXXXXXXXXXXX
    from_number: +15552014545
    to_number: +15553035681
    media_url: https://demo.twilio.com/logo.png
  delegate_to: localhost

```

## License

TODO

## Author Information
  - ['Matt Makai (@makaimc)']
