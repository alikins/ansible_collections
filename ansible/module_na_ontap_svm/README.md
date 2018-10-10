# Ansible module: ansible.module_na_ontap_svm


Manage NetApp ONTAP svm

## Description

Create, modify or delete svm on NetApp ONTAP

## Requirements

TODO

## Arguments

``` json
{
    "aggr_list": "{'description': ['List of aggregates assigned for volume operations.', 'These aggregates could be shared for use with other Vservers.', 'When specified as part of a vserver-create, this field represents the list of aggregates that are assigned to the Vserver for volume operations.', 'When part of vserver-get-iter call, this will return the list of Vservers which have any of the aggregates specified as part of the aggr-list.']}",
    "allowed_protocols": "{'description': ['Allowed Protocols.', 'When specified as part of a vserver-create, this field represent the list of protocols allowed on the Vserver.', 'When part of vserver-get-iter call, this will return the list of Vservers which have any of the protocols specified as part of the allowed-protocols.', 'When part of vserver-modify, this field should include the existing list along with new protocol list to be added to prevent data disruptions.', 'Possible values', 'nfs   NFS protocol,', 'cifs   CIFS protocol,', 'fcp   FCP protocol,', 'iscsi   iSCSI protocol,', 'ndmp   NDMP protocol,', 'http   HTTP protocol,', 'nvme   NVMe protocol']}",
    "from_name": "{'description': ['Name of the SVM to be renamed'], 'version_added': '2.7'}",
    "hostname": "{'required': True, 'description': ['The hostname or IP address of the ONTAP instance.']}",
    "http_port": "{'description': ['Override the default port (80 or 443) with this port'], 'type': 'int'}",
    "https": "{'description': ['Enable and disable https'], 'type': 'bool', 'default': False}",
    "ipspace": "{'description': ['IPSpace name', 'Cannot be modified after creation.'], 'version_added': '2.7'}",
    "language": "{'description': ['Language to use for the SVM', 'Default to C.UTF-8', 'Possible values   Language', 'c                 POSIX', 'ar                Arabic', 'cs                Czech', 'da                Danish', 'de                German', 'en                English', 'en_us             English (US)', 'es                Spanish', 'fi                Finnish', 'fr                French', 'he                Hebrew', 'hr                Croatian', 'hu                Hungarian', 'it                Italian', 'ja                Japanese euc-j', 'ja_v1             Japanese euc-j', 'ja_jp.pck         Japanese PCK (sjis)', 'ja_jp.932         Japanese cp932', 'ja_jp.pck_v2      Japanese PCK (sjis)', 'ko                Korean', 'no                Norwegian', 'nl                Dutch', 'pl                Polish', 'pt                Portuguese', 'ro                Romanian', 'ru                Russian', 'sk                Slovak', 'sl                Slovenian', 'sv                Swedish', 'tr                Turkish', 'zh                Simplified Chinese', 'zh.gbk            Simplified Chinese (GBK)', 'zh_tw             Traditional Chinese euc-tw', 'zh_tw.big5        Traditional Chinese Big 5'], 'version_added': '2.7'}",
    "name": "{'description': ['The name of the SVM to manage.'], 'required': True}",
    "password": "{'required': True, 'description': ['Password for the specified user.'], 'aliases': ['pass']}",
    "root_volume": "{'description': ['Root volume of the SVM.', 'Cannot be modified after creation.']}",
    "root_volume_aggregate": "{'description': ['The aggregate on which the root volume will be created.', 'Cannot be modified after creation.']}",
    "root_volume_security_style": "{'description': ['Security Style of the root volume.', 'When specified as part of the vserver-create, this field represents the security style for the Vserver root volume.', 'When specified as part of vserver-get-iter call, this will return the list of matching Vservers.', "The 'unified' security style, which applies only to Infinite Volumes, cannot be applied to a Vserver's root volume.", 'Cannot be modified after creation.'], 'choices': ['unix', 'ntfs', 'mixed', 'unified']}",
    "snapshot_policy": "{'description': ['Default snapshot policy setting for all volumes of the Vserver. This policy will be assigned to all volumes created in this Vserver unless the volume create request explicitly provides a snapshot policy or volume is modified later with a specific snapshot policy. A volume-level snapshot policy always overrides the default Vserver-wide snapshot policy.'], 'version_added': '2.7'}",
    "state": "{'description': ['Whether the specified SVM should exist or not.'], 'choices': ['present', 'absent'], 'default': 'present'}",
    "subtype": "{'description': ['The subtype for vserver to be created.', 'Cannot be modified after creation.'], 'choices': ['default', 'dp_destination', 'sync_source', 'sync_destination'], 'version_added': '2.7'}",
    "username": "{'required': True, 'description': ['This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required. For more information, please read the documentation U(https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/).'], 'aliases': ['user']}",
    "validate_certs": "{'description': ['If set to C(False), the SSL certificates will not be validated.', 'This should only set to C(False) used on personally controlled sites using self-signed certificates.'], 'default': True, 'type': 'bool'}",
}
```

## Examples


``` yaml


    - name: Create SVM
      na_ontap_svm:
        state: present
        name: ansibleVServer
        root_volume: vol1
        root_volume_aggregate: aggr1
        root_volume_security_style: mixed
        hostname: "{{ netapp_hostname }}"
        username: "{{ netapp_username }}"
        password: "{{ netapp_password }}"


```

## License

TODO

## Author Information
  - ['NetApp Ansible Team (ng-ansibleteam@netapp.com)']
