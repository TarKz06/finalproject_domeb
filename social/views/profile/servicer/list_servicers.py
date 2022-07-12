from django.shortcuts import render
from django.views import View
from social.models.user_profile import UserProfile


class ListServicers(View):
    def get(self, request, pk, *args, **kwargs):
        servicers = self.get_all_servicer(pk)
        context = self.create_context(self.get_profile(pk),servicers)

        return render(request, 'social/servicers_list.html', context)

    def get_profile(self, user_id):
        return UserProfile.objects.get(pk=user_id)

    def get_all_servicer(self, user_id):
        profile = self.get_profile(user_id)
        return profile.services.all()

    def create_context(self, profile, servicers):
        return {
            'profile': profile,
            'servicers': servicers,
        }
