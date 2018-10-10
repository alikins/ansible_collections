# Ansible module: ansible.module_netact_cm_command


Manage network configuration data in Nokia Core and Radio networks

## Description

n
e
t
a
c
t
_
c
m
_
c
o
m
m
a
n
d
 
c
a
n
 
b
e
 
u
s
e
d
 
t
o
 
r
u
n
 
v
a
r
i
o
u
s
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
m
a
n
a
g
e
m
e
n
t
 
o
p
e
r
a
t
i
o
n
s
.
 
T
h
i
s
 
m
o
d
u
l
e
 
r
e
q
u
i
r
e
s
 
t
h
a
t
 
t
h
e
 
t
a
r
g
e
t
 
h
o
s
t
s
 
h
a
v
e
 
N
o
k
i
a
 
N
e
t
A
c
t
 
n
e
t
w
o
r
k
 
m
a
n
a
g
e
m
e
n
t
 
s
y
s
t
e
m
 
i
n
s
t
a
l
l
e
d
.
 
M
o
d
u
l
e
 
w
i
l
l
 
a
c
c
e
s
s
 
t
h
e
 
C
o
n
f
i
g
u
r
a
t
o
r
 
c
o
m
m
a
n
d
 
l
i
n
e
 
i
n
t
e
r
f
a
c
e
 
i
n
 
N
e
t
A
c
t
 
t
o
 
u
p
l
o
a
d
 
n
e
t
w
o
r
k
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
t
o
 
N
e
t
A
c
t
,
 
r
u
n
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
e
x
p
o
r
t
,
 
p
l
a
n
 
i
m
p
o
r
t
 
a
n
d
 
c
o
n
f
i
g
u
r
a
t
i
o
n
 
p
r
o
v
i
s
i
o
n
 
o
p
e
r
a
t
i
o
n
s
 
T
o
 
s
e
t
 
t
h
e
 
s
c
o
p
e
 
o
f
 
t
h
e
 
o
p
e
r
a
t
i
o
n
,
 
d
e
f
i
n
e
 
D
i
s
t
i
n
g
u
i
s
h
e
d
 
N
a
m
e
 
(
D
N
)
 
o
r
 
W
o
r
k
i
n
g
 
S
e
t
 
(
W
S
)
 
o
r
 
M
a
i
n
t
e
n
a
n
c
e
 
R
e
g
i
o
n
 
(
M
R
)
 
a
s
 
i
n
p
u
t

## Requirements

TODO

## Arguments

``` json
{
    "backupPlanName": "{'description': ['Specifies a backup plan name'], 'required': False}",
    "createBackupPlan": "{'description': ['Specifies if backup plan generation is enabled.'], 'required': False, 'type': 'bool'}",
    "DN": "{'description': ['Sets the exact scope of the operation in form of a list of managed object Distinguished Names (DN) in the network. A single DN or a list of DNs can be given (comma separated list without spaces). Alternatively, if DN or a list of DNs is not given, working set (WS) or Maintenance Region (MR) must be provided as parameter to set the scope of operation.'], 'required': False}",
    "extra_opts": "{'description': ['Extra options to be set for operations. Check Configuration Management > Configuration Management Operating Procedures > Command Line Operations in Nokia NetAct user documentation for further information for extra options.'], 'required': False}",
    "fileFormat": "{'description': ['Indicates file format.'], 'required': False, 'choices': ['RAML2', 'CSV', 'XLSX']}",
    "fileName": "{'description': ['Specifies a file name. Valid for Import and Export operations.'], 'required': False}",
    "inputFile": "{'description': ['Specifies full path to plan file location for the import operation. This parameter (inputFile) or the fileName parameter must be filled. If both are present then the inputFile is used.'], 'required': False}",
    "MR": "{'description': ['Sets the scope of the operation to network elements assigned to a Maintenance Region (MR) Value can be set as MR IDs including the Maintenance Region Collection (MRC) information (for example MRC-FIN1/MR-Hel). Multiple MRs can be given (comma-separated list without spaces) The value of this parameter is searched through MR IDs under given MRC. If there is no match, then it is searched from all MR names. Alternatively, if MR ID or a list or MR IDs is not given, Distinguished Name (DN) or Working Set (WS) must be provided as parameter to set the scope of operation.'], 'required': False}",
    "operation": "{'description': ['Supported operations allow user to upload actual configuration from the network, to import and provision prepared plans, or export reference or actual configuration for planning purposes. Provision_Mass_Modification enables provisioning the same parameters to multiple network elements. This operation supports modifications only to one object class at a time. With this option NetAct Configurator creates and provisions a plan to the network with the given scope and options.'], 'required': True, 'choices': ['upload', 'provision', 'import', 'export', 'Provision_Mass_Modification'], 'aliases': ['op']}",
    "opsName": "{'description': ['user specified operation name'], 'required': False}",
    "planName": "{'description': ['Specifies a plan name.'], 'required': False}",
    "typeOption": "{'description': ['Specifies the type of the export operation.'], 'required': False, 'choices': ['plan', 'actual', 'reference', 'template', 'siteTemplate'], 'aliases': ['type']}",
    "verbose": "{'description': ['NetAct Configurator will print more info'], 'required': False}",
    "WS": "{'description': ['Sets the scope of the operation to use one or more pre-defined working sets (WS) in NetAct. A working set contains network elements selected by user according to defined criteria. A single WS name, or multiple WSs can be provided (comma-separated list without spaces). Alternatively, if a WS name or a list of WSs is not given, Distinguished Name (DN) or Maintenance Region(MR) must be provided as parameter to set the scope of operation.'], 'required': False}",
}
```

## Examples


``` yaml

# Pass in a message
- name: Upload
  netact_cm_command:
    operation: "Upload"
    opsname: 'Uploading_test'
    dn: "PLMN-PLMN/MRBTS-746"
    extra_opts: '-btsContentInUse true'

- name: Provision
  netact_cm_command:
    operation: "Provision"
    opsname: 'Provision_test'
    dn: "PLMN-PLMN/MRBTS-746"
    planName: 'mySiteTemplate'
    type: 'actual'
    createBackupPlan: true
    backupPlanName: 'myBackupPlanName'

- name: Export and fetching data from target
  netact_cm_command:
    operation: "Export"
    opsname: 'Export_test'
    planName: 'mySiteTemplate'
    type: 'actual'
    fileName: 'exportTest.xml'
- fetch:
    src: /var/opt/nokia/oss/global/racops/export/exportTest.xml
    dest: fetched

- name: Import
  netact_cm_command:
    operation: "Import"
    opsname: 'Import_test'
    fileFormat: 'CSV'
    type: 'plan'
    fileName: 'myCSVFile'
    planName: 'myPlanName'
    extra_ops: 'enablePolicyPlans true'

# fail the module
- name: Test failure of the module
  netact_cm_command:
    name: fail me

```

## License

TODO

## Author Information
  - ['Harri Tuominen (@hatuomin)']
