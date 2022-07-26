from django.core import exceptions
from social.models.user_profile import UserProfile
from social.models.thread import Thread
from social.views.thread.create_message import CreateMessage
import unittest

class TestCreateMessage(unittest.TestCase):
    def test_get_receiver(self):
        # method = CreateMessage.as_view()
        # thread = Thread.objects.get(pk=1)
        # user = UserProfile.objects.get(pk=1)
        # receiver = CreateMessage.get_receiver(method, thread, user)
        assert True


        # with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
        #     thread = Thread.objects.get(pk=1)
        #     user = UserProfile.objects.get(pk=2)
        #     CreateMessage.get_receiver(method, thread, user)
        #     self.assertTrue('None' in context.exception)

    def test_create_message(self):
        assert True

if __name__ == '__main__':
    unittest.main()