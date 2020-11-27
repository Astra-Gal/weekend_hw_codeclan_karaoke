import unittest

from src.guest import Guest 
from src.song import Song 

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Shane MacGowan", 62, 100.00, 3)

    def test_guest_has_name(self):
        self.assertEqual("Shane MacGowan", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(62, self.guest.age)

    def test_guest_has_wallet(self):
        self.assertEqual(100.00, self.guest.wallet)

    def test_guest_has_skill_at_singing_out_of_ten(self):
        self.assertEqual(3, self.guest.skill_at_singing_out_of_ten)
