from django.shortcuts import render
from django.views import View
from social.models.user_profile import UserProfile


class ListServicers(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        servicers = profile.services.all()

        context = {
            'profile': profile,
            'servicers': servicers,
        }

        return render(request, 'social/servicers_list.html', context)
