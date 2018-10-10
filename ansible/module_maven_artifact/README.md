# Ansible module: ansible.module_maven_artifact


Downloads an Artifact from a Maven Repository

## Description

Downloads an artifact from a maven repository given the maven coordinates provided to the module.
Can retrieve snapshots or release versions of the artifact and will resolve the latest available version if one is not available.

## Requirements

TODO

## Arguments

``` json
{
    "artifact_id": "{'description': ['The maven artifactId coordinate'], 'required': True}",
    "attributes": "{'description': ['The attributes the resulting file or directory should have.', 'To get supported flags look at the man page for I(chattr) on the target system.', 'This string should contain the attributes in the same order as the one displayed by I(lsattr).', 'The C(=) operator is assumed as default, otherwise C(+) or C(-) operators need to be included in the string.'], 'aliases': ['attr'], 'version_added': '2.3'}",
    "classifier": "{'description': ['The maven classifier coordinate']}",
    "dest": "{'description': ['The path where the artifact should be written to', 'If file mode or ownerships are specified and destination path already exists, they affect the downloaded file'], 'required': True}",
    "extension": "{'description': ['The maven type/extension coordinate'], 'default': 'jar'}",
    "group": "{'description': ['Name of the group that should own the file/directory, as would be fed to I(chown).']}",
    "group_id": "{'description': ['The Maven groupId coordinate'], 'required': True}",
    "keep_name": "{'description': ["If C(yes), the downloaded artifact's name is preserved, i.e the version number remains part of it.", 'This option only has effect when C(dest) is a directory and C(version) is set to C(latest).'], 'type': 'bool', 'default': False, 'version_added': '2.4'}",
    "mode": "{'description': ['The permissions the resulting file or directory should have.', "For those used to I(/usr/bin/chmod) remember that modes are actually octal numbers. You must either add a leading zero so that Ansible's YAML parser knows it is an octal number (like C(0644) or C(01777)) or quote it (like C('644') or C('1777')) so Ansible receives a string and can do its own conversion from string into number.", 'Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.', 'As of version 1.8, the mode may be specified as a symbolic mode (for example, C(u+rwx) or C(u=rw,g=r,o=r)).', 'As of version 2.6, the mode may also be the special string C(preserve).', 'When set to C(preserve) the file will be given the same permissions as the source file.']}",
    "owner": "{'description': ['Name of the user that should own the file/directory, as would be fed to I(chown).']}",
    "password": "{'description': ['The password to authenticate with to the Maven Repository. Use AWS secret access key of the repository is hosted on S3'], 'aliases': ['aws_secret_access_key']}",
    "repository_url": "{'description': ['The URL of the Maven Repository to download from.', 'Use s3://... if the repository is hosted on Amazon S3, added in version 2.2.', 'Use file://... if the repository is local, added in version 2.6'], 'default': 'http://repo1.maven.org/maven2'}",
    "selevel": "{'description': ['The level part of the SELinux file context.', 'This is the MLS/MCS attribute, sometimes known as the C(range).', 'When set to C(_default), it will use the C(level) portion of the policy if available.'], 'default': 's0'}",
    "serole": "{'description': ['The role part of the SELinux file context.', 'When set to C(_default), it will use the C(role) portion of the policy if available.']}",
    "setype": "{'description': ['The type part of the SELinux file context.', 'When set to C(_default), it will use the C(type) portion of the policy if available.']}",
    "seuser": "{'description': ['The user part of the SELinux file context.', 'By default it uses the C(system) policy, where applicable.', 'When set to C(_default), it will use the C(user) portion of the policy if available.']}",
    "state": "{'description': ['The desired state of the artifact'], 'default': 'present', 'choices': ['present', 'absent']}",
    "timeout": "{'description': ['Specifies a timeout in seconds for the connection attempt'], 'default': 10, 'version_added': '2.3'}",
    "unsafe_writes": "{'description': ['Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target file.', 'By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target files, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted files, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.', "This option allows Ansible to fall back to unsafe methods of updating files when atomic operations fail (however, it doesn't force Ansible to perform unsafe writes).", 'IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.'], 'type': 'bool', 'default': False, 'version_added': '2.2'}",
    "username": "{'description': ['The username to authenticate as to the Maven Repository. Use AWS secret key of the repository is hosted on S3'], 'aliases': ['aws_secret_key']}",
    "validate_certs": "{'description': ['If C(no), SSL certificates will not be validated. This should only be set to C(no) when no other option exists.'], 'type': 'bool', 'default': True, 'version_added': '1.9.3'}",
    "verify_checksum": "{'description': ['If C(never), the md5 checksum will never be downloaded and verified.', 'If C(download), the md5 checksum will be downloaded and verified only after artifact download. This is the default.', 'If C(change), the md5 checksum will be downloaded and verified if the destination already exist, to verify if they are identical. This was the behaviour before 2.6. Since it downloads the md5 before (maybe) downloading the artifact, and since some repository software, when acting as a proxy/cache, return a 404 error if the artifact has not been cached yet, it may fail unexpectedly. If you still need it, you should consider using C(always) instead - if you deal with a checksum, it is better to use it to verify integrity after download.', 'C(always) combines C(download) and C(change).'], 'required': False, 'default': 'download', 'choices': ['never', 'download', 'change', 'always'], 'version_added': '2.6'}",
    "version": "{'description': ['The maven version coordinate'], 'default': 'latest'}",
}
```

## Examples


``` yaml

# Download the latest version of the JUnit framework artifact from Maven Central
- maven_artifact:
    group_id: junit
    artifact_id: junit
    dest: /tmp/junit-latest.jar

# Download JUnit 4.11 from Maven Central
- maven_artifact:
    group_id: junit
    artifact_id: junit
    version: 4.11
    dest: /tmp/junit-4.11.jar

# Download an artifact from a private repository requiring authentication
- maven_artifact:
    group_id: com.company
    artifact_id: library-name
    repository_url: 'https://repo.company.com/maven'
    username: user
    password: pass
    dest: /tmp/library-name-latest.jar

# Download a WAR File to the Tomcat webapps directory to be deployed
- maven_artifact:
    group_id: com.company
    artifact_id: web-app
    extension: war
    repository_url: 'https://repo.company.com/maven'
    dest: /var/lib/tomcat7/webapps/web-app.war

# Keep a downloaded artifact's name, i.e. retain the version
- maven_artifact:
    version: latest
    artifact_id: spring-core
    group_id: org.springframework
    dest: /tmp/
    keep_name: yes

# Download the latest version of the JUnit framework artifact from Maven local
- maven_artifact:
    group_id: junit
    artifact_id: junit
    dest: /tmp/junit-latest.jar
    repository_url: "file://{{ lookup('env','HOME') }}/.m2/repository"

```

## License

TODO

## Author Information
  - ['Chris Schmidt (@chrisisbeef)']
