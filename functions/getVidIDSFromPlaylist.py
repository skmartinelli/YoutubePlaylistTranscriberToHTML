import re
from pytube import Playlist

def get_video_ids(playlist_url):
    # Create a Playlist object
    playlist = Playlist(playlist_url)
    
    # This fixes the empty playlist.videos list
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    # Extract and print video IDs
    video_ids = [video.video_id for video in playlist.videos]
    return video_ids

