# Ansible module: ansible.module_win_iis_webapppool


Configure IIS Web Application Pools

## Description

Creates, removes and configures an IIS Web Application Pool.

## Requirements

TODO

## Arguments

``` json
{
    "attributes": "{'description': ['This field is a free form dictionary value for the application pool attributes.', 'These attributes are based on the naming standard at U(https://www.iis.net/configreference/system.applicationhost/applicationpools/add#005), see the examples section for more details on how to set this.', 'You can also set the attributes of child elements like cpu and processModel, see the examples to see how it is done.', 'While you can use the numeric values for enums it is recommended to use the enum name itself, e.g. use SpecificUser instead of 3 for processModel.identityType.', 'managedPipelineMode may be either "Integrated" or "Classic".', 'startMode may be either "OnDemand" or "AlwaysRunning".', 'Use C(state) module parameter to modify the state of the app pool.', "When trying to set 'processModel.password' and you receive a 'Value does fall within the expected range' error, you have a corrupted keystore. Please follow U(http://structuredsight.com/2014/10/26/im-out-of-range-youre-out-of-range/) to help fix your host."]}",
    "name": "{'description': ['Name of the application pool.'], 'required': True}",
    "state": "{'choices': ['absent', 'present', 'restarted', 'started', 'stopped'], 'default': 'present', 'description': ['The state of the application pool.', 'If C(absent) will ensure the app pool is removed.', 'If C(present) will ensure the app pool is configured and exists.', 'If C(restarted) will ensure the app pool exists and will restart, this is never idempotent.', 'If C(started) will ensure the app pool exists and is started.', 'If C(stopped) will ensure the app pool exists and is stopped.']}",
}
```

## Examples


``` yaml

- name: return information about an existing application pool
  win_iis_webapppool:
    name: DefaultAppPool
    state: present

- name: create a new application pool in 'Started' state
  win_iis_webapppool:
    name: AppPool
    state: started

- name: stop an application pool
  win_iis_webapppool:
    name: AppPool
    state: stopped

- name: restart an application pool (non-idempotent)
  win_iis_webapppool:
    name: AppPool
    state: restart

- name: change application pool attributes using new dict style
  win_iis_webapppool:
    name: AppPool
    attributes:
      managedRuntimeVersion: v4.0
      autoStart: no

- name: creates an application pool, sets attributes and starts it
  win_iis_webapppool:
    name: AnotherAppPool
    state: started
    attributes:
      managedRuntimeVersion: v4.0
      autoStart: no

# In the below example we are setting attributes in child element processModel
# https://www.iis.net/configreference/system.applicationhost/applicationpools/add/processmodel
- name: manage child element and set identity of application pool
  win_iis_webapppool:
    name: IdentitiyAppPool
    state: started
    attributes:
      managedPipelineMode: Classic
      processModel.identityType: SpecificUser
      processModel.userName: '{{ansible_user}}'
      processModel.password: '{{ansible_password}}'
      processModel.loadUserProfile: True

- name: manage a timespan attribute
  win_iis_webapppool:
    name: TimespanAppPool
    state: started
    attributes:
      # Timespan with full string "day:hour:minute:second.millisecond"
      recycling.periodicRestart.time: "00:00:05:00.000000"
      recycling.periodicRestart.schedule: ["00:10:00", "05:30:00"]
      # Shortened timespan "hour:minute:second"
      processModel.pingResponseTime: "00:03:00"

```

## License

TODO

## Author Information
  - ['Henrik Wallström (@henrikwallstrom)', 'Jordan Borean (@jborean93)']
  - ['Henrik Wallström (@henrikwallstrom)', 'Jordan Borean (@jborean93)']
