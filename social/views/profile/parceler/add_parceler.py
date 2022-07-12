from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from social.models.user_profile import UserProfile
from social.models.notification import Notification


class AddParceler(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = self.get_profile(pk)
        parcelers = request.user
        new_parcelers = self.add_parceler(profile, parcelers)
        notification = self.send_notification(parcelers, profile)

        return redirect('profile', pk=profile.pk)

    def get_profile(self, user_id):
        return UserProfile.objects.get(pk=user_id)

    def add_parceler(self, profile, parceler):
        profile.parcels.add(parceler)
        return profile

    def send_notification(self, user, profile):
        return Notification.objects.create(notification_type=3, from_user=user, to_user=profile.user)
