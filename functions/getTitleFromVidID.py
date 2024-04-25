from pytube import YouTube

def get_video_title(video_id):
    # Construct the video URL from the given video ID
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    
    # Create a YouTube object
    yt = YouTube(video_url)
    
    # Return the title of the video
    return yt.title


