# Ansible module: ansible.module_psexec


Runs commands on a remote Windows host based on the PsExec model

## Description

Runs a remote command from a Linux host to a Windows host without WinRM being set up.
Can be run on the Ansible controller to bootstrap Windows hosts to get them ready for WinRM.

## Requirements

TODO

## Arguments

``` json
{
    "arguments": "{'description': ['Any arguments as a single string to use when running the executable.']}",
    "asynchronous": "{'description': ['Will run the command as a detached process and the module returns immediately after starting the processs while the process continues to run in the background.', 'The I(stdout) and I(stderr) return values will be null when this is set to C(yes).', 'The I(stdin) option does not work with this type of process.', 'The I(rc) return value is not set when this is C(yes)'], 'type': 'bool', 'default': False}",
    "connection_password": "{'description': ['The password for I(connection_user).', 'Required if the Kerberos requirements are not installed or the username is a local account to the Windows host.', 'Can be omitted to use a Kerberos principal ticket for the principal set by I(connection_user) if the Kerberos library is installed and the ticket has already been retrieved with the C(kinit) command before.']}",
    "connection_timeout": "{'description': ['The timeout in seconds to wait when receiving the initial SMB negotiate response from the server.'], 'default': 60}",
    "connection_username": "{'description': ['The username to use when connecting to the remote Windows host.', 'This user must be a member of the C(Administrators) group of the Windows host.', 'Required if the Kerberos requirements are not installed or the username is a local account to the Windows host.', 'Can be omitted to use the default Kerberos principal ticket in the local credential cache if the Kerberos library is installed.', 'If I(process_username) is not specified, then the remote process will run under a Network Logon under this account.']}",
    "encrypt": "{'description': ['Will use SMB encryption to encrypt the SMB messages sent to and from the host.', 'This requires the SMB 3 protocol which is only supported from Windows Server 2012 or Windows 8, older versions like Windows 7 or Windows Server 2008 (R2) must set this to C(no) and use no encryption.', 'When setting to C(no), the packets are in plaintext and can be seen by anyone sniffing the network, any process options are included in this.'], 'type': 'bool', 'default': True}",
    "executable": "{'description': ['The executable to run on the Windows host.'], 'required': True}",
    "hostname": "{'description': ['The remote Windows host to connect to, can be either an IP address or a hostname.'], 'required': True}",
    "integrity_level": "{'description': ['The integrity level of the process when I(process_username) is defined and is not equal to C(System).', 'When C(default), the default integrity level based on the system setup.', 'When C(elevated), the command will be run with Administrative rights.', 'When C(limited), the command will be forced to run with non-Administrative rights.'], 'choices': ['limited', 'default', 'elevated'], 'default': 'default'}",
    "interactive": "{'description': ['Will run the process as an interactive process that shows a process Window of the Windows session specified by I(interactive_session).', 'The I(stdout) and I(stderr) return values will be null when this is set to C(yes).', 'The I(stdin) option does not work with this type of process.'], 'type': 'bool', 'default': False}",
    "interactive_session": "{'description': ['The Windows session ID to use when displaying the interactive process on the remote Windows host.', 'This is only valid when I(interactive) is C(yes).', 'The default is C(0) which is the console session of the Windows host.'], 'default': 0}",
    "load_profile": "{'description': ["Runs the remote command with the user's profile loaded."], 'type': 'bool', 'default': True}",
    "port": "{'description': ['The port that the remote SMB service is listening on.'], 'default': 445}",
    "priority": "{'description': ["Set the command's priority on the Windows host.", 'See U(https://msdn.microsoft.com/en-us/library/windows/desktop/ms683211.aspx) for more details.'], 'choices': ['above_normal', 'below_normal', 'high', 'idle', 'normal', 'realtime'], 'default': 'normal'}",
    "process_password": "{'description': ['The password for I(process_username).', 'Required if I(process_username) is defined and not C(System).']}",
    "process_timeout": "{'description': ['The timeout in seconds that is placed upon the running process.', 'A value of C(0) means no timeout.'], 'default': 0}",
    "process_username": "{'description': ['The user to run the process as.', "This can be set to run the process under an Interactive logon of the specified account which bypasses limitations of a Network logon used when this isn't specified.", 'If omitted then the process is run under the same account as I(connection_username) with a Network logon.', 'Set to C(System) to run as the builtin SYSTEM account, no password is required with this account.', 'If I(encrypt) is C(no), the username and password are sent as a simple XOR scrambled byte string that is not encrypted. No special tools are required to get the username and password just knowledge of the protocol.']}",
    "show_ui_on_logon_screen": "{'description': ['Shows the process UI on the Winlogon secure desktop when I(process_username) is C(System).'], 'type': 'bool', 'default': False}",
    "stdin": "{'description': ['Data to send on the stdin pipe once the process has started.', 'This option has no effect when I(interactive) or I(asynchronous) is C(yes).']}",
    "working_directory": "{'description': ['Changes the working directory set when starting the process.'], 'default': 'C:\\Windows\\System32'}",
}
```

## Examples


``` yaml

- name: run a cmd.exe command
  psexec:
    hostname: server
    connection_username: username
    connection_password: password
    executable: cmd.exe
    arguments: /c echo Hello World

- name: run a PowerShell command
  psexec:
    hostname: server.domain.local
    connection_username: username@DOMAIN.LOCAL
    connection_password: password
    executable: powershell.exe
    arguments: Write-Host Hello World

- name: send data through stdin
  psexec:
    hostname: 192.168.1.2
    connection_username: username
    connection_password: password
    executable: powershell.exe
    arguments: '-'
    stdin: |
      Write-Host Hello World
      Write-Error Error Message
      exit 0

- name: Run the process as a different user
  psexec:
    hostname: server
    connection_user: username
    connection_password: password
    executable: whoami.exe
    arguments: /all
    process_username: anotheruser
    process_password: anotherpassword

- name: Run the process asynchronously
  psexec:
    hostname: server
    connection_username: username
    connection_password: password
    executable: cmd.exe
    arguments: /c rmdir C:\temp
    asynchronous: yes

- name: Use Kerberos authentication for the connection (requires smbprotocol[kerberos])
  psexec:
    hostname: host.domain.local
    connection_username: user@DOMAIN.LOCAL
    executable: C:\some\path\to\executable.exe
    arguments: /s

- name: Disable encryption to work with WIndows 7/Server 2008 (R2)
  psexec:
    hostanme: windows-pc
    connection_username: Administrator
    connection_password: Password01
    encrypt: no
    integrity_level: elevated
    process_username: Administrator
    process_password: Password01
    executable: powershell.exe
    arguments: (New-Object -ComObject Microsoft.Update.Session).CreateUpdateInstaller().IsBusy

- name: Download and run ConfigureRemotingForAnsible.ps1 to setup WinRM
  psexec:
    hostname: windows-pc
    connection_username: Administrator
    connection_password: Password01
    encrypt: yes
    executable: powershell.exe
    arguments: '-'
    stdin: |
      $ErrorActionPreference = "Stop"
      $sec_protocols = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::SystemDefault
      $sec_protocols = $sec_protocols -bor [Net.SecurityProtocolType]::Tls12
      [Net.ServicePointManager]::SecurityProtocol = $sec_protocols
      $url = "https://github.com/ansible/ansible/raw/devel/examples/scripts/ConfigureRemotingForAnsible.ps1"
      Invoke-Expression ((New-Object Net.WebClient).DownloadString($url))
      exit

```

## License

TODO

## Author Information
  - ['Jordan Borean (@jborean93)']
