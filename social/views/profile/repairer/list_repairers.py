from django.shortcuts import render
from django.views import View
from social.models.user_profile import UserProfile


class ListRepairers(View):
    def get(self, request, pk, *args, **kwargs):
        repairers = self.get_all_repairer(pk)
        context = self.create_context(self.get_profile(pk),repairers)

        return render(request, 'social/repairers_list.html', context)

    def get_profile(self, user_id):
        return UserProfile.objects.get(pk=user_id)

    def get_all_repairer(self, user_id):
        profile = self.get_profile(user_id)
        return profile.repairs.all()

    def create_context(self, profile, repairers):
        return {
            'profile': profile,
            'repairers': repairers,
        }
