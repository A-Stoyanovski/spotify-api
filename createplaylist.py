import os
from spotifyclient import SpotifyClient


def main():
    spotify_client = SpotifyClient(os.getenv('SPOTIFY_AUTHORIZATION_TOKEN'),
                                   os.getenv('SPOTIFY_USER_UID'))

    num_tracks_to_visualise = int(input('How many tracks would you like to visualise? '))
    last_played_tracks = spotify_client.get_last_played_tracks(num_tracks_to_visualise)

    print(f'Here are the last {num_tracks_to_visualise} tracks you listened to on Spotify:')
    for index, track in enumerate(last_played_tracks):
        print(f'{index + 1}- {track}')

    indexes = input(
        'Enter a list of up to 5 tracks you\'d like to use as base tracks. Use indexes separated by a single space: ')
    indexes = indexes.split()
    base_tracks = [last_played_tracks[int(index) - 1] for index in indexes]

    recommended_tracks = spotify_client.get_track_recommendations(base_tracks)
    print('Here are the recommended tracks which will be included in your new playlist:')
    for index, track in enumerate(recommended_tracks):
        print(f'{index - 1}- {track}')

    playlist_name = input('How would you like to call your playlist?')
    playlist = spotify_client.create_playlist(playlist_name)
    print(f'Playlist "{playlist.name}" was created successfully!')

    spotify_client.populate_playlist(playlist, recommended_tracks)
    print(f'Recommended tracks were successfully uploaded to playlist "{playlist.name}"!')


if __name__ == '__main__':
    main()
