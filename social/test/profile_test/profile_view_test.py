from django.test import TestCase
from social.models.user_profile import UserProfile


class ProfileViewTest(TestCase):
    def test_profile_not_found(self):
        user = UserProfile.objects.get(pk=1)
        self.assertEqual(user.name, 'oat431')
