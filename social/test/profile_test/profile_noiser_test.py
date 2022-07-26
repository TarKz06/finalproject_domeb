from django.core import exceptions
from social.models.user_profile import UserProfile
from social.views.profile.profile import ProfileView
from social.models.notification import Notification
from social.views.profile.noiser.add_noiser import AddNoiser
from social.views.profile.noiser.noise_notification import NoiseNotification
from social.views.profile.noiser.list_noisers import ListNoisers
from social.views.profile.noiser.remove_noiser import RemoveNoiser
import unittest

class MyTestCase(unittest.TestCase):

    def test_add_noiser(self):
        method = AddNoiser.as_view()
        user = UserProfile.objects.get(pk=1)
        ProfileView.check_noiser(method, user.noises.all(), UserProfile.objects.get(pk=2))

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            user = UserProfile.objects.get(pk=1)
            ProfileView.check_noiser(method, user.noises.all(), UserProfile.objects.get(pk=998))
            self.assertTrue('None' in context.exception)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            user = UserProfile.objects.get(pk=999)
            ProfileView.check_noiser(method, user.noises.all(), UserProfile.objects.get(pk=2))
            self.assertTrue('None' in context.exception)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            user = UserProfile.objects.get(pk=999)
            ProfileView.check_noiser(method, user.noises.all(), UserProfile.objects.get(pk=998))
            self.assertTrue('None' in context.exception)

    def test_get_all_noiser(self):
        method = ListNoisers.as_view()
        noiser = UserProfile.objects.get(pk=1)
        noisers = noiser.noises.all()
        self.assertTrue(noisers)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            UserProfile.objects.get(pk=999)
            self.assertTrue('None' in context.exception)

    def test_noiser_notification(self):
        method = NoiseNotification.as_view()
        notification = Notification.objects.get(pk=1)
        testnoise = NoiseNotification.noiser_notification(method, notification)
        notification.user_has_seen = True
        self.assertEqual(testnoise.user_has_seen, notification.user_has_seen)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            Notification.objects.get(pk=999)
            self.assertTrue('None' in context.exception)

    def test_remove_noiser(self):
        method = RemoveNoiser.as_view()
        user_1 = UserProfile.objects.get(pk=1)
        user_2 = UserProfile.objects.get(pk=2)
        test = user_1.noises.remove(user_2.user)
        self.assertEqual(test, None)


if __name__ == '__main__':
    unittest.main()
