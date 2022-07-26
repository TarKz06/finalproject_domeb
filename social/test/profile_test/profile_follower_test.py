from django.core import exceptions
from social.models.user_profile import UserProfile
from social.models.notification import Notification
from social.views.profile.profile import ProfileView
from social.views.profile.follower.add_follower import AddFollower
from social.views.profile.follower.follow_notification import FollowNotification
from social.views.profile.follower.list_followers import ListFollowers
from social.views.profile.follower.remove_follower import RemoveFollower
import unittest


class MyTestCase(unittest.TestCase):
    def test_check_follower(self):
        method = ProfileView.as_view()
        user = UserProfile.objects.get(pk=1)
        ProfileView.check_following(method, user.followers.all(), UserProfile.objects.get(pk=2))

    def test_get_profile(self):
        method = AddFollower.as_view()
        user = UserProfile.objects.get(pk=1)
        user_id = 1
        follower = AddFollower.get_profile(method,user_id)
        self.assertEqual(user.name, follower.name)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            UserProfile.objects.get(pk=999)
            self.assertTrue('None' in context.exception)

    def test_add_follower(self):
        method = ProfileView.as_view()
        user = UserProfile.objects.get(pk=1)
        ProfileView.check_following(method, user.followers.all(), UserProfile.objects.get(pk=2))

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            user = UserProfile.objects.get(pk=1)
            ProfileView.check_following(method, user.followers.all(), UserProfile.objects.get(pk=998))
            self.assertTrue('None' in context.exception)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            user = UserProfile.objects.get(pk=999)
            ProfileView.check_following(method, user.followers.all(), UserProfile.objects.get(pk=2))
            self.assertTrue('None' in context.exception)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            user = UserProfile.objects.get(pk=999)
            ProfileView.check_following(method, user.followers.all(), UserProfile.objects.get(pk=998))
            self.assertTrue('None' in context.exception)

    def test_send_notification(self):
        method = AddFollower.as_view()
        user_1 = UserProfile.objects.get(pk=1)
        user_2 = UserProfile.objects.get(pk=2)
        function = AddFollower.send_notification(method, user_1.user, user_2)
        notification = Notification.objects.get(id=50)
        self.assertEqual(function, notification)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            user_1 = UserProfile.objects.get(pk=1)
            user_2 = UserProfile.objects.get(pk=998)
            AddFollower.send_notification(method, user_1.user, user_2)
            self.assertTrue('None' in context.exception)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            user_1 = UserProfile.objects.get(pk=999)
            user_2 = UserProfile.objects.get(pk=2)
            AddFollower.send_notification(method, user_1.user, user_2)
            self.assertTrue('None' in context.exception)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            user_1 = UserProfile.objects.get(pk=999)
            user_2 = UserProfile.objects.get(pk=998)
            AddFollower.send_notification(method, user_1.user, user_2)
            self.assertTrue('None' in context.exception)

    def test_follower_notification(self):
        method = FollowNotification.as_view()
        notification = Notification.objects.get(pk=1)
        testnoti = FollowNotification.follower_notification(method, notification)
        notification.user_has_seen = True
        self.assertEqual(testnoti.user_has_seen, notification.user_has_seen)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            Notification.objects.get(pk=999)
            self.assertTrue('None' in context.exception)

    def test_get_all_follower(self):
        method = ListFollowers.as_view()
        follower = UserProfile.objects.get(pk=1)
        noisers = follower.noises.all()
        self.assertTrue(noisers)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            UserProfile.objects.get(pk=999)
            self.assertTrue('None' in context.exception)

    def test_remove_follower(self):
        method = RemoveFollower.as_view()
        user_1 = UserProfile.objects.get(pk=1)
        user_2 = UserProfile.objects.get(pk=2)
        test = user_1.followers.remove(user_2.user)
        self.assertEqual(test, None)

if __name__ == '__main__':
    unittest.main()
