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

### Example

Assuming that your media is stored in `/mnt/plex`, this will copy your playlist files to a USB mounted at `/mnt/usb`.

```bash
python playlist-cat.py -u "http://localhost:32400" -t "xxx" "My Playlist" | while read file; do
  relative_path="${file#/mnt/plex/}"
  dest_path="/mnt/usb/${relative_path}"
  new_dir="$(dirname ${dest_path})"
  mkdir -p "${new_dir}"
  cp -v "${file}" "${dest_path}"
```

