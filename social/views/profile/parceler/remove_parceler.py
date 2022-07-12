from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from social.models.user_profile import UserProfile


class RemoveParceler(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = self.remove_parceler(pk, request.user)
        return redirect('profile', pk=profile.pk)

    def get_profile(self, profile_id):
        return UserProfile.objects.get(pk=profile_id)

    def remove_parceler(self, profile_id, parceler):
        profile = self.get_profile(profile_id)
        profile.parcels.remove(parceler)
        return profile
