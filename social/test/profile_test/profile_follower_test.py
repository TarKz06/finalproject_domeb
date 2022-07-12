import unittest
from social.models.user_profile import UserProfile


class MyTestCase(unittest.TestCase):
    def test_follower(self):
        self.assertEqual(2, 2)


if __name__ == '__main__':
    unittest.main()
