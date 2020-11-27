import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("The Parting Glass", "The Pogues", "Messy Folk-Punk", 2.17)

    def test_song_has_title(self):
        self.assertEqual("The Parting Glass", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("The Pogues", self.song.artist)

    def test_song_has_genre(self):
        self.assertEqual("Messy Folk-Punk", self.song.genre)

    def test_song_has_duration(self):
        self.assertEqual(2.17, self.song.duration)