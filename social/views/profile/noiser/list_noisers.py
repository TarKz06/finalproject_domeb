from django.shortcuts import render
from django.views import View
from social.models.user_profile import UserProfile


class ListNoisers(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        noisers = profile.noises.all()

        context = {
            'profile': profile,
            'noisers': noisers,
        }

        return render(request, 'social/noisers_list.html', context)
