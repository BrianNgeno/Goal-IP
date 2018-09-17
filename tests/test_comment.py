import unittest
from app.models import Comments

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_comment =Comments( comment_name = 'lol')