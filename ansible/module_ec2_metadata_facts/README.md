# Ansible module: ansible.module_ec2_metadata_facts


Gathers facts (instance metadata) about remote hosts within ec2

## Description

This module fetches data from the instance metadata endpoint in ec2 as per http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html. The module must be called from within the EC2 instance itself.

## Requirements

TODO

## Arguments

}
```

## Examples


``` yaml

# Gather EC2 metadata facts
- ec2_metadata_facts:

- debug:
    msg: "This instance is a t1.micro"
  when: ansible_ec2_instance_type == "t1.micro"

```

## License

TODO

## Author Information
  - ['Silviu Dicu (@silviud)', 'Vinay Dandekar (@roadmapper)']
  - ['Silviu Dicu (@silviud)', 'Vinay Dandekar (@roadmapper)']
