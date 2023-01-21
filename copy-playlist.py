import argparse
import getpass
import os
import shutil
from plexapi.server import PlexServer

def copy_playlist_files(url:str, token:str, playlist_title:str, target_dir:str):
    plex = PlexServer(url, token)

    playlist = plex.playlist(playlist_title)

    for item in playlist.items():
        file_path = item.media[0].parts[0].file
        print(f'{file_path} -> {target_dir}')
        #shutil.copy2(file_path, target_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Copy files from a Plex playlist to a specified target directory')
    parser.add_argument('playlist_title', type=str, help='title of the playlist to copy')
    parser.add_argument('target_dir', type=str, help='directory to copy the files to')
    parser.add_argument('-u', '--url', default='http://localhost:32400', type=str, help='URL for the Plex server')
    parser.add_argument('-t', '--token', type=str, help='authentication token')

    args = parser.parse_args()

    copy_playlist_files(args.url, args.token, args.playlist_title, args.target_dir)

