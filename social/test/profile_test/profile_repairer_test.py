from django.core import exceptions
from social.models.user_profile import UserProfile
from social.views.profile.profile import ProfileView
from social.models.notification import Notification
from social.views.profile.repairer.add_repairer import AddRepairer
from social.views.profile.repairer.repair_notification import RepairNotification
from social.views.profile.repairer.list_repairers import ListRepairers
from social.views.profile.repairer.remove_repairer import RemoveRepairer
import unittest


class MyTestCase(unittest.TestCase):
    def test_add_repairer(self):
        method = AddRepairer.as_view()
        user = UserProfile.objects.get(pk=1)
        ProfileView.check_repariers(method, user.repairs.all(), UserProfile.objects.get(pk=2))

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            user = UserProfile.objects.get(pk=1)
            ProfileView.check_repariers(method, user.repairs.all(), UserProfile.objects.get(pk=998))
            self.assertTrue('None' in context.exception)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            user = UserProfile.objects.get(pk=999)
            ProfileView.check_repariers(method, user.repairs.all(), UserProfile.objects.get(pk=2))
            self.assertTrue('None' in context.exception)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            user = UserProfile.objects.get(pk=999)
            ProfileView.check_repariers(method, user.repairs.all(), UserProfile.objects.get(pk=998))
            self.assertTrue('None' in context.exception)

    def test_get_all_repairer(self):
        method = ListRepairers.as_view()
        repairer = UserProfile.objects.get(pk=1)
        repairers = repairer.repairs.all()
        self.assertTrue(repairers)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            UserProfile.objects.get(pk=999)
            self.assertTrue('None' in context.exception)

    def test_repairer_notification(self):
        method = RepairNotification.as_view()
        notification = Notification.objects.get(pk=1)
        testrepair = RepairNotification.reparier_notification(method, notification)
        notification.user_has_seen = True
        self.assertEqual(testrepair.user_has_seen, notification.user_has_seen)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            Notification.objects.get(pk=999)
            self.assertTrue('None' in context.exception)

    def test_remove_repairer(self):
        method = RemoveRepairer.as_view()
        user_1 = UserProfile.objects.get(pk=1)
        user_2 = UserProfile.objects.get(pk=2)
        test = user_1.repairs.remove(user_2.user)
        self.assertEqual(test, None)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            user_1 = UserProfile.objects.get(pk=999)
            self.assertTrue('None' in context.exception)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            user_2 = UserProfile.objects.get(pk=998)
            self.assertTrue('None' in context.exception)

        with self.assertRaises(exceptions.ObjectDoesNotExist) as context:
            user_1 = UserProfile.objects.get(pk=999)
            user_2 = UserProfile.objects.get(pk=998)
            self.assertTrue('None' in context.exception)


if __name__ == '__main__':
    unittest.main()
