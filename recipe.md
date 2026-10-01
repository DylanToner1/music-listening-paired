As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

```python
class MusicLibrary:
    def __init__(self):
        # list of tracks
        self.tracks = []
        pass

    def add_track(self, track):
        # paramaters:
        # track: Track object, the track to add
        # outputs:
        # None
        # effects:
        # add the track to the music library
        pass

    def list_tracks(self):
        # paramaters:
        # None
        # outputs:
        # list of tracks (name), call track.format()
        # effects:
        # none
        pass


class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def format(self):
        # paramaters:
        # none
        # output:
        # title by artist
        # effects:
        # none
        pass
```

## Tests
```python
track = Track("title", "artist")
track.format() => "title by artist"

track = Track("title     ", "artist")
track.format() => "title by artist"

track = Track("", "artist")
raise ValueError("Can't have blank title or artist")



library = MusicLibrary()
library.add_track(track)
library.tracks => [track]

library = MusicLibrary()
library.add_track(track)
library.add_track(track2)
library.list_tracks() => ["title by artist", "title2 by artist2"]


library = MusicLibrary()
library.add_track(track)
library.add_track(track) # try to add it again, does nothing
raise TrackAlreadyExistsException
```