from django.core import exceptions
from social.models.user_profile import UserProfile
from social.views.profile.profile import ProfileView
from social.models.notification import Notification
from social.views.profile.servicer.add_servicer import AddServicer
from social.views.profile.servicer.service_notification import ServiceNotification
from social.views.profile.servicer.list_servicers import ListServicers
from social.views.profile.servicer.remove_servicer import RemoveServicer
import unittest

class MyTestCase(unittest.TestCase):
    def test_add_servicer(self):
        method = AddServicer.as_view()
        user = UserProfile.objects.get(pk=1)
        ProfileView.check_servicer(method, user.services.all(), UserProfile.objects.get(pk=2))

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            user = UserProfile.objects.get(pk=1)
            ProfileView.check_servicer(method, user.services.all(), UserProfile.objects.get(pk=998))
            self.assertTrue('None' in context.exception)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            user = UserProfile.objects.get(pk=999)
            ProfileView.check_servicer(method, user.services.all(), UserProfile.objects.get(pk=2))
            self.assertTrue('None' in context.exception)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            user = UserProfile.objects.get(pk=999)
            ProfileView.check_servicer(method, user.services.all(), UserProfile.objects.get(pk=998))
            self.assertTrue('None' in context.exception)

    def test_get_all_servicer(self):
        method = ListServicers.as_view()
        servicer = UserProfile.objects.get(pk=1)
        servicers = servicer.services.all()
        self.assertTrue(servicers)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            UserProfile.objects.get(pk=999)
            self.assertTrue('None' in context.exception)

    def test_servicer_notification(self):
        method = ServiceNotification.as_view()
        notification = Notification.objects.get(pk=1)
        testservice = ServiceNotification.service_notification(method, notification)
        notification.user_has_seen = True
        self.assertEqual(testservice.user_has_seen, notification.user_has_seen)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            Notification.objects.get(pk=999)
            self.assertTrue('None' in context.exception)

    def test_remove_servicer(self):
        method = RemoveServicer.as_view()
        user_1 = UserProfile.objects.get(pk=1)
        user_2 = UserProfile.objects.get(pk=2)
        test = user_1.services.remove(user_2.user)
        self.assertEqual(test, None)

if __name__ == '__main__':
    unittest.main()
