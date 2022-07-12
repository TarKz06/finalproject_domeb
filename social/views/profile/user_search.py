from django.shortcuts import render
from django.db.models import Q
from django.views import View
from social.models.user_profile import UserProfile


class UserSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        profile_list = self.search_profile(query)
        context = self.create_context(profile_list)
        return render(request, 'social/search.html', context)

    def search_profile(self,query):
        return UserProfile.objects.filter(
            Q(user__username__icontains=query)
        )

    def create_context(self, profile_list):
        return {
            'profile_list': profile_list,
        }
