import spotipy
from spotipy.oauth2 import SpotifyOAuth
from SECRETS import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URI))

q = 'Poranek Cyrk Deriglasoff'
search_results = sp.search(q, limit=10, offset=0, type='track', market=None)
if len(search_results['tracks']['items']):
    track_id = search_results['tracks']['items'][0]["id"]
    print(search_results['tracks']['items'][0]["name"])

    audio_features_results = sp.audio_features(tracks=[track_id])[0]
    track_features = dict((key, audio_features_results[key]) for key in ['danceability', 'energy', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo'])
    track_features['popularity'] = search_results['tracks']['items'][0]["popularity"]
    print(track_features)

    artist_id = search_results['tracks']['items'][0]["artists"][0]["id"]
    track_author = sp.artist(artist_id)
    track_genre = track_author["genres"]
    print(track_genre)
    print({})
