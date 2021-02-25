from youtube_client import YouTubeClient
from spotify_client import SpotifyClient
import os


def run():
    # 1. Get a list of our playlists from youtube
    # global spotify_song_id, song
    youtube_client = YouTubeClient('./creds/client_secret.json')
    spotify_client = SpotifyClient("BQCUTFUBb4uglkTXAtLd0E0WmkgZiVw6cxiySJXOuIkSj23U9so_XyUY9J2Rg71sBnmmcAoGGe2"
                                   "-IaU8fc-B2shQNPrWj_tp-EPqKQPUzZN3bG2bjOkVpzm6r7CSNRb"
                                   "-7r3pjN5_c5pIpVplJaw7GCmbt2IcgEHeoDdr")
    playlists = youtube_client.get_playlist()

    # 2. Ask which playlist we want to get the music videos from

    for index, playlist in enumerate(playlists):
        print(f"{index}: {playlist.title}")
    choice = int(input("Enter your choice: "))
    chosen_playlist = playlists[choice]
    print(f"You selected: {chosen_playlist.title}")

    # 3. For each video in the playlist, get the song information from youtube

    songs = youtube_client.get_video_from_playlist(chosen_playlist.id)
    print(f"Attempting to add {len(songs)} to spotify")

    # 4. Search for the song on Spotify
    for song in songs:
        spotify_song_id = spotify_client.serach_song(song.artist, song.track)

    # 5. If we found the song, add it to our Spotify liked songs
    if spotify_song_id:
        added_song = spotify_client.add_song_to_spotify(spotify_song_id)
        if added_song:
            print(f"We added {song.artist} - {song.track} successfully")


if __name__ == '__main__':
    run()
