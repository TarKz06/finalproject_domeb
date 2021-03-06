from django.shortcuts import redirect
from django.views import View
from social.models.user_profile import UserProfile
from social.models.notification import Notification


class NoiseNotification(View):
    def get(self, request, notification_pk, profile_pk, *args, **kwargs):
        notification = Notification.objects.get(pk=notification_pk)
        profile = UserProfile.objects.get(pk=profile_pk)
        notification = self.noiser_notification(notification)

        return redirect('profile', pk=profile_pk)

    def noiser_notification(self, notification):
        notification.user_has_seen = True
        notification.save()
        return notification
