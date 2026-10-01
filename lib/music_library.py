from lib.tracks import TrackAlreadyExistsException


class MusicLibrary:
    def __init__(self):
        # list of tracks
        self.tracks = []

    def add_track(self, new_track):
        for track in self.tracks:
            if track.format() == new_track.format():
                raise TrackAlreadyExistsException
        self.tracks.append(new_track)

    def list_tracks(self):
        return [track.format() for track in self.tracks]
