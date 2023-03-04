import argparse
import getpass
import os
import shutil
from plexapi.server import PlexServer

def print_playlist_files(url:str, token:str, playlist_title:str):
    plex = PlexServer(url, token)

    playlist = plex.playlist(playlist_title)

    for item in playlist.items():
        file_path = item.media[0].parts[0].file
        print(f'{file_path}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print files from a Plex playlist to stdout')
    parser.add_argument('playlist_title', type=str, help='title of the playlist to cat')
    parser.add_argument('-u', '--url', default='http://localhost:32400', type=str, help='URL for the Plex server')
    parser.add_argument('-t', '--token', type=str, help='authentication token')

    args = parser.parse_args()

    print_playlist_files(args.url, args.token, args.playlist_title)

