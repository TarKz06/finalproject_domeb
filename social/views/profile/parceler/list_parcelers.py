from django.shortcuts import render
from django.views import View
from social.models.user_profile import UserProfile


class Listparcelers(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        parcelers = profile.parcels.all()

        context = {
            'profile': profile,
            'parcelers': parcelers,
        }

        return render(request, 'social/parcelers_list.html', context)
