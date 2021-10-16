from os import getenv

from dotenv import find_dotenv, load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv(find_dotenv())
CLIENT_ID = getenv('CLIENT_ID')
CLIENT_SECRET = getenv('CLIENT_SECRET')
REDIRECT_URI = getenv('REDIRECT_URI')
SCOPES = getenv('SCOPES')

TID = 'spotify:track:{id}'
TRACK = '/track/'
SONG_ID_LENGTH = 22

TRACK_FEATURES = """
```
  Tempo:    {tempo} BPM
  Key:      {key} {mode}
  Loudness: {loudness} dB

  Danceability:    {danceability} %
  Energy:          {energy} %
  Speechiness:     {speechiness} %
  Acousticness:    {acousticness} %
  Instrumentalness:{instrumentalness} %
  Liveness:        {liveness} %
  Valence:         {valence} %
```
"""

KEY_CODE_TO_KEY_NOTICE = {
    0: 'C',
    1: 'C#',
    2: 'D',
    3: 'D#',
    4: 'E',
    5: 'F',
    6: 'F#',
    7: 'G',
    8: 'G#',
    9: 'A',
    10: 'Bb',
    11: 'H',
}

MODE_CODE_TO_MODE_NOTICE = {
    0: 'Minor',
    1: 'Major'
}


def get_song_data(uri):
    sp = Spotify(auth_manager=SpotifyClientCredentials(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    ))

    def get_track_title(tid):
        data = sp.track(tid)
        artist = data['album']['artists'][0]['name']
        title = data['name']
        release_year = data['album']['release_date'][:4]
        return f'*{artist} — {title} ({release_year})*'

    def get_track_features(tid):
        data = sp.audio_features(tid)[0]
        danceability = str(int(data['danceability'] * 100))
        energy = str(int(data['energy'] * 100))
        key = KEY_CODE_TO_KEY_NOTICE[data['key']]
        loudness = data['loudness']
        mode = MODE_CODE_TO_MODE_NOTICE[data['mode']]
        speechiness = str(int(data['speechiness'] * 100))
        acousticness = str(int(data['acousticness'] * 100))
        instrumentalness = str(int(data['instrumentalness'] * 100))
        liveness = str(int(data['liveness'] * 100))
        valence = str(int(data['valence'] * 100))
        tempo = data['tempo']
        return TRACK_FEATURES.format(
            danceability=danceability.rjust(3),
            energy=energy.rjust(3),
            key=key,
            loudness=loudness,
            mode=mode,
            speechiness=speechiness.rjust(3),
            acousticness=acousticness.rjust(3),
            instrumentalness=instrumentalness.rjust(3),
            liveness=liveness.rjust(3),
            valence=valence.rjust(3),
            tempo=tempo
        )

    track_pnt = uri.find(TRACK)
    if track_pnt == -1:
        return (
            """
            URI format unrecognized!
            Correct URI format is:
            https://open.spotify.com/track/TRACK_ID
            """
        )
    start = track_pnt + len(TRACK)
    song_id = uri[start:start + SONG_ID_LENGTH]
    tid = TID.format(id=song_id)
    result = ''
    result += get_track_title(tid)
    result += get_track_features(tid)
    return result
