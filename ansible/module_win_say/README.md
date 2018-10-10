# Ansible module: ansible.module_win_say


Text to speech module for Windows to speak messages and optionally play sounds

## Description

Uses .NET libraries to convert text to speech and optionally play .wav sounds.  Audio Service needs to be running and some kind of speakers or headphones need to be attached to the windows target(s) for the speech to be audible.

## Requirements

TODO

## Arguments

``` json
{
    "end_sound_path": "{'description': ['Full path to a C(.wav) file containing a sound to play after the text has been spoken.', 'Useful on conference calls to alert other speakers that ansible has finished speaking.'], 'type': 'path'}",
    "msg": "{'description': ['The text to be spoken.', 'Use either C(msg) or C(msg_file).', 'Optional so that you can use this module just to play sounds.']}",
    "msg_file": "{'description': ['Full path to a windows format text file containing the text to be spokend.', 'Use either C(msg) or C(msg_file).', 'Optional so that you can use this module just to play sounds.'], 'type': 'path'}",
    "speech_speed": "{'description': ['How fast or slow to speak the text.', 'Must be an integer value in the range -10 to 10.', '-10 is slowest, 10 is fastest.'], 'type': 'int', 'default': 0}",
    "start_sound_path": "{'description': ['Full path to a C(.wav) file containing a sound to play before the text is spoken.', 'Useful on conference calls to alert other speakers that ansible has something to say.'], 'type': 'path'}",
    "voice": "{'description': ['Which voice to use. See notes for how to discover installed voices.', 'If the requested voice is not available the default voice will be used. Example voice names from Windows 10 are C(Microsoft Zira Desktop) and C(Microsoft Hazel Desktop).'], 'default': 'system default voice'}",
}
```

## Examples


``` yaml

- name: Warn of impending deployment
  win_say:
    msg: Warning, deployment commencing in 5 minutes, please log out.

- name: Using a different voice and a start sound
  win_say:
    start_sound_path: C:\Windows\Media\ding.wav
    msg: Warning, deployment commencing in 5 minutes, please log out.
    voice: Microsoft Hazel Desktop

- name: With start and end sound
  win_say:
    start_sound_path: C:\Windows\Media\Windows Balloon.wav
    msg: New software installed
    end_sound_path: C:\Windows\Media\chimes.wav

- name: Text from file example
  win_say:
    start_sound_path: C:\Windows\Media\Windows Balloon.wav
    msg_file: AppData\Local\Temp\morning_report.txt
    end_sound_path: C:\Windows\Media\chimes.wav

```

## License

TODO

## Author Information
  - ['Jon Hawkesworth (@jhawkesworth)']
