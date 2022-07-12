from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from social.models.user_profile import UserProfile


class RemoveFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = self.remove_follower(pk, request.user)
        return redirect('profile', pk=profile.pk)

    def get_profile(self, profile_id):
        return UserProfile.objects.get(pk=profile_id)

    def remove_follower(self, profile_id, follower):
        profile = self.get_profile(profile_id)
        profile.followers.remove(follower)
        return profile
