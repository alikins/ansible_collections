# Ansible module: ansible.module_win_dotnet_ngen


Runs ngen to recompile DLLs after .NET  updates

## Description

After .NET framework is installed/updated, Windows will probably want to recompile things to optimise for the host.
This happens via scheduled task, usually at some inopportune time.
This module allows you to run this task on your own schedule, so you incur the CPU hit at some more convenient and controlled time.
U(http://blogs.msdn.com/b/dotnet/archive/2013/08/06/wondering-why-mscorsvw-exe-has-high-cpu-usage-you-can-speed-it-up.aspx)

## Requirements

TODO

## Arguments

}
```

## Examples


``` yaml

- name: run ngen tasks
  win_dotnet_ngen:

```

## License

TODO

## Author Information
  - ['Peter Mounce (@petemounce)']
