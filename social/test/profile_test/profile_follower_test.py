import unittest
from social.models.user_profile import UserProfile
from social.models.notification import Notification

class MyTestCase(unittest.TestCase):
    def test_follower(self):
        self.assertEqual(2, 2)

    def test_get_profile(self):
        assert False

    def test_add_follower(self):
        assert False

    def test_send_notification(self):
        assert False

    def test_follower_notification(self):
        assert False

    def test_get_all_follower(self):
        assert False

    def test_remove_follower(self):
        assert False

if __name__ == '__main__':
    unittest.main()
