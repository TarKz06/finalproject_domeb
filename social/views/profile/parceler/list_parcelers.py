from django.shortcuts import render
from django.views import View
from social.models.user_profile import UserProfile


class Listparcelers(View):
    def get(self, request, pk, *args, **kwargs):
        parcelers = self.get_all_parceler(pk)
        context = self.create_context(self.get_profile(pk), parcelers)

        return render(request, 'social/parcelers_list.html', context)

    def get_profile(self, user_id):
        return UserProfile.objects.get(pk=user_id)

    def get_all_parceler(self, user_id):
        profile = self.get_profile(user_id)
        return profile.parcels.all()

    def create_context(self, profile, parcelers):
        return {
            'profile': profile,
            'parcelers': parcelers,
        }
