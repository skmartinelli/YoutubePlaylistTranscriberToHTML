from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

def get_transcript(vidID):
    try:
        # Retrieve the transcript for the video using the provided video ID
        transcript = YouTubeTranscriptApi.get_transcript(vidID)
        
        # Extract only the text from each transcript entry
        text_transcript = ' '.join([entry['text'] for entry in transcript])
        
        return text_transcript

    except TranscriptsDisabled:
        # Handle the case where transcripts are disabled for the video
        print(f"Transcripts are disabled for the video with ID {vidID}. Skipping...")
        return None

    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"An error occurred while fetching the transcript for video ID {vidID}: {e}")
        return None
