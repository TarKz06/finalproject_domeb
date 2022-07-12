from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from social.models.user_profile import UserProfile


class RemoveNoiser(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = self.remove_noiser(pk, request.user)
        return redirect('profile', pk=profile.pk)

    def get_profile(self, profile_id):
        return UserProfile.objects.get(pk=profile_id)

    def remove_noiser(self, profile_id, noiser):
        profile = self.get_profile(profile_id)
        profile.noises.remove(noiser)
        return profile
