import requests
import urllib


class SpotifyClient(object):
    def __init__(self, api_token):
        self.api_token = api_token

    def serach_song(self, artist, track):
        query = urllib.parse.quote(f'{artist} {track}')
        url = f"https://api.spotify.com/v1/search?q={query}&type=track"

        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        response_json = response.json()

        results = response_json['tracks']['items']
        if results:
            # let's assume the first track in the list is the song we want
            return results[0]['id']

        else:
            raise Exception(f"No song found for {artist} = {track}")

    def add_song_to_spotify(self, song_id):
        print(f"Inside add song to spotify fun, Song Id: {song_id}")
        for song_id in song_id:
            url = "https://api.spotify.com/v1/me/tracks"
            response = requests.put(
                url,
                json={
                    "ids": [song_id]
                },
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.api_token}"
                }
            )
        return response.ok
