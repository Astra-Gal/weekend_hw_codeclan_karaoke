import unittest

from src.guest import Guest 
from src.song import Song 

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Shane MacGowan", 62, 100.00, 3)

    def test_guest_has_name(self):
        self.assertEqual("Shane MacGowan", self.guest.name)
