
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_CLIENT_ID",
                                               client_secret="YOUR_CLIENT_SECRET",
                                               redirect_uri="YOUR_REDIRECT_URI",
                                               scope="playlist-read-private"))

def get_spotify_playlist(playlist_id):
    results = sp.playlist(playlist_id)
    tracks = results['tracks']['items']
    playlist_data = [{'name': track['track']['name'], 'artist': track['track']['artists'][0]['name']} for track in tracks]
    return playlist_data

playlist_id = "YOUR_SPOTIFY_PLAYLIST_ID"
playlist_data = get_spotify_playlist(playlist_id)
print(playlist_data)
