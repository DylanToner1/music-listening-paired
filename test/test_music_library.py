from lib.music_library import MusicLibrary
from lib.tracks import Track
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