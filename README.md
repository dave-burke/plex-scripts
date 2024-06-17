# Plex Scripts

```sh
# Set up virtual environment (1-time after cloning)
python -m venv ./

# If pip goes missing
python -m ensurepip --default-pip

# Updates / dependency changes
pip install --upgrade pip
pip install -r requirements.txt
```

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

## playlist-put.py

This creates a playlist from a text file.

```
usage: playlist-put.py [-h] [-u URL] -t TOKEN playlist_title file_path

Create a Plex playlist from a text file

positional arguments:
  playlist_title          Title of the new playlist
  file_path               Path to the text file with media file paths

options:
  -h, --help              show this help message and exit
  -u URL, --url URL       URL for the Plex server
  -t TOKEN, --token TOKEN Authentication token
```

## Examples

### Copy all files from a playlist to a new directory (like a USB drive)

Assuming that your media is stored in `/mnt/plex`, this will copy your playlist files to a USB mounted at `/mnt/usb`.

```bash
python playlist-cat.py -u "http://localhost:32400" -t "xxx" "My Playlist" | while read file; do
  relative_path="${file#/mnt/plex/}"
  dest_path="/mnt/usb/${relative_path}"
  new_dir="$(dirname ${dest_path})"
  mkdir -p "${new_dir}"
  cp -v "${file}" "${dest_path}"
done
```

### Edit a playlist as a text file

```bash
python playlist-cat.py -u "http://localhost:32400" -t "xxx" "My Playlist" > my-playlist.txt
vim my-playlist.txt
python playlist-put.py -u "http://localhost:32400" -t "xxx" "My New Playlist my-playlist.txt
```

