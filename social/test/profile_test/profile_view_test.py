from django.contrib.auth.models import User
from django.core import exceptions
import unittest

class ProfileViewTest(unittest.TestCase):
    def test_profile_view(self):
        user = User.objects.get(id=1)
        self.assertEqual(user.username, 'domeb')

    def test_profile_not_found(self):
        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            User.objects.get(id=999)
            self.assertTrue('None' in context.exception)