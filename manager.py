from credentials import my_client_secret, my_client_id,yt_api
from extract_spotify import connect,fetch_playlist_by_id,extract_data,query_builder
from ytOauth import makePlaylist, addItemToPlaylist, makeService
from youtubeapi import getVideoIds

#Insira aqui a playlist a ser migrada
playlist_id = "Your-playlist-id"

def main(pl_id):
    api = connect(my_client_id,my_client_secret)
    items_name = fetch_playlist_by_id(api,pl_id)
    name = items_name[1]
    queries = query_builder(extract_data(api,items_name[0]))
    videoIds = getVideoIds(queries,yt_api)
   
    service = makeService()
    new_play_id = makePlaylist(service,name)
    addItemToPlaylist(service,new_play_id,videoIds)
    print("finished migrating")
    # return queries
    return new_play_id

print(main(playlist_id))