# Plex Scripts

## playlist-cat.py

This script can be used in a bash script to do any number of things with the files in a playlist, such as copying them to another directory.

```
usage: playlist-cat.py [-h] [-u URL] [-t TOKEN] playlist_title

Print files from a Plex playlist to stdout

positional arguments:
  playlist_title          title of the playlist to copy

options:
  -h, --help              show this help message and exit
  -u URL, --url URL       URL for the Plex server (default: http://localhost:32400)
  -t TOKEN, --token TOKEN Authentication token
```
