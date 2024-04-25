import functions.getTranscriptTextFromVidID as getTranscriptTextFromVidID
import functions.getVidIDSFromPlaylist as getVidIDSFromPlaylist
import functions.getTitleFromVidID as getTitleFromVidID
import functions.getPlaylistTitle as getPlaylistTitle

playlistURL = input ("What playlist do you want to parse?")
filetype = input("What filetype do you want to save it as? Currently supports html and md")
vidIDs = getVidIDSFromPlaylist.get_video_ids(playlistURL)


def createHTML(playlistURL, vidIDs):
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



def createMarkdown(playlistURL, vidIDs):
    md_title = getPlaylistTitle.get_playlist_title(playlistURL) + ".md"
    md_content = "# Full Transcripts from Playlist\n\n"
    for vidID in vidIDs:
        title = getTitleFromVidID.get_video_title(vidID)
        print("Parsing Transcript for " + title)
        transcript = getTranscriptTextFromVidID.get_transcript(vidID)
        md_content += f"## {title}\n\n{transcript}\n\n"
    with open(md_title, 'w', encoding='utf-8') as file:
        file.write(md_content)
    print("Markdown file created successfully.")

if filetype == "html":
    createHTML(playlistURL, vidIDs)
elif filetype == "md":
    createMarkdown(playlistURL, vidIDs)

else:
    print("Invalid filetype")
