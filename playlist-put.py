import argparse
import os
from plexapi.server import PlexServer
from plexapi.exceptions import NotFound

def create_playlist_from_file(url: str, token: str, playlist_title: str, file_path: str):
    plex = PlexServer(url, token)

    with open(file_path, 'r') as file:
        file_paths = [line.strip() for line in file.readlines()]

    music = plex.library.section('Music')

    print("Loading tracks from server for matching...")
    all_tracks = music.all(libtype="track")
    track_map = {}
    for track in all_tracks:
        if hasattr(track, 'media'):
            for media in track.media:
                if hasattr(media, 'parts'):
                    for part in media.parts:
                        if hasattr(part, 'file'):
                            track_map[part.file] = track
                        else:
                            print(f"No file on {part}")
                else:
                    print(f"No parts on {media}")
        else:
            print(f"No media on {track}")

    media_items = []
    for path in file_paths:
        media = track_map.get(path)
        if media:
            media_items.append(media)
        else:
            print(f"Media not found for path: {path}")

    if not media_items:
        print("No valid media items found. Playlist creation aborted.")
        return

    # Create the playlist
    plex.createPlaylist(playlist_title, items=media_items)

    print(f'Playlist "{playlist_title}" created successfully from {file_path} with {len(media_items)} items.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a Plex playlist from a text file')
    parser.add_argument('playlist_title', type=str, help='Title of the new playlist')
    parser.add_argument('file_path', type=str, help='Path to the text file with media file paths')
    parser.add_argument('-u', '--url', default='http://localhost:32400', type=str, help='URL for the Plex server')
    parser.add_argument('-t', '--token', type=str, required=True, help='Authentication token')

    args = parser.parse_args()

    create_playlist_from_file(args.url, args.token, args.playlist_title, args.file_path)
