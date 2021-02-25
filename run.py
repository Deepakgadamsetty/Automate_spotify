from youtube_client import YouTubeClient
from spotify_client import SpotifyClient
import os


def run():
    # 1. Get a list of our playlists from youtube
    # global spotify_song_id, song
    youtube_client = YouTubeClient('./creds/client_secret.json')
    spotify_client = SpotifyClient("BQAFONxZ-DWGU5H"
                                   "-xjaja1e2Jm4oPVDZad4af8SDGS4KwhQ6ma0KurPekFGg2YCIBCABD_Fj8VNaVMWQHdIcRiozwhoUHxuullaTfQcFSI8lzKIl3AxM79V5KAU0jwPR6PAPO9hZ00apAbWN7k5u4zbYSFBQBPrSFKq-")
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
    spotify_song_id = []
    for song in songs:
        spotify_song_id.append(spotify_client.serach_song(song.artist, song.track))

        print(f"Inside search fun in run class {song.artist} -- {song.track} -- {spotify_song_id}")

    # 5. If we found the song, add it to our Spotify liked songs
    if spotify_song_id:
        added_song = spotify_client.add_song_to_spotify(spotify_song_id)
        if added_song:
            print(f"We added {song.artist} - {song.track} successfully")


if __name__ == '__main__':
    run()
