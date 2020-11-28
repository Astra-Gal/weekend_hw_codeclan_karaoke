import unittest

from src.room import Room
from src.guest import Guest 
from src.song import Song 

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Wannabe", 10)

    def test_room_has_name(self):
        self.assertEqual("Wannabe", self.room_1.name)

    def test_room_has_capacity(self):
        self.assertEqual(10, self.room_1.capacity)