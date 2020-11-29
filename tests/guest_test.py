import unittest

from src.guest import Guest 
from src.song import Song
from src.room import Room 

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Shane MacGowan", 62, 100.00, 3)

        self.room_1 = Room("Wannabe", 10, 10.00)
        self.room_2 = Room("Simply The Best", 3, 30.00)

        self.song_1 = Song("The Parting Glass", "The Pogues", "Messy Folk-Punk", 2.17)
        self.song_2 = Song("Song 2", "Blur", "Indie", 2.02)
        self.song_3 = Song("Bohemian Rhapsody", "Queen", "Pop-Opera", 5.55)
        self.song_4 = Song("Let It Go", "Idina Menzel/Frozen", "Disney", 4.03)
        self.song_5 = Song("Wonderwall", "Oasis", "Indie", 4.38)
        self.song_6 = Song("I Wanna Dance With Somebody", "Whitney Houston", "Pop", 5.15)

    def test_guest_has_name(self):
        self.assertEqual("Shane MacGowan", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(62, self.guest.age)

    def test_guest_has_wallet(self):
        self.assertEqual(100.00, self.guest.wallet)

    def test_guest_has_skill_at_singing_out_of_ten(self):
        self.assertEqual(3, self.guest.skill_at_singing_out_of_ten)

   