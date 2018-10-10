# Ansible module: ansible.module_ecs_taskdefinition


register a task definition in ecs

## Description

Registers or deregisters task definitions in the Amazon Web Services (AWS) EC2 Container Service (ECS)

## Requirements

TODO

## Arguments

``` json
{
    "arn": "{'description': ['The arn of the task description to delete'], 'required': False}",
    "aws_access_key": "{'description': ['AWS access key. If not set then the value of the AWS_ACCESS_KEY_ID, AWS_ACCESS_KEY or EC2_ACCESS_KEY environment variable is used.'], 'aliases': ['ec2_access_key', 'access_key']}",
    "aws_secret_key": "{'description': ['AWS secret key. If not set then the value of the AWS_SECRET_ACCESS_KEY, AWS_SECRET_KEY, or EC2_SECRET_KEY environment variable is used.'], 'aliases': ['ec2_secret_key', 'secret_key']}",
    "containers": "{'description': ['A list of containers definitions'], 'required': False}",
    "cpu": "{'description': ['The number of cpu units used by the task. If using the EC2 launch type, this field is optional and any value can be used. If using the Fargate launch type, this field is required and you must use one of [256, 512, 1024, 2048, 4096]'], 'required': False, 'version_added': 2.7}",
    "ec2_url": "{'description': ['Url to use to connect to EC2 or your Eucalyptus cloud (by default the module will use EC2 endpoints). Ignored for modules where region is required. Must be specified for all other modules if region is not used. If not set then the value of the EC2_URL environment variable, if any, is used.']}",
    "execution_role_arn": "{'description': ['The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.'], 'required': False, 'version_added': 2.7}",
    "family": "{'description': ['A Name that would be given to the task definition'], 'required': False}",
    "force_create": "{'description': ['Always create new task definition'], 'required': False, 'version_added': 2.5}",
    "launch_type": "{'description': ['The launch type on which to run your task'], 'required': False, 'version_added': 2.7, 'choices': ['EC2', 'FARGATE']}",
    "memory": "{'description': ['The amount (in MiB) of memory used by the task. If using the EC2 launch type, this field is optional and any value can be used. If using the Fargate launch type, this field is required and is limited by the cpu'], 'required': False, 'version_added': 2.7}",
    "network_mode": "{'description': ['The Docker networking mode to use for the containers in the task.', 'C(awsvpc) mode was added in Ansible 2.5'], 'required': False, 'default': 'bridge', 'choices': ['bridge', 'host', 'none', 'awsvpc'], 'version_added': 2.3}",
    "profile": "{'description': ['Uses a boto profile. Only works with boto >= 2.24.0.'], 'version_added': '1.6'}",
    "region": "{'description': ['The AWS region to use. If not specified then the value of the AWS_REGION or EC2_REGION environment variable, if any, is used. See U(http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region)'], 'required': False, 'aliases': ['aws_region', 'ec2_region']}",
    "revision": "{'description': ['A revision number for the task definition'], 'required': False}",
    "security_token": "{'description': ['AWS STS security token. If not set then the value of the AWS_SECURITY_TOKEN or EC2_SECURITY_TOKEN environment variable is used.'], 'aliases': ['access_token'], 'version_added': '1.6'}",
    "state": "{'description': ['State whether the task definition should exist or be deleted'], 'required': True, 'choices': ['present', 'absent']}",
    "task_role_arn": "{'description': ['The Amazon Resource Name (ARN) of the IAM role that containers in this task can assume. All containers in this task are granted the permissions that are specified in this role.'], 'required': False, 'version_added': 2.3}",
    "validate_certs": "{'description': ['When set to "no", SSL certificates will not be validated for boto versions >= 2.6.0.'], 'type': 'bool', 'default': True, 'version_added': '1.5'}",
    "volumes": "{'description': ['A list of names of volumes to be attached'], 'required': False}",
}
```

## Examples


``` yaml

- name: Create task definition
  ecs_taskdefinition:
    containers:
    - name: simple-app
      cpu: 10
      essential: true
      image: "httpd:2.4"
      memory: 300
      mountPoints:
      - containerPath: /usr/local/apache2/htdocs
        sourceVolume: my-vol
      portMappings:
      - containerPort: 80
        hostPort: 80
      logConfiguration:
        logDriver: awslogs
        options:
          awslogs-group: ecs
          awslogs-region: us-west-2
    - name: busybox
      command:
        - >
          /bin/sh -c "while true; do echo '<html><head><title>Amazon ECS Sample App</title></head><body><div><h1>Amazon ECS Sample App</h1><h2>Congratulations!
          </h2><p>Your application is now running on a container in Amazon ECS.</p>' > top; /bin/date > date ; echo '</div></body></html>' > bottom;
          cat top date bottom > /usr/local/apache2/htdocs/index.html ; sleep 1; done"
      cpu: 10
      entryPoint:
      - sh
      - "-c"
      essential: false
      image: busybox
      memory: 200
      volumesFrom:
      - sourceContainer: simple-app
    volumes:
    - name: my-vol
    family: test-cluster-taskdef
    state: present
  register: task_output

- name: Create task definition
  ecs_taskdefinition:
    family: nginx
    containers:
    - name: nginx
      essential: true
      image: "nginx"
      portMappings:
      - containerPort: 8080
        hostPort:      8080
      cpu: 512
      memory: 1GB
    state: present

- name: Create task definition
  ecs_taskdefinition:
    family: nginx
    containers:
    - name: nginx
      essential: true
      image: "nginx"
      portMappings:
      - containerPort: 8080
        hostPort:      8080
    launch_type: FARGATE
    cpu: 512
    memory: 1GB
    state: present
    network_mode: awsvpc

```

## License

TODO

## Author Information
  - ['Mark Chance (@Java1Guy)']
