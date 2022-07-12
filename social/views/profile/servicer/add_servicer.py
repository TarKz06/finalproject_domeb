from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from social.models.user_profile import UserProfile
from social.models.notification import Notification


class AddServicer(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        servicer = request.user
        new_servicers = self.add_servicer(profile, servicer)
        notification = self.send_notification(servicer,profile)

        return redirect('profile', pk=profile.pk)

    def get_profile(self, user_id):
        return UserProfile.objects.get(pk=user_id)

    def add_servicer(self, profile, servicer):
        profile.services.add(servicer)
        return profile

    def send_notification(self, user, profile):
        return Notification.objects.create(notification_type=3, from_user=user, to_user=profile.user)
