from pytube import Playlist

def get_playlist_title(url):
    try:
        playlist = Playlist(url)
        # Fetch the playlist title
        return playlist.title
    except Exception as e:
        return f"An error occurred: {e}"

