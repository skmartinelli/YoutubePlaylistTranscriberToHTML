import functions.getTranscriptTextFromVidID as getTranscriptTextFromVidID
import functions.getVidIDSFromPlaylist as getVidIDSFromPlaylist
import functions.getTitleFromVidID as getTitleFromVidID
import functions.getPlaylistTitle as getPlaylistTitle

playlistURL = input ("What playlist do you want to parse?")
vidIDs = getVidIDSFromPlaylist.get_video_ids(playlistURL)


html_title = getPlaylistTitle.get_playlist_title(playlistURL) 
html_title += ".html"

# Start of the HTML content
html_content = "<html><head><title>Playlist Transcripts</title></head> <body>"

html_content +="<h1>Full Transcripts from Playlist</h1>"
print("wahoo")

for vidID in vidIDs:
    title = getTitleFromVidID.get_video_title(vidID)
    print("Parsing Transcript for " + title)
    transcript = getTranscriptTextFromVidID.get_transcript(vidID)
    
    # Adding each video's title and transcript to the HTML content
    html_content += f"<h2>{title}</h2><p>{transcript}</p>"

# End of the HTML content
html_content += "</body></html>"


with open(html_title, 'w', encoding='utf-8') as file:
    file.write(html_content)

print("HTML file created successfully.")
