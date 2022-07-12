from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from social.models.user_profile import UserProfile
from social.models.notification import Notification


class AddNoiser(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = self.get_profile(pk)
        noiser = request.user
        new_noiser = self.add_noiser(profile, noiser)
        notification = self.send_notification(noiser, profile)

        return redirect('profile', pk=profile.pk)

    def get_profile(self, user_id):
        return UserProfile.objects.get(pk=user_id)

    def add_noiser(self, profile, noiser):
        profile.noises.add(noiser)
        return profile

    def send_notification(self, user, profile):
        return Notification.objects.create(notification_type=3, from_user=user, to_user=profile.user)
