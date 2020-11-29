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

