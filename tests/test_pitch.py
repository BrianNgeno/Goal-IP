import unittest
from app.models import Pitches

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitches(category = 'Personal_Blog')