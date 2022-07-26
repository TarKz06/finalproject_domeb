from django.core import exceptions
from social.models.user_profile import UserProfile
from social.views.profile.profile import ProfileView
from social.models.notification import Notification
from social.views.profile.parceler.add_parceler import AddParceler
from social.views.profile.parceler.parcel_notification import ParcelNotification
from social.views.profile.parceler.list_parcelers import Listparcelers
from social.views.profile.parceler.remove_parceler import RemoveParceler
import unittest

class MyTestCase(unittest.TestCase):

    def test_add_parceler(self):
        method = AddParceler.as_view()
        user = UserProfile.objects.get(pk=1)
        ProfileView.check_parcelers(method, user.parcels.all(), UserProfile.objects.get(pk=2))

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            user = UserProfile.objects.get(pk=1)
            ProfileView.check_parcelers(method, user.parcels.all(), UserProfile.objects.get(pk=998))
            self.assertTrue('None' in context.exception)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            user = UserProfile.objects.get(pk=999)
            ProfileView.check_parcelers(method, user.parcels.all(), UserProfile.objects.get(pk=2))
            self.assertTrue('None' in context.exception)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            user = UserProfile.objects.get(pk=999)
            ProfileView.check_parcelers(method, user.parcels.all(), UserProfile.objects.get(pk=998))
            self.assertTrue('None' in context.exception)

    def test_get_all_parceler(self):
        method = Listparcelers.as_view()
        parceler = UserProfile.objects.get(pk=1)
        parcelers = parceler.parcels.all()
        self.assertTrue(parcelers)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            UserProfile.objects.get(pk=999)
            self.assertTrue('None' in context.exception)

    def test_parceler_notification(self):
        method = ParcelNotification.as_view()
        notification = Notification.objects.get(pk=1)
        testparcel = ParcelNotification.parceler_notification(method, notification)
        notification.user_has_seen = True
        self.assertEqual(testparcel.user_has_seen, notification.user_has_seen)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            Notification.objects.get(pk=999)
            self.assertTrue('None' in context.exception)

    def test_remove_parceler(self):
        method = RemoveParceler.as_view()
        user_1 = UserProfile.objects.get(pk=1)
        user_2 = UserProfile.objects.get(pk=2)
        test = user_1.parcels.remove(user_2.user)
        self.assertEqual(test, None)


if __name__ == '__main__':
    unittest.main()
