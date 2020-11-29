import unittest

from src.room import Room
from src.guest import Guest 
from src.song import Song 

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Wannabe", 10)
        self.room_2 = Room("Simply The Best", 3)

        self.guest_1 = Guest("Shane MacGowan", 62, 100.00, 3)
        self.guest_2 = Guest("Tina Turner", 81, 50.00, 9)
        self.guest_3 = Guest("Angel Olsen", 33, 25.00, 7)
        self.guest_4 = Guest("Emma Kirkby", 71, 40.00, 10)
        self.guest_5 = Guest("Little Tiny Baby", 1, 100.00, 2)
        self.guest_6 = Guest("Poor Paul", 18, 1.00, 8)

        self.song_1 = Song("The Parting Glass", "The Pogues", "Messy Folk-Punk", 2.17)
        self.song_2 = Song("Song 2", "Blur", "Indie", 2.02)
        self.song_3 = Song("Bohemian Rhapsody", "Queen", "Pop-Opera", 5.55)
        self.song_4 = Song("Let It Go", "Idina Menzel/Frozen", "Disney", 4.03)
        self.song_5 = Song("Wonderwall", "Oasis", "Indie", 4.38)
        self.song_6 = Song("I Wanna Dance With Somebody", "Whitney Houston", "Pop", 5.15)


    def test_room_has_name(self):
        self.assertEqual("Wannabe", self.room_1.name)

    def test_room_has_capacity(self):
        self.assertEqual(10, self.room_1.capacity)

    def test_check_room_capacity_starts_at_0(self):
        self.assertEqual(0, self.room_1.check_capacity())

    def test_room_can_check_in_guest(self):
        self.room_1.check_in_guest(self.guest_1)
        self.assertEqual(1, self.room_1.check_capacity())

    def test_room_cannot_check_in_too_many_guests(self):
        self.room_2.check_in_guest(self.guest_1)
        self.room_2.check_in_guest(self.guest_2)
        self.room_2.check_in_guest(self.guest_3)
        self.room_2.check_in_guest(self.guest_4)
        self.assertEqual("Sorry! Over Capacity", self.room_2.check_in_guest(self.guest_4))

    def test_guest_is_old_enough__returns_true(self):
        self.assertEqual(True, self.room_1.guest_is_old_enough(self.guest_1))

    def test_guest_is_old_enough__returns_false(self):
        self.assertEqual(False, self.room_1.guest_is_old_enough(self.guest_5))
 
    def test_guest_can_add_song_to_playlist(self):
        self.room_1.add_song_to_playlist(self.song_2)
        self.assertEqual(1, self.room_1.playlist_length())