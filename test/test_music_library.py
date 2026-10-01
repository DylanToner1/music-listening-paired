from lib.music_library import MusicLibrary
from lib.tracks import Track, TrackAlreadyExistsException
import pytest


def test_track_format():
    track = Track("title", "artist")
    assert track.format() == "title by artist"


def test_track_clean_input():
    track = Track("title     ", "artist")
    assert track.format() == "title by artist"


def test_track_blank_input():
    with pytest.raises(ValueError, match="Can't have blank title or artist"):
        Track("", "artist")


def test_track_is_added():
    library = MusicLibrary()
    track = Track("title", "artist")
    library.add_track(track)
    assert library.tracks == [track]


def test_two_tracks():
    library = MusicLibrary()

    track = Track("title", "artist")
    track2 = Track("title2", "artist2")

    library.add_track(track)
    library.add_track(track2)
    assert library.list_tracks() == ["title by artist", "title2 by artist2"]


def test_does_not_add_same_track():
    library = MusicLibrary()
    track = Track("title", "artist")
    track2 = Track("title", "artist")
    library.add_track(track)
    with pytest.raises(TrackAlreadyExistsException):
        library.add_track(track2)
