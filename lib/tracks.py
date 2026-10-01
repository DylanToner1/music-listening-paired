class Track:
    def __init__(self, title, artist):
        if not title:
            raise ValueError("Can't have blank title or artist")
        self.title = title.strip()
        self.artist = artist.strip()

    def format(self):
        return f"{self.title} by {self.artist}"


class TrackAlreadyExistsException(Exception):
    pass
