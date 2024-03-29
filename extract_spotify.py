import spotipy
import json

from credentials import my_client_id, my_client_secret
from spotipy.oauth2 import SpotifyClientCredentials

#create api
def connect(cl_id, cl_secret):
    sp = spotipy.Spotify(
        auth_manager=SpotifyClientCredentials(
            client_id= my_client_id, client_secret= my_client_secret 
        )
    )
    return sp

#fetch playlist
def fetch_playlist_by_id(api,id):
    playlist_response = api.playlist(playlist_id= id)
    name = playlist_response['name']
    playlist_items = playlist_response['tracks']['items']

    return playlist_items, name

pl_id = '6ZkwfPHoQFEvxtuXf6dUnr'

#run functions

api = connect(my_client_id, my_client_secret)
playlist_items = fetch_playlist_by_id(api, pl_id)

# print(json.dumps(playlist_items)) #test01

#extract song data from playlist items
def extract_data(api, items):
    tracks_data = []
    for i in items:
        item = dict.fromkeys(['track_name','artist_name','album_name'])
        track_name = i['track']['name']
        artist_name = i['track']['artists'][0]['name']
        album_name = i['track']['album']['name']

        item['track_name'] = track_name
        item['artist_name']= artist_name
        item['album_name']= album_name

        tracks_data.append(item)
        # print(item)
    return tracks_data

#build queries to search on yt 
def query_builder(pl_data):
    queries = []
    for obj in pl_data:
        q = "{} {} {}".format(obj['track_name'],obj['album_name'],obj['artist_name'])
        queries.append(q)
    return queries