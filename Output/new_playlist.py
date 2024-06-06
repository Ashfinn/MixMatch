from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

def create_youtube_playlist(playlist_name, recommendations):
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=["https://www.googleapis.com/auth/youtube.force-ssl"])
    credentials = flow.run_console()
    youtube = build("youtube", "v3", credentials=credentials)

    request = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": playlist_name,
                "description": "Playlist created with recommendations",
                "tags": ["Music", "Recommendations"],
                "defaultLanguage": "en"
            },
            "status": {
                "privacyStatus": "private"
            }
        }
    )
    response = request.execute()
    playlist_id = response['id']

    for track in recommendations:
        youtube.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": playlist_id,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": track['videoId']
                    }
                }
            }
        ).execute()

create_youtube_playlist("Recommended Playlist", recommendations)
