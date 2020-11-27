import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("The Parting Glass", "The Pogues", 2.17)

    def test_song_has_title(self):
        self.assertEqual("The Parting Glass", self.song.title)