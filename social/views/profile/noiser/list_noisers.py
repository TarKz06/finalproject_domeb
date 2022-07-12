from django.shortcuts import render
from django.views import View
from social.models.user_profile import UserProfile


class ListNoisers(View):
    def get(self, request, pk, *args, **kwargs):
        noisers = self.get_all_noiser(pk)
        context = self.create_context(self.get_profile(pk),noisers)
        return render(request, 'social/noisers_list.html', context)

    def get_profile(self, user_id):
        return UserProfile.objects.get(pk=user_id)

    def get_all_noiser(self, user_id):
        profile = self.get_profile(user_id)
        return profile.noises.all()

    def create_context(self, profile, noisers):
        return {
            'profile': profile,
            'noisers': noisers,
        }
