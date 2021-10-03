import redis,boto3,json,uuid,lyricsgenius,os
from flask import Flask,jsonify,request
from decouple import config

#init redis
redis_cache = redis.StrictRedis()
r = redis.Redis()

#redis variables
redis_cache = redis.Redis(config('REDIS_HOST'),config('REDIS_PORT'),config('REDIS_DB'),config('REDIS_PASSWORD'))

#get genius token
genius = lyricsgenius.Genius(config('GENIUS_TOKEN'))

app = Flask(__name__)


#init dynamodb table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('artists')

def get_artist_songs(artist_name):
    if redis_cache.get(artist_name) is not None and request.args.get('cache') != "False":
        return jsonify(json.loads(redis_cache.get(artist_name)))

    if redis_cache.get(artist_name) is not None and request.args.get('cache') == "False":
        artist = genius.search_artist(artist_name, max_songs=10, sort="popularity", include_features=True)
        r.delete(artist_name)
        artist_list = []
        if artist:
            for song in artist.songs:
                artist_info = {
                    "id":song.id,
                    "artist":song.artist,
                    "lyrics":song.lyrics,
                    "song_art_image_thumbnail_url":song.song_art_image_thumbnail_url,
                    "song_art_image_url":song.song_art_image_url,
                    "title":song.title
                    }
                artist_list.append(artist_info)
        else:
            return jsonify({"error":"Error artist not found"}),404
        return jsonify(artist_list),201


    else:
        artist = genius.search_artist(artist_name, max_songs=10, sort="popularity", include_features=True)
        artist_list = []
        if artist:
            for song in artist.songs:
                artist_info = {
                    "id": song.id,
                    "artist":song.artist,
                    "lyrics":song.lyrics,
                    "song_art_image_thumbnail_url":song.song_art_image_thumbnail_url,
                    "song_art_image_url":song.song_art_image_url,
                    "title":song.title
                    }
                dynamoinfo = {
                    "id": str(uuid.uuid4()),
                    "artist":song.artist,
                }
                artist_list.append(artist_info)
            table.put_item(Item=dynamoinfo)
            redis_cache.set(artist_name,json.dumps(artist_list)) 
            redis_cache.expire(artist_name, 604800) # Expiration in one week

        else:
            return jsonify({"error":"Error artist not found"}),404

    return jsonify(artist_list),201

@app.route("/genius/<artist_name>/")
def get(artist_name):
    return get_artist_songs(artist_name)

    
if __name__ == '__main__':
    app.run(debug=True)