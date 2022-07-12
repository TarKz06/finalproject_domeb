from django.shortcuts import render
from django.views import View
from social.models.user_profile import UserProfile


class ListRepairers(View):
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        repairers = profile.repairs.all()

        context = {
            'profile': profile,
            'repairers': repairers,
        }

        return render(request, 'social/repairers_list.html', context)
