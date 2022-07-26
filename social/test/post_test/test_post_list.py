from django.core import exceptions
from social.models.user_profile import UserProfile
from social.views.profile.profile import ProfileView
from social.models.notification import Notification
from social.views.profile.servicer.add_servicer import AddServicer
from social.views.profile.servicer.service_notification import ServiceNotification
from social.views.profile.servicer.list_servicers import ListServicers
from social.views.profile.servicer.remove_servicer import RemoveServicer
import unittest

class TestPostListView(unittest.TestCase):
    def test_create_post(self):
        assert True
if __name__ == '__main__':
    unittest.main()