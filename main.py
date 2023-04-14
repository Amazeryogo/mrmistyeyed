import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials
from keys import *
from pprint import pprint

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id = SPOTIPY_CLIENT_ID, client_secret = SPOTIPY_CLIENT_SECRET))

response = sp.current_user_saved_tracks()
results = response["items"]

pprint(response)
