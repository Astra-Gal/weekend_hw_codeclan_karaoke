import unittest

from src.room import Room
from src.guest import Guest 
from src.song import Song 

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Wannabe", 10)
        self.guest_1 = Guest("Shane MacGowan", 62, 100.00, 3)

    def test_room_has_name(self):
        self.assertEqual("Wannabe", self.room_1.name)

    def test_room_has_capacity(self):
        self.assertEqual(10, self.room_1.capacity)

    def test_check_room_capacity(self):
        self.assertEqual(0, self.room_1.check_capacity())

    # def test_room_can_check_in_guest(self):
    #     self.room_1.check_in_guest(self.guest_1)
